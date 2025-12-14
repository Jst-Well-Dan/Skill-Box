---
name: web-fetch
description: Use this skill when users want to scrape web content and convert it to clean Markdown. Handles workflows like "Save this webpage as markdown", "Fetch this article", or "抓取网页内容". Supports crawl4ai for general web scraping and specialized WeChat (微信公众号) article fetching.
---

# Web Fetch

Fetch web content and convert to clean Markdown format. Supports general websites and WeChat (微信公众号) articles.

## Features

- Automatic noise removal (navigation, headers, footers, sidebars)
- Image preservation with alt text
- WeChat article special handling (lazy-loaded images, metadata extraction)
- Clean Markdown output ready for translation or processing

## Dependencies

```bash
pip install crawl4ai requests beautifulsoup4 markdownify
```

## Usage

### General Web Pages

For most websites, use the crawl4ai-based fetcher:

```bash
python scripts/fetch_web_content.py <url> <output_filename>
```

Example:
```bash
python scripts/fetch_web_content.py https://example.com/article article.md
```

### WeChat Articles (微信公众号)

For WeChat articles, use the specialized fetcher:

```bash
python scripts/fetch_weixin.py <url> <output_filename>
```

Example:
```bash
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" article.md
```

## Response Pattern

When user requests web content fetching:

1. **Identify URL type:**
   - WeChat URL (`mp.weixin.qq.com`) → use `fetch_weixin.py`
   - Other URLs → use `fetch_web_content.py`

2. **Determine output filename:**
   - Use user-specified name, or
   - Generate from article title/URL

3. **Execute appropriate script:**
   ```bash
   python scripts/fetch_web_content.py <url> <output>.md
   # or
   python scripts/fetch_weixin.py <url> <output>.md
   ```

4. **Report results:**
   - Confirm file saved
   - Show statistics (characters, words, images)
   - Offer next steps (translate, summarize, etc.)

## Common Workflows

### Fetch and Process

1. Fetch content: `python scripts/fetch_web_content.py <url> article.md`
2. Process the markdown (summarize, translate with other tools, etc.)

### Batch Processing

For multiple URLs, loop through and fetch each:
```bash
for url in url1 url2 url3; do
  python scripts/fetch_web_content.py "$url" "output_$(date +%s).md"
done
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Empty content | Try different CSS selector or use WeChat fetcher |
| Missing images | Check if site blocks external requests |
| Encoding issues | Content is saved as UTF-8 by default |
| WeChat blocked | May require login for restricted articles |
