---
name: web-fetch
description: Use this skill when users want to scrape web content, clean/format it, and translate it to Chinese. Handles workflows like "Save this webpage as markdown and translate it" or "Scrape and translate this article to Chinese". Supports crawl4ai for web scraping and Zhipu AI GLM-4-Flash for immersive translation.
---

# Web Translator

## Overview

This skill enables scraping web content, cleaning and formatting the result, and providing immersive Chinese translation using Zhipu AI's GLM-4-Flash model. The workflow includes fetching content with crawl4ai, manual cleaning to remove unwanted elements, and bilingual translation that preserves both original and translated text.

## Workflow

The web translation process follows three sequential steps:

### Step 1: Fetch Web Content

Use the `fetch_web_content.py` script to scrape the target webpage using crawl4ai.

**Usage:**
```bash
python scripts/fetch_web_content.py <url> <output_filename>
```

**Example:**
```bash
python scripts/fetch_web_content.py https://example.com/article article.md
```

The script will:
- Fetch the webpage using crawl4ai's AsyncWebCrawler
- Convert HTML to markdown automatically
- Save the result to the specified output file

### Step 2: Clean and Format Content

Manually review and clean the scraped markdown file to remove unwanted content and improve formatting:

**Common cleaning tasks:**
- Remove navigation links, headers, and footers
- Delete social media links and share buttons
- Clean up author information or metadata blocks
- Reorganize title hierarchy (H1, H2, H3)
- Format dates and publication info as blockquotes
- Remove excessive empty lines
- Add section headings for better structure

**Example transformations:**
```markdown
# Before
[Home](/) [About](/about)
# My Article
Posted on Jan 1, 2024
...footer content...

# After
# My Article

> Published: Jan 1, 2024
...cleaned content...
```

**Approach:**
- Use Edit tool to make targeted removals and adjustments
- Focus on preserving the core content while removing chrome
- Improve markdown structure for readability

### Step 3: Immersive Translation

Use the `immersive_translate.py` script to translate the cleaned markdown file.

**Configuration:**
Edit the script to set your Zhipu AI API key:
```python
API_KEY = "your_api_key_here"
```

**Usage:**
```bash
python scripts/immersive_translate.py <input_file> <output_file>
```

**Example:**
```bash
python scripts/immersive_translate.py article.md article_zh.md
```

The script will:
- Preserve the original English text
- Add Chinese translation in italics below each paragraph, heading, and list item
- Maintain markdown formatting and links
- Skip code blocks and URLs
- Apply rate limiting to avoid API throttling

**Translation output format:**
```markdown
# Original Heading
# *翻译后的标题*

Original paragraph text here.
*这里是翻译后的段落文本。*

  * [Original Link Text](url)
  * *[翻译后的链接文本](url)*
```

## Scripts

### fetch_web_content.py

Scrapes web content using crawl4ai and saves as markdown.

**Key features:**
- Uses AsyncWebCrawler for reliable fetching
- Automatic HTML to markdown conversion
- Configurable output location
- Progress indicators

### immersive_translate.py

Provides bilingual translation with original and translated text side-by-side.

**Key features:**
- Uses Zhipu AI GLM-4-Flash model (free tier)
- Preserves markdown structure
- Smart detection of translatable content
- Handles links, lists, headings, and paragraphs
- Rate limiting for API compliance
- Skips code blocks and technical content

**Translation behavior:**
- **Headings**: Translates and adds as new heading with italic marker
- **Paragraphs**: Translates and adds as italic text below
- **List items**: Translates list content, preserves links
- **Links**: Translates link text while preserving URLs
- **Code blocks**: Skipped entirely
- **Empty lines**: Preserved for structure

## Tips

**When to use this skill:**
- User provides a URL and asks to save/translate it
- User wants bilingual content (English + Chinese)
- User requests web scraping with translation
- User mentions crawl4ai or Zhipu AI

**Best practices:**
- Always clean content before translating to avoid wasting API calls on unwanted text
- Review the scraped markdown first to understand the structure
- For complex pages, break cleaning into multiple edit operations
- Check that API key is configured before running translation
- Consider adding section headings during cleaning for better organization

**Limitations:**
- crawl4ai may not work on JavaScript-heavy sites (use alternative methods if needed)
- Translation quality depends on Zhipu AI's model
- Rate limits apply to translation API
- Manual cleaning required (no automated cleanup)
