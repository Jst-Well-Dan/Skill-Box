---
name: baoyu-infographic
description: 生成具有20种布局类型和17种视觉风格的职业信息图。分析内容，推荐布局×风格组合，并生成可发布的信息图。当用户要求创建“信息图”、“信息图”、“视觉摘要”或“可视化”时使用。
---

# 信息图生成器

两个维度：**布局**（信息结构）× **风格**（视觉美学）。自由组合任何布局与任何风格。

## 使用方法

```bash
/baoyu-infographic path/to/content.md
/baoyu-infographic path/to/content.md --layout hierarchical-layers --style technical-schematic
/baoyu-infographic path/to/content.md --aspect portrait --lang zh
/baoyu-infographic  # 然后粘贴内容
```

## 选项

| 选项 | 值 |
|------|----|
| `--layout` | 20个选项（见布局画廊），默认：bento-grid |
| `--style` | 17个选项（见风格画廊），默认：craft-handmade |
| `--aspect` | 景观（16:9），肖像（9:16），方形（1:1） |
| `--lang` | en, zh, ja, 等。 |

## 布局画廊

| 布局 | 适用于 |
|------|--------|
| `linear-progression` | 时间线、流程、教程 |
| `binary-comparison` | A与B、前后、优劣 |
| `comparison-matrix` | 多因素比较 |
| `hierarchical-layers` | 金字塔、优先级 |
| `tree-branching` | 分类、分类法 |
| `hub-spoke` | 中心概念及相关项目 |
| `structural-breakdown` | 拆解视图、横截面 |
| `bento-grid` | 多个主题、概述（默认） |
| `iceberg` | 表面与隐藏方面 |
| `bridge` | 问题-解决方案 |
| `funnel` | 转化、过滤 |
| `isometric-map` | 空间关系 |
| `dashboard` | 指标、KPI |
| `periodic-table` | 分类集合 |
| `comic-strip` | 叙事、序列 |
| `story-mountain` | 情节结构、张力弧 |
| `jigsaw` | 相互关联的部分 |
| `venn-diagram` | 重叠概念 |
| `winding-roadmap` | 旅程、里程碑 |
| `circular-flow` | 循环、重复过程 |

完整定义：`references/layouts/<layout>.md`

## 风格画廊

| 风格 | 描述 |
|------|------|
| `craft-handmade` | 手绘、纸艺（默认） |
| `claymation` | 3D粘土人偶、定格动画 |
| `kawaii` | 日本可爱风格、粉彩 |
| `storybook-watercolor` | 软性绘画、异想天开 |
| `chalkboard` | 粉笔在黑板上 |
| `cyberpunk-neon` | 荧光、未来主义 |
| `bold-graphic` | 漫画风格、半色调 |
| `aged-academia` | 老式科学、棕褐色 |
| `corporate-memphis` | 平面矢量、鲜艳 |
| `technical-schematic` | 蓝图、工程 |
| `origami` | 折纸、几何 |
| `pixel-art` | 复古8位 |
| `ui-wireframe` | 灰度界面原型 |
| `subway-map` | 交通图 |
| `ikea-manual` | 最小化线艺术 |
| `knolling` | 有序的平铺 |
| `lego-brick` | 玩具砖结构 |

完整定义：`references/styles/<style>.md`

## 推荐组合

| 内容类型 | 布局 + 风格 |
|----------|-------------|
| 时间线/历史 | `linear-progression` + `craft-handmade` |
| 步骤说明 | `linear-progression` + `ikea-manual` |
| A与B | `binary-comparison` + `corporate-memphis` |
| 层次 | `hierarchical-layers` + `craft-handmade` |
| 重叠 | `venn-diagram` + `craft-handmade` |
| 转化 | `funnel` + `corporate-memphis` |
| 循环 | `circular-flow` + `craft-handmade` |
| 技术 | `structural-breakdown` + `technical-schematic` |
| 指标 | `dashboard` + `corporate-memphis` |
| 教育 | `bento-grid` + `chalkboard` |
| 旅程 | `winding-roadmap` + `storybook-watercolor` |
| 分类 | `periodic-table` + `bold-graphic` |

