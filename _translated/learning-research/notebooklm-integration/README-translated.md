<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:13:46
翻译模型: glm-4-flash
原文大小: 15,746 字符
-->

```markdown
<div align="center">

# NotebookLM Claude Code 技能

**直接通过 [Claude Code](https://github.com/anthropics/claude-code) 与 NotebookLM 进行聊天，获取基于您上传文档的源信息回答**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Claude Code 技能](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://www.anthropic.com/news/skills)
[![基于](https://img.shields.io/badge/Based%20on-NotebookLM%20MCP-green.svg)](https://github.com/PleasePrompto/notebooklm-mcp)
[![GitHub](https://img.shields.io/github/stars/PleasePrompto/notebooklm-skill?style=social)](https://github.com/PleasePrompto/notebooklm-skill)

> 使用此技能直接从 Claude Code 查询您的 Google NotebookLM 笔记本，从 Gemini 获取基于源和引用的答案。浏览器自动化、库管理、持久认证。大幅减少幻觉 - 只从您上传的文档中获取答案。

[安装](#installation) • [快速入门](#quick-start) • [为什么选择 NotebookLM 而不是本地 RAG](#why-notebooklm-not-local-rag) • [工作原理](#how-it-works) • [MCP 替代方案](https://github.com/PleasePrompto/notebooklm-mcp)

</div>

---

## ⚠️ 重要：仅限本地 Claude Code

**此技能仅与本地 [Claude Code](https://github.com/anthropics/claude-code) 安装兼容，不支持在 Web UI 中使用。**

Web UI 在没有网络访问权限的沙盒中运行技能，而此技能需要浏览器自动化，因此您必须在您的计算机上本地使用 [Claude Code](https://github.com/anthropics/claude-code)。

---

## 问题

当您告诉 [Claude Code](https://github.com/anthropics/claude-code) “搜索我的本地文档”时，以下是会发生的情况：

- **大量令牌消耗**：搜索文档意味着反复读取多个文件
- **检索不准确**：搜索关键词，错过文档之间的上下文和联系
- **幻觉**：当找不到东西时，它会发明听起来合理的 API
- **手动复制粘贴**：不断在 NotebookLM 浏览器和您的编辑器之间切换

## 解决方案

此 Claude Code 技能允许 [Claude Code](https://github.com/anthropics/claude-code) 直接与 [**NotebookLM**](https://notebooklm.google/) 进行聊天 — 由 Gemini 2.5 驱动的 Google **源信息知识库**，它仅从您上传的文档中提供智能、综合的答案。

```
您的任务 → Claude 向 NotebookLM 提问 → Gemini 综合答案 → Claude 编写正确的代码
```

**不再需要复制粘贴**：Claude 直接提问并在 CLI 中直接获取答案。它通过自动跟进建立深入的理解，获取具体的实现细节、边缘情况和最佳实践。

---

## 为什么选择 NotebookLM 而不是本地 RAG？

| 方法 | 令牌成本 | 设置时间 | 幻觉 | 答案质量 |
|------|----------|----------|------|----------|
| **将文档提供给 Claude** | 🔴 非常高（多次文件读取） | 瞬间 | 是 - 填补空白 | 可变检索 |
| **网络搜索** | 🟡 中等 | 瞬间 | 高 - 不可靠的来源 | 击中或错过 |
| **本地 RAG** | 🟡 中等至高 | 几小时（嵌入，分块） | 中等 - 检索空白 | 取决于设置 |
| **NotebookLM 技能** | 🟢 最小 | 5 分钟 | **最小** - 仅基于源信息 | 专家综合 |

### NotebookLM 的优势是什么？

1. **由 Gemini 预处理**：上传文档一次，即可获得即时专家知识
2. **自然语言问答**：不仅仅是检索 — 实际理解和综合
3. **多源关联**：连接 50 多个文档中的信息
4. **基于引用**：每个答案都包含来源引用
5. **无需基础设施**：无需向量数据库、嵌入或分块策略

---

## 安装

### 世界上最简单的安装方法：

```bash
# 1. 创建技能目录（如果不存在）
mkdir -p ~/.claude/skills

