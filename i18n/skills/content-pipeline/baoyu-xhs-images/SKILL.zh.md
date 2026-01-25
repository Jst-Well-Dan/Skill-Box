---
name: baoyu-xhs-images
description: 生成包含9种视觉风格和6种布局的Xiaohongshu（小红书）信息图系列。将内容拆分为1-10张卡通风格的图片，优化XHS互动。当用户提及“小红书图片”、“XHS图片”、“RedNote信息图”、“小红书种草”或想要中国平台的社交媒体信息图时使用。
---

# 小红书信息图系列生成器

将复杂内容分解为引人注目的信息图系列，适用于Xiaohongshu，并提供多种风格选项。

## 使用方法

```bash
# 根据内容自动选择风格和布局
/baoyu-xhs-images posts/ai-future/article.md

# 指定风格
/baoyu-xhs-images posts/ai-future/article.md --style notion

# 指定布局
/baoyu-xhs-images posts/ai-future/article.md --layout dense

# 组合风格和布局
/baoyu-xhs-images posts/ai-future/article.md --style notion --layout list

# 直接输入内容
/baoyu-xhs-images
[paste content]

# 直接输入内容并指定选项
/baoyu-xhs-images --style bold --layout comparison
[paste content]
```

## 选项

| 选项 | 描述 |
|--------|-------------|
| `--style <name>` | 视觉风格（见风格画廊） |
| `--layout <name>` | 信息布局（见布局画廊） | 

## 两个维度

| 维度 | 控制 | 选项 |
|-----------|----------|---------|
| **风格** | 视觉美学：颜色、线条、装饰 | cute、fresh、warm、bold、minimal、retro、pop、notion、chalkboard |
| **布局** | 信息结构：密度、排列 | sparse、balanced、dense、list、comparison、flow | 

风格 × 布局可以自由组合。例如：`--style notion --layout dense` 创建了一个具有高信息密度的知识卡片风格的信息图。

## 风格画廊

| 风格 | 描述 |
|-------|-------------|
| `cute` (默认) | 甜美、可爱、女性化 - 经典小红书美学 |
| `fresh` | 清新、爽口、自然 |
| `warm` | 舒适、友好、易接近 |
| `bold` | 高冲击力、吸引注意 |
| `minimal` | 超级简洁、精致 |
| `retro` | 复古、怀旧、时尚 |
| `pop` | 生机勃勃、充满活力、引人注目 |
| `notion` | 极简主义手绘线条艺术，知识性 |
| `chalkboard` | 黑板上的彩色粉笔，教育性 |

详细风格定义：`references/presets/<style>.md`

## 布局画廊

| 布局 | 描述 |
|--------|-------------|
| `sparse` (默认) | 最少信息，最大冲击力（1-2点） |
| `balanced` | 标准内容布局（3-4点） |
| `dense` | 高信息密度，知识卡片风格（5-8点） |
| `list` | 列举和排名格式（4-7项） |
| `comparison` | 并列对比布局 |
| `flow` | 流程和时序布局（3-6步） |

详细布局定义：`references/elements/canvas.md`

## 自动选择

| 内容信号 | 风格 | 布局 |
|-----------------|-------|--------|
| 美丽、时尚、可爱、女孩、粉色 | `cute` | sparse/balanced |
| 健康、自然、清洁、新鲜、有机 | `fresh` | balanced/flow |
| 生活、故事、情感、感觉、温暖 | `warm` | balanced |
| 警告、重要、必须、关键 | `bold` | list/comparison |
| 专业、商业、优雅、简单 | `minimal` | sparse/balanced |
| 经典、复古、旧、传统 | `retro` | balanced |
| 有趣、兴奋、哇、惊人 | `pop` | sparse/list |
| 知识、概念、生产力、SaaS | `notion` | dense/list |
| 教育、教程、学习、教学、教室 | `chalkboard` | balanced/dense | 

