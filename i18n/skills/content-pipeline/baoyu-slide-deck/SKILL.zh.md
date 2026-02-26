---
name: baoyu-slide-deck
description: 从内容生成专业的幻灯片演示图像。创建带有样式说明的大纲，然后生成单个幻灯片图像。当用户请求“创建幻灯片”、“制作演示文稿”、“生成演示文稿”、“幻灯片演示文稿”或“PPT”时使用。
---

# 幻灯片演示文稿生成器

将内容转换为专业的幻灯片演示文稿图像。

## 使用方法

```bash
/baoyu-slide-deck 路径/to/content.md
/baoyu-slide-deck 路径/to/content.md --style sketch-notes
/baoyu-slide-deck 路径/to/content.md --audience executives
/baoyu-slide-deck 路径/to/content.md --lang zh
/baoyu-slide-deck 路径/to/content.md --slides 10
/baoyu-slide-deck 路径/to/content.md --outline-only
/baoyu-slide-deck  # 然后粘贴内容
```

## 脚本目录

**代理执行说明**：
1. 确定此 SKILL.md 文件的目录路径为 `SKILL_DIR`
2. 脚本路径 = `${SKILL_DIR}/scripts/<script-name>.ts`

| 脚本 | 目的 |
|--------|---------|
| `scripts/merge-to-pptx.ts` | 将幻灯片合并到 PowerPoint |
| `scripts/merge-to-pdf.ts` | 将幻灯片合并到 PDF |

## 选项

| 选项 | 描述 |
|--------|-------------|
| `--style <name>` | 视觉样式：预设名称、`custom` 或自定义样式名称 |
| `--audience <type>` | 目标：初学者、中级、专家、高管、普通 |
| `--lang <code>` | 输出语言（en、zh、ja 等） |
| `--slides <number>` | 目标幻灯片数量（推荐 8-25，最大 30） |
| `--outline-only` | 仅生成大纲，跳过图像生成 |
| `--prompts-only` | 生成大纲 + 提示，跳过图像 |
| `--images-only` | 从现有提示目录生成图像 |
| `--regenerate <N>` | 重新生成特定幻灯片：`--regenerate 3` 或 `--regenerate 2,5,8` |

**内容长度与幻灯片数量**：
| 内容 | 幻灯片 |
|---------|--------|
| < 1000 字 | 5-10 |
| 1000-3000 字 | 10-18 |
| 3000-5000 字 | 15-25 |
| > 5000 字 | 20-30（考虑拆分） |

## 样式系统

### 预设

| 预设 | 尺寸 | 最佳用途 |
|--------|------------|----------|
| `blueprint`（默认） | 网格 + 冷色调 + 技术感 + 平衡 | 建筑学、系统设计 |
| `chalkboard` | 有机 + 暖色调 + 手写 + 平衡 | 教育、教程 |
| `corporate` | 清洁 + 专业 + 几何 + 平衡 | 投资者演示文稿、提案 |
| `minimal` | 清洁 + 中性 + 几何 + 简约 | 高管简报 |
| `sketch-notes` | 有机 + 暖色调 + 手写 + 平衡 | 教育、教程 |
| `watercolor` | 有机 + 暖色调 + 人文 + 简约 | 生活方式、健康 |
| `dark-atmospheric` | 清洁 + 深色 + 编辑 + 平衡 | 娱乐、游戏 |
| `notion` | 清洁 + 中性 + 几何 + 稠密 | 产品演示、SaaS |
| `bold-editorial` | 清洁 + 鲜艳 + 编辑 + 平衡 | 产品发布、演讲 |
| `editorial-infographic` | 清洁 + 冷色调 + 编辑 + 稠密 | 科技解释、研究 |
| `fantasy-animation` | 有机 + 鲜艳 + 手写 + 简约 | 教育、故事讲述 |
| `intuition-machine` | 清洁 + 冷色调 + 技术 + 稠密 | 技术文档、学术 |
| `pixel-art` | 像素 + 鲜艳 + 技术 + 平衡 | 游戏、开发者演讲 |
| `scientific` | 清洁 + 冷色调 + 技术 + 稠密 | 生物学、化学、医学 |
| `vector-illustration` | 清洁 + 鲜艳 + 人文 + 平衡 | 创意、儿童内容 |
| `vintage` | 纸张 + 暖色调 + 编辑 + 平衡 | 历史、遗产 |

