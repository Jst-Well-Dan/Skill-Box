---
name: baoyu-comic
description: 支持多种艺术风格和基调的知识漫画创作者。创建具有详细分镜布局和连续图像生成的原创教育漫画。当用户请求创建“知识漫画”、“教育漫画”、“传记漫画”、“教程漫画”或“Logicomix风格漫画”时使用。
---

# 知识漫画创作者

创建具有灵活艺术风格 × 基调组合的原创知识漫画。

## 使用方法

```bash
/baoyu-comic posts/turing-story/source.md
/baoyu-comic article.md --art manga --tone warm
/baoyu-comic  # 然后粘贴内容
```

## 选项

### 视觉维度

| 选项 | 值 | 描述 |
|--------|--------|-------------|
| `--art` | ligne-claire (默认), manga, realistic, ink-brush, chalk | 艺术风格 / 渲染技术 |
| `--tone` | neutral (默认), warm, dramatic, romantic, energetic, vintage, action | 情绪 / 氛围 |
| `--layout` | standard (默认), cinematic, dense, splash, mixed, webtoon | 分镜排列 |
| `--aspect` | 3:4 (默认，纵向), 4:3 (横向), 16:9 (宽屏) | 页面宽高比 |
| `--lang` | auto (默认), zh, en, ja, etc. | 输出语言 |

### 部分工作流程选项

| 选项 | 描述 |
|--------|-------------|
| `--storyboard-only` | 仅生成分镜，跳过提示和图像 |
| `--prompts-only` | 生成分镜 + 提示，跳过图像 |
| `--images-only` | 从现有的提示目录生成图像 |
| `--regenerate N` | 仅重新生成特定页面（例如，`3` 或 `2,5,8`） |

详情：[references/partial-workflows.md](references/partial-workflows.md)

### 艺术风格 (画风)

| 风格 | 中文 | 描述 |
|-------|------|-------------|
| `ligne-claire` | 清线 | 统一的线条，平涂颜色，欧洲漫画传统（丁丁，Logicomix） |
| `manga` | 日漫 | 大眼睛，漫画惯例，表情丰富 |
| `realistic` | 写实 | 数字绘画，写实比例，复杂 |
| `ink-brush` | 水墨 | 中国画笔触，水墨效果 |
| `chalk` | 粉笔 | 粉笔美学，手绘温暖 |

### 基调 (基调)

| 基调 | 中文 | 描述 |
|------|------|-------------|
| `neutral` | 中性 | 平衡，理性，教育 |
| `warm` | 温馨 | 怀旧，个人，舒适 |
| `dramatic` | 戏剧 | 高对比度，强烈，有力 |
| `romantic` | 浪漫 | 温柔，美丽，装饰元素 |
| `energetic` | 活力 | 明亮，动态，激动人心 |
| `vintage` | 复古 | 历史，老化，时代真实性 |
| `action` | 动作 | 速度线，冲击效果，战斗 |

### 预设快捷方式

具有超出艺术 + 基调的特殊规则的预设：

| 预设 | 等效 | 特殊规则 |
|--------|-----------|---------------|
| `--style ohmsha` | `--art manga --tone neutral` | 视觉隐喻，NO talking heads，设备揭示 |
| `--style wuxia` | `--art ink-brush --tone action` | 气功效果，战斗视觉，氛围元素 |
| `--style shoujo` | `--art manga --tone romantic` | 装饰元素，眼睛细节，浪漫节奏 |

### 兼容性矩阵

| 艺术风格 | ✓✓ 最佳 | ✓ 可以 | ✗ 避免 |
|-----------|---------|---------|---------|
| ligne-claire | neutral, warm | dramatic, vintage, energetic | romantic, action |
| manga | neutral, romantic, energetic, action | warm, dramatic | vintage |
| realistic | neutral, warm, dramatic, vintage | action | romantic, energetic |
| ink-brush | neutral, dramatic, action, vintage | warm | romantic, energetic |
| chalk | neutral, warm, energetic | vintage | dramatic, action, romantic |

