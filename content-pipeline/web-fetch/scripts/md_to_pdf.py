#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的Markdown到PDF批量转换工具（修复中文支持）
使用 markdown + reportlab 实现完美中文显示
"""

import os
import sys
from pathlib import Path
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def check_dependencies():
    """检查并安装必要的依赖"""
    required = {
        'markdown': 'markdown',
        'reportlab': 'reportlab',
        'html5lib': 'html5lib',
        'bs4': 'beautifulsoup4'
    }

    missing = []
    for module, package in required.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)

    if missing:
        print(f"📦 需要安装以下依赖包: {', '.join(missing)}")
        print(f"正在安装...")
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q'] + missing)
        print("✅ 依赖安装完成\n")


# 检查依赖
check_dependencies()

import markdown
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from bs4 import BeautifulSoup
import re
import urllib.request
import tempfile


class SimpleMDtoPDFConverter:
    """简单的Markdown到PDF转换器（支持中文）"""

    def __init__(self, output_dir: str = None):
        self.output_dir = output_dir
        self.md_file_dir = None  # 用于解析相对路径的图片
        self._register_fonts()
        self._setup_styles()

    def _register_fonts(self):
        """注册中文字体"""
        try:
            # 尝试注册Windows系统字体
            font_paths = [
                ('msyh', 'C:/Windows/Fonts/msyh.ttc'),      # 微软雅黑
                ('simsun', 'C:/Windows/Fonts/simsun.ttc'),  # 宋体
                ('simhei', 'C:/Windows/Fonts/simhei.ttf'),  # 黑体
            ]

            self.chinese_font = None
            for font_name, font_path in font_paths:
                if os.path.exists(font_path):
                    try:
                        pdfmetrics.registerFont(TTFont(font_name, font_path))
                        self.chinese_font = font_name
                        break
                    except:
                        continue

            if not self.chinese_font:
                # 如果都失败，使用内置字体
                self.chinese_font = 'Helvetica'
                print("⚠️  警告：未找到中文字体，将使用默认字体（可能无法显示中文）")
        except Exception as e:
            self.chinese_font = 'Helvetica'
            print(f"⚠️  字体注册失败: {e}")

    def _setup_styles(self):
        """设置样式"""
        self.styles = getSampleStyleSheet()

        # 标题1样式
        self.styles.add(ParagraphStyle(
            name='CustomHeading1',
            parent=self.styles['Heading1'],
            fontName=self.chinese_font,
            fontSize=18,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=12,
            spaceBefore=12,
            borderWidth=0,
            borderColor=colors.HexColor('#3498db'),
            borderPadding=5
        ))

        # 标题2样式
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontName=self.chinese_font,
            fontSize=14,
            textColor=colors.HexColor('#34495e'),
            spaceAfter=10,
            spaceBefore=10
        ))

        # 标题3样式
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontName=self.chinese_font,
            fontSize=12,
            textColor=colors.HexColor('#555555'),
            spaceAfter=8,
            spaceBefore=8
        ))

        # 正文样式
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontName=self.chinese_font,
            fontSize=10,
            leading=16,
            textColor=colors.HexColor('#333333')
        ))

        # 代码样式
        self.styles.add(ParagraphStyle(
            name='CustomCode',
            parent=self.styles['Code'],
            fontName='Courier',
            fontSize=9,
            textColor=colors.HexColor('#333333'),
            backColor=colors.HexColor('#f8f8f8'),
            borderWidth=1,
            borderColor=colors.HexColor('#3498db'),
            borderPadding=8,
            leftIndent=10
        ))

    def _get_output_path(self, md_file: str) -> str:
        """获取输出PDF路径"""
        basename = os.path.splitext(os.path.basename(md_file))[0]
        pdf_filename = f"{basename}.pdf"

        if self.output_dir:
            os.makedirs(self.output_dir, exist_ok=True)
            return os.path.join(self.output_dir, pdf_filename)
        else:
            return os.path.join(os.path.dirname(md_file), pdf_filename)

    def _load_image(self, img_src: str) -> str:
        """加载图片（支持URL和本地路径）"""
        try:
            # 如果是HTTP/HTTPS URL
            if img_src.startswith(('http://', 'https://')):
                # 下载到临时文件
                with urllib.request.urlopen(img_src, timeout=10) as response:
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
                    temp_file.write(response.read())
                    temp_file.close()
                    return temp_file.name

            # 如果是本地文件
            elif os.path.isabs(img_src):
                if os.path.exists(img_src):
                    return img_src

            # 尝试相对于markdown文件的路径
            elif self.md_file_dir:
                full_path = os.path.join(self.md_file_dir, img_src)
                if os.path.exists(full_path):
                    return full_path

            return None
        except Exception as e:
            print(f"⚠️  图片加载失败 {img_src}: {e}")
            return None

    def _parse_html_to_elements(self, html_content: str) -> List:
        """将HTML解析为ReportLab元素"""
        soup = BeautifulSoup(html_content, 'html5lib')
        elements = []

        for element in soup.body.children if soup.body else []:
            if element.name == 'h1':
                text = element.get_text()
                elements.append(Paragraph(text, self.styles['CustomHeading1']))
                elements.append(Spacer(1, 0.3*cm))

            elif element.name == 'h2':
                text = element.get_text()
                elements.append(Paragraph(text, self.styles['CustomHeading2']))
                elements.append(Spacer(1, 0.2*cm))

            elif element.name == 'h3':
                text = element.get_text()
                elements.append(Paragraph(text, self.styles['CustomHeading3']))
                elements.append(Spacer(1, 0.2*cm))

            elif element.name == 'p':
                # 检查段落中是否包含图片
                img_tag = element.find('img')
                if img_tag and img_tag.get('src'):
                    img_src = img_tag.get('src')
                    img_path = self._load_image(img_src)

                    if img_path:
                        try:
                            # 创建图片对象
                            img = Image(img_path)

                            # 计算合适的尺寸（最大宽度为页面宽度的80%）
                            max_width = 15*cm  # A4宽度 - 左右边距
                            max_height = 20*cm  # 合理的最大高度

                            # 按比例缩放
                            img_width, img_height = img.imageWidth, img.imageHeight
                            aspect = img_height / float(img_width)

                            if img_width > max_width:
                                img_width = max_width
                                img_height = img_width * aspect

                            if img_height > max_height:
                                img_height = max_height
                                img_width = img_height / aspect

                            img.drawWidth = img_width
                            img.drawHeight = img_height

                            elements.append(img)

                            # 添加图片说明（如果有alt text）
                            alt_text = img_tag.get('alt', '')
                            if alt_text:
                                caption_style = ParagraphStyle(
                                    'ImageCaption',
                                    parent=self.styles['CustomBody'],
                                    fontSize=9,
                                    textColor=colors.HexColor('#666666'),
                                    alignment=TA_CENTER
                                )
                                elements.append(Paragraph(alt_text, caption_style))

                            elements.append(Spacer(1, 0.3*cm))
                        except Exception as e:
                            print(f"⚠️  图片处理失败 {img_src}: {e}")
                            # 如果图片处理失败，显示alt文本
                            alt_text = img_tag.get('alt', f'[图片: {img_src}]')
                            elements.append(Paragraph(alt_text, self.styles['CustomBody']))
                            elements.append(Spacer(1, 0.2*cm))
                else:
                    # 普通段落
                    text = element.get_text()
                    if text.strip():
                        elements.append(Paragraph(text, self.styles['CustomBody']))
                        elements.append(Spacer(1, 0.2*cm))

            elif element.name == 'pre':
                code_text = element.get_text()
                # 使用Preformatted保持代码格式
                elements.append(Preformatted(code_text, self.styles['CustomCode']))
                elements.append(Spacer(1, 0.3*cm))

            elif element.name == 'ul':
                for li in element.find_all('li', recursive=False):
                    text = f"• {li.get_text()}"
                    elements.append(Paragraph(text, self.styles['CustomBody']))
                elements.append(Spacer(1, 0.2*cm))

            elif element.name == 'ol':
                for idx, li in enumerate(element.find_all('li', recursive=False), 1):
                    text = f"{idx}. {li.get_text()}"
                    elements.append(Paragraph(text, self.styles['CustomBody']))
                elements.append(Spacer(1, 0.2*cm))

            elif element.name == 'blockquote':
                text = element.get_text()
                quote_style = ParagraphStyle(
                    'Quote',
                    parent=self.styles['CustomBody'],
                    leftIndent=20,
                    rightIndent=20,
                    textColor=colors.HexColor('#666666'),
                    borderWidth=1,
                    borderColor=colors.HexColor('#3498db'),
                    borderPadding=10
                )
                elements.append(Paragraph(text, quote_style))
                elements.append(Spacer(1, 0.2*cm))

        return elements

    def convert_file(self, md_file: str) -> Dict:
        """转换单个文件"""
        try:
            # 设置markdown文件目录（用于解析相对路径的图片）
            self.md_file_dir = os.path.dirname(os.path.abspath(md_file))

            # 读取Markdown文件
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # 转换为HTML
            html_content = markdown.markdown(
                md_content,
                extensions=[
                    'extra',
                    'codehilite',
                    'tables',
                    'fenced_code',
                    'nl2br'
                ]
            )

            # 输出路径
            output_pdf = self._get_output_path(md_file)

            # 创建PDF
            doc = SimpleDocTemplate(
                output_pdf,
                pagesize=A4,
                leftMargin=2*cm,
                rightMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm
            )

            # 解析HTML为元素
            elements = self._parse_html_to_elements(html_content)

            # 如果没有元素，添加原始内容
            if not elements:
                elements = [Paragraph(md_content, self.styles['CustomBody'])]

            # 构建PDF
            doc.build(elements)

            return {
                'file': os.path.basename(md_file),
                'input': md_file,
                'output': output_pdf,
                'success': True,
                'size': os.path.getsize(output_pdf)
            }

        except Exception as e:
            return {
                'file': os.path.basename(md_file),
                'input': md_file,
                'output': None,
                'success': False,
                'error': str(e)
            }

    def batch_convert(self, input_dir: str, concurrency: int = 4) -> List[Dict]:
        """批量转换"""
        # 获取所有md文件
        md_files = [os.path.join(input_dir, f)
                   for f in os.listdir(input_dir)
                   if f.endswith('.md') and not f.startswith('.')]

        if not md_files:
            print(f"❌ 在目录 {input_dir} 中未找到Markdown文件")
            return []

        print(f"\n📁 输入目录: {input_dir}")
        print(f"📄 找到 {len(md_files)} 个Markdown文件")
        if self.output_dir:
            print(f"📂 输出目录: {self.output_dir}")
        else:
            print(f"📂 输出目录: 与源文件同目录")
        print(f"🔤 使用字体: {self.chinese_font}")
        print(f"⚙️  并发数: {concurrency}")
        print()

        results = []

        # 使用线程池并发转换
        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            future_to_file = {
                executor.submit(self.convert_file, md_file): md_file
                for md_file in md_files
            }

            with tqdm(total=len(md_files), desc="转换进度", unit="file") as pbar:
                for future in as_completed(future_to_file):
                    result = future.result()
                    results.append(result)
                    pbar.update(1)

        return results

    def generate_report(self, results: List[Dict]) -> str:
        """生成报告"""
        report = []
        report.append("\n" + "="*80)
        report.append("📊 PDF转换报告")
        report.append("="*80)

        success = [r for r in results if r['success']]
        failed = [r for r in results if not r['success']]

        report.append(f"\n✅ 成功: {len(success)} 个文件")
        report.append(f"❌ 失败: {len(failed)} 个文件")

        if success:
            total_size = sum(r['size'] for r in success)
            report.append(f"📦 总大小: {total_size / 1024 / 1024:.2f} MB")

        if success and len(success) <= 20:
            report.append("\n✅ 成功转换的文件:")
            for r in success:
                size_kb = r['size'] / 1024
                report.append(f"  • {r['file']} ({size_kb:.1f} KB)")

        if failed:
            report.append("\n❌ 转换失败的文件:")
            for r in failed:
                error_msg = r.get('error', '未知错误')
                report.append(f"  • {r['file']}: {error_msg}")

        if success:
            report.append(f"\n✨ PDF文件已保存到: {self.output_dir if self.output_dir else '源文件目录'}")

        report.append("\n" + "="*80)

        return '\n'.join(report)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='将Markdown文件转换为PDF（支持中文和图片）')
    parser.add_argument('input', help='输入文件或目录')
    parser.add_argument('--output', '-o', help='输出文件或目录（默认与源文件同目录）')
    parser.add_argument('--concurrency', '-c', type=int, default=4,
                       help='并发数（批量转换时使用，默认: 4）')

    args = parser.parse_args()

    # 创建转换器
    converter = SimpleMDtoPDFConverter(output_dir=args.output)

    # 判断输入是文件还是目录
    if os.path.isfile(args.input):
        # 单文件转换
        print(f"📄 转换文件: {args.input}")
        if args.output and not args.output.endswith('.pdf'):
            print(f"⚠️  输出路径将被忽略，使用默认输出路径")
            converter.output_dir = None

        result = converter.convert_file(args.input)

        if result['success']:
            size_kb = result['size'] / 1024
            print(f"✅ 转换成功!")
            print(f"📂 输出文件: {result['output']}")
            print(f"📦 文件大小: {size_kb:.1f} KB")
        else:
            print(f"❌ 转换失败: {result.get('error', '未知错误')}")
            sys.exit(1)

    elif os.path.isdir(args.input):
        # 批量转换
        results = converter.batch_convert(args.input, args.concurrency)

        # 生成并显示报告
        report = converter.generate_report(results)
        print(report)

    else:
        print(f"❌ 错误: 输入路径不存在: {args.input}")
        sys.exit(1)


if __name__ == "__main__":
    main()
