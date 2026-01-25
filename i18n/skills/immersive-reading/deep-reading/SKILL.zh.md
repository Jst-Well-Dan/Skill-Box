---
name: deep-reading
description: Deep reading collaborative system using multi-layered AI agents to help transform articles from "read" to "understood" to "mastered", with actionable plans. Use when users need to deeply understand complex articles/papers, organize reading notes systematically, think critically about content, discover hidden logical issues and assumptions, or transform knowledge into action plans. Trigger keywords - deep reading, 深度阅读, critical thinking, 批判性思维, reading notes, 阅读笔记, article analysis, 文章分析, Socratic questioning, 苏格拉底提问, action plan, 行动计划
---

# Deep Reading - 深度阅读协作系统

深度阅读协作系统,通过多层次的 AI agents 协作,帮助你将文章从"读过"到"读懂"再到"读透",最终转化为可执行的行动计划。

## 使用场景

使用本 skill 当用户需要:
- 深度理解一篇复杂的文章、论文或长文
- 将阅读笔记系统化整理
- 批判性思考文章内容
- 发现隐藏的逻辑问题和假设
- 将知识转化为行动计划

## 核心功能

系统包含三层协作架构:

### 🔍 内化层(读薄) - 顺序执行
- **整理者**: 生成结构化的 Markdown 笔记
- **转述者**: 使用 SCQA + 费曼技巧通俗化解释

### 🎯 拓展层(读厚) - 并行执行
- **诊断引擎**: 批判性分析 + 逻辑剖析 (后台)
- **苏格拉底**: 引导性提问,不给答案 (前台)

### 🚀 产出层(行动)
- **规划师**: 将认知转化为具体的行动计划

## Response Pattern

当用户请求深度阅读分析时:

1. **接收输入**:
   ```
   - 检查是否提供了文章路径和草稿笔记路径
   - 如果没有,询问用户或请求粘贴内容
   - 解析可选参数 (--internalize-only, --expand-only, --no-action)
   ```

2. **确认配置**:
   ```
   - 确认要启用的层次 (默认全部启用)
   - 确认输出目录 (默认 outputs/[timestamp]/)
   - 显示即将执行的流程
   ```

3. **执行处理流程**:
   ```
   步骤 3.1: 内化层 (如果启用)
   - 调用 Task tool, subagent_type: "general-purpose"
     - Agent 1: 读取 references/agents/organizer.md
     - 输入: 原文 + 草稿
     - 输出: organized-notes.md

   - 调用 Task tool, subagent_type: "general-purpose"
     - Agent 2: 读取 references/agents/explainer.md
     - 输入: organized-notes.md
     - 输出: explained-notes.md

   步骤 3.2: 拓展层 (如果启用, 并行执行)
   - 并行调用两个 Task tools:
     - Agent 3: 读取 references/agents/diagnosis.md
       输入: organized-notes.md + explained-notes.md
       输出: diagnosis-report.json

     - Agent 4: 读取 references/agents/socratic.md
       输入: diagnosis-report.json
       输出: socratic-questions.md

   步骤 3.3: 产出层 (如果启用)
   - 调用 Task tool, subagent_type: "general-purpose"
     - Agent 5: 读取 references/agents/planner.md
     - 输入: 所有前序分析结果
     - 输出: action-plan.md
   ```

4. **整合输出**:
   ```
   - 创建时间戳目录 (如 outputs/2026-01-21-14-20/)
   - 保存所有生成的文件
   - 生成汇总报告 SUMMARY.md
   - 向用户报告:
     ✓ 文件列表
     ✓ 输出目录路径
     ✓ 关键发现摘要
   ```

5. **可选: 交互式对话**:
   ```
   如果用户请求,基于 socratic-questions.md 进行深度对话
   ```

## 详细文档

- **完整工作流程**: 参考 `references/workflow.md`
- **Agent 提示词**:
  - `references/agents/organizer.md` - 内容整理专家
  - `references/agents/explainer.md` - 费曼技巧转述者
  - `references/agents/diagnosis.md` - 批判性诊断引擎
  - `references/agents/socratic.md` - 苏格拉底式提问者
  - `references/agents/planner.md` - 行动规划师

## 使用示例

```bash
# 完整流程
/deep-reading examples/sample-article.md examples/sample-draft.md

# 仅内化层
/deep-reading --internalize-only article.md draft.md

# 仅拓展层
/deep-reading --expand-only article.md draft.md

# 无行动计划
/deep-reading --no-action article.md draft.md
```

## 输出文件

所有输出保存在 `outputs/[timestamp]/`:
- `organized-notes.md` - 结构化笔记
- `explained-notes.md` - 通俗化解释
- `diagnosis-report.json` - 诊断报告
- `socratic-questions.md` - 苏格拉底式问题
- `action-plan.md` - 行动计划
- `SUMMARY.md` - 汇总报告

## 依赖

- Claude Code CLI
- Task tool (用于调用 sub-agents)
- 文件系统访问权限

---

**提示**: 首次使用建议先查看 `examples/` 目录下的示例文件,了解输入格式。完整架构设计参见项目根目录的 `architecture-design.md`。