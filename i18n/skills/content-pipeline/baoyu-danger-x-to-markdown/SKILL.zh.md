---
name: baoyu-danger-x-to-markdown
description: 将 X（Twitter）推文和文章转换为带 YAML 前置信息的 markdown 格式。使用需要用户同意的逆向工程 API。当用户提到“X to markdown”、“tweet to markdown”、“save tweet”或提供 x.com/twitter.com 网址进行转换时使用。
---

# X to Markdown

将 X 内容转换为 markdown：
- 推文/讨论 → 带有 YAML 前置信息的 markdown
- X 文章 → 完全内容提取

## 脚本目录

脚本位于 `scripts/` 子目录中。

**路径解析**：
1. `SKILL_DIR` = 本 SKILL.md 的目录
2. 脚本路径 = `${SKILL_DIR}/scripts/main.ts`

## 同意要求

**在任何转换之前**，请检查并获得同意。

### 同意流程

**步骤 1**：检查同意文件

```bash
# macOS
cat ~/Library/Application\ Support/baoyu-skills/x-to-markdown/consent.json

# Linux
cat ~/.local/share/baoyu-skills/x-to-markdown/consent.json
```

**步骤 2**：如果 `accepted: true` 且 `disclaimerVersion: "1.0"` 则打印警告并继续：
```
Warning: 使用逆向工程的 X API。同意时间：<acceptedAt>
```

**步骤 3**：如果文件缺失或版本不匹配则显示免责声明：
````
DISCLAIMER

此工具使用逆向工程的 X API，非官方。

风险：
- 如果 X 改变 API，则可能会中断
- 无任何保证或支持
- 可能会受限账户
- 自行承担风险

接受条款并继续？
```
使用 `AskUserQuestion` 并提供选项："是的，我接受" | "不，我拒绝"

**步骤 4**：在同意后创建同意文件：
```json
{
  "version": 1,
  "accepted": true,
  "acceptedAt": "<ISO timestamp>",
  "disclaimerVersion": "1.0"
}
```

**步骤 5**：在拒绝后输出 "用户拒绝。退出。" 并停止。

## Preferences (EXTEND.md)

使用 Bash 检查 EXTEND.md 的存在（优先级顺序）：

```bash
# 首先检查项目级
test -f .baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md && echo "project"

# 然后用户级（跨平台：$HOME 在 macOS/Linux/WSL 上都有效）
test -f "$HOME/.baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md" && echo "user"
```

┌────────────────────────────────────────────────────────────┬───────────────────┐
│                            路径                            │     位置          │
├────────────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md         │ 项目目录          │
├────────────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md   │ 用户家目录        │
└────────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  行动                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、应用设置                                                       │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用默认值                                                              │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：默认输出目录 | 输出格式偏好

## 使用方法

```bash
npx -y bun ${SKILL_DIR}/scripts/main.ts <url>
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> -o output.md
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> --json
```

## 选项

| 选项 | 描述 |
|--------|-------------|
| `<url>` | 推文或文章 URL |
| `-o <path>` | 输出路径 |
| `--json` | JSON 输出 |
| `--login` | 仅刷新 cookie | 

## 支持的 URL

- `https://x.com/<user>/status/<id>`
- `https://twitter.com/<user>/status/<id>`
- `https://x.com/i/article/<id>`

## 输出

```markdown
---
url: https://x.com/user/status/123
author: "Name (@user)"
tweet_count: 3
---

内容...
```

**文件结构**：`x-to-markdown/{username}/{tweet-id}.md`

## 认证

1. **环境变量**（首选）：`X_AUTH_TOKEN`，`X_CT0`
2. **Chrome 登录**（后备）：自动打开 Chrome，本地缓存 cookie

## 扩展支持

通过 EXTEND.md 进行自定义配置。请参阅 **偏好设置** 部分了解路径和支持的选项。