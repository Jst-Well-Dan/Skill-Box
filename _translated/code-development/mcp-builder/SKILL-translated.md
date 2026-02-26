<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:11:56
翻译模型: glm-4-flash
原文大小: 13,511 字符
-->

---
name: mcp-builder
description: 指南，用于创建高质量的 MCP（模型上下文协议）服务器，使 LLM（大型语言模型）能够通过精心设计的工具与外部服务交互。在构建 MCP 服务器以集成外部 API 或服务时使用，无论是 Python（FastMCP）还是 Node/TypeScript（MCP SDK）。
license: 详细条款请参阅 LICENSE.txt
---

# MCP 服务器开发指南

## 概述

为了创建高质量的 MCP（模型上下文协议）服务器，使 LLM（大型语言模型）能够有效地与外部服务交互，请使用本指南。MCP 服务器提供工具，允许 LLM 访问外部服务和 API。MCP 服务器的质量通过其使 LLM 使用提供的工具完成实际任务的能力来衡量。

---

# 流程

## 🚀 高级工作流程

创建高质量的 MCP 服务器涉及四个主要阶段：

### 阶段 1：深入研究与规划

#### 1.1 理解以代理为中心的设计原则

在深入实施之前，通过审查以下原则来了解如何为 AI 代理设计工具：

**为工作流程而构建，而不仅仅是 API 端点：**
- 不要简单地包装现有的 API 端点 - 构建深思熟虑、影响深远的工作流程工具
- 合并相关操作（例如，`schedule_event` 同时检查可用性并创建事件）
- 专注于能够完成完整任务的工具，而不仅仅是单个 API 调用
- 考虑代理实际需要完成的流程

**优化有限上下文：**
- 代理具有受限的上下文窗口 - 每个令牌都很重要
- 返回高信号信息，而不是详尽的数据转储
- 提供“简洁”与“详细”的响应格式选项
- 默认使用人类可读的标识符而不是技术代码（名称而不是 ID）
- 考虑代理的上下文预算是一种稀缺资源

**设计可操作的错误消息：**
- 错误消息应指导代理走向正确的使用模式
- 建议具体的下一步操作：“尝试使用 filter='active_only' 来减少结果”
- 使错误具有教育意义，而不仅仅是诊断性
- 通过清晰的反馈帮助代理学习正确的工具使用方法

**遵循自然任务细分：**
- 工具名称应反映人类对任务的思考方式
- 使用一致的名称前缀将相关工具分组以提高可发现性
- 围绕自然工作流程设计工具，而不仅仅是 API 结构

**使用以评估驱动的开发：**
- 早期创建现实世界的评估场景
- 让代理反馈推动工具改进
- 快速原型设计并基于实际代理性能进行迭代

#### 1.3 学习 MCP 协议文档

**获取最新的 MCP 协议文档：**

使用 WebFetch 加载：`https://modelcontextprotocol.io/llms-full.txt`

这份全面的文档包含了完整的 MCP 规范和指南。

#### 1.4 学习框架文档

**加载并阅读以下参考文件：**

- **MCP 最佳实践**：[📋 查看最佳实践](./reference/mcp_best_practices.md) - 所有 MCP 服务器的基本指南

**对于 Python 实现，还要加载：**
- **Python SDK 文档**：使用 WebFetch 加载 `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Python 实现指南](./reference/python_mcp_server.md) - Python 特定的最佳实践和示例

**对于 Node/TypeScript 实现，还要加载：**
- **TypeScript SDK 文档**：使用 WebFetch 加载 `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ TypeScript 实现指南](./reference/node_mcp_server.md) - Node/TypeScript 特定的最佳实践和示例

#### 1.5 详尽地学习 API 文档

为了集成服务，阅读所有可用的 API 文档：
- 官方 API 参考文档
- 身份验证和授权要求
- 速率限制和分页模式
- 错误响应和状态码
- 可用端点和它们的参数
- 数据模型和模式

**为了收集全面的信息，根据需要使用网络搜索和 WebFetch 工具。**

#### 1.6 创建全面的实施计划

根据您的调查，创建一个详细的计划，包括：

**工具选择：**
- 列出要实现的最有价值的端点/操作
- 优先考虑能够实现最常见和最重要的用例的工具
- 考虑哪些工具可以一起工作以实现复杂的流程