### 样式维度

| 维度 | 选项 | 描述 |
|-----------|---------|-------------|
| **纹理** | clean、grid、organic、pixel、paper | 视觉纹理和背景处理 |
| **氛围** | professional、warm、cool、vibrant、dark、neutral | 色温和国家风格 |
| **字体** | geometric、humanist、handwritten、editorial、technical | 标题和正文文本样式 |
| **密度** | minimal、balanced、dense | 每张幻灯片的信息密度 |

完整规格：`references/dimensions/*.md`

### 自动样式选择

| 内容信号 | 预设 |
|-----------------|--------|
| tutorial、learn、education、guide、beginner | `sketch-notes` |
| classroom、teaching、school、chalkboard | `chalkboard` |
| architecture、system、data、analysis、technical | `blueprint` |
| creative、children、kids、cute | `vector-illustration` |
| briefing、academic、research、bilingual | `intuition-machine` |
| executive、minimal、clean、simple | `minimal` |
| saas、product、dashboard、metrics | `notion` |
| investor、quarterly、business、corporate | `corporate` |
| launch、marketing、keynote、magazine | `bold-editorial` |
| entertainment、music、gaming、atmospheric | `dark-atmospheric` |
| explainer、journalism、science communication | `editorial-infographic` |
| story、fantasy、animation、magical | `fantasy-animation` |
| gaming、retro、pixel、developer | `pixel-art` |
| biology、chemistry、medical、scientific | `scientific` |
| history、heritage、vintage、expedition | `vintage` |
| lifestyle、wellness、travel、artistic | `watercolor` |
| 默认 | `blueprint` |

## 设计理念

为 **阅读和分享** 而设计的演示文稿，而不是现场演示：
- 每张幻灯片无需口头说明即可自解释
- 滚动时的逻辑流程
- 每张幻灯片内包含所有必要上下文
- 优化用于社交媒体分享

有关以下内容，请参阅 `references/design-guidelines.md`：
- 目标受众原则
- 视觉层次结构
- 内容密度指南
- 颜色和字体选择
- 字体推荐

请参阅 `references/layouts.md` 了解布局选项。

## 文件管理

### 输出目录

```
slide-deck/{topic-slug}/
├── source-{slug}.{ext}
├── outline.md
├── prompts/
│   └── 01-slide-cover.md, 02-slide-{slug}.md, ...
├── 01-slide-cover.png, 02-slide-{slug}.png, ...
├── {topic-slug}.pptx
└── {topic-slug}.pdf
```

**Slug**：提取主题（2-4 个单词，短横线分隔法）。例如：“机器学习简介”→ `intro-machine-learning`

**冲突处理**：请参阅步骤 1.3 了解现有内容检测和用户选项。

## 语言处理

**检测优先级**：
1. `--lang` 标志（显式）
2. EXTEND.md `language` 设置
3. 用户的对话语言（输入语言）
4. 源内容语言

**规则**：所有响应都使用用户的首选语言：
- 问题和对确认
- 进度报告
- 错误消息
- 完成摘要

技术术语（样式名称、文件路径、代码）保持英文。

## 工作流程

复制此检查表，并在完成任务时勾选：

```
幻灯片演示文稿进度：
- [ ] 第 1 步：设置与分析
  - [ ] 1.1 加载首选项
  - [ ] 1.2 分析内容
  - [ ] 1.3 检查现有内容 ⚠️ 必需
- [ ] 第 2 步：确认 ⚠️ 必需（第 1 轮，可选第 2 轮）
- [ ] 第 3 步：生成大纲
- [ ] 第 4 步：审查大纲（条件）
- [ ] 第 5 步：生成提示
- [ ] 第 6 步：审查提示（条件）
- [ ] 第 7 步：生成图像
- [ ] 第 8 步：合并到 PPTX/PDF
- [ ] 第 9 步：输出摘要
```