## 概要策略

针对不同内容目标的三种差异化概要策略：

### 策略A：故事驱动型

| 方面 | 描述 |
|--------|-------------|
| **概念** | 以个人经历为主线，情感共鸣优先 |
| **特点** | 从痛点出发，展示前后变化，强烈的真实性 |
| **最佳用途** | 评论、个人分享、转型故事 |
| **结构** | 引子 → 问题 → 发现 → 经验 → 结论 | 

### 策略B：信息密集型

| 方面 | 描述 |
|--------|-------------|
| **概念** | 价值优先，高效的信息传递 |
| **特点** | 结构清晰，观点明确，专业可信 |
| **最佳用途** | 指南、比较、产品评论、清单 |
| **结构** | 核心结论 → 信息卡片 → 优缺点 → 推荐 | 

### 策略C：视觉优先型

| 方面 | 描述 |
|--------|-------------|
| **概念** | 视觉冲击为核心，最少文字 |
| **特点** | 大图、氛围感强、吸引力强 |
| **最佳用途** | 高美感产品、生活方式、基于情绪的内容 |
| **结构** | 英雄图像 → 细节图像 → 生活方式场景 → CTA | 

## 文件结构

每个会话创建一个独立的目录，目录名称由内容缩略语命名：

```
xhs-images/{topic-slug}/
├── source-{slug}.{ext}             # 源文件（文本、图像等）
├── analysis.md                     # 深度分析 + 提出的问题
├── outline-strategy-a.md           # 策略A：故事驱动型
├── outline-strategy-b.md           # 策略B：信息密集型
├── outline-strategy-c.md           # 策略C：视觉优先型
├── outline.md                      # 最终选定/合并的概要
├── prompts/
│   ├── 01-cover-[slug].md
│   ├── 02-content-[slug].md
│   └── ...
├── 01-cover-[slug].png
├── 02-content-[slug].png
└── NN-ending-[slug].png
```

**缩略语生成**：
1. 从内容中提取主要主题（2-4个单词，短横线连接）
2. 例如：“AI工具推荐” → `ai-tools-recommend`

**冲突解决**：
如果 `xhs-images/{topic-slug}/` 已存在：
- 添加时间戳：`{topic-slug}-YYYYMMDD-HHMMSS`
- 例如：`ai-tools` 已存在 → `ai-tools-20260118-143052`

**源文件**：
复制所有源文件，命名 `source-{slug}.{ext}`：
- `source-article.md`、`source-photo.jpg` 等
- 支持多个源文件：文本、图像、来自对话的文件

## 工作流程

### 进度清单

复制并跟踪进度：

```bash
XHS信息图进度：
- [ ] 步骤0：检查首选项（EXTEND.md）⚠️ 如未找到，则必须
- [ ] 步骤1：分析内容 → analysis.md
- [ ] 步骤2：确认1 - 内容理解⚠️ 如未找到，则必须
- [ ] 步骤3：生成3个概要 + 风格变体
- [ ] 步骤4：确认2 - 概要 + 风格 + 元素选择⚠️ 如未找到，则必须
- [ ] 步骤5：生成图像（顺序）
- [ ] 步骤6：完成报告
```

### 流程

```bash
输入 → 分析 → [确认1] → 3个概要 → [确认2：概要 + 风格 + 元素] → 生成 → 完成
```

### 步骤0：加载首选项（EXTEND.md）⚠️

**目的**：加载用户首选项或运行首次设置。**如未找到EXTEND.md，则切勿跳过设置。**

使用Bash检查EXTEND.md的存在（优先顺序）：

```bash
# 首先检查项目级别
test -f .baoyu-skills/baoyu-xhs-images/EXTEND.md && echo "project"

# 然后用户级别（跨平台：$HOME在macOS/Linux/WSL上有效）
test -f "$HOME/.baoyu-skills/baoyu-xhs-images/EXTEND.md" && echo "user"
```