**共享实用程序和助手：**
- 识别常见的 API 请求模式
- 规划分页助手
- 设计过滤和格式化实用程序
- 规划错误处理策略

**输入/输出设计：**
- 定义输入验证模型（Python 的 Pydantic，TypeScript 的 Zod）
- 设计一致的响应格式（例如，JSON 或 Markdown），以及可配置的详细程度（例如，详细或简洁）
- 规划大规模使用（数千名用户/资源）
- 实现字符限制和截断策略（例如，25,000 个令牌）

**错误处理策略：**
- 规划优雅的失败模式
- 设计清晰、可操作、LLM 友好的自然语言错误消息，这些消息可以提示进一步的操作
- 考虑速率限制和超时场景
- 处理身份验证和授权错误

---

### 阶段 2：实施

现在您已经制定了全面的计划，开始根据语言特定的最佳实践进行实施。

#### 2.1 设置项目结构

**对于 Python：**
- 创建单个 `.py` 文件或如果复杂则组织到模块中（参见 [🐍 Python 指南](./reference/python_mcp_server.md)）
- 使用 MCP Python SDK 进行工具注册
- 定义 Pydantic 模型进行输入验证

**对于 Node/TypeScript：**
- 创建适当的项目结构（参见 [⚡ TypeScript 指南](./reference/node_mcp_server.md)）
- 设置 `package.json` 和 `tsconfig.json`
- 使用 MCP TypeScript SDK
- 定义 Zod 架构进行输入验证

#### 2.2 首先实施核心基础设施

**为了开始实施，在实施工具之前创建共享实用程序：**
- API 请求辅助函数
- 错误处理实用程序
- 响应格式化函数（JSON 和 Markdown）
- 分页助手
- 身份验证/令牌管理

#### 2.3 系统地实施工具

对于计划中的每个工具：

**定义输入架构：**
- 使用 Pydantic（Python）或 Zod（TypeScript）进行验证
- 包括适当的约束（最小/最大长度、正则表达式模式、最小/最大值、范围）
- 提供清晰、描述性的字段说明
- 在字段说明中包含多样化的示例

**编写全面的文档字符串/描述：**
- 一行总结工具的作用
- 详细说明目的和功能
- 明确参数类型和示例
- 完整的返回类型架构
- 使用示例（何时使用，何时不使用）
- 错误处理文档，概述在特定错误的情况下如何进行操作

**实现工具逻辑：**
- 使用共享实用程序以避免代码重复
- 遵循异步/等待模式进行所有 I/O
- 实现适当的错误处理
- 支持多种响应格式（JSON 和 Markdown）
- 尊重分页参数
- 检查字符限制并适当截断

**添加工具注释：**
- `readOnlyHint`: true（对于只读操作）
- `destructiveHint`: false（对于非破坏性操作）
- `idempotentHint`: true（如果重复调用具有相同的效果）
- `openWorldHint`: true（如果与外部系统交互）

#### 2.4 遵循语言特定的最佳实践

**在此阶段，加载适当的语言指南：**

**对于 Python：加载 [🐍 Python 实现指南](./reference/python_mcp_server.md) 并确保以下内容：**
- 使用 MCP Python SDK 进行适当的工具注册
- Pydantic v2 模型具有 `model_config`
- 类型提示贯穿始终
- 异步/等待模式用于所有 I/O 操作
- 正确的导入组织
- 模块级常量（CHARACTER_LIMIT，API_BASE_URL）

**对于 Node/TypeScript：加载 [⚡ TypeScript 实现指南](./reference/node_mcp_server.md) 并确保以下内容：**
- 正确使用 `server.registerTool`
- Zod 架构具有 `.strict()`
- 启用 TypeScript 严格模式
- 不使用 `any` 类型 - 使用正确的类型
- 明确的 Promise<T> 返回类型
- 配置构建过程（`npm run build`）

---

### 阶段 3：审查和改进

在初步实施之后：

#### 3.1 代码质量审查

为了确保质量，审查代码以：
- **DRY 原则**：工具之间没有重复的代码
- **可组合性**：共享逻辑提取到函数中
- **一致性**：类似操作返回类似格式
- **错误处理**：所有外部调用都有错误处理
- **类型安全**：完整的类型覆盖（Python 类型提示，TypeScript 类型）
- **文档**：每个工具都有全面的文档字符串/描述