### 流程

```
输入 → 首选项 → 分析 → [检查现有内容?] → 确认（1-2 轮）→ 大纲 → [审查大纲?] → 提示 → [审查提示?] → 图像 → 合并 → 完成
```

### 第 1 步：设置与分析

**1.1 加载首选项（EXTEND.md）**

使用 Bash 检查 EXTEND.md 的存在（优先级顺序）：

```bash
# 首先检查项目级别的
test -f .baoyu-skills/baoyu-slide-deck/EXTEND.md && echo "project"

# 然后用户级别的（跨平台：$HOME 在 macOS/Linux/WSL 上有效）
test -f "$HOME/.baoyu-skills/baoyu-slide-deck/EXTEND.md" && echo "user"
```

┌──────────────────────────────────────────────────┬───────────────────┐
│                       路径                       │     位置          │
├──────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-slide-deck/EXTEND.md         │ 项目目录          │
├──────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-slide-deck/EXTEND.md   │ 用户家目录        │
└──────────────────────────────────────────────────┴───────────────────┘

**当找到 EXTEND.md 时** → 读取、解析、**向用户输出摘要**：

````
📋 从 [完整路径] 加载首选项
├─ 样式：[预设/自定义名称]
├─ 目标受众：[目标受众或 "自动检测"]
├─ 语言：[语言或 "自动检测"]
└─ 审查：[启用/禁用]
```

**当没有找到 EXTEND.md 时** → 首次设置使用 AskUserQuestion 或使用默认值。

**EXTEND.md 支持**：首选样式 | 自定义维度 | 默认目标受众 | 语言首选项 | 审查首选项

架构：`references/config/preferences-schema.md`

**1.2 分析内容**

1. 保存源内容（如果粘贴，则保存为 `source.md`）
2. 根据 `references/analysis-framework.md` 进行内容分析
3. 分析内容信号以获得样式建议
4. 检测源语言
5. 确定推荐的幻灯片数量
6. 从内容生成主题 slug

**1.3 检查现有内容** ⚠️ 必需

**必须在此步骤之前执行**。

使用 Bash 检查输出目录是否存在：

```bash
test -d "slide-deck/{topic-slug}" && echo "exists"
```

**如果目录存在**，则使用 AskUserQuestion：

````
header: "现有内容"
question: "现有内容发现。如何处理？"
options:
  - label: "重新生成大纲"
    description: "保留图像，仅重新生成大纲"
  - label: "重新生成图像"
    description: "保留大纲，仅重新生成图像"
  - label: "备份并重新生成"
    description: "备份到 {slug}-backup-{timestamp}，然后重新生成所有内容"
  - label: "退出"
    description: "取消，保持现有内容不变"
```

**保存到 `analysis.md`**：
- 主题、目标受众、内容信号
- 基于自动样式选择推荐的样式
- 基于内容长度的推荐幻灯片数量
- 语言检测

### 第 2 步：确认 ⚠️ 必需

**两轮确认**：第 1 轮始终，第 2 轮仅在选择“自定义维度”时。

**语言**：使用用户的输入语言或保存的语言首选项。

**显示摘要**：
- 内容类型 + 识别的主题
- 语言：[来自 EXTEND.md 或检测]
- **推荐样式**：[预设]（基于内容分析）
- **推荐幻灯片数量**：[N]（基于内容长度）

#### 第 1 轮（始终）

**使用 AskUserQuestion** 对所有 5 个问题进行提问：

**问题 1：样式**

````
header: "样式"
question: "此演示文稿的视觉样式是哪个？"
options:
  - label: "{recommended_preset}（推荐）"
    description: "基于内容分析的最佳匹配"
  - label: "{alternative_preset}"
    description: "[替代样式描述]"
  - label: "自定义维度"
    description: "分别选择纹理、氛围、字体、密度"
