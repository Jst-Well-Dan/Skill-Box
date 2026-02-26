---
name: web-fetch
description: 当用户想要抓取网页内容并将其转换为干净的 Markdown 或 PDF 时使用此技能。处理诸如“将此网页保存为 PDF”、“获取此文章”、“抓取网页内容”或“转换为 PDF”等工作流。支持用于通用网页抓取的 crawl4ai 和用于带有反机器人绕过的微信公众号文章抓取的 Playwright。默认情况下自动转换为 PDF，除非用户指定仅 Markdown。
---

# 网页抓取 (Web Fetch)

抓取网页内容并将其转换为干净的 Markdown 和 PDF 格式。支持通用网站和微信公众号文章。

## 功能特性

- 自动去除干扰内容（导航栏、页眉、页脚、侧边栏）
- 保留带有替代文本的图片
- 微信文章特殊处理（懒加载图片、元数据提取）
- 干净的 Markdown 输出，便于翻译或后续处理
- **具有清晰阅读风格的 PDF 转换**
- **支持中文内容的 CJK 字体**
- **默认同输出 MD 和 PDF**

## 依赖项

```bash
# 核心依赖
pip install crawl4ai requests beautifulsoup4 markdownify

# 微信文章抓取
pip install playwright
playwright install chromium

# 带有 CJK 字体支持的 PDF 转换
pip install reportlab markdown beautifulsoup4
```

**注意**: `reportlab` 提供了出色的 CJK 字体支持，并且无需系统依赖即可在 Windows/Mac/Linux 上运行。

## 使用方法

### 通用网页

对于大多数网站，使用基于 crawl4ai 的抓取工具：

```bash
python scripts/fetch_web_content.py <url> <output_filename>
```

示例:
```bash
python scripts/fetch_web_content.py https://example.com/article article.md
```

### 微信公众号文章

对于微信文章，使用带有反机器人绕过功能的基于 Playwright 的抓取工具：

```bash
python scripts/fetch_weixin.py <url> [output_filename]
```

示例:
```bash
# 自动生成文件名 (YYYYMMDD+标题 格式)
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

# 自定义文件名
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" article.md
```

**功能:**
- 使用真实的 Chromium 浏览器绕过反机器人保护
- 自动处理懒加载图片
- 自动从发布日期 + 标题生成文件名 (YYYYMMDD格式)
- 支持可见浏览器（用于调试）和无头模式

### 将 Markdown 转换为 PDF

抓取内容为 Markdown 后，转换为 PDF：

```bash
python scripts/md_to_pdf.py <markdown_file> [--output output.pdf]
```

示例:
```bash
# 将单个文件转换为 PDF (自动生成输出名称)
python scripts/md_to_pdf.py article.md

# 使用自定义输出名称转换
python scripts/md_to_pdf.py article.md --output custom_name.pdf

# 批量转换整个目录
python scripts/md_to_pdf.py ./articles_folder --concurrency 4
```

**功能:**
- 使用 Microsoft YaHei 提供出色的中文 (CJK) 字体支持
- 图片渲染支持 (HTTP/HTTPS URL 和本地路径)
- 保持纵横比的自动图片缩放
- 支持单个文件和批量目录转换
- 针对中文内容优化的清晰易读排版

## 响应模式 (已更新)

当用户请求网页内容抓取时：

1. **识别 URL 类型:**
   - 微信 URL (`mp.weixin.qq.com`) → 使用 `fetch_weixin.py`
   - 其他 URL → 使用 `fetch_web_content.py`

2. **确定输出格式:**
   - 用户明确提到 "PDF" → MD + PDF
   - 用户说 "only MD"/"no PDF"/"markdown only"/"只要 markdown" → 仅 MD
   - **请求模棱两可** → 询问: "您希望我也将其转换为 PDF 格式吗？"

   **检测示例:**
   - "Fetch as PDF" / "转换为PDF" → MD + PDF
   - "Save to PDF" / "保存为 PDF" → MD + PDF
   - "Get markdown only" / "只要 markdown" → 仅 MD
   - "Fetch this article" / "获取这篇文章" → **询问用户**
   - "抓取网页内容" → **询问用户**

