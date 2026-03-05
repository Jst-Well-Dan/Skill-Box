---
name: defuddle
description: 使用 Defuddle CLI 从网页中提取干净的 Markdown 内容，移除干扰项和导航以节省 Token。在用户提供 URL 要求阅读或分析时（如在线文档、文章、博客等），建议代替 WebFetch 优先使用。
---

# Defuddle

使用 Defuddle CLI 提取网页的干净可读内容。对于标准网页，优先于 WebFetch 使用——它会移除导航、广告和干扰，减少 Token 消耗。

## 使用方法

始终使用 `--md` 获取 Markdown 输出：
`defuddle parse <url> --md`

保存到文件：
`defuddle parse <url> --md -o content.md`

提取特定元数据：
`defuddle parse <url> -p title`
