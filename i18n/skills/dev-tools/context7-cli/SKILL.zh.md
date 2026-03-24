---
name: context7-cli
description: 使用 ctx7 CLI 获取库文档，管理 AI 编码技能，并配置 Context7 MCP。当用户需要获取任何库的最新文档、安装/搜索/生成技能或为 AI 编码助手设置 Context7 时触发。
---

# ctx7 CLI

Context7 CLI 提供三个核心功能：获取最新的库文档，管理 AI 编码技能，以及为编辑器设置 Context7 MCP。

请在运行命令前确保 CLI 是最新版本：

```bash
npm install -g ctx7@latest
```

或直接运行（免安装）：

```bash
npx ctx7@latest <command>
```

## 技能涵盖范围

- **文档 (Documentation)** — 获取任何库的最新文档。在编写代码、验证 API 签名或训练数据可能过时时使用。
- **技能管理 (Skills management)** — 安装、搜索、推荐、列出、移除和生成 AI 编码技能。
- **配置 (Setup)** — 为 Claude Code / Cursor / OpenCode 配置 Context7 MCP。
