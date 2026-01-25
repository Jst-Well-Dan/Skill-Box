---
name: baoyu-url-to-markdown
description: 使用 Chrome CDP 捕取任何 URL 并将其转换为 markdown。支持两种模式 - 页面加载时自动捕获，或等待用户信号（适用于需要登录的页面）。当用户想将网页保存为 markdown 时使用。
---

# URL 转换为 Markdown

通过 Chrome CDP 捕取任何 URL 并将 HTML 转换为干净的 markdown。

## 脚本目录

**重要**: 所有脚本都位于此技能的 `scripts/` 子目录中。

**代理执行说明**：
1. 确定此 SKILL.md 文件目录路径为 `SKILL_DIR`
2. 脚本路径 = `${SKILL_DIR}/scripts/<script-name>.ts`
3. 在本文档中替换所有 `${SKILL_DIR}` 为实际路径

**脚本参考**：
| 脚本 | 目的 |
|------|------|
| `scripts/main.ts` | CLI 入口点，用于 URL 捕取 |

## 预设（EXTEND.md）

使用 Bash 检查 EXTEND.md 存在（优先顺序）：

```bash
# 首先检查项目级
test -f .baoyu-skills/baoyu-url-to-markdown/EXTEND.md && echo "project"

# 然后是用户级（跨平台：$HOME 在 macOS/Linux/WSL 上都有效）
test -f "$HOME/.baoyu-skills/baoyu-url-to-markdown/EXTEND.md" && echo "user"
```

┌────────────────────────────────────────────────────────┬───────────────────┐
│                          路径                          │     位置          │
├────────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-url-to-markdown/EXTEND.md          │ 项目目录          │
├────────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-url-to-markdown/EXTEND.md    │ 用户家目录        │
└────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  操作                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、应用设置                                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用默认值                                                              │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：默认输出目录 | 默认捕获模式 | 超时设置

## 功能

- 使用 Chrome CDP 进行完整的 JavaScript 渲染
- 两种捕获模式：自动或等待用户
- 带有元数据的干净 markdown 输出
- 通过等待模式处理需要登录的页面

## 使用方法

```bash
# 自动模式（默认）- 页面加载时捕获
npx -y bun ${SKILL_DIR}/scripts/main.ts <url>

# 等待模式 - 在捕获之前等待用户信号
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> --wait

# 保存到特定文件
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> -o output.md
```

## 选项

| 选项 | 描述 |
|------|------|
| `<url>` | 要获取的 URL |
| `-o <path>` | 输出文件路径（默认：自动生成） |
| `--wait` | 在捕获之前等待用户信号 |
| `--timeout <ms>` | 页面加载超时（默认：30000） |

## 捕获模式

| 模式 | 行为 | 使用场景 |
|------|------|----------|
| 自动（默认） | 网络空闲时捕获 | 公共页面、静态内容 |
| 等待（`--wait`） | 用户准备就绪时进行捕获 | 需要登录、懒加载、付费墙 |

**等待模式工作流程**：
1. 使用 `--wait` 运行 → 脚本输出 "准备好时按 Enter"
2. 要求用户确认页面已准备好
3. 向 stdin 发送换行符以触发捕获

## 输出格式

YAML 前置信息带有 `url`、`title`、`description`、`author`、`published`、`captured_at` 字段，后跟转换后的 markdown 内容。

## 输出目录

````
url-to-markdown/<domain>/<slug>.md
```

- `<slug>`：来自页面标题或 URL 路径（短横线分隔，2-6 个单词）
- 冲突解决：追加时间戳 `<slug>-YYYYMMDD-HHMMSS.md`

## 环境变量

| 变量 | 描述 |
|------|------|
| `URL_CHROME_PATH` | 自定义 Chrome 可执行文件路径 |
| `URL_DATA_DIR` | 自定义数据目录 |
| `URL_CHROME_PROFILE_DIR` | 自定义 Chrome 配置文件目录 |

**故障排除**：Chrome 未找到 → 设置 `URL_CHROME_PATH`。超时 → 增加 `--timeout`。复杂页面 → 尝试 `--wait` 模式。

## 扩展支持

通过 EXTEND.md 进行自定义配置。有关路径和支持选项，请参阅 **预设** 部分。