#### 3.2 测试和构建

**重要提示**：MCP 服务器是长时间运行的进程，它们在 stdio/stdin 或 sse/http 上等待请求。直接在主进程中运行它们（例如，`python server.py` 或 `node dist/index.js`）会导致您的进程无限期地挂起。

**安全测试服务器的方法：**
- 使用评估工具（参见阶段 4）- 建议的方法
- 在 tmux 中运行服务器以将其保持在主进程之外
- 测试时使用超时：`timeout 5s python server.py`

**对于 Python：**
- 验证 Python 语法：`python -m py_compile your_server.py`
- 通过检查文件来验证导入是否正确工作
- 手动测试：在 tmux 中运行服务器，然后在主进程中测试评估工具
- 或者直接使用评估工具（它管理服务器以 stdio 传输）

**对于 Node/TypeScript：**
- 运行 `npm run build` 并确保它无错误完成
- 验证 dist/index.js 已创建
- 手动测试：在 tmux 中运行服务器，然后在主进程中测试评估工具
- 或者直接使用评估工具（它管理服务器以 stdio 传输）

#### 3.3 使用质量检查清单

为了验证实施质量，从语言特定的指南中加载适当的检查清单：
- Python：请参阅 [🐍 Python 指南](./reference/python_mcp_server.md) 中的“质量检查清单”
- Node/TypeScript：请参阅 [⚡ TypeScript 指南](./reference/node_mcp_server.md) 中的“质量检查清单”

---

### 阶段 4：创建评估

在实施您的 MCP 服务器后，创建全面的评估以测试其有效性。

**加载 [✅ 评估指南](./reference/evaluation.md) 以获取完整的评估指南。**

#### 4.1 理解评估目的

评估测试 LLM 是否能够有效地使用您的 MCP 服务器来回答现实、复杂的问题。

#### 4.2 创建 10 个评估问题

为了创建有效的评估，遵循评估指南中概述的过程：

1. **工具检查**：列出可用的工具并了解其功能
2. **内容探索**：使用只读操作来探索可用的数据
3. **问题生成**：创建 10 个复杂、现实的问题
4. **答案验证**：自己解决每个问题以验证答案

#### 4.3 评估要求

每个问题必须：
- **独立**：不依赖于其他问题
- **只读**：仅需要非破坏性操作
- **复杂**：需要多个工具调用和深入探索
- **现实**：基于人类会关心的真实用例
- **可验证**：单个、清晰的答案可以通过字符串比较进行验证
- **稳定**：答案不会随时间变化

#### 4.4 输出格式

创建一个具有以下结构的 XML 文件：

```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

# 参考文件

## 📚 文档库

在开发过程中根据需要加载以下资源：

### 核心MCP文档（首先加载）
- **MCP 协议**：从 `https://modelcontextprotocol.io/llms-full.txt` 获取 - 完整的 MCP 规范
- [📋 MCP 最佳实践](./reference/mcp_best_practices.md) - 包括服务器和工具命名约定、响应格式指南（JSON 与 Markdown）、分页最佳实践、字符限制和截断策略、工具开发指南以及安全和错误处理标准的通用 MCP 指南

### SDK 文档（在阶段 1/2 加载）
- **Python SDK**：从 `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md` 获取
- **TypeScript SDK**：从 `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md` 获取

### 语言特定的实现指南（在阶段 2 加载）
- [🐍 Python 实现指南](./reference/python_mcp_server.md) - 包含服务器初始化模式、Pydantic 模型示例、使用 `@mcp.tool` 进行工具注册、完整的工作示例以及质量检查清单的完整的 Python/FastMCP 指南
- [⚡ TypeScript 实现指南](./reference/node_mcp_server.md) - 包含项目结构、Zod 架构模式、使用 `server.registerTool` 进行工具注册、完整的工作示例以及质量检查清单的完整的 TypeScript 指南

### 评估指南（在阶段 4 加载）
- [✅ 评估指南](./reference/evaluation.md) - 包含问题创建指南、答案验证策略、XML 格式规范、示例问题和答案以及使用提供的脚本来运行评估的完整评估创建指南