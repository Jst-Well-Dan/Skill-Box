---
name: baoyu-cover-image
description: Generates article cover images with 4 dimensions (type, style, text, mood) and 20 hand-drawn styles. Supports cinematic (2.35:1), widescreen (16:9), and square (1:1) aspects. Use when user asks to "generate cover image", "create article cover", "make cover", or mentions "封面图".
---

# 封面图生成器

生成具有 4 维度定制（类型、风格、文本、情绪）和 20 种手绘风格的优雅文章封面图。

## 使用方法

```bash
# 根据内容自动选择所有维度
/baoyu-cover-image 路径/to/article.md

# 快速模式：跳过确认，使用自动选择
/baoyu-cover-image article.md --quick

# 指定维度
/baoyu-cover-image article.md --type conceptual --style blueprint
/baoyu-cover-image article.md --text title-subtitle --mood bold

# 仅视觉（无标题文本）
/baoyu-cover-image article.md --no-title

# 直接内容输入
/baoyu-cover-image
[paste content]

# 直接输入带选项
/baoyu-cover-image --style notion --aspect 1:1 --quick
[paste content]
```

## 选项

| 选项 | 描述 |
|------|------|
| `--type <name>` | 封面类型：hero、conceptual、typography、metaphor、scene、minimal |
| `--style <name>` | 封面风格（见风格画廊） |
| `--text <level>` | 文本密度：none、title-only、title-subtitle、text-rich |
| `--mood <level>` | 情感强度：subtle、balanced、bold |
| `--aspect <ratio>` | 16:9（默认）、2.35:1、4:3、3:2、1:1、3:4 |
| `--lang <code>` | 标题语言（en、zh、ja 等） |
| `--no-title` | `--text none` 的别名 |
| `--quick` | 跳过确认，使用自动选择缺失的维度 |

## 四个维度

| 维度 | 控制 | 值 | 默认 |
|------|------|-----|------|
| **类型** | 视觉构图、信息结构 | hero、conceptual、typography、metaphor、scene、minimal | auto |
| **风格** | 视觉美学、颜色、技术 | 20 种内置风格 | auto |
| **文本** | 文本密度、信息层次 | none、title-only、title-subtitle、text-rich | title-only |
| **情绪** | 情感强度、视觉重量 | subtle、balanced、bold | balanced |

维度可以自由组合。例如：`--type conceptual --style blueprint --text title-only --mood subtle` 创建一个平静的技术概念可视化。

## 类型画廊

| 类型 | 描述 | 最佳用途 |
|------|------|----------|
| `hero` | 大型视觉冲击，标题叠加 | 产品发布、品牌推广、重大公告 |
| `conceptual` | 概念可视化，抽象核心思想 | 技术文章、方法论、架构设计 |
| `typography` | 以文本为重点的布局，标题突出 | 观点文章、引言、洞见 |
| `metaphor` | 视觉隐喻，具体表达抽象 | 哲学、成长、个人发展 |
| `scene` | 氛围场景，叙事感 | 故事、旅行、生活方式 |
| `minimal` | 极简构图，大量留白 | 禅意、专注、核心概念 |

## 自动类型选择

当省略 `--type` 时，根据内容信号进行选择：

| 信号 | 类型 |
|------|------|
| 产品、发布、公告、发布、揭露 | `hero` |
| 架构、框架、系统、API、技术、模型 | `conceptual` |
| 引用、观点、洞见、思想、标题、声明 | `typography` |
| 哲学、成长、抽象、意义、反思 | `metaphor` |
| 故事、旅程、旅行、生活方式、经验、叙事 | `scene` |
| 禅意、专注、本质、核心、简单、纯粹 | `minimal` |

## 风格画廊

| 风格 | 描述 |
|------|------|
| `elegant`（默认） | 精致、复杂 |
| `blueprint` | 技术图表 |
| `bold-editorial` | 杂志影响 |
| `chalkboard` | 粉笔在黑板上 |
| `dark-atmospheric` | 电影式暗色调 |
| `editorial-infographic` | 视觉叙事 |
| `fantasy-animation` | 吉卜力/迪士尼灵感 |
| `flat-doodle` | 色彩柔和，可爱形状 |
| `intuition-machine` | 技术，双语 |
| `minimal` | 极简、禅意 |
| `nature` | 有机、自然 |
| `notion` | SaaS 仪表板 |
| `pixel-art` | 复古 8 位 |
| `playful` | 有趣、俏皮 |
| `retro` | 半色调、复古 |
| `sketch-notes` | 手绘，温暖 |
| `vector-illustration` | 平面矢量 |
| `vintage` | 老化、探险 |
| `warm` | 友好、人性化 |
| `watercolor` | 柔软的手绘 |

风格定义：[references/styles/](references/styles/)

## 自动风格选择

当省略 `--style` 时，根据内容信号进行选择：