┌────────────────────────────────────────────────────┬───────────────────┐
│                        路径                        │     位置      │
├────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-xhs-images/EXTEND.md           │ 项目目录 │
├────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-xhs-images/EXTEND.md     │ 用户家目录 │
└────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果   │                                  行动                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、显示摘要 → 继续步骤1                         │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ ⚠️ 必须运行首次设置（见下文）→ 然后继续步骤1        │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**首次设置**（当EXTEND.md不存在时）：

**语言**：使用用户的输入语言或保存的语言首选项。

使用AskUserQuestion在一次性调用中提出所有问题。有关问题详细信息的说明，请参阅`references/config/first-time-setup.md`。

**EXTEND.md 支持**：水印 | 首选风格/布局 | 自定义风格定义 | 语言首选项

架构：`references/config/preferences-schema.md`

### 步骤1：分析内容 → `analysis.md`

读取源内容，如有必要则保存，并进行深度分析。

**操作**：
1. **保存源内容**（如果尚未是文件）：
   - 如果用户提供了文件路径：使用原样
   - 如果用户粘贴了内容：保存到目标目录中的`source.md`
2. 读取源内容
3. **深度分析**按照`references/workflows/analysis-framework.md`进行：
   - 内容类型分类（种草/干货/测评/教程/避坑...）
   - 引子分析（爆款标题潜力）
   - 目标受众识别
   - 互动潜力（收藏/分享/评论）
   - 视觉机会映射
   - 滑动流程设计
4. 检测源语言
5. 确定推荐图像数量（2-10）
6. **生成澄清问题**（见步骤2）
7. **保存到`analysis.md`** 

### 步骤2：确认1 - 内容理解⚠️

**目的**：验证理解 + 收集缺失信息。**切勿跳过。**

**显示摘要**：
- 识别的内容类型 + 主题
- 提取的关键点
- 检测到语调
- 源图像数量

**使用AskUserQuestion进行**：
1. 核心卖点（多选：true）
2. 目标受众
3. 风格偏好：真实分享 / 专业评论 / 美学氛围 / 自动
4. 其他背景（可选）

**响应后**：更新`analysis.md`→步骤3

### 步骤3：生成3个概要 + 风格变体

根据分析和用户上下文，创建三个不同的策略变体。每个变体都包括**概要结构**和**视觉风格推荐**。

**对于每个策略**：

| 策略 | 文件名 | 概要 | 推荐风格 |
|----------|----------|---------|-------------------|
| A | `outline-strategy-a.md` | 故事驱动型：情感、前后对比 | warm、cute、fresh |
| B | `outline-strategy-b.md` | 信息密集型：结构化、事实性 | notion、minimal、chalkboard |
| C | `outline-strategy-c.md` | 视觉优先型：氛围感、最少文字 | bold、pop、retro | 

**概要格式**（YAML前端元数据 + 内容）：
```yaml
---
strategy: a  # a、b或c
name: Story-Driven
style: warm  # 此策略的推荐风格
style_reason: "温暖的色调增强情感故事讲述和个人联系"
elements:  # 从风格预设中获取，可以在步骤4中自定义
  background: solid-pastel
  decorations: [clouds, stars-sparkles]
  emphasis: star-burst
  typography: highlight
layout: balanced  # 主要布局
image_count: 5
--- 

## P1 封面
**类型**：封面
**引子**：“入冬后脸不干了🥹终于找到对的面霜”
**视觉**：产品英雄图像与舒适的冬季氛围
**布局**：sparse

## P2 问题
**类型**：痛点
**信息**：干皮肤的前期挣扎
**视觉**：前期状态，相关场景
**布局**：balanced

...
```

**差异化要求**：
- 每个策略都必须有不同的概要结构和不同的推荐风格
- 调整页面数量：A通常4-6页，B通常3-5页，C通常3-4页
- 包含`style_reason`解释为什么这种风格适合这种策略
- 考虑用户在步骤2的风格偏好

