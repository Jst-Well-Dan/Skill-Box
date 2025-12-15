#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
发票识别脚本 - 使用 GLM-4.1V-Thinking-Flash 模型
支持批量处理发票图片和PDF文件，提取结构化信息并保存为 JSON
PDF文件会自动转换为图片后进行识别
"""

import os
import json
import base64
import asyncio
import aiohttp
import tempfile
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime

# 获取 .env 文件路径（脚本上级目录）
SCRIPT_DIR = Path(__file__).resolve().parent
ENV_FILE = SCRIPT_DIR.parent / '.env'


def load_env_file() -> Dict[str, str]:
    """从 .env 文件加载环境变量"""
    if not ENV_FILE.exists():
        return {}

    env_vars = {}
    with open(ENV_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()
    return env_vars

try:
    import fitz  # PyMuPDF
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False
    print("警告: 未安装 PyMuPDF，PDF 支持已禁用。安装命令: pip install PyMuPDF")


class InvoiceOCR:
    """发票OCR识别类"""

    # API配置
    API_ENDPOINT = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    MODEL_NAME = "glm-4.1v-thinking-flash"
    MAX_CONCURRENT = 5  # 最大并发数

    def __init__(self, api_key: str):
        """
        初始化发票OCR识别器

        Args:
            api_key: 智谱AI API密钥
        """
        self.api_key = api_key
        self.semaphore = asyncio.Semaphore(self.MAX_CONCURRENT)

    @staticmethod
    def encode_image_to_base64(image_path: str) -> Optional[str]:
        """
        将图片编码为base64字符串

        Args:
            image_path: 图片文件路径

        Returns:
            base64编码的图片字符串，失败返回None
        """
        try:
            with open(image_path, 'rb') as f:
                image_data = f.read()
                # 检查文件大小（5MB限制）
                if len(image_data) > 5 * 1024 * 1024:
                    print(f"警告: 图片 {image_path} 超过5MB限制")
                    return None
                return base64.b64encode(image_data).decode('utf-8')
        except Exception as e:
            print(f"读取图片失败 {image_path}: {e}")
            return None

    @staticmethod
    def convert_pdf_to_images(pdf_path: str, dpi: int = 200) -> List[Tuple[str, str]]:
        """
        将PDF文件转换为图片

        Args:
            pdf_path: PDF文件路径
            dpi: 图片分辨率，默认200

        Returns:
            图片路径列表 [(临时文件路径, 原始文件名_页码), ...]
        """
        if not PDF_SUPPORT:
            print(f"错误: PDF支持未启用，无法处理 {pdf_path}")
            return []

        images = []
        try:
            pdf_document = fitz.open(pdf_path)
            pdf_name = Path(pdf_path).stem

            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]

                # 将DPI转换为缩放因子
                zoom = dpi / 72  # 72是PDF的默认DPI
                mat = fitz.Matrix(zoom, zoom)

                # 渲染页面为图片
                pix = page.get_pixmap(matrix=mat)

                # 创建临时文件保存图片
                temp_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix='.png',
                    prefix=f'{pdf_name}_page{page_num + 1}_'
                )
                temp_path = temp_file.name
                temp_file.close()

                # 保存图片
                pix.save(temp_path)

                # 记录原始文件名和页码
                original_name = f"{pdf_name}_第{page_num + 1}页"
                images.append((temp_path, original_name))

                print(f"  转换 PDF 第 {page_num + 1}/{len(pdf_document)} 页")

            pdf_document.close()
            print(f"PDF转换完成: {pdf_path} ({len(images)} 页)")

        except Exception as e:
            print(f"PDF转换失败 {pdf_path}: {e}")

        return images

    def build_prompt(self) -> str:
        """
        构建发票识别的提示词

        Returns:
            提示词字符串
        """
        return """请识别这张发票图片，提取以下信息并以JSON格式返回：

1. 发票类型 (invoice_type)
2. 发票号码 (invoice_number)
3. 开票日期 (invoice_date)
4. 购买方名称 (buyer_name)
5. 销售方名称 (seller_name)
6. 合计金额/不含税 (total_amount_excluding_tax)
7. 合计税额 (total_tax)
8. 价税合计 (total_amount_including_tax)
9. 项目名称 (item_names) - 如果有多个项目，用数组表示

