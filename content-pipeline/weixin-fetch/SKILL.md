---
name: weixin-fetch
description: Use this skill when users want to fetch WeChat (微信公众号) articles and convert them to clean Markdown. Handles workflows like "抓取微信文章", "Fetch this WeChat article", "保存公众号文章". Uses Playwright-based browser automation with anti-bot bypass for reliable WeChat content extraction.
---

# WeChat Article Fetcher (微信文章抓取)

Fetch WeChat (微信公众号) articles and convert to clean Markdown using Playwright browser automation.

## Features

- Real Chromium browser to bypass WeChat anti-bot protections
- Automatic lazy-loaded image handling (data-src → src)
- Auto-generated filename from publish date + title (YYYYMMDD format)
- Metadata extraction (author, publish time)
- Clean Markdown output with preserved images

## Dependencies

```bash
pip install playwright markdownify
playwright install chromium
```

## Usage

```bash
# Auto-generate filename (YYYYMMDD+Title format)
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

# Custom filename
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" article.md
```

## Response Pattern

When user requests WeChat article fetching:

1. **Validate URL**: Ensure it's a WeChat URL (`mp.weixin.qq.com`)

2. **Execute fetching:**
   ```bash
   python scripts/fetch_weixin.py <url> [output_filename]
   ```
   Output filename is optional - auto-generates as YYYYMMDD+Title

3. **Report results:**
   - Confirm file saved with statistics (characters, words, images)
   - Show the auto-generated filename

## Example Workflows

### Auto-generated filename

```bash
# User: "抓取这篇微信文章"
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

# Result:
# ✓ Saved: 20251214关于财政政策和货币政策的关系.md
# ✓ Statistics: 12,345 characters, 8,234 words, 5 images
```

### Custom filename

```bash
# User: "Fetch this WeChat article, save as economy.md"
python scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" economy.md

# Result:
# ✓ Saved: economy.md
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| WeChat blocked | Script uses real browser to bypass anti-bot |
| Timeout | Script has 60s timeout with retry - usually succeeds on second attempt |
| Playwright not installed | Run: `pip install playwright && playwright install chromium` |
| Empty content | Wait for page to fully load; check if article is still accessible |
| Missing images | Script auto-converts lazy-loaded images; check network connectivity |