````

**问题 2：目标受众**

````
header: "目标受众"
question: "主要读者是谁？"
options:
  - label: "普通读者（推荐）"
    description: "广泛吸引力，易于理解的内容"
  - label: "初学者/学习者"
    description: "教育重点，清晰的解释"
  - label: "专家/专业人士"
    description: "技术深度，领域知识"
  - label: "高管"
    description: "高层见解，细节最少"
````

**问题 3：幻灯片数量**

````
header: "幻灯片"
question: "多少张幻灯片？"
options:
  - label: "{N} 幻灯片（推荐）"
    description: "基于内容长度"
  - label: "更少（{N-3} 幻灯片）"
    description: "更紧凑，细节更少"
  - label: "更多（{N+3} 幻灯片）"
    description: "更详细的分解"
````

**问题 4：审查大纲**

````
header: "大纲"
question: "在生成提示之前审查大纲？"
options:
  - label: "是，审查大纲（推荐）"
    description: "审查幻灯片标题和结构"
  - label: "否，跳过大纲审查"
    description: "直接进入提示生成"
````

**问题 5：审查提示**

````
header: "提示"
question: "在生成图像之前审查提示？"
options:
  - label: "是，审查提示（推荐）"
    description: "审查图像生成提示"
  - label: "否，跳过提示审查"
    description: "直接进入图像生成"
````

#### 第 2 轮（仅在“自定义维度”选择时）

**使用 AskUserQuestion** 对所有 4 个维度进行提问：

**问题 1：纹理**

````
header: "纹理"
question: "哪种视觉纹理？"
options:
  - label: "clean"
    description: "纯固体颜色，无纹理"
  - label: "grid"
    description: "细微的网格叠加，技术感"
  - label: "organic"
    description: "柔软的纹理，手绘感"
  - label: "pixel"
    description: "块状像素，8 位美学"
````
(Note: "paper" 可通过 Other 获取)

**问题 2：氛围**

````
header: "氛围"
question: "哪种颜色氛围？"
options:
  - label: "professional"
    description: "冷色调-中性，海军蓝/金色"
  - label: "warm"
    description: "地球色调，友好"
  - label: "cool"
    description: "蓝色、灰色，分析性"
  - label: "vibrant"
    description: "高饱和度，大胆"
````
(Note: "dark"、"neutral" 可通过 Other 获取)

**问题 3：字体**

````
header: "字体"
question: "哪种字体样式？"
options:
  - label: "geometric"
    description: "现代无衬线，清洁"
  - label: "humanist"
    description: "友好，易读"
  - label: "handwritten"
    description: "记号笔/画笔，有机"
  - label: "editorial"
    description: "杂志风格，戏剧性"
````
(Note: "technical" 可通过 Other 获取)

**问题 4：密度**

````
header: "密度"
question: "信息密度？"
options:
  - label: "balanced（推荐）"
    description: "每张幻灯片 2-3 个关键点"
  - label: "minimal"
    description: "一个焦点点，最大空白"
  - label: "dense"
    description: "多个数据点，紧凑"
````

**在第 2 轮之后**：将自定义维度作为样式配置存储。

**在确认之后**：
1. 更新 `analysis.md` 以包含确认的首选项
2. 存储 `skip_outline_review` 标志（来自问题 4）
3. 存储 `skip_prompt_review` 标志（来自问题 5）
4. → 第 3 步

### 第 3 步：生成大纲

使用第 2 步中确认的样式创建大纲。

**样式解析**：
- 如果选择预设 → 读取 `references/styles/{preset}.md`
- 如果自定义维度 → 读取 `references/dimensions/` 中的维度文件并组合

**生成**：
1. 根据 `references/outline-template.md` 进行结构
2. 从样式或维度构建 STYLE_INSTRUCTIONS
3. 应用确认的目标受众、语言