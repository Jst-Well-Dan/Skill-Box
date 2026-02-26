---
name: baoyu-image-gen
description: 使用官方 OpenAI 和 Google API 通过 AI SDK 生成图像。支持文本到图像、参考图像、宽高比和预设质量。当用户请求“使用 API 生成图像”、“使用官方 API 生成图像”或需要基于 API 的生成而不是基于浏览器的生成时使用。
---

# 图像生成（AI SDK）

官方基于 API 的图像生成。支持 OpenAI 和 Google 提供商。

## 脚本目录

**代理执行**：
1. `SKILL_DIR` = 此 SKILL.md 文件所在的目录
2. 脚本路径 = `${SKILL_DIR}/scripts/main.ts`

## 预设（EXTEND.md）

使用 Bash 检查 EXTEND.md 存在性（优先级顺序）：

```bash
# 首先检查项目级别
test -f .baoyu-skills/baoyu-image-gen/EXTEND.md && echo "project"

# 然后是用户级别（跨平台：$HOME 在 macOS/Linux/WSL 上有效）
test -f "$HOME/.baoyu-skills/baoyu-image-gen/EXTEND.md" && echo "user"
```

┌──────────────────────────────────────────────────┬───────────────────┐
│                       路径                       │     位置          │
├──────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-image-gen/EXTEND.md          │ 项目目录          │
├──────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-image-gen/EXTEND.md    │ 用户家目录         │
└──────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  操作                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、应用设置                                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用默认值                                                              │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：默认提供商 | 默认质量 | 默认宽高比

## 使用方法

```bash
# 基本使用
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "一只猫" --image cat.png

# 使用宽高比
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "一幅风景" --image out.png --ar 16:9

# 高质量
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "一只猫" --image out.png --quality 2k

# 从提示文件中
npx -y bun ${SKILL_DIR}/scripts/main.ts --promptfiles system.md content.md --image out.png

# 使用参考图像（仅 Google 多模态）
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "让蓝色" --image out.png --ref source.png

# 指定提供商
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "一只猫" --image out.png --provider openai
```

## 选项

| 选项 | 描述 |
|--------|-------------|
| `--prompt <text>`, `-p` | 提示文本 |
| `--promptfiles <files...>` | 从文件中读取提示（连接） |
| `--image <path>` | 输出图像路径（必需） |
| `--provider google|openai` | 强制提供商（默认：google） |
| `--model <id>`, `-m` | 模型 ID |
| `--ar <ratio>` | 宽高比（例如，`16:9`，`1:1`，`4:3`） |
| `--size <WxH>` | 大小（例如，`1024x1024`） |
| `--quality normal|2k` | 质量预设（默认：2k） |
| `--imageSize 1K|2K|4K` | Google 的图像大小（默认：从质量） |
| `--ref <files...>` | 参考图像（仅 Google 多模态） |
| `--n <count>` | 图像数量 |
| `--json` | JSON 输出 |

## 环境变量

| 变量 | 描述 |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API 密钥 |
| `GOOGLE_API_KEY` | Google API 密钥 |
| `OPENAI_IMAGE_MODEL` | OpenAI 模型覆盖 |
| `GOOGLE_IMAGE_MODEL` | Google 模型覆盖 |
| `OPENAI_BASE_URL` | 自定义 OpenAI 端点 |
| `GOOGLE_BASE_URL` | 自定义 Google 端点 |

**加载优先级**：CLI 参数 > 环境变量 > `<cwd>/.baoyu-skills/.env` > `~/.baoyu-skills/.env`

## 提供商选择

1. `--provider` 指定 → 使用它
2. 仅有一个 API 密钥可用 → 使用该提供商
3. 两者都可用 → 默认为 Google

## 质量预设

| 预设 | Google imageSize | OpenAI Size | 用例 |
|--------|------------------|-------------|----------|
| `normal` | 1K | 1024px | 快速预览 |
| `2k`（默认） | 2K | 2048px | 封面、插图、信息图表 |

**Google imageSize**：可以用 `--imageSize 1K|2K|4K` 覆盖

## 宽高比

支持：`1:1`，`16:9`，`9:16`，`4:3`，`3:4`，`2.35:1`

- Google 多模态：使用 `imageConfig.aspectRatio`
- Google Imagen：使用 `aspectRatio` 参数
- OpenAI：映射到最接近的受支持大小

## 错误处理

- 缺少 API 密钥 → 显示错误并带有设置说明
- 生成失败 → 自动重试一次
- 无效的宽高比 → 警告，继续使用默认值
- 使用非多模态模型的参考图像 → 警告，忽略参考图像

## 扩展支持

通过 EXTEND.md 进行自定义配置。有关路径和支持选项，请参阅**预设**部分。