详情：[references/auto-selection.md](references/auto-selection.md)

## 自动选择

内容信号决定默认艺术 + 基调 + 布局（或预设）：

| 内容信号 | 推荐 |
|-----------------|-------------|
| 教程，如何做，编程，教育 | **ohmsha** 预设 |
| 1950 年前，古典，古代 | realistic + vintage |
| 个人故事，导师 | ligne-claire + warm |
| 武术，武侠 | **wuxia** 预设 |
| 爱情，校园生活 | **shoujo** 预设 |
| 传记，平衡 | ligne-claire + neutral |

**当推荐预设时**：加载 `references/presets/{preset}.md` 并应用所有特殊规则。

详情：[references/auto-selection.md](references/auto-selection.md)

## 脚本目录

**重要**：所有脚本都位于此技能的 `scripts/` 子目录中。

**代理执行指令**：
1. 确定此 SKILL.md 文件的目录路径为 `SKILL_DIR`
2. 脚本路径 = `${SKILL_DIR}/scripts/<script-name>.ts`
3. 将此文档中的所有 `${SKILL_DIR}` 替换为实际路径

**脚本参考**：
| 脚本 | 目的 |
|--------|---------|
| `scripts/merge-to-pdf.ts` | 将漫画页面合并为 PDF |

## 文件结构

输出目录：`comic/{topic-slug}/`
- Slug：主题的 2-4 个单词 kebab-case（例如，`alan-turing-bio`）
- 冲突：附加时间戳（例如，`turing-story-20260118-143052`）

**内容**：

| 文件 | 描述 |
|------|-------------|
| `source-{slug}.{ext}` | 源文件 |
| `analysis.md` | 内容分析 |
| `storyboard.md` | 分镜，包含分镜分解 |
| `characters/characters.md` | 角色定义 |
| `characters/characters.png` | 角色参考表 |
| `prompts/NN-{cover|page}-{slug}.md` | 生成提示 |
| `NN-{cover|page}-{slug}.png` | 生成的图像 |
| `{topic-slug}.pdf` | 最终合并的 PDF |

## 语言处理

**检测优先级**：
1. `--lang` 标志（显式）
2. EXTEND.md `language` 设置
3. 用户的对话语言
4. 源内容语言

**规则**：使用用户的输入语言或保存的语言偏好进行所有交互：
- 分镜概要和场景描述
- 图像生成提示
- 用户选择选项和确认
- 进度更新，问题，错误，摘要

技术术语保持英文。

## 工作流程

### 进度清单

```
漫画进度：
- [ ] 步骤 1：设置 & 分析（1.1 偏好，1.2 分析，1.3 检查现有）
- [ ] 步骤 2：确认 - 风格 & 选项 ⚠️ 必需
- [ ] 步骤 3：生成分镜 + 角色
- [ ] 步骤 4：审查概要（条件）
- [ ] 步骤 5：生成提示
- [ ] 步骤 6：审查提示（条件）
- [ ] 步骤 7：生成图像 ⚠️ 角色参考必需
  - [ ] 7.1 首先生成角色表单 → characters/characters.png
  - [ ] 7.2 生成页面 WITH --ref characters/characters.png
- [ ] 步骤 8：合并到 PDF
- [ ] 步骤 9：完成报告
```

### 流程

```
输入 → 偏好 → 分析 → [检查现有？] → [确认：风格 + 审查] → 分镜 → [审查？] → 提示 → [审查？] → 图像 → PDF → 完成
```

### 步骤概要

