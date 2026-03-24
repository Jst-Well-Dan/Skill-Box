---
name: nlm-skill
description: "Google NotebookLM 的专家指南及接口工具（包含 `nlm` CLI 及 MCP 服务器）。当用户希望以编程方式与 NotebookLM 交互时使用，功能包括：创建/管理笔记本，添加数据源（URL、Youtube、文本、Google Drive），生成内容（播客、报告、测验、抽认卡、思维导图、幻灯片、视频、数据表格等），进行深入研究，与数据源对话，或进行工作流自动化。"
version: "0.5.5"
---

# NotebookLM CLI 与 MCP 专家

本技能为您提供如何通过 `nlm` 命令行界面及 MCP 工具来使用 NotebookLM 的全面指引。

## 工具检测规则 (非常关键！)

**操作前务必确认哪些工具可用：**
1. **检查 MCP 工具**：寻找以 `mcp__notebooklm-mcp__*` 或 `mcp_notebooklm_*` 开头的工具。
2. **如果同时存在 MCP 与 CLI 工具**：必须先**询问用户**偏好哪种方式再继续。
3. **如果只有 MCP 可用**：直接使用 MCP 调用。
4. **如果只有 CLI 可用**：通过 Bash 执行命令行。

_（完整细节文档和命令行列表详见对应的源英文文档）_
