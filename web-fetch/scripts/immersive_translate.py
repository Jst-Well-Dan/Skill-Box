#!/usr/bin/env python3
"""
Immersive Markdown Translator using Zhipu AI GLM-4-Flash

Translates English markdown to Chinese while preserving the original text.
Creates a bilingual document with English and Chinese side-by-side.

Usage:
    python immersive_translate.py <input_file> <output_file>

Example:
    python immersive_translate.py article.md article_zh.md

Configuration:
    Set your Zhipu AI API key in the API_KEY variable below.
"""

import sys
import requests
import re
import time


class ImmersiveTranslator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        self.model = "GLM-4-Flash"

    def translate_text(self, text):
        """Translate text using Zhipu AI"""
        if not text.strip():
            return text

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": f"请将以下英文翻译成中文，只返回翻译结果，不要添加任何解释：\n\n{text}"
                }
            ],
            "temperature": 0.3
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            result = response.json()

            if 'choices' in result and len(result['choices']) > 0:
                translation = result['choices'][0]['message']['content'].strip()
                return translation
            else:
                print(f"⚠ API response format unexpected: {result}")
                return text

        except Exception as e:
            print(f"⚠ Translation error: {e}")
            return text

    def is_code_block(self, line):
        """Check if line is a code block marker"""
        return line.strip().startswith('```')

    def should_translate(self, line):
        """Determine if line should be translated"""
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            return False

        # Skip pure URLs
        if stripped.startswith('http://') or stripped.startswith('https://'):
            return False

        # Skip code block markers
        if stripped.startswith('```'):
            return False

        # Check if contains English letters
        if not bool(re.search(r'[a-zA-Z]', stripped)):
            return False

        return True

    def translate_markdown(self, input_file, output_file):
        """Translate markdown file immersively"""
        print(f"[TRANSLATE] Starting translation: {input_file}")

        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        translated_lines = []
        in_code_block = False

        for i, line in enumerate(lines):
            # Add original line
            translated_lines.append(line.rstrip('\n'))

            # Check code block status
            if self.is_code_block(line):
                in_code_block = not in_code_block
                continue

            # Skip translation inside code blocks
            if in_code_block:
                continue

            # Determine if translation is needed
            if self.should_translate(line):
                # Handle list items
                match = re.match(r'^(\s*[\*\-\+]\s+)(.*)', line)
                if match:
                    indent = match.group(1)
                    content = match.group(2).strip()

                    # Check if it's a link format [text](url)
                    link_match = re.match(r'^\[(.*?)\]\((.*?)\)(.*)$', content)
                    if link_match:
                        link_text = link_match.group(1)
                        link_url = link_match.group(2)
                        remaining = link_match.group(3)

                        # Translate link text
                        translation = self.translate_text(link_text)
                        translated_lines.append(f"{indent}*[{translation}]({link_url}){remaining}*")
                        print(f"✓ Translated link: {link_text[:50]}...")
                    else:
                        # Regular list item
                        translation = self.translate_text(content)
                        translated_lines.append(f"{indent}*{translation}*")
                        print(f"✓ Translated list item: {content[:50]}...")

                    time.sleep(0.5)  # Rate limiting

                # Handle headings
                elif line.strip().startswith('#'):
                    match = re.match(r'^(#+)\s+(.*)', line)
                    if match:
                        level = match.group(1)
                        content = match.group(2).strip()
                        translation = self.translate_text(content)
                        translated_lines.append(f"{level} *{translation}*")
                        print(f"✓ Translated heading: {content}")
                        time.sleep(0.5)

                # Handle regular paragraphs
                elif line.strip() and not re.match(r'^\s*[\*\-\+]', line):
                    content = line.strip()
                    # Skip pure links and special formats
                    if not (content.startswith('[') or content.startswith('http')):
                        translation = self.translate_text(content)
                        translated_lines.append(f"*{translation}*")
                        print(f"✓ Translated paragraph: {content[:50]}...")
                        time.sleep(0.5)

        # Save translation
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(translated_lines))

        print(f"\n✓ Translation complete! Saved to: {output_file}")


def main():
    # Configuration - Set your API key here
    API_KEY = "00ca9058f2ac487ba8626e991383d664.bZyNLSmVLmV3uMAa"

    if len(sys.argv) != 3:
        print("Usage: python immersive_translate.py <input_file> <output_file>")
        print("Example: python immersive_translate.py article.md article_zh.md")
        sys.exit(1)

    if API_KEY == "your_api_key_here":
        print("⚠ Error: Please set your Zhipu AI API key in the script")
        print("Edit the API_KEY variable in immersive_translate.py")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure output file has .md extension
    if not output_file.endswith('.md'):
        output_file += '.md'

    translator = ImmersiveTranslator(API_KEY)
    translator.translate_markdown(input_file, output_file)


if __name__ == "__main__":
    main()
