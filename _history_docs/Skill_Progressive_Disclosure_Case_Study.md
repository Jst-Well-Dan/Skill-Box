# Case Study：Skill 设计中的渐进式披露 (Progressive Disclosure)

## 0. 案例选择：Deep Reading Analyst (深度阅读分析师)

在 `Skill Box` 项目中，`immersive-reading/deep-reading-analyst-skill` 是体现“渐进式披露”设计模式的最佳案例。

**选择理由：**
1.  **非脚本依赖**：完全依赖 Prompt 和 Markdown 知识库，不包含任何 Python/JS 执行代码。
2.  **海量文本库**：包含 11 个以上的思维模型框架文件（SCQA, Crutial Thinking, Systems Thinking 等），如果一次性全部加载会极大消耗 Token 并干扰与 Context。
3.  **显式设计**：在该 Skill 的 `SKILL.md` 中 [Line 154] 明确定义了 "Progressive Disclosure Design" 章节。

---

## 1. 核心设计理念

渐进式披露（Progressive Disclosure）的核心在于**“仅在需要时加载信息”**。对于一个拥有庞大知识库的 Agent Skill，这意味着不能在初始 Prompt 中塞入所有规则和知识，而应该建立一个**分层索引系统**。

### 架构分层

该 Skill 将信息分为三个密度层级：

| 层级 | 内容形式 | 加载时机 | 作用 |
| :--- | :--- | :--- | :--- |
| **L1: 元数据层** | 文件名 + `description` | 始终可见 | 让 Agent 知道“我有这个能力”，用于路由匹配。 |
| **L2: 索引/路由层** | `SKILL.md` | 被唤醒时加载 | 提供“地图”，指导 Agent 在特定场景下该去查阅哪个具体文件。 |
| **L3: 知识/执行层** | `references/` 下的具体文件 | 按需加载 (Tool Call) | 包含具体的思维模型操作步骤、模板和详细指南。 |

---

## 2. 实现细节解析

### 第一层：入口索引 (SKILL.md)

`SKILL.md` 是这个 Skill 的“大脑”，它不包含具体的思维模型细节，而是定义了**判断逻辑**。

在该文件中，设计者没有写出 "SCQA 是什么" 或 "批判性思维的具体步骤"，而是定义了一个**深度等级表**：

```markdown
## Analysis Depth Levels

| Level | Time | Frameworks | Output |
|-------|------|-----------|---------|
| **Level 1 (Quick)** | 15min | SCQA + 5W2H | Structure + gaps... |
| **Level 2 (Standard)** | 30min | + Critical Thinking + Inversion | Argument evaluation... |
| ...
```

以及一个**文件映射表**：

```markdown
## Framework Arsenal

### Level 1: Quick Analysis
- 📋 **SCQA** -> `references/frameworks/quick/scqa.md`
- 🔍 **5W2H** -> `references/frameworks/quick/5w2h.md`

### Level 2: Standard Analysis
- 🎯 **Critical Thinking** -> `references/frameworks/standard/critical_thinking.md`
...
```

**设计意图**：Agent 读取 `SKILL.md` 后，只知道“如果用户要素描（Level 1），我需要去读 `scqa.md`”，而此时 Agent 的 Context 中还没有 SCQA 的具体内容。

### 第二层：按需加载 (On-Demand Loading)

当用户请求：“帮我快速分析这篇关于 AI 的文章”时：

1.  **Agent 思考**：用户需要 "快速分析" -> 对应 "Level 1" -> 需要 `SCQA` 和 `5W2H` 模型。
2.  **Agent 动作**：调用 `view_file` 读取 `references/frameworks/quick/scqa.md`。
3.  **执行分析**：读取到 SCQA 的具体指南（情境-冲突-问题-答案）后，以此为 Context 处理用户文章。

**优势**：此时 Agent 的 Context 中**没有** Level 3 的“系统思维”或 Level 4 的“交叉对比矩阵”内容。这保持了 Context 的纯净，避免了模型在简单的任务中发生幻觉（例如在只需要简单总结时强行套用复杂的系统循环图）。

### 第三层：动态组合 (Dynamic Composition)

该设计允许 Agent 根据对话动态组合知识库，而不是死板地执行脚本。

例如用户说：“这篇文章的逻辑好像有问题，但也很有趣。”
Agent 可以组合：
-   `references/frameworks/standard/critical_thinking.md` (检查逻辑漏洞)
-   `references/frameworks/quick/scqa.md` (提取核心论点)

这种组合在 `SKILL.md` 的 "Advanced Usage" 章节被显式鼓励，实现了静态文本库的动态能力。

---

## 3. 实际效益 (Benefits)

1.  **Token 效率**：只消耗当前任务所需知识的 Token。全量知识库可能有 20k tokens，但单次执行可能只需要 2k tokens 的规则。
2.  **专注度提升**：LLM 在 Context 越短、干扰越少的情况下，遵循指令的效果越好。不加载无关的“深度思维模型”能防止 Agent 过度解读简单文本。
3.  **可维护性**：
    -   如果要修改 SCQA 的定义，只需修改 `references/.../scqa.md` 一个文件。
    -   `SKILL.md` 不需要变更，因为它只持有引用地址。
4.  **可扩展性**：可以随时在 `references/` 下添加新的思维模型（如 SWOT, Pestel），只需在 `SKILL.md` 加一行索引，不会破坏现有的 Prompt 结构。

## 4. 总结

`deep-reading-analyst-skill` 展示了如何将一个庞大的“分析方法论”拆解为可被 AI 动态调用的文件系统。它通过**索引文件 (SKILL.md)** 与**详情文件 (References)** 的分离，完美实现了 Prompt Engineering 中的渐进式披露原则。
