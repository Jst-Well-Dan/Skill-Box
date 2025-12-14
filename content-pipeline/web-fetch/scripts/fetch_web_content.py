#!/usr/bin/env python3
"""
Web content fetcher using crawl4ai with advanced cleaning

Fetches web pages and automatically cleans them using CSS selector strategy
to remove navigation, headers, footers, and other noise elements.

Usage:
    python fetch_web_content.py <url> <output_filename>

Example:
    python fetch_web_content.py https://example.com/article article.md
"""

import sys
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def fetch_web_content(url, output_file):
    """
    Fetch web content using crawl4ai with CSS selector cleaning strategy

    This configuration:
    - Uses CSS selectors to target main content area
    - Removes navigation, headers, footers, sidebars
    - Excludes social media links
    - Removes overlay elements (popups, modals)
    - Preserves all images with alt text
    - Maintains article structure and formatting
    """
    print(f"[FETCH] Fetching content from: {url}")
    print(f"[CLEAN] Using CSS Selector strategy for noise removal")

    # Configure markdown generator with cleaning options
    markdown_generator = DefaultMarkdownGenerator(
        options={
            "ignore_links": False,           # Keep all links
            "skip_internal_links": True,     # Skip navigation links
            "body_only": True,               # Focus on main content
        }
    )

    # Configure crawler with aggressive cleaning
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=markdown_generator,

        # Target main content area using CSS selectors
        # These selectors match common content containers
        css_selector="main, article, [role='main'], .main-content, #main-content, #content, .content, .post-content, .entry-content, #js_content, .Post-RichText, #content_views",

        # Exclude noise elements
        excluded_tags=[
            'nav',      # Navigation menus
            'footer',   # Page footers
            'header',   # Page headers (site-wide)
            'aside',    # Sidebars
            'script',   # JavaScript code
            'style',    # CSS styles
            'form',     # Forms (usually search/login)
            'iframe',   # Embedded frames
        ],

        # Additional cleaning options
        exclude_social_media_links=True,     # Remove social sharing links
        word_count_threshold=10,             # Minimum words per text block
        remove_overlay_elements=True,        # Remove popups and modals
        exclude_external_images=False,       # Keep all images
    )

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url, config=config)

        if not result.success:
            print(f"✗ Failed to fetch content: {result.error_message}")
            sys.exit(1)

        # Save markdown content
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.markdown)

        # Display statistics
        char_count = len(result.markdown)
        word_count = len(result.markdown.split())
        image_count = result.markdown.count('![')

        print(f"✓ Content saved to: {output_file}")
        print(f"✓ Statistics:")
        print(f"  • Characters: {char_count:,}")
        print(f"  • Words: {word_count:,}")
        print(f"  • Images: {image_count}")
        print(f"\n✓ Content cleaned and ready to use!")


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
