#!/usr/bin/env python3
"""
WeChat (微信公众号) article fetcher

Fetches WeChat articles using requests + BeautifulSoup, no browser needed.
Handles WeChat-specific HTML structure and encoding.

Usage:
    python fetch_weixin.py <url> <output_filename>

Example:
    python fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" article.md
"""

import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def fetch_weixin_article(url, output_file):
    """
    Fetch WeChat article content

    WeChat article structure:
    - Title: #activity-name
    - Content: #js_content
    - Author: #js_name (optional)
    - Publish time: #publish_time (optional)
    """
    print(f"[FETCH] Fetching WeChat article: {url}")

    # WeChat requires specific headers to avoid blocking
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://mp.weixin.qq.com/',
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        print(f"✗ Failed to fetch URL: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title_elem = soup.select_one('#activity-name')
    title = title_elem.get_text(strip=True) if title_elem else "Untitled"
    print(f"[INFO] Title: {title}")

    # Extract author (optional)
    author_elem = soup.select_one('#js_name')
    author = author_elem.get_text(strip=True) if author_elem else None

    # Extract publish time (optional)
    time_elem = soup.select_one('#publish_time')
    publish_time = time_elem.get_text(strip=True) if time_elem else None

    # Extract main content
    content_elem = soup.select_one('#js_content')
    if not content_elem:
        print("✗ Could not find article content (#js_content)")
        print("  This may be a restricted article or require login")
        sys.exit(1)

    # Remove hidden elements and scripts
    for elem in content_elem.select('script, style, .hide, [style*="display:none"], [style*="display: none"]'):
        elem.decompose()

    # Process images
    image_count = 0
    for img in content_elem.find_all('img'):
        # WeChat image URL priority: data-src > data-original > data-actualsrc > src
        # WeChat uses lazy loading, real URL is usually in data-src
        img_url = (
            img.get('data-src') or
            img.get('data-original') or
            img.get('data-actualsrc') or
            img.get('src')
        )

        if img_url:
            # Skip tracking pixels and empty images
            if 'mmbiz.qlogo.cn' in img_url or len(img_url) < 20:
                img.decompose()
                continue

            # Clean URL: remove tracking parameters but keep format params
            # Keep: wx_fmt, tp (important for image format)
            # Remove: wxfrom, from, scene, etc (tracking)
            if '?' in img_url:
                base_url, params = img_url.split('?', 1)
                keep_params = []
                for param in params.split('&'):
                    if param.startswith(('wx_fmt=', 'tp=')):
                        keep_params.append(param)
                img_url = base_url + ('?' + '&'.join(keep_params) if keep_params else '')

            img['src'] = img_url
            image_count += 1

            # Set alt text from data-backw/h or default
            if not img.get('alt'):
                width = img.get('data-w') or img.get('data-backw', '')
                height = img.get('data-h') or img.get('data-backh', '')
                if width and height:
                    img['alt'] = f'图片 ({width}x{height})'
                else:
                    img['alt'] = '图片'
        else:
            # No valid URL, remove the image tag
            img.decompose()

    print(f"[INFO] Found {image_count} images")

    # Convert to markdown
    content_md = md(str(content_elem), heading_style="ATX", bullets="-")

    # Clean up excessive whitespace
    lines = content_md.split('\n')
    cleaned_lines = []
    prev_empty = False
    for line in lines:
        line = line.rstrip()
        is_empty = len(line.strip()) == 0
        if is_empty and prev_empty:
            continue
        cleaned_lines.append(line)
        prev_empty = is_empty
    content_md = '\n'.join(cleaned_lines).strip()

    # Build final markdown
    markdown_parts = [f"# {title}\n"]

    if author or publish_time:
        meta_parts = []
        if author:
            meta_parts.append(f"**作者**: {author}")
        if publish_time:
            meta_parts.append(f"**发布时间**: {publish_time}")
        markdown_parts.append(" | ".join(meta_parts) + "\n")

    markdown_parts.append("---\n")
    markdown_parts.append(content_md)

    final_markdown = '\n'.join(markdown_parts)

    # Save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_markdown)

    # Display statistics
    char_count = len(final_markdown)
    word_count = len(final_markdown.split())
    image_count = final_markdown.count('![')

    print(f"✓ Content saved to: {output_file}")
    print(f"✓ Statistics:")
    print(f"  • Characters: {char_count:,}")
    print(f"  • Words: {word_count:,}")
    print(f"  • Images: {image_count}")
    print(f"\n✓ WeChat article fetched successfully!")


def main():
    if len(sys.argv) != 3:
        print("Usage: python fetch_weixin.py <url> <output_filename>")
        print("Example: python fetch_weixin.py 'https://mp.weixin.qq.com/s/xxxxx' article.md")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    # Validate URL
    if 'mp.weixin.qq.com' not in url:
        print("⚠ Warning: URL does not appear to be a WeChat article")
        print("  Expected: https://mp.weixin.qq.com/s/...")

    # Ensure output file has .md extension
    if not output_file.endswith('.md'):
        output_file += '.md'

    fetch_weixin_article(url, output_file)


if __name__ == "__main__":
    main()
