---
name: baoyu-compress-image
description: Compresses images to WebP (default) or PNG with automatic tool selection. Use when user asks to "compress image", "optimize image", "convert to webp", or reduce image file size.
---

# 图像压缩器

使用最佳可用工具（sips → cwebp → ImageMagick → Sharp）压缩图像。

## 脚本目录

`scripts/` 子目录中的脚本。将 `${SKILL_DIR}` 替换为此 SKILL.md 的目录路径。

| 脚本 | 目的 | 
|--------|---------| 
| `scripts/main.ts` | 图像压缩 CLI |

## 预设（EXTEND.md）

使用 Bash 检查 EXTEND.md 的存在（优先级顺序）：

```bash
# 首先检查项目级别
test -f .baoyu-skills/baoyu-compress-image/EXTEND.md && echo "project"

# 然后用户级别（跨平台：$HOME 在 macOS/Linux/WSL 上有效）
test -f "$HOME/.baoyu-skills/baoyu-compress-image/EXTEND.md" && echo "user"
```

┌────────────────────────────────────────────────────────┬───────────────────┐
│                          路径                          │     位置          │
├────────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-compress-image/EXTEND.md           │ 项目目录          │
├────────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-compress-image/EXTEND.md     │ 用户家目录        │
└────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  结果     │                                  操作                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ 读取、解析、应用设置                                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ 使用默认值                                                              │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md 支持**：默认格式 | 默认质量 | 保持原始偏好

## 使用方法

```bash
npx -y bun ${SKILL_DIR}/scripts/main.ts <input> [options]
```

## 选项

| 选项 | 简写 | 描述 | 默认值 | 
|--------|-------|-------------|---------| 
| `<input>` | | 文件或目录 | 必需 | 
| `--output` | `-o` | 输出路径 | 同路径，新扩展名 | 
| `--format` | `-f` | webp, png, jpeg | webp | 
| `--quality` | `-q` | 质量 0-100 | 80 | 
| `--keep` | `-k` | 保持原始 | false | 
| `--recursive` | `-r` | 处理子目录 | false | 
| `--json` | | JSON 输出 | false |

## 示例

```bash
# 单个文件 → WebP（替换原始文件）
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png

# 保持 PNG 格式
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png -f png --keep

# 目录递归
npx -y bun ${SKILL_DIR}/scripts/main.ts ./images/ -r -q 75

# JSON 输出
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png --json
```

**输出**：
```
image.png → image.webp (245KB → 89KB，64% 减少)
```

## 扩展支持

通过 EXTEND.md 进行自定义配置。有关路径和支持选项，请参阅 **预设** 部分。