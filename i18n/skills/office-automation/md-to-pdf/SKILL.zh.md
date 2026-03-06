---
name: md-to-pdf
description: 当用户想要将 Markdown 文件转换为 PDF 时使用此技能。处理诸如「转换为 PDF」、「批量转换 MD 文件」、「Convert this markdown to PDF」等工作流。支持单文件和批量目录转换，完美支持 CJK 中文字体、图片嵌入和清晰排版。
---

# Markdown 转 PDF 转换器

将 Markdown 文件转换为格式精美的 PDF 文档，完全支持 CJK（中文/日文/韩文）字体。

## 功能特性

- 使用微软雅黑提供出色的中文（CJK）字体支持
- 图片渲染支持（HTTP/HTTPS URL 和本地路径）
- 保持纵横比的自动图片缩放
- 支持单文件和批量目录转换
- 针对中文内容优化的清晰易读排版
- 带进度跟踪的并发批量处理

## 依赖项

```bash
pip install reportlab markdown beautifulsoup4 html5lib tqdm
```

## 使用方法

### 单文件

```bash
# 自动生成输出名称（同名 .pdf 扩展名）
python scripts/md_to_pdf.py article.md

# 自定义输出名称
python scripts/md_to_pdf.py article.md --output custom_name.pdf
```

### 批量转换目录

```bash
python scripts/md_to_pdf.py ./articles_folder --concurrency 4
```

## 响应模式

当用户请求 Markdown 转 PDF 时：

1. **识别输入：**
   - 单文件 → 直接转换
   - 目录 → 批量转换

2. **执行转换：**
   ```bash
   # 单文件
   python scripts/md_to_pdf.py <markdown_file> [--output output.pdf]

   # 批量目录
   python scripts/md_to_pdf.py <directory> [--concurrency 4]
   ```

3. **报告结果：**
   - 确认输出文件路径和大小
   - 批量转换时：显示成功/失败计数和总大小

## 示例工作流

### 单文件转换

```bash
# 用户: "把这个 markdown 转成 PDF"
python scripts/md_to_pdf.py article.md

# 结果:
# ✅ 输出: article.pdf (128.5 KB)
```

### 批量转换

```bash
# 用户: "批量转换这个文件夹里的所有 markdown"
python scripts/md_to_pdf.py ./articles --concurrency 4

# 结果:
# ✅ 成功: 15 个文件
# ❌ 失败: 0 个文件
# 📦 总大小: 2.35 MB
```

## 故障排除

| 问题 | 解决方案 |
|-------|----------|
| PDF 转换失败 | 安装: `pip install reportlab markdown beautifulsoup4` |
| 中文乱码 | 自动检测微软雅黑字体；确保 Windows 字体可用 |
| PDF 图片丢失 | 检查图片 URL 是否可访问或本地路径是否正确 |
| PDF 太大 | 图片以原始分辨率嵌入；考虑预先压缩图片 |