请只返回JSON格式的数据，格式如下：
{
    "invoice_type": "增值税专用发票",
    "invoice_number": "12345678",
    "invoice_date": "2024-01-01",
    "buyer_name": "公司A",
    "seller_name": "公司B",
    "total_amount_excluding_tax": "1000.00",
    "total_tax": "130.00",
    "total_amount_including_tax": "1130.00",
    "item_names": ["商品1", "商品2"]
}

如果某些信息无法识别，请用null表示。"""

    async def recognize_invoice(
        self,
        session: aiohttp.ClientSession,
        image_path: str
    ) -> Dict:
        """
        异步识别单张发票

        Args:
            session: aiohttp会话
            image_path: 图片路径

        Returns:
            识别结果字典
        """
        async with self.semaphore:
            print(f"开始处理: {image_path}")

            # 编码图片
            base64_image = self.encode_image_to_base64(image_path)
            if not base64_image:
                return {
                    "file_path": image_path,
                    "status": "error",
                    "error": "图片编码失败或文件过大"
                }

            # 获取图片扩展名
            ext = Path(image_path).suffix.lower().replace('.', '')
            mime_type = f"image/{ext if ext != 'jpg' else 'jpeg'}"

            # 构建请求
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": self.MODEL_NAME,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": self.build_prompt()
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "temperature": 0.1  # 降低温度以获得更稳定的输出
            }

            try:
                async with session.post(
                    self.API_ENDPOINT,
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        print(f"API错误 {image_path}: {response.status} - {error_text}")
                        return {
                            "file_path": image_path,
                            "status": "error",
                            "error": f"API返回错误: {response.status}"
                        }

                    result = await response.json()

                    # 提取识别结果
                    content = result.get('choices', [{}])[0].get('message', {}).get('content', '')

                    # 尝试解析JSON结果
                    try:
                        # 提取JSON部分（可能包含在```json```代码块中）
                        if '```json' in content:
                            json_start = content.find('```json') + 7
                            json_end = content.find('```', json_start)
                            json_str = content[json_start:json_end].strip()
                        elif '```' in content:
                            json_start = content.find('```') + 3
                            json_end = content.find('```', json_start)
                            json_str = content[json_start:json_end].strip()
                        else:
                            # 尝试找到JSON对象的开始和结束
                            json_start = content.find('{')
                            json_end = content.rfind('}') + 1
                            json_str = content[json_start:json_end].strip()

                        invoice_data = json.loads(json_str)

                        print(f"完成处理: {image_path}")
                        return {
                            "file_path": image_path,
                            "status": "success",
                            "data": invoice_data,
                            "raw_response": content
                        }
                    except json.JSONDecodeError as e:
                        print(f"JSON解析失败 {image_path}: {e}")
                        return {
                            "file_path": image_path,
                            "status": "error",
                            "error": "JSON解析失败",
                            "raw_response": content
                        }

            except asyncio.TimeoutError:
                print(f"请求超时: {image_path}")
                return {
                    "file_path": image_path,
                    "status": "error",
                    "error": "请求超时"
                }
            except Exception as e:
                print(f"处理异常 {image_path}: {e}")
                return {
                    "file_path": image_path,
                    "status": "error",
                    "error": str(e)
                }

    async def process_batch(self, image_paths: List[str]) -> List[Dict]:
        """
        批量处理发票图片

        Args:
            image_paths: 图片路径列表

        Returns:
            识别结果列表
        """
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.recognize_invoice(session, image_path)
                for image_path in image_paths
            ]
            return await asyncio.gather(*tasks)

    def save_results(self, results: List[Dict], output_path: str):
        """
        保存识别结果为JSON文件

        Args:
            results: 识别结果列表
            output_path: 输出文件路径
        """
        output_data = {
            "timestamp": datetime.now().isoformat(),
            "total_count": len(results),
            "success_count": sum(1 for r in results if r.get('status') == 'success'),
            "error_count": sum(1 for r in results if r.get('status') == 'error'),
            "results": results
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\n结果已保存到: {output_path}")


def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Invoice OCR processor using GLM-4.1V vision model')
    parser.add_argument('-i', '--input', default='invoices',
                        help='Input path (directory or file, default: invoices)')
    parser.add_argument('-o', '--output', default='invoice_results.json',
                        help='Output JSON file (default: invoice_results.json)')
    args = parser.parse_args()

    # 从 .env 文件加载配置
    env_vars = load_env_file()
    API_KEY = env_vars.get('GLM_API_KEY')
    INPUT_PATH = args.input
    OUTPUT_JSON = args.output

    # 检查API密钥
    if not API_KEY:
        print(f"错误: 请在 .env 文件中设置 GLM_API_KEY")
        print(f".env 文件路径: {ENV_FILE}")
        print("格式: GLM_API_KEY=your-actual-api-key")
        return

    # 收集文件
    image_paths = []
    pdf_files = []
    image_formats = {'.jpg', '.jpeg', '.png'}
    supported_formats = image_formats | {'.pdf'} if PDF_SUPPORT else image_formats

    if os.path.isfile(INPUT_PATH):
        ext = Path(INPUT_PATH).suffix.lower()
        if ext in image_formats:
            image_paths.append(INPUT_PATH)
        elif ext == '.pdf' and PDF_SUPPORT:
            pdf_files.append(INPUT_PATH)
    elif os.path.isdir(INPUT_PATH):
        for root, _, files in os.walk(INPUT_PATH):
            for file in files:
                file_path = os.path.join(root, file)
                ext = Path(file).suffix.lower()
                if ext in image_formats:
                    image_paths.append(file_path)
                elif ext == '.pdf' and PDF_SUPPORT:
                    pdf_files.append(file_path)
    else:
        print(f"错误: 路径不存在: {INPUT_PATH}")
        return

    if not image_paths and not pdf_files:
        print(f"未找到支持的文件 (支持格式: {', '.join(supported_formats)})")
        return

    print(f"找到 {len(image_paths)} 张图片文件, {len(pdf_files)} 个PDF文件")

    # 处理PDF文件，转换为图片
    temp_files = []  # 记录临时文件以便后续清理
    pdf_file_mapping = {}  # 映射临时图片路径到原始PDF信息

    if pdf_files:
        print("-" * 50)
        print("正在转换PDF文件...")
        for pdf_path in pdf_files:
            print(f"处理PDF: {pdf_path}")
            converted_images = InvoiceOCR.convert_pdf_to_images(pdf_path)
            for temp_path, original_name in converted_images:
                image_paths.append(temp_path)
                temp_files.append(temp_path)
                pdf_file_mapping[temp_path] = {
                    'original_pdf': pdf_path,
                    'page_name': original_name
                }

    if not image_paths:
        print("没有可处理的图片")
        return

    print("-" * 50)
    print(f"共 {len(image_paths)} 张图片待处理")
    print(f"最大并发数: {InvoiceOCR.MAX_CONCURRENT}")
    print("-" * 50)

    # 创建OCR识别器
    ocr = InvoiceOCR(api_key=API_KEY)

    # 批量处理
    results = asyncio.run(ocr.process_batch(image_paths))

    # 更新结果中的文件路径信息（将临时文件路径替换为原始PDF信息）
    for result in results:
        file_path = result.get('file_path')
        if file_path in pdf_file_mapping:
            pdf_info = pdf_file_mapping[file_path]
            result['original_file'] = pdf_info['original_pdf']
            result['page_info'] = pdf_info['page_name']
            result['file_path'] = f"{pdf_info['original_pdf']} - {pdf_info['page_name']}"

    # 清理临时文件
    if temp_files:
        print("-" * 50)
        print("清理临时文件...")
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception as e:
                print(f"清理临时文件失败 {temp_file}: {e}")

    # 保存结果
    ocr.save_results(results, OUTPUT_JSON)

    # 打印统计信息
    success_count = sum(1 for r in results if r.get('status') == 'success')
    error_count = sum(1 for r in results if r.get('status') == 'error')

    print("-" * 50)
    print(f"处理完成!")
    print(f"成功: {success_count} / 失败: {error_count} / 总计: {len(results)}")

    # 显示成功识别的发票信息摘要
    if success_count > 0:
        print("\n识别成功的发票摘要:")
        for result in results:
            if result.get('status') == 'success':
                data = result.get('data', {})
                print(f"  - {Path(result['file_path']).name}")
                print(f"    类型: {data.get('invoice_type', 'N/A')}")
                print(f"    号码: {data.get('invoice_number', 'N/A')}")
                print(f"    金额: {data.get('total_amount_including_tax', 'N/A')}")


if __name__ == '__main__':
    main()