# 2. 克隆此存储库
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm

# 3. 那就结束了！在 Claude Code 中输入：
"What are my skills?"
```

当您首次使用此技能时，它会自动：

- 创建一个独立的 Python 环境（`.venv`）
- 安装所有依赖项，包括 **Google Chrome**
- 使用 Chrome（而不是 Chromium）设置浏览器自动化，以实现最大可靠性
- 所有一切都包含在技能文件夹中

**注意**：设置使用真实的 Chrome 而不是 Chromium，以实现跨平台可靠性、一致的浏览器指纹和与 Google 服务的更好反检测

---

## 快速入门

### 1. 检查您的技能

在 Claude Code 中说：
```
"What skills do I have?"
```

Claude 将列出您的可用技能，包括 NotebookLM。

### 2. 使用 Google 进行一次性的身份验证

```
"设置 NotebookLM 身份验证"
```
*一个 Chrome 窗口打开 → 使用您的 Google 账户登录*

### 3. 创建您的知识库

转到 [notebooklm.google.com](https://notebooklm.google.com) → 创建笔记本 → 上传您的文档：
- 📄 PDF、Google Docs、Markdown 文件
- 🔗 网站、GitHub 仓库
- 🎥 YouTube 视频
- 📚 每个笔记本中的多个来源

分享：**⚙️ 分享 → 任何有链接的人 → 复制**

### 4. 将其添加到您的库中

**选项 A：让 Claude 解决它（智能添加）**
```
"查询此笔记本的内容并将其添加到我的库中：[您的链接]"
```
Claude 将自动查询笔记本以发现其内容，然后将其添加并带有适当的元数据。

**选项 B：手动添加**
```
"将此 NotebookLM 添加到我的库中：[您的链接]"
```
Claude 将要求您输入名称和主题，然后将其保存以供将来使用。

### 5. 开始研究

```
"我的 React 文档中关于 hooks 的内容是什么？"
```

Claude 自动选择正确的笔记本并直接从 NotebookLM 获取答案。

---

## 工作原理

这是一个 **Claude Code 技能** — 一个包含指令和脚本的本地文件夹，Claude Code 在需要时可以使用。与 [MCP 服务器版本](https://github.com/PleasePrompto/notebooklm-mcp) 不同，此版本直接在 Claude Code 中运行，无需单独的服务器。

### 与 MCP 服务器的主要区别

| 功能 | 此技能 | MCP 服务器 |
|------|--------|------------|
| **协议** | Claude 技能 | 模型上下文协议 |
| **安装** | 克隆到 `~/.claude/skills` | `claude mcp add ...` |
| **会话** | 每个问题一个新鲜浏览器 | 持久聊天会话 |
| **兼容性** | Claude Code 仅限（本地） | Claude Code、Codex、Cursor 等 |
| **语言** | Python | TypeScript |
| **分发** | Git 克隆 | npm 包 |

### 架构

```
~/.claude/skills/notebooklm/
├── SKILL.md              # Claude 指令
├── scripts/              # Python 自动化脚本
│   ├── ask_question.py   # 查询 NotebookLM
│   ├── notebook_manager.py # 库管理
│   └── auth_manager.py   # Google 认证
├── .venv/                # 独立的 Python 环境（自动创建）
└── data/                 # 本地笔记本库
```

当您提及 NotebookLM 或发送笔记本 URL 时，Claude：

1. 加载技能指令
2. 运行适当的 Python 脚本
3. 打开浏览器，提出您的问题
4. 直接将答案返回给您
5. 使用该知识帮助您完成任务

---

## 核心功能

### **基于源信息的回答**

NotebookLM 通过仅从您上传的文档中回答来显著减少幻觉。如果信息不可用，它将表示不确定性而不是发明内容。

### **直接集成**

无需在浏览器和编辑器之间进行复制粘贴。Claude 以编程方式提问并接收答案。

### **智能库管理**

保存带有标签和描述的 NotebookLM 链接。Claude 自动选择正确的笔记本以完成您的任务。

### **自动认证**

一次性 Google 登录，然后认证在会话之间持续。

### **自包含**

一切都在技能文件夹中运行，具有独立的 Python 环境。无需全局安装。

### **类似人类的自动化**

使用类似人类的打字速度和交互模式，以避免检测。

---

## 常见命令

| 您说的话 | 发生的事情 |
|----------|------------|
| *"设置 NotebookLM 认证"* | 打开 Chrome 进行 Google 登录 |
| *"将 [链接] 添加到我的 NotebookLM 库中"* | 保存笔记本并带有元数据 |
| *"显示我的 NotebookLM 笔记本"* | 列出所有保存的笔记本 |
| *"询问我的 API 文档关于 [主题]"* | 查询相关的笔记本 |
| *"使用 React 笔记本"* | 设置活动笔记本 |
| *"清除 NotebookLM 数据"* | 从头开始（保留库） |

---

## 真实世界的示例

### 示例 1：研讨会手册查询

**用户询问**： "检查我的 Suzuki GSR 600 工作手册中的刹车油类型、发动机油规格和后轴扭矩。"

**Claude 自动**：
- 使用 NotebookLM 进行认证
- 就每个规格提出全面的问题
- 当被提示“这是您需要知道的所有内容吗？”时进行跟进
- 提供准确的规格：DOT 4 刹车油，SAE 10W-40 油液，100 N·m 后轴扭矩

![NotebookLM 聊天示例](images/example_notebookchat.png)

### 示例 2：无幻觉构建

**您**： "我需要为 Gmail 垃圾邮件过滤构建一个 n8n 工作流程。使用我的 n8n 笔记本。"

**Claude 的内部过程**：
```
→ 加载 NotebookLM 技能
→ 激活 n8n 笔记本
→ 提出全面的问题并进行跟进
→ 从多个查询中综合完整的答案
```

**结果**： 第一次尝试即可获得有效的工作流程，无需调试幻觉 API。

---

## 技术细节

### 核心技术
- **Patchright**：浏览器自动化库（基于 Playwright）
- **Python**：此技能的实现语言
- **隐蔽技术**：类似人类的打字速度和交互模式

注意：MCP 服务器使用相同的 Patchright 库，但通过 TypeScript/npm 生态系统。

### 依赖项
- **patchright==1.55.2**：浏览器自动化
- **python-dotenv==1.0.0**：环境配置
- 在首次使用时自动安装到 `.venv` 中

### 数据存储

所有数据都存储在技能目录中：

```
~/.claude/skills/notebooklm/data/
├── library.json       - 您的笔记本库及其元数据
├── auth_info.json     - 认证状态信息
└── browser_state/     - 浏览器 Cookie 和会话数据
```

**重要安全提示**：
- `data/` 目录包含敏感的认证数据和个人笔记本
- 它会自动通过 `.gitignore` 排除
- 永远不要手动提交或共享 `data/` 目录的内容

### 会话模型

与 MCP 服务器不同，此技能使用 **无状态模型**：
- 每个问题打开一个新鲜浏览器
- 提出问题，获取答案
- 添加一个跟进提示，鼓励 Claude 提出更多问题
- 立即关闭浏览器

这意味着：
- 没有持久的聊天上下文
- 每个问题都是独立的
- 但您的笔记本库持续存在
- **跟进机制**：每个答案都包含“这是您需要知道的所有内容吗？”以提示 Claude 提出全面的跟进问题

对于多步骤研究，Claude 在需要时自动提出跟进问题。

---

## 局限性

### 技能特定
- **仅限本地 Claude Code** - 不支持在 Web UI 中使用（沙盒限制）
- **无会话持久性** - 每个问题都是独立的
- **无跟进上下文** - 无法引用“上一个答案”

### NotebookLM
- **速率限制** - 免费层有每日查询限制
- **手动上传** - 您必须首先将文档上传到 NotebookLM
- **共享要求** - 笔记本必须公开共享

---

## 常见问题解答

**为什么这个技能在 Claude Web UI 中无法使用？**
Web UI 在没有网络访问权限的沙盒中运行技能。浏览器自动化需要网络访问才能访问 NotebookLM。

**这与 MCP 服务器有何不同？**
这是一个更简单、基于 Python 的实现，直接作为 Claude 技能运行。MCP 服务器功能更丰富，具有持久会话和多工具支持。

**我是否可以使用此技能和 MCP 服务器？**
是的！它们服务于不同的目的。使用技能进行快速 Claude Code 集成，使用 MCP 服务器进行持久会话和多工具支持。

**如果 Chrome 崩溃怎么办？**
运行：`"清除 NotebookLM 浏览器数据"` 并重试。

**我的 Google 账户安全吗？**
Chrome 在您的计算机上本地运行。您的凭据永远不会离开您的计算机。如果您担心，请使用专用 Google 账户进行自动化——想想看，这就像网络爬虫一样：可能没问题，但最好还是小心为妙！

---

## 故障排除

### 技能未找到
```bash
# 确保它在正确的位置
ls ~/.claude/skills/notebooklm/
# 应显示：SKILL.md、scripts/、等
```

### 认证问题
说：`"重置 NotebookLM 认证"`

### 浏览器崩溃
说：`"清除 NotebookLM 浏览器数据"`

### 依赖项问题
```bash
# 如果需要，请手动重新安装
cd ~/.claude/skills/notebooklm
rm -rf .venv
python -m venv .venv
source .venv/bin/activate  # 或 .venv\Scripts\activate 在 Windows 上
pip install -r requirements.txt
```

---

## 免责声明

此工具自动化浏览器与 NotebookLM 的交互，以提高您的效率。但是，以下是一些友好的提醒：

**关于浏览器自动化：**
虽然我已内置了使自动化行为更自然的特征（类似人类的打字速度、自然延迟、鼠标移动），但我无法保证 Google 不会检测或标记自动化使用。我建议使用专用 Google 账户进行自动化，而不是您的首选账户——想想看，这就像网络爬虫一样：可能没问题，但最好还是小心为妙！

**关于 CLI 工具和 AI 代理：**
CLI 工具（如 Claude Code、Codex 和类似的 AI 辅助代理）非常强大，但它们可能会出错。请谨慎使用并保持警觉：
- 在提交或部署更改之前始终进行审查
- 在安全环境中首先进行测试
- 保留重要工作的备份
- 记住：AI 代理是助手，而不是无懈可击的先知

我构建此工具是为了我自己，因为我厌倦了在 NotebookLM 和我的编辑器之间进行复制粘贴。我希望它也能帮助其他人，但我不能对可能发生的问题、数据丢失或账户问题承担责任。自行判断并谨慎使用。

尽管如此，如果您遇到问题或有问题，请随时在 GitHub 上提交问题。我很乐意帮助您解决问题！

---

## 致谢

此技能受我的 [**NotebookLM MCP 服务器**](https://github.com/PleasePrompto/notebooklm-mcp) 启发，并提供了一个作为 Claude Code 技能的替代实现：
- 两者都使用 Patchright 进行浏览器自动化（MCP 使用 TypeScript/npm 生态系统，技能使用 Python）
- 技能版本直接在 Claude Code 中运行，无需 MCP 协议
- 无状态设计针对技能架构进行了优化

如果您需要：
- **持久会话** → 使用 [MCP 服务器](https://github.com/PleasePrompto/notebooklm-mcp)
- **多工具支持**（Codex、Cursor）→ 使用 [MCP 服务器](https://github.com/PleasePrompto/notebooklm-mcp)
- **快速 Claude Code 集成** → 使用此技能

---

## 总结

**没有此技能**：浏览器中的 NotebookLM → 复制答案 → 粘贴到 Claude → 复制下一个问题 → 返回浏览器...

**使用此技能**：Claude 直接进行研究 → 立即获取答案 → 编写正确的代码

停止复制粘贴。开始在 Claude Code 中直接获取准确、基于源信息的答案。

```bash
# 30 秒内开始
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
# 打开 Claude Code： "What are my skills?"
```

---

<div align="center">

作为我的 [NotebookLM MCP 服务器](https://github.com/PleasePrompto/notebooklm-mcp) 的 Claude Code 技能改编

在 Claude Code 中进行基于源信息和文档的研究

</div>
```