参考：`references/workflows/outline-template.md`

### 步骤4：确认2 - 概要 & 风格 & 元素选择⚠️

**目的**：用户选择概要策略，确认视觉风格，并自定义元素。**切勿跳过。**

**显示每个策略**：
- 策略名称 + 页面数量 + 推荐风格
- 页面摘要（P1 → P2 → P3...）

**使用AskUserQuestion进行三个问题**：

**问题1：概要策略**
- 策略A（如果“真实分享”推荐）
- 策略B（如果“专业评论”推荐）
- 策略C（如果“美学氛围”推荐）
- 组合：指定每个中的页面

**问题2：视觉风格**
- 使用策略的推荐风格（显示哪种风格）
- 或从：cute / fresh / warm / bold / minimal / retro / pop / notion / chalkboard 中选择
- 或输入自定义风格描述

**问题3：视觉元素**（在风格选择后显示）
显示所选风格的默认元素预设，然后询问：
- 使用风格默认值（推荐）- 显示预览：背景、装饰、强调
- 调整背景 - 选项：solid-pastel / solid-saturated / gradient-linear / gradient-radial / paper-texture / grid
- 调整装饰 - 选项：hearts / stars-sparkles / flowers / clouds / leaves / confetti
- 输入自定义元素偏好

**响应后**：
- 单个策略 → 将确认的样式复制到`outline.md`中
- 组合 → 合并指定的页面和确认的样式
- 自定义请求 → 根据反馈重新生成
- 风格默认值 → 使用预设的元素组合作为默认值
- 背景调整 → 使用用户选择更新elements.background
- 装饰调整 → 使用用户选择更新elements.decorations
- 自定义元素 → 将用户的偏好解析到元素字段中
- 更新`outline.md`前端元数据，包含最终样式和元素

### 步骤5：生成图像

根据确认的概要、风格和布局：

**对于每个图像（封面 + 内容 + 结尾）**：
1. 将提示保存到`prompts/NN-{type}-[slug].md`（在用户的首选语言中）
2. 使用确认的样式和布局生成图像
3. 生成后报告进度

**水印应用**（如果首选项中启用了水印）：
将以下内容添加到每个图像生成的提示中：
``` 
包含一个细微的水印"[内容]"，位置在[position]，大约[opacity*100]%的可见性。水印应该是可辨认的，但不能分散主要内容。
```
参考：`references/config/watermark-guide.md`

**图像生成技能选择**：
- 检查可用的图像生成技能
- 如果有多个技能可用，询问用户偏好

**会话管理**：
如果图像生成技能支持`--sessionId`：
1. 生成唯一的会话ID：`xhs-{topic-slug}-{timestamp}`
2. 使用相同的会话ID生成所有图像
3. 确保生成的图像之间视觉一致性

### 步骤6：完成报告

```bash
Xiaohongshu Infographic Series Complete!

主题：[topic]
策略：[A/B/C/Combined]
风格：[style name]
布局：[layout name or "varies"]
位置：[directory path]
图像：N total

✓ analysis.md
✓ outline-strategy-a.md
✓ outline-strategy-b.md
✓ outline-strategy-c.md
✓ outline.md (selected: [strategy])

文件：
- 01-cover-[slug].png ✓ 封面（sparse）
- 02-content-[slug].png ✓ 内容（balanced）
- 03-content-[slug].png ✓ 内容（dense）
- 04-ending-[slug].png ✓ 结尾（sparse）
```

## 图像修改

| 操作 | 步骤 |
|--------|-------|
| **编辑** | 更新提示 → 使用相同的会话ID重新生成 |
| **添加** | 指定位置 → 创建提示 → 生成 → 重新编号后续文件（NN+1）→ 更新概要 |
| **删除** | 删除文件 → 重新编号后续（NN-1）→