#!/usr/bin/env python3
"""
WeChat article fetcher using Playwright with local browser

Uses Playwright to launch a real browser for fetching WeChat articles,
which helps bypass anti-bot protections and properly load dynamic content.

Usage:
    python fetch_weixin.py <url> [output_filename]

Example:
    # Auto-generate filename (YYYYMMDD+Title format)
    python fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx"

    # Custom filename
    python fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" article.md
"""

import sys
import asyncio
import re
from playwright.async_api import async_playwright
from markdownify import markdownify as md


def parse_publish_date(publish_time):
    """
    Parse publish time and extract date in YYYYMMDD format

    Examples:
        "2025年12月6日 13:31" -> "20251206"
        "2024年1月5日" -> "20240105"
    """
    if not publish_time:
        return None

    # Match pattern: YYYY年MM月DD日
    match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', publish_time)
    if match:
        year = match.group(1)
        month = match.group(2).zfill(2)  # Pad with zero if single digit
        day = match.group(3).zfill(2)    # Pad with zero if single digit
        return f"{year}{month}{day}"

    return None


def sanitize_filename(filename):
    """
    Remove or replace invalid characters in filename

    Windows invalid characters: < > : " / \\ | ? *
    Also remove leading/trailing spaces and dots
    """
    # Replace invalid characters with empty string or underscore
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)

    # Replace multiple spaces with single space
    filename = re.sub(r'\s+', ' ', filename)

    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')

    # Limit length (Windows MAX_PATH is 260, leave room for path)
    max_length = 200
    if len(filename) > max_length:
        filename = filename[:max_length]

    return filename


async def fetch_weixin_article(url, output_file=None):
    """
    Fetch WeChat article using Playwright browser automation

    Benefits of using Playwright:
    - Real browser environment (can execute JavaScript)
    - Better handling of anti-bot protections
    - Proper loading of lazy-loaded images
    - Can wait for dynamic content to load
    """
    print(f"[FETCH] Fetching WeChat article with Playwright: {url}")
    print(f"[INFO] Launching browser (this may take a moment)...")

    async with async_playwright() as p:
        # Launch browser with headless=False to see the browser window
        browser = await p.chromium.launch(
            headless=False,  # Set to True for background operation
            args=['--disable-blink-features=AutomationControlled']
        )

        # Create context with mobile user agent (WeChat articles work well on mobile)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Linux; Android 12; SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            viewport={'width': 414, 'height': 896},
            locale='zh-CN',
        )

        page = await context.new_page()

        try:
            # Navigate to the article
            print(f"[LOAD] Loading page...")
            await page.goto(url, wait_until='domcontentloaded', timeout=90000)

            # Wait for content to load with longer timeout
            print(f"[WAIT] Waiting for content to appear...")
            try:
                await page.wait_for_selector('#js_content', timeout=60000)
            except Exception as e:
                # Try waiting a bit more in case of slow loading
                print(f"[WAIT] Content not found, waiting additional time...")
                await asyncio.sleep(5)

                # Take screenshot for debugging
                try:
                    screenshot_path = "debug_page.png"
                    await page.screenshot(path=screenshot_path)
                    print(f"[DEBUG] Screenshot saved to: {screenshot_path}")
                except:
                    pass

                # Check if it's an error page
                page_title = await page.title()
                print(f"[DEBUG] Page title: {page_title}")

                await page.wait_for_selector('#js_content', timeout=30000)

            # Additional wait for lazy-loaded images and dynamic content
            print(f"[WAIT] Waiting for images to load...")
            await asyncio.sleep(3)

            # Extract title
            title = await page.locator('#activity-name').text_content()
            title = title.strip() if title else "Untitled"
            print(f"[INFO] Title: {title}")

            # Extract author (optional)
            try:
                author = await page.locator('#js_name').text_content()
                author = author.strip() if author else None
            except:
                author = None

            # Extract publish time (optional)
            try:
                publish_time = await page.locator('#publish_time').text_content()
                publish_time = publish_time.strip() if publish_time else None
            except:
                publish_time = None

            # Process images - replace data-src with src for lazy-loaded images
            await page.evaluate("""
                () => {
                    const images = document.querySelectorAll('#js_content img');
                    images.forEach(img => {
                        const dataSrc = img.getAttribute('data-src') ||
                                      img.getAttribute('data-original') ||
                                      img.getAttribute('data-actualsrc');
                        if (dataSrc) {
                            img.src = dataSrc;
                        }
                    });
                }
            """)

            # Get the cleaned HTML content
            content_html = await page.locator('#js_content').inner_html()

            # Count images
            image_count = await page.locator('#js_content img').count()
            print(f"[INFO] Found {image_count} images")

            # Convert to markdown
            content_md = md(content_html, heading_style="ATX", bullets="-")

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

            # Generate filename if not provided
            if output_file is None:
                date_str = parse_publish_date(publish_time)
                clean_title = sanitize_filename(title)

                if date_str:
                    output_file = f"{date_str}{clean_title}.md"
                else:
                    output_file = f"{clean_title}.md"

                print(f"[INFO] Auto-generated filename: {output_file}")

            # Save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_markdown)

            # Display statistics
            char_count = len(final_markdown)
            word_count = len(final_markdown.split())
            md_image_count = final_markdown.count('![')

            print(f"✓ Content saved to: {output_file}")
            print(f"✓ Statistics:")
            print(f"  • Characters: {char_count:,}")
            print(f"  • Words: {word_count:,}")
            print(f"  • Images: {md_image_count}")
            print(f"\n✓ WeChat article fetched successfully!")

        except Exception as e:
            print(f"✗ Error fetching article: {e}")
            sys.exit(1)
        finally:
            await browser.close()


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_weixin.py <url> [output_filename]")
        print("\nExamples:")
        print("  # Auto-generate filename (YYYYMMDD+Title format)")
        print("  python fetch_weixin.py 'https://mp.weixin.qq.com/s/xxxxx'")
        print("\n  # Custom filename")
        print("  python fetch_weixin.py 'https://mp.weixin.qq.com/s/xxxxx' article.md")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    # Validate URL
    if 'mp.weixin.qq.com' not in url:
        print("⚠ Warning: URL does not appear to be a WeChat article")
        print("  Expected: https://mp.weixin.qq.com/s/...")

    # Ensure output file has .md extension if provided
    if output_file and not output_file.endswith('.md'):
        output_file += '.md'

    # Run async function
    asyncio.run(fetch_weixin_article(url, output_file))


if __name__ == "__main__":
    main()