| 步骤 | 动作 | 关键输出 |
|------|--------|------------|
| 1.1 | 加载 EXTEND.md 偏好 | 配置加载 |
| 1.2 | 分析内容 | `analysis.md` |
| 1.3 | 检查现有目录 | 处理冲突 |
| 2 | 确认风格，焦点，受众，审查 | 用户偏好 |
| 3 | 生成分镜 + 角色 | `storyboard.md`，`characters/` |
| 4 | 审查概要（如果请求） | 用户批准 |
| 5 | 生成提示 | `prompts/*.md` |
| 6 | 审查提示（如果请求） | 用户批准 |
| **7.1** | **首先生成角色表单** | `characters/characters.png` |
| **7.2** | 生成页面 **WITH 角色参考** | `*.png` 文件 |
| 8 | 合并到 PDF | `{slug}.pdf` |
| 9 | 完成报告 | 摘要 |

### 步骤 7：图像生成 ⚠️ 关键

**角色参考是视觉一致性必需的。**

**7.1 首先生成角色表单**：
```bash
# 使用 characters/characters.md 中的参考表单提示
npx -y bun ${SKILL_DIR}/../baoyu-image-gen/scripts/main.ts \
  --promptfiles characters/characters.md \
  --image characters/characters.png --ar 4:3
```

**7.2 生成每个页面 WITH 角色参考**：

| 技能能力 | 策略 |
|------------------|----------|
| 支持 `--ref` | 将 `characters/characters.png` 与每个页面一起传递 |
| 不支持 `--ref` | 将角色描述预置到每个提示文件中 | 

```bash
# 示例：始终包含 --ref 以确保一致性
npx -y bun ${SKILL_DIR}/../baoyu-image-gen/scripts/main.ts \
  --promptfiles prompts/01-page-xxx.md \
  --image 01-page-xxx.png --ar 3:4 \
  --ref characters/characters.png
```

**完整工作流程详情**：[references/workflow.md](references/workflow.md)

### EXTEND.md 路径

| 路径 | 位置 |
|------|----------|
| `.baoyu-skills/baoyu-comic/EXTEND.md` | 项目目录 |
| `$HOME/.baoyu-skills/baoyu-comic/EXTEND.md` | 用户家目录 |

**EXTEND.md 支持**：水印 | 偏好的艺术/基调/布局 | 自定义样式定义 | 角色预设 | 语言偏好

模式：[references/config/preferences-schema.md](references/config/preferences-schema.md)

## 参考资料

**核心模板**：
- [analysis-framework.md](references/analysis-framework.md) - 深度内容分析
- [character-template.md](references/character-template.md) - 角色定义格式
- [storyboard-template.md](references/storyboard-template.md) - 分镜结构
- [ohmsha-guide.md](references/ohmsha-guide.md) - Ohmsha 漫画具体细节

**风格定义**：
- `references/art-styles/` - 艺术风格（ligne-claire，manga，realistic，ink-brush，chalk）
- `references/tones/` - 基调（neutral，warm，dramatic，romantic，energetic，vintage，action）
- `references/presets/` - 具有特殊规则的预设（ohmsha，wuxia，shoujo）
- `references/layouts/` - 布局（standard，cinematic，dense，splash，mixed，webtoon）

**工作流程**：
- [workflow.md](references/workflow.md) - 完整工作流程详情
- [auto-selection.md](references/auto-selection.md) - 内容信号分析
- [partial-workflows.md](references/partial-workflows.md) - 部分工作流程选项

**配置**：
- [config/preferences-schema.md](references/config/preferences-schema.md) - EXTEND.md 模式
- [config/first-time-setup.md](references/config/first-time-setup.md) - 首次设置
- [config/watermark-guide.md](references/config/watermark-guide.md) - 水印配置

## 备注

- 图像生成：每页 10-30 秒
- 生成失败时自动重试一次
- 使用风格化的替代方案处理敏感公众人物
- 通过会话 ID 维护风格一致性
- **步骤 2 确认必需** - 不要跳过
- **步骤 4/6 条件** - 只有在步骤 2 中用户请求时才执行
- **步骤 7.1 角色表单必须生成在页面之前** - 确保一致性
- **步骤 7.2 每个页面都必须引用角色** - 使用 `--ref` 或嵌入描述
- 水印/语言在 EXTEND.md 中配置一次