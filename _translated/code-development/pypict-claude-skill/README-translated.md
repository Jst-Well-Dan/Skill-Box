<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:11:56
翻译模型: glm-4-flash
原文大小: 12,472 字符
-->

# PICT 测试设计器 - Claude 技能

一个用于使用 PICT（成对独立组合测试）设计全面测试用例的 Claude 技能。此技能通过成对组合测试，在保持高覆盖率的同时，以最少的测试用例进行系统化测试用例设计。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude](https://img.shields.io/badge/Claude-Skill-blue.svg)](https://claude.ai)

## 🎯 什么是 PICT？

PICT（成对独立组合测试）是由微软开发的一种组合测试工具。它生成测试用例，有效地覆盖所有参数的成对组合，同时与穷举测试相比，大大减少了总的测试数量。

**示例：** 测试一个具有 8 个参数且每个参数有 3-5 个值的系统：
- 穷举测试：**25,920 个测试用例**
- PICT 成对测试：**~30 个测试用例**（减少 99.88%！）

## 🚀 功能

- **自动化测试用例生成**：将需求转换为结构化的 PICT 模型
- **基于约束的测试**：应用业务规则以消除无效组合
- **预期输出生成**：自动确定每个测试用例的预期结果
- **全面覆盖**：确保测试所有成对参数交互
- **多个领域**：适用于软件功能、API、网页表单、配置等

## 📋 目录

- [安装](#安装)
  - [先决条件](#先决条件)
  - [在 Claude Code CLI 中安装](#在-claude-code-cli-中安装)
  - [在 Claude Code Desktop 中安装](#在-claude-code-desktop-中安装)
- [快速入门](#快速入门)
- [示例：ATM 系统测试](#示例-atm-系统测试)
- [工作原理](#工作原理)
- [用例](#用例)
- [致谢](#致谢)
- [贡献](#贡献)
- [许可证](#许可证)

## 🔧 安装

### 先决条件

- Claude Code CLI 或 Claude Code Desktop
- （可选）Python 3.7+ 和 `pypict` 以进行高级使用

### 安装方法

Claude Code 技能可以通过插件市场或手动将其放置在 `.claude/skills/` 目录中安装。

### 方法 1：通过 Claude Code 插件市场安装（最简单）🌟

直接通过 Claude Code 的插件系统安装：

```bash
# 添加市场
/plugin marketplace add omkamal/pypict-claude-skill

# 安装插件
/plugin install pict-test-designer@pypict-claude-skill
```

这将自动安装技能并保持其更新。该技能将在所有项目中可用。

### 方法 2：从 GitHub 安装（手动）

**个人使用（所有项目）：**

```bash
# 将存储库克隆到您的个人技能目录
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer

# 重新启动 Claude Code 以加载技能
# 技能现在将在所有项目中可用
```

**项目特定使用：**

```bash
# 从您的项目目录
git clone https://github.com/omkamal/pypict-claude-skill.git .claude/skills/pict-test-designer

# 如果不想提交，请将其添加到 .gitignore
echo ".claude/skills/" >> .gitignore

# 或者提交以与您的团队共享
git add .claude/skills/pict-test-designer
git commit -m "添加 PICT 测试设计器技能"
```

### 方法 3：通过 Git Submodule 安装（团队共享）

如果您想通过版本控制与您的团队共享此技能：

```bash
# 从您的项目目录
git submodule add https://github.com/omkamal/pypict-claude-skill.git .claude/skills/pict-test-designer
git commit -m "将 PICT 测试设计器技能作为子模块添加"

# 团队成员克隆时：
git clone --recurse-submodules <your-repo-url>

# 或者如果已经克隆：
git submodule update --init --recursive
```

### 方法 4：从发布版下载最小包

从 [GitHub 发布版](https://github.com/omkamal/pypict-claude-skill/releases) 下载预打包的最小安装包：

```bash
# 从发布版下载最新的最小包
wget https://github.com/omkamal/pypict-claude-skill/releases/latest/download/pict-test-designer-minimal.zip

# 解压并安装以供个人使用
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal ~/.claude/skills/pict-test-designer

# 或者为项目特定使用
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal .claude/skills/pict-test-designer
```

**包含内容：** SKILL.md、LICENSE、references/（语法和示例）
**排除内容：** 完整示例、辅助脚本、扩展文档
**大小：** ~9 KB | **最新版本：** [查看发布版](https://github.com/omkamal/pypict-claude-skill/releases)

### 方法 5：下载完整存储库

1. **从 GitHub 下载存储库** 作为 ZIP 文件
2. **提取到技能目录**：

```bash
# 对于个人使用（所有项目）
unzip pypict-claude-skill-main.zip
mv pypict-claude-skill-main ~/.claude/skills/pict-test-designer

# 对于项目特定使用
unzip pypict-claude-skill-main.zip
mv pypict-claude-skill-main .claude/skills/pict-test-designer
```

### 验证安装

安装后，重新启动 Claude Code。技能将在相关时自动加载。您可以通过询问 Claude 来验证：

```
您是否有访问 pict-test-designer 技能的权限？
```

或者简单地开始使用它：

```
为具有用户名、密码和记住我复选框的登录功能设计测试用例。
```

## 🚀 快速入门

安装后，您可以通过简单地询问 Claude 来使用此技能：

```
为具有用户名、密码和记住我复选框的登录功能设计测试用例。
```

Claude 将：
1. 分析需求
2. 识别参数和值
3. 生成具有约束的 PICT 模型
4. 创建具有预期输出的测试用例
5. 以格式化的表格形式呈现结果

## 📊 示例：ATM 系统测试

此存储库包含测试 ATM 系统的完整真实世界示例。请参阅 [examples](examples/) 目录中的：

- **[ATM 规范](examples/atm-specification.md)**：完整的 ATM 系统规范，包含 11 个部分，涵盖硬件、软件、安全性和功能需求
- **[ATM 测试计划](examples/atm-test-plan.md)**：使用 PICT 方法生成的全面测试计划，包含 31 个测试用例（从 25,920 个可能的组合中减少）

### ATM 示例摘要

**系统参数：**
- 交易类型（5）：取款、存款、余额查询、转账、PIN 更改
- 卡类型（3）：EMV 芯片、磁条、无效
- PIN 状态（4）：有效、无效尝试 1-3
- 账户类型（3）：支票账户、储蓄账户、两者
- 交易金额（4）：在限制内、最大值、超过交易、超过每日
- 现金可用性（3）：充足、不足、空
- 网络状态（3）：主网络、备份、断开连接
- 卡状态（3）：良好、损坏、过期

**测试结果：**
- 可能的组合总数：**25,920**
- 生成的 PICT 测试用例：**31**
- **减少：99.88%**
- 覆盖率：所有成对（双向）交互
- 测试执行时间：从数周减少到数小时

### 运行 ATM 示例

```bash
# 在 Claude Code
Ask: "使用 pict-test-designer 技能分析 examples/atm-specification.md 中的 ATM 规范并生成测试用例"
```

## 🔍 工作原理

### 1. 需求分析

Claude 分析您的需求以识别：
- **参数**：输入变量、配置选项、环境因素
- **值**：使用等价类划分的可能值
- **约束**：业务规则和依赖关系
- **预期结果**：对于不同的组合应该发生什么

### 2. PICT 模型生成

创建一个结构化模型：

```
# 参数
Browser: Chrome, Firefox, Safari
OS: Windows, MacOS, Linux
Memory: 4GB, 8GB, 16GB

# 约束
IF [OS] = "MacOS" THEN [Browser] <> "IE";
IF [Memory] = "4GB" THEN [OS] <> "MacOS";
```

### 3. 测试用例生成

生成覆盖所有成对组合的最小测试用例：

| 测试 # | 浏览器 | OS | 内存 | 预期输出 |
|--------|---------|----|---------|-----------------------------|
| 1 | Chrome | Windows | 4GB | 成功 |
| 2 | Firefox | MacOS | 8GB | 成功 |
| 3 | Safari | Linux | 16GB | 成功 |
| ... | ... | ... | ... | ... |

### 4. 预期输出确定

对于每个测试用例，Claude 根据以下内容确定预期结果：
- 业务需求
- 代码逻辑
- 有效的/无效的组合

## 🎯 用例

### 软件测试
- 多参数的功能测试
- API 端点测试
- 数据库查询测试
- 算法验证

### 配置测试
- 系统配置组合
- 功能标志测试
- 环境设置验证
- 浏览器兼容性测试

### 网络应用程序测试
- 表单验证
- 用户身份验证流程
- 电子商务结账流程
- 购物车功能

### 移动测试
- 设备和操作系统组合
- 屏幕尺寸和方向
- 网络条件
- 应用程序权限

### 硬件测试
- 设备兼容性
- 接口测试
- 协议验证
- 在不同条件下的性能

## 📚 文档

- **[SKILL.md](SKILL.md)**：完整的技能文档，包括工作流程和最佳实践
- **[PICT 语法参考](references/pict_syntax.md)**：完整的语法指南（待创建）
- **[示例](references/examples.md)**：跨领域的真实世界示例（待创建）
- **[辅助脚本](scripts/pict_helper.py)**：PICT 的 Python 工具（待创建）

## 💡 最佳结果提示

### 良好的参数名称
✅ 使用描述性名称：`AuthMethod`、`UserRole`、`PaymentType`
✅ 应用等价类划分：`FileSize: 小、中、大`
✅ 包含边界值：`Age: 0, 17, 18, 65, 66`
✅ 添加负值：`Amount: ~-1, 0, 100, ~999999`

### 编写约束
✅ 记录理由：`# Safari 仅在 MacOS 上可用`
✅ 从简单开始，逐步添加
✅ 测试约束是否按预期工作

### 预期输出
✅ 要具体：`登录成功，用户被重定向到仪表板`
❌ 不要模糊：`工作`或`成功`

## 🙏 致谢

此技能建立在以下出色工作的基础上：

- **[Microsoft PICT](https://github.com/microsoft/pict)**：微软研究开发的原始成对独立组合测试工具
- **[pypict](https://github.com/kmaehashi/pypict)**：由 Kenichi Maehashi 开发的 PICT 的 Python 绑定
- **社区贡献者**：所有帮助改进 PICT 工具的贡献者

### 关于 PICT

PICT 由微软研究部的 Jacek Czerwonka 开发。它是一个强大的组合测试工具，已在微软内部广泛用于测试具有多个交互参数的复杂系统。

**参考：**
- [PICT：成对独立组合测试](https://github.com/microsoft/pict)
- [成对测试方法](https://www.pairwisetesting.com/)
- [组合测试设计](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software)

## 🤝 贡献

欢迎贡献！以下是如何帮助您的方式：

1. **分支存储库**
2. **创建功能分支**：`git checkout -b feature/amazing-feature`
3. **进行更改**
4. **添加示例或文档**
5. **提交更改**：`git commit -m '添加惊人的功能'`
6. **推送到分支**：`git push origin feature/amazing-feature`
7. **打开拉取请求**

### 贡献领域

- 更多真实世界示例
- 增强的约束模式
- 支持更多测试领域
- 改进文档
- 错误修复和改进

## 📝 许可证

此项目采用 MIT 许可证 - 请参阅 [LICENSE](LICENSE) 文件以获取详细信息。

微软的底层 PICT 工具也采用 MIT 许可证。

## 🔗 链接

- **Claude AI**：https://claude.ai
- **Claude 文档**：https://docs.claude.com
- **Microsoft PICT**：https://github.com/microsoft/pict
- **pypict**：https://github.com/kmaehashi/pypict
- **在线 PICT 工具**：
  - https://pairwise.yuuniworks.com/
  - https://pairwise.teremokgames.com/

## 📧 支持

如果您遇到问题或有问题：

1. 检查 [examples](examples/) 目录以获取参考
2. 查阅 [SKILL.md](SKILL.md) 文档
3. 在 GitHub 上打开问题
4. 加入问题部分的讨论

## 🌟 星此存储库

如果您发现此技能很有用，请星此存储库以帮助其他人发现它！

---

**用 ❤️ 为 Claude 和测试社区制作**

**由 Microsoft PICT 和 pypict 驱动**