| 信号 | 风格 |
|------|------|
| 架构、系统设计 | `blueprint` |
| 产品发布、营销 | `bold-editorial` |
| 教育、教程 | `chalkboard` |
| 娱乐、高端 | `dark-atmospheric` |
| 科技解说、研究 | `editorial-infographic` |
| 奇幻、儿童 | `fantasy-animation` |
| 技术文档、双语 | `intuition-machine` |
| 个人故事、情感 | `warm` |
| 禅意、专注、本质 | `minimal` |
| 有趣、初学者、休闲 | `playful` |
| 自然、健康、生态 | `nature` |
| SaaS、仪表板 | `notion` |
| 工作流程、生产力 | `flat-doodle` |
| 游戏、复古技术 | `pixel-art` |
| 知识分享 | `sketch-notes` |
| 创意提案 | `vector-illustration` |
| 历史、探索 | `vintage` |
| 生活方式、旅行 | `watercolor` |
| 商业、专业 | `elegant` |

## 文本维度

| 值 | 标题 | 副标题 | 标签 | 用例 |
|-----|:-----:|:--------:|:----:|----------|
| `none` | - | - | - | 纯视觉，无文本 |
| `title-only` | ✓ (≤8字) | - | - | 简单标题（默认） |
| `title-subtitle` | ✓ | ✓ (≤15字) | - | 标题 + 支持性内容 |
| `text-rich` | ✓ | ✓ | ✓ (2-4) | 信息密集型 |

完整指南：[references/dimensions/text.md](references/dimensions/text.md)

## 自动文本选择

当省略 `--text` 时，根据内容信号进行选择：

| 信号 | 文本级别 |
|------|----------|
| 视觉、摄影、抽象、艺术 | `none` |
| 文章、博客、标准封面 | `title-only` |
| 系列作品、教程、带上下文的科技文章 | `title-subtitle` |
| 公告、功能、多要点、信息图 | `text-rich` |

默认：`title-only`

## 情绪维度

| 值 | 对比度 | 饱和度 | 重量 | 用例 |
|-----|:--------:|:----------:|:------:|----------|
| `subtle` | 低 | 淡化 | 轻柔 | 企业、思想领导 |
| `balanced` | 中等 | 正常 | 中等 | 一般文章（默认） |
| `bold` | 高 | 明亮 | 重 | 公告、促销 |

完整指南：[references/dimensions/mood.md](references/dimensions/mood.md)

## 自动情绪选择

当省略 `--mood` 时，根据内容信号进行选择：

| 信号 | 情绪级别 |
|------|----------|
| 专业、企业、思想领导、学术、奢华 | `subtle` |
| 一般、教育、标准、博客、文档 | `balanced` |
| 发布、公告、促销、活动、游戏、娱乐 | `bold` |

默认：`balanced`

## 兼容性矩阵

### 类型 × 风格

| | elegant | blueprint | notion | warm | minimal | watercolor | bold-editorial | dark-atmospheric |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hero | ✓✓ | ✓ | ✓ | ✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓ |
| conceptual | ✓✓ | ✓✓ | ✓✓ | ✓ | ✓✓ | ✗ | ✓ | ✓ |
| typography | ✓✓ | ✓ | ✓✓ | ✓ | ✓✓ | ✓ | ✓✓ | ✓✓ |
| metaphor | ✓✓ | ✗ | ✓ | ✓✓ | ✓ | ✓✓ | ✓ | ✓ |
| scene | ✓ | ✗ | ✗ | ✓✓ | ✓ | ✓✓ | ✓ | ✓✓ |
| minimal | ✓✓ | ✓ | ✓✓ | ✓ | ✓✓ | ✓ | ✗ | ✓ |

✓✓ = 高度推荐 | ✓ = 兼容 | ✗ = 不推荐

### 类型 × 文本

| | none | title-only | title-subtitle | text-rich |
|---|:---:|:---:|:---:|:---:|
| hero | ✓ | ✓✓ | ✓✓ | ✓ |
| conceptual | ✓✓ | ✓✓ | ✓ | ✓ |
| typography | ✗ | ✓ | ✓✓ | ✓✓ |
| metaphor | ✓✓ | ✓ | ✓ | ✗ |
| scene | ✓✓ | ✓ | ✓ | ✗ |
| minimal | ✓✓ | ✓✓ | ✓ | ✗ |

### 类型 × 情绪

| | subtle | balanced | bold |
|---|:---:|:---:|:---:|
| hero | ✓ | ✓✓ | ✓✓ |
| conceptual | ✓✓ | ✓✓ | ✓ |
| typography | ✓ | ✓✓ | ✓✓ |
| metaphor | ✓✓ | ✓✓ | ✓ |
| scene | ✓✓ | ✓✓ | ✓ |
| minimal | ✓✓ | ✓✓ | ✗ |

✓✓ = 高度推荐 | ✓ = 兼容 | ✗ = 不推荐

## 文件结构

每个会话创建一个以内容短标题命名的独立目录：

```
cover-image/{topic-slug}/
├── source-{slug}.{ext}    # 源文件（文本、图像等）
├── prompts/cover.md       # 生成提示
└── cover.png              # 输出图像
```

**短标题生成**：
1. 从内容中提取主要主题（2-4 个单词，短横线分隔）
2. 示例：“人工智能的未来”→ `future-of-ai`