3. **执行抓取:**
   ```bash
   python scripts/fetch_web_content.py <url> <output>.md
   # 或
   python scripts/fetch_weixin.py <url> [output].md
   ```

   **注意:** 对于微信文章，输出文件名是可选的 - 它会自动生成为 YYYYMMDD+标题

4. **转换为 PDF (如果请求):**
   ```bash
   python scripts/md_to_pdf.py <output>.md
   ```
   这将在 `<output>.md` 旁边创建 `<output>.pdf`

5. **报告结果:**
   - 确认两个文件都已保存 (如果是 PDF)
   - 显示两种格式的统计信息
   - 建议后续步骤

## 示例工作流

### 工作流 1: 抓取并生成 PDF (明确请求)

```bash
# 用户: "把这篇文章抓取为 PDF: https://example.com/article"

# 步骤 1: 抓取 markdown
python scripts/fetch_web_content.py https://example.com/article article.md

# 步骤 2: 转换为 PDF
python scripts/md_to_pdf.py article.md

# 结果:
# ✓ 已保存: article.md (45 KB, 8,234 字)
# ✓ PDF: article.pdf (包含嵌入的图片)
```

### 工作流 2: 仅抓取 Markdown

```bash
# 用户: "只要 markdown"

# 步骤 1: 抓取 markdown
python scripts/fetch_web_content.py https://example.com/article article.md

# 步骤 2: 跳过 PDF 转换

# 结果:
# ✓ 已保存: article.md (45 KB, 8,234 字)
```

### 工作流 3: 模棱两可的请求

```bash
# 用户: "获取这篇文章: https://example.com/article"

# Claude 询问: "我会为您抓取这篇文章。您希望我也将其转换为 PDF 格式吗？"
# 用户: "是的"

# 然后继续工作流 1
```

### 工作流 4: 微信文章生成 PDF

```bash
# 用户: "抓取微信文章为PDF"

# 步骤 1: 抓取 markdown (自动生成文件名为 YYYYMMDD+标题)
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

# 步骤 2: 转换为 PDF (使用自动生成的文件名)
python scripts/md_to_pdf.py 20251214关于财政政策和货币政策的关系.md

# 结果:
# ✓ 已保存: 20251214关于财政政策和货币政策的关系.md (中文内容)
# ✓ PDF: 20251214关于财政政策和货币政策的关系.pdf (完美支持中文和图片)
```

### 批量处理

对于多个 URL，循环遍历并抓取每个：
```bash
for url in url1 url2 url3; do
  filename="output_$(date +%s)"
  python scripts/fetch_web_content.py "$url" "$filename.md"
  python scripts/md_to_pdf.py "$filename.md"  # 可选: 添加 PDF
done
```

## 故障排除

| 问题 | 解决方案 |
|-------|----------|
| 内容为空 | 尝试不同的 CSS 选择器或使用微信 Playwright 抓取工具 |
| 图片丢失 | 检查网站是否阻止外部请求 |
| 编码问题 | 内容默认保存为 UTF-8 |
| 微信被拦截 | 使用 Playwright 抓取工具 - 它启动真实浏览器以绕过反机器人 |
| **微信超时** | 脚本有 60秒超时并重试 - 通常在第二次尝试时成功 |
| **Playwright 未安装** | 运行: `pip install playwright && playwright install chromium` |
| **PDF 转换失败** | 安装依赖: `pip install reportlab markdown beautifulsoup4` |
| **PDF 中文乱码** | 自动使用 Microsoft YaHei 字体 (出色的 CJK 支持) |
| **PDF 图片丢失** | 检查图片 URL 是否可访问或本地图片路径是否正确 |
| **PDF 太大** | 图片已嵌入并缩放; 原始图片大小会影响 PDF 大小 |