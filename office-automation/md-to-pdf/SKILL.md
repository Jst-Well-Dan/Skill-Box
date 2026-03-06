---
name: md-to-pdf
description: Use this skill when users want to convert Markdown files to PDF. Handles workflows like "Convert this markdown to PDF", "转换为PDF", "批量转换MD文件". Supports single file and batch directory conversion with excellent CJK (Chinese) font support, image embedding, and clean typography.
---

# Markdown to PDF Converter

Convert Markdown files to beautifully formatted PDF documents with full CJK (Chinese/Japanese/Korean) font support.

## Features

- Excellent Chinese (CJK) font support using Microsoft YaHei
- Image rendering support (HTTP/HTTPS URLs and local paths)
- Automatic image scaling with aspect ratio preservation
- Single file and batch directory conversion
- Clean, readable typography optimized for Chinese content
- Concurrent batch processing with progress tracking

## Dependencies

```bash
pip install reportlab markdown beautifulsoup4 html5lib tqdm
```

## Usage

### Single file

```bash
# Auto-generates output name (same name with .pdf extension)
python scripts/md_to_pdf.py article.md

# Custom output name
python scripts/md_to_pdf.py article.md --output custom_name.pdf
```

### Batch convert directory

```bash
python scripts/md_to_pdf.py ./articles_folder --concurrency 4
```

## Response Pattern

When user requests Markdown to PDF conversion:

1. **Identify input:**
   - Single file → direct conversion
   - Directory → batch conversion

2. **Execute conversion:**
   ```bash
   # Single file
   python scripts/md_to_pdf.py <markdown_file> [--output output.pdf]

   # Batch directory
   python scripts/md_to_pdf.py <directory> [--concurrency 4]
   ```

3. **Report results:**
   - Confirm output file path and size
   - For batch: show success/failure counts and total size

## Example Workflows

### Single file conversion

```bash
# User: "把这个markdown转成PDF"
python scripts/md_to_pdf.py article.md

# Result:
# ✅ Output: article.pdf (128.5 KB)
```

### Batch conversion

```bash
# User: "批量转换这个文件夹里的所有markdown"
python scripts/md_to_pdf.py ./articles --concurrency 4

# Result:
# ✅ Success: 15 files
# ❌ Failed: 0 files
# 📦 Total size: 2.35 MB
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| PDF conversion failed | Install: `pip install reportlab markdown beautifulsoup4` |
| Chinese characters garbled | Microsoft YaHei font is auto-detected; ensure Windows fonts are available |
| Images missing in PDF | Check that image URLs are accessible or local paths are correct |
| PDF too large | Images are embedded at original resolution; consider pre-compressing images |