**冲突解决**：
如果 `cover-image/{topic-slug}/` 已经存在：
- 添加时间戳：`{topic-slug}-YYYYMMDD-HHMMSS`
- 示例：`ai-future` 存在 → `ai-future-20260118-143052`

**源文件**：
复制所有源文件，命名 `source-{slug}.{ext}`：
- `source-article.md`、`source-reference.png` 等
- 支持多个源文件：文本、图像、来自对话的文件

## 工作流程

### 进度清单

复制并跟踪进度：

```plaintext
封面图进度：
- [ ] 步骤 0：检查首选项（EXTEND.md）⚠️ 必要时如未找到
- [ ] 步骤 1：分析内容
- [ ] 步骤 2：确认选项（4 个维度）⚠️ 必要时除非 --quick 或所有指定
- [ ] 步骤 3：创建提示
- [ ] 步骤 4：生成图像
- [ ] 步骤 5：完成报告
```

### 流程

```plaintext
输入 → [步骤 0：首选项/设置] → 分析 → [确认：4 个维度] → 提示 → 生成 → 完成
                                                      ↓
                                              (如果 --quick 或所有维度指定则跳过)
```

### 步骤 0：加载首选项（EXTEND.md）⚠️

**目的**：加载用户首选项或运行首次设置。**如果未找到 EXTEND.md，则切勿跳过设置**。

使用 Bash 检查 EXTEND.md 存在性（优先顺序）：

```bash
# 检查项目级别首先
test -f .baoyu-skills/baoyu-cover-image/EXTEND.md && echo "project"

# 然后用户级别（跨平台：$HOME 在 macOS/Linux/WSL 上有效）
test -f "$HOME/.baoyu-skills/baoyu-cover-image/EXTEND.md" && echo "user"
```

┌──────────────────────────────────────────────────┬───────────────────┐
│                       路径                       │     位置          │
├──────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-cover-image/EXTEND.md        │ 项目目录          │
├──────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-cover-image/EXTEND.md  │ 用户主目录        │
└──────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  操作                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、显示首选项摘要（见下文）→ 继续到步骤 1 │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ ⚠️ 必须运行首次设置（见下文）→ 然后继续到步骤 1        │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**首选项摘要**（当找到 EXTEND.md 时）：

显示加载的首选项：

```plaintext
从 [项目/用户] 加载首选项：
• 水印：[启用/禁用] [启用时内容]
• 类型：[首选类型或 "auto"]
• 风格：[首选风格或 "auto"]
• 文本：[首选文本或 "title-only"]
• 情绪：[首选情绪或 "balanced"]
• 比例：[默认比例]
• 快速模式：[启用/禁用]
• 语言：[语言或 "auto"]
```

**首次设置**（当未找到 EXTEND.md 时）：

**语言**：使用用户的输入语言或保存的语言首选项。

使用 AskUserQuestion 在一个调用中提出所有问题：

**Q1：水印**
```yaml
header: "水印"
question: "生成封面图的水印文本？"
options:
  - label: "无水印（推荐）"
    description: "干净的封面，可以稍后在 EXTEND.md 中启用"
```

**Q2：首选类型**
```yaml
header: "类型"
question: "默认封面类型首选项？"
options:
  - label: "自动选择（推荐）"
    description: "每次根据内容分析进行选择"
  - label: "hero"
    description: "大型视觉冲击 - 产品发布、公告"
  - label: "conceptual"
    description: "概念可视化 - 技术、架构"
```

**Q3：首选风格**
```yaml
header: "风格"
question: "默认封面风格首选项？"
options:
  - label: "自动选择（推荐）"
    description: "每次根据内容分析进行选择"
  - label: "elegant"
    description: "精致、复杂 - 专业商业"
  - label: "notion"
    description: "SaaS 仪表板 - 生产力/技术内容"
```

**Q4：默认比例**
```yaml
header: "比例"
question: "封面图的默认比例？"
options:
  - label: "16:9（推荐）"
    description: "标准宽屏 - YouTube、演示文稿、通用"
  - label: "2.35:1"
    description: "电影式宽屏 - 文章标题、博客文章"
  - label: "1:1"
    description: "正方形 - Instagram、微信、社交媒体卡"
  - label: "3:4"
    description: "纵向 - 红书、Pinterest、移动端内容"
```

注意：生成时还有更多比例（4:3、3:2）可用。这设置了默认推荐。

**Q5：快速模式**
```yaml
header: "快速"
question: "默认启用快速模式？"
options:
  - label: "否（推荐）"
    description: "每次确认维度选择"
  - label: "是"
    description: "跳过确认，使用自动选择"
```

**Q6：保存位置**
```yaml
header: "保存"
question: "在哪里保存首选项？"
options:
  - label: "项目（推荐）"
    description: ".baoyu-skills/（仅此项目）"
  - label: "用户"
    description: "~/.baoyu-skills/（所有项目）"
```

**设置后**：创建包含用户选择的 EXTEND.md，然后继续到步骤 1。

