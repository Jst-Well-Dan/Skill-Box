---
name: baoyu-post-to-wechat
description: 通过 Chrome CDP 自动化将内容发布到微信公众号（微信公众号）。支持带完整 Markdown 格式的文章发布（文章）和多图图文（图文）发布。
---

# 发布到微信公众号

## 脚本目录

**代理执行**：将此 SKILL.md 目录指定为 `SKILL_DIR`，然后使用 `${SKILL_DIR}/scripts/<name>.ts`。

| 脚本 | 目的 |
|--------|---------|
| `scripts/wechat-browser.ts` | 图文发布（图文） |
| `scripts/wechat-article.ts` | 文章发布（文章） |
| `scripts/md-to-wechat.ts` | Markdown → WeChat HTML |

## 预设（EXTEND.md）

使用 Bash 检查 EXTEND.md 的存在（优先级顺序）：

```bash
# 首先检查项目级别
test -f .baoyu-skills/baoyu-post-to-wechat/EXTEND.md && echo "project"

# 然后是用户级别（跨平台：$HOME 在 macOS/Linux/WSL 上有效）
test -f "$HOME/.baoyu-skills/baoyu-post-to-wechat/EXTEND.md" && echo "user"
```

┌────────────────────────────────────────────────────────┬───────────────────┐
│                          路径                          │     位置          │
├────────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-post-to-wechat/EXTEND.md           │ 项目目录          │
├────────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-post-to-wechat/EXTEND.md     │ 用户家目录        │
└────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  行动                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、应用设置                                               │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用默认值                                                              │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：默认主题 | 自动提交预设 | Chrome 配置文件路径

## 使用方法

### 图文

```bash
npx -y bun ${SKILL_DIR}/scripts/wechat-browser.ts --markdown article.md --images ./images/
npx -y bun ${SKILL_DIR}/scripts/wechat-browser.ts --title "标题" --content "内容" --image img.png --submit
```

### 文章

```bash
npx -y bun ${SKILL_DIR}/scripts/wechat-article.ts --markdown article.md --theme grace
```

## 详细参考

| 主题 | 参考 |
|-------|-----------|
| 图文参数，自动压缩 | [references/image-text-posting.md](references/image-text-posting.md) |
| 文章主题，图片处理 | [references/article-posting.md](references/article-posting.md) |

## 功能比较

| 功能 | 图文 | 文章 |
|---------|------------|---------|
| 多图 | ✓ (最多 9 张) | ✓ (内联) |
| Markdown 支持 | 标题/内容提取 | 完整格式化 |
| 自动压缩 | ✓ (标题：20 字，内容：1000 字) | ✗ |
| 主题 | ✗ | ✓ (默认，grace，simple) |

## 先决条件

- Google Chrome
- 首次运行：登录微信公众号（会话保留）

## 故障排除

| 问题 | 解决方案 |
|-------|----------|
| 未登录 | 首次运行打开浏览器 - 扫描二维码登录 |
| Chrome 未找到 | 设置 `WECHAT_BROWSER_CHROME_PATH` 环境变量 |
| 粘贴失败 | 检查系统剪贴板权限 |

## 扩展支持

通过 EXTEND.md 进行自定义配置。请参阅 **预设** 部分了解路径和支持的选项。