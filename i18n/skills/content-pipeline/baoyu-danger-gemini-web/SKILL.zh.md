---
name: baoyu-danger-gemini-web
description: 通过逆向工程 Gemini Web API 生成图像和文本。支持文本生成、从提示生成图像、视觉输入的参考图像和多轮对话。当其他技能需要图像生成后端，或者用户请求“使用 Gemini 生成图像”、“Gemini 文本生成”或需要具备视觉能力的 AI 生成时使用。
---

# Gemini Web 客户端

通过 Gemini Web API 生成文本/图像。支持参考图像和多轮对话。

## 脚本目录

**重要**：所有脚本都位于此技能的 `scripts/` 子目录中。

**代理执行说明**：
1. 确定此 `SKILL.md` 文件的目录路径为 `SKILL_DIR`
2. 脚本路径 = `${SKILL_DIR}/scripts/<script-name>.ts`
3. 将此文档中的所有 `${SKILL_DIR}` 替换为实际路径

**脚本参考**：
| 脚本 | 目的 |
|--------|---------|
| `scripts/main.ts` | 文本/图像生成的 CLI 入口点 |
| `scripts/gemini-webapi/*` | `gemini_webapi` 的 TypeScript 版本（GeminiClient、类型、工具） |

## 许可检查（必需）

首次使用前，请验证用户对逆向工程 API 使用权的同意。

**许可文件位置**：
- macOS：`~/Library/Application Support/baoyu-skills/gemini-web/consent.json`
- Linux：`~/.local/share/baoyu-skills/gemini-web/consent.json`
- Windows：`%APPDATA%\baoyu-skills\gemini-web\consent.json`

**流程**：
1. 检查是否存在包含 `accepted: true` 和 `disclaimerVersion: "1.0"` 的许可文件
2. 如果存在有效的许可 → 打印包含 `acceptedAt` 日期的警告，继续
3. 如果没有许可 → 显示免责声明，通过 `AskUserQuestion` 向用户提问：
   - "是的，我接受" → 创建包含 ISO 时间戳的许可文件，继续
   - "不，我拒绝" → 输出拒绝消息，停止
4. 许可文件格式：`{"version":1,"accepted":true,"acceptedAt":"<ISO>","disclaimerVersion":"1.0"}`

---

## 首选项（EXTEND.md）

使用 Bash 检查 EXTEND.md 的存在（优先顺序）：

```bash
# 首先检查项目级别
test -f .baoyu-skills/baoyu-danger-gemini-web/EXTEND.md && echo "project"

# 然后是用户级别（跨平台：$HOME 在 macOS/Linux/WSL 上都有效）
test -f "$HOME/.baoyu-skills/baoyu-danger-gemini-web/EXTEND.md" && echo "user"
```

┌──────────────────────────────────────────────────────────┬───────────────────┐
│                           路径                           │     位置          │
├──────────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-danger-gemini-web/EXTEND.md          │ 项目目录          │
├──────────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-danger-gemini-web/EXTEND.md    │ 用户主目录        │
└──────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  行动                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、应用设置                                                       │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用默认值                                                              │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：默认模型 | 代理设置 | 自定义数据目录

## 使用方法

```bash
# 文本生成
npx -y bun ${SKILL_DIR}/scripts/main.ts "您的提示"
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "您的提示" --model gemini-2.5-pro

# 图像生成
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "一只可爱的猫" --image cat.png
npx -y bun ${SKILL_DIR}/scripts/main.ts --promptfiles system.md content.md --image out.png

# 视觉输入（参考图像）
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "描述这个" --reference image.png
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "创建变体" --reference a.png --image out.png

# 多轮对话
npx -y bun ${SKILL_DIR}/scripts/main.ts "记住：42" --sessionId session-abc
npx -y bun ${SKILL_DIR}/scripts/main.ts "什么数字？" --sessionId session-abc

# JSON 输出
npx -y bun ${SKILL_DIR}/scripts/main.ts "Hello" --json
```

## 选项

| 选项 | 描述 |
|--------|-------------|
| `--prompt`, `-p` | 提示文本 |
| `--promptfiles` | 从文件读取提示（连接） |
| `--model`, `-m` | 模型：gemini-3-pro（默认），gemini-2.5-pro，gemini-2.5-flash |
| `--image [path]` | 生成图像（默认：generated.png） |
| `--reference`, `--ref` | 视觉输入的参考图像 |
| `--sessionId` | 多轮对话的会话 ID |
| `--list-sessions` | 列出保存的会话 |
| `--json` | 输出为 JSON |
| `--login` | 刷新 cookies，然后退出 |
| `--cookie-path` | 自定义 cookies 文件路径 |
| `--profile-dir` | Chrome 配置文件目录 | 

## 模型

| 模型 | 描述 |
|-------|-------------|
| `gemini-3-pro` | 默认，最新 |
| `gemini-2.5-pro` | 以前的 pro |
| `gemini-2.5-flash` | 快速，轻量级 |

## 认证

首次运行时打开浏览器进行 Google 认证。Cookies 自动缓存。

支持的浏览器（自动检测）：Chrome，Chrome Canary/Beta，Chromium，Edge。

强制刷新：`--login` 标志。覆盖浏览器：`GEMINI_WEB_CHROME_PATH` 环境变量。

## 环境变量

| 变量 | 描述 |
|----------|-------------|
| `GEMINI_WEB_DATA_DIR` | 数据目录 |
| `GEMINI_WEB_COOKIE_PATH` | Cookies 文件路径 |
| `GEMINI_WEB_CHROME_PROFILE_DIR` | Chrome 配置文件目录 |
| `GEMINI_WEB_CHROME_PATH` | Chrome 可执行文件路径 |
| `HTTP_PROXY`, `HTTPS_PROXY` | Google 访问的代理（与命令内联设置） | 

## 会话

会话文件存储在数据目录下的 `sessions/<id>.json`。

包含：`id`、`metadata`（Gemini 聊天状态）、`messages` 数组、时间戳。

## 扩展支持

通过 EXTEND.md 进行自定义配置。请参阅 **首选项** 部分了解路径和支持的选项。