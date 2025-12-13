#!/usr/bin/env python3
"""
Web content fetcher using crawl4ai

Usage:
    python fetch_web_content.py <url> <output_filename>

Example:
    python fetch_web_content.py https://example.com/article article.md
"""

import sys
import asyncio
from crawl4ai import AsyncWebCrawler


async def fetch_web_content(url, output_file):
    """Fetch web content and save as markdown"""
    print(f"[FETCH] Fetching content from: {url}")

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url)

        # Save markdown content
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.markdown)

        print(f"✓ Content saved to: {output_file}")
        print(f"✓ Total characters: {len(result.markdown)}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python fetch_web_content.py <url> <output_filename>")
        print("Example: python fetch_web_content.py https://example.com article.md")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure output file has .md extension
    if not output_file.endswith('.md'):
        output_file += '.md'

    asyncio.run(fetch_web_content(url, output_file))


if __name__ == "__main__":
    main()