默认：`bento-grid` + `craft-handmade`

## 输出结构

```
infographic/{topic-slug}/
├── source-{slug}.{ext}
├── analysis.md
├── structured-content.md
├── prompts/infographic.md
└── infographic.png
```

别名：2-4个单词的kebab-case主题。冲突：附加 `-YYYYMMDD-HHMMSS`。

## 核心原则

- 保留所有源数据 **逐字逐句**—不摘要或改写
- 在结构化内容之前定义学习目标
- 为视觉沟通结构化（标题、标签、视觉元素）

## 工作流程

### 第1步：设置与分析

**1.1 加载首选项（EXTEND.md）**

使用Bash检查EXTEND.md是否存在（优先顺序）：

```bash
# 首先检查项目级别的
test -f .baoyu-skills/baoyu-infographic/EXTEND.md && echo "project"

# 然后用户级别（跨平台：$HOME在macOS/Linux/WSL上有效）
test -f "$HOME/.baoyu-skills/baoyu-infographic/EXTEND.md" && echo "user"
```

┌────────────────────────────────────────────────────┬───────────────────┐
│                        路径                        │     位置          │
├────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-infographic/EXTEND.md          │ 项目目录          │
├────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-infographic/EXTEND.md    │ 用户家目录        │
└────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  操作                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、显示摘要                                              │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用AskUserQuestion询问用户（见references/config/first-time-setup.md） │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：首选布局/风格 | 默认宽高比 | 自定义风格定义 | 语言偏好

模式：`references/config/preferences-schema.md`

**1.2 分析内容 → analysis.md**

1. 保存源内容（文件路径或粘贴→ source.md）
2. 分析：主题、数据类型、复杂性、语气、受众
3. 检测源语言和用户语言
4. 从用户输入中提取设计指令
5. 保存分析

有关详细格式，请参阅`references/analysis-framework.md`。

### 第2步：生成结构化内容 → structured-content.md

将内容转换为信息图结构：
1. 标题和学习目标
2. 部分包括：关键概念、内容（逐字逐句）、视觉元素、文本标签
3. 数据点（所有统计数据/引语都复制得非常准确）
4. 用户的设计指令

**规则**：仅Markdown。无新信息。所有数据逐字逐句。

有关详细格式，请参阅`references/structured-content-template.md`。

### 第3步：推荐组合

根据以下内容推荐3-5个布局×风格组合：
- 数据结构→匹配布局
- 内容语气→匹配风格
- 受众期望
- 用户设计指令

### 第4步：确认选项

在单个确认中呈现所有选项：
1. **组合**（始终）：3+个选项及其理由
2. **宽高比**（始终）：景观/肖像/方形
3. **语言**（仅当源语言≠用户语言时）：哪种语言用于文本

### 第5步：生成提示 → prompts/infographic.md

结合：
1. 布局定义来自`references/layouts/<layout>.md`
2. 风格定义来自`references/styles/<style>.md`
3. 基础模板来自`references/base-prompt.md`
4. 第2步的结构化内容
5. 所有文本都确认了语言

### 第6步：生成图像

1. 选择可用的图像生成技能（如果有多个，则询问用户）
2. 使用提示文件和输出路径调用
3. 失败时，自动重试一次

### 第7步：输出摘要

报告：主题、布局、风格、宽高比、语言、输出路径、创建的文件。

## 参考资料

- `references/analysis-framework.md` - 分析方法
- `references/structured-content-template.md` - 内容格式
- `references/base-prompt.md` - 提示模板
- `references/layouts/<layout>.md` - 20个布局定义
- `references/styles/<style>.md` - 17个风格定义

## 扩展支持

通过EXTEND.md进行自定义配置。有关路径和支持选项，请参阅**第1.1步**。

