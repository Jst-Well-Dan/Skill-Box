---
name: weixin-fetch
description: 当用户想要抓取微信公众号（WeChat）文章并将其转换为干净的 Markdown 时使用此技能。处理“抓取微信文章”、“获取这篇公众号文章”、“保存公众号文章”等工作流程。使用基于 Playwright 的浏览器自动化和防机器人绕过技术，实现可靠的微信内容提取。
---

# 微信文章抓取 (WeChat Article Fetcher)

使用 Playwright 浏览器自动化抓取微信公众号文章并转换为干净的 Markdown 格式。

## 功能特性

- 真实的 Chromium 浏览器，绕过微信防机器人保护。
- 自动处理懒加载图片（data-src → src）。
- 根据发布日期 + 标题自动生成文件名（YYYYMMDD 格式）。
- 元数据提取（作者、发布时间）。
- 生成保留图片的干净 Markdown 输出。

## 依赖要求

```bash
pip install playwright markdownify
playwright install chromium
```

## 使用方法

```bash
# 自动生成文件名 (YYYYMMDD+标题 格式)
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

# 自定义文件名
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" article.md
```

## 响应模式

当用户请求抓取微信文章时：

1. **验证 URL**：确保它是微信文章链接 (`mp.weixin.qq.com`)。

2. **执行抓取**：
   ```bash
   python scripts/fetch_weixin.py <url> [output_filename]
   ```
   输出文件名是可选的 - 默认为 YYYYMMDD+标题。

3. **报告结果**：
   - 确认文件已保存并显示统计信息（字符数、字数、图片数）。
   - 显示自动生成的文件名。

## 工作流示例

### 自动生成文件名

```bash
# 用户：“抓取这篇微信文章”
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

# 结果：
# ✓ 已保存：20251214关于财政政策和货币政策的关系.md
# ✓ 统计信息：12,345 字符，8,234 字，5 张图片
```

### 自定义文件名

```bash
# 用户：“获取这篇微信文章，保存为 economy.md”
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" economy.md

# 结果：
# ✓ 已保存：economy.md
```

## 故障排除

| 问题 | 解决方案 |
|-------|----------|
| 微信屏蔽 | 脚本使用真实浏览器绕过防机器人检测 |
| 超时 | 脚本具有 60 秒超时并带重试，通常第二次尝试即可成功 |
| Playwright 未安装 | 运行：`pip install playwright && playwright install chromium` |
| 内容为空 | 等待页面完全加载；检查文章是否仍可访问 |
| 图片丢失 | 脚本会自动转换懒加载图片；检查网络连接 |
