<!--
本文件由智谱 AI 自动翻译生成
原文件: reference.md
翻译时间: 2025-12-12 16:14:29
翻译模型: glm-4-flash
原文大小: 16,692 字符
-->

# PDF 处理高级参考

本文档包含高级 PDF 处理功能、详细示例和主技能说明中未涵盖的附加库。

## pypdfium2 库（Apache/BSD 许可证）

### 概述
pypdfium2 是 PDFium（Chromium 的 PDF 库）的 Python 绑定。它非常适合快速 PDF 渲染、图像生成，并可作为 PyMuPDF 的替代品。

### 将 PDF 渲染为图像
```python
import pypdfium2 as pdfium
from PIL import Image

# 加载 PDF
pdf = pdfium.PdfDocument("document.pdf")

# 将页面渲染为图像
page = pdf[0]  # 第一页
bitmap = page.render(
    scale=2.0,  # 更高分辨率
    rotation=0  # 无旋转
)

# 转换为 PIL 图像
img = bitmap.to_pil()
img.save("page_1.png", "PNG")

# 处理多页
for i, page in enumerate(pdf):
    bitmap = page.render(scale=1.5)
    img = bitmap.to_pil()
    img.save(f"page_{i+1}.jpg", "JPEG", quality=90)
```

### 使用 pypdfium2 提取文本
```python
import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("document.pdf")
for i, page in enumerate(pdf):
    text = page.get_text()
    print(f"第 {i+1} 页文本长度：{len(text)} 个字符")
```

## JavaScript 库

### pdf-lib（MIT 许可证）

pdf-lib 是一个强大的 JavaScript 库，用于在任何 JavaScript 环境中创建和修改 PDF 文档。

#### 加载和操作现有 PDF
```javascript
import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

async function manipulatePDF() {
    // 加载现有 PDF
    const existingPdfBytes = fs.readFileSync('input.pdf');
    const pdfDoc = await PDFDocument.load(existingPdfBytes);

    // 获取页面数量
    const pageCount = pdfDoc.getPageCount();
    console.log(`文档有 ${pageCount} 页`);

    // 添加新页面
    const newPage = pdfDoc.addPage([600, 400]);
    newPage.drawText('由 pdf-lib 添加', {
        x: 100,
        y: 300,
        size: 16
    });

    // 保存修改后的 PDF
    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync('modified.pdf', pdfBytes);
}
```

#### 从头创建复杂 PDF
```javascript
import { PDFDocument, rgb, StandardFonts } from 'pdf-lib';
import fs from 'fs';

async function createPDF() {
    const pdfDoc = await PDFDocument.create();

    // 添加字体
    const helveticaFont = await pdfDoc.embedFont(StandardFonts.Helvetica);
    const helveticaBold = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

    // 添加页面
    const page = pdfDoc.addPage([595, 842]); // A4 尺寸
    const { width, height } = page.getSize();

    // 添加带样式的文本
    page.drawText('发票 #12345', {
        x: 50,
        y: height - 50,
        size: 18,
        font: helveticaBold,
        color: rgb(0.2, 0.2, 0.8)
    });

    // 添加矩形（页眉背景）
    page.drawRectangle({
        x: 40,
        y: height - 100,
        width: width - 80,
        height: 30,
        color: rgb(0.9, 0.9, 0.9)
    });

    // 添加类似表格的内容
    const items = [
        ['项目', '数量', '价格', '总计'],
        ['小部件', '2', '$50', '$100'],
        ['小玩意', '1', '$75', '$75']
    ];

    let yPos = height - 150;
    items.forEach(row => {
        let xPos = 50;
        row.forEach(cell => {
            page.drawText(cell, {
                x: xPos,
                y: yPos,
                size: 12,
                font: helveticaFont
            });
            xPos += 120;
        });
        yPos -= 25;
    });

    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync('created.pdf', pdfBytes);
}
```

#### 高级合并和拆分操作
```javascript
import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

async function mergePDFs() {
    // 创建新文档
    const mergedPdf = await PDFDocument.create();

    // 加载源 PDF
    const pdf1Bytes = fs.readFileSync('doc1.pdf');
    const pdf2Bytes = fs.readFileSync('doc2.pdf');

    const pdf1 = await PDFDocument.load(pdf1Bytes);
    const pdf2 = await PDFDocument.load(pdf2Bytes);

    // 从第一个 PDF 复制页面
    const pdf1Pages = await mergedPdf.copyPages(pdf1, pdf1.getPageIndices());
    pdf1Pages.forEach(page => mergedPdf.addPage(page));

    // 从第二个 PDF 复制特定页面（页面 0、2、4）
    const pdf2Pages = await mergedPdf.copyPages(pdf2, [0, 2, 4]);
    pdf2Pages.forEach(page => mergedPdf.addPage(page));

    const mergedPdfBytes = await mergedPdf.save();
    fs.writeFileSync('merged.pdf', mergedPdfBytes);
}
```

### pdfjs-dist（Apache 许可证）

PDF.js 是 Mozilla 的 JavaScript 库，用于在浏览器中渲染 PDF。

#### 基本 PDF 加载和渲染
```javascript
import * as pdfjsLib from 'pdfjs-dist';

// 配置 worker（对性能很重要）
pdfjsLib.GlobalWorkerOptions.workerSrc = './pdf.worker.js';

async function renderPDF() {
    // 加载 PDF
    const loadingTask = pdfjsLib.getDocument('document.pdf');
    const pdf = await loadingTask.promise;

    console.log(`已加载包含 ${pdf.numPages} 页的 PDF`);

    // 获取第一页
    const page = await pdf.getPage(1);
    const viewport = page.getViewport({ scale: 1.5 });

    // 渲染到 canvas
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    const renderContext = {
        canvasContext: context,
        viewport: viewport
    };

    await page.render(renderContext).promise;
    document.body.appendChild(canvas);
}
```

#### 使用坐标提取文本
```javascript
import * as pdfjsLib from 'pdfjs-dist';

async function extractText() {
    const loadingTask = pdfjsLib.getDocument('document.pdf');
    const pdf = await loadingTask.promise;

    let fullText = '';

    // 从所有页面提取文本
    for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const textContent = await page.getTextContent();

        const pageText = textContent.items
            .map(item => item.str)
            .join(' ');

        fullText += `\n--- 第 ${i} 页 ---\n${pageText}`;

        // 获取具有坐标的文本（用于高级处理）
        const textWithCoords = textContent.items.map(item => ({
            text: item.str,
            x: item.transform[4],
            y: item.transform[5],
            width: item.width,
            height: item.height
        }));
    }

    console.log(fullText);
    return fullText;
}
```

#### 提取注释和表单
```javascript
import * as pdfjsLib from 'pdfjs-dist';

async function extractAnnotations() {
    const loadingTask = pdfjsLib.getDocument('annotated.pdf');
    const pdf = await loadingTask.promise;

    for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const annotations = await page.getAnnotations();

        annotations.forEach(annotation => {
            console.log(`注释类型：${annotation.subtype}`);
            console.log(`内容：${annotation.contents}`);
            console.log(`坐标：${JSON.stringify(annotation.rect)}`);
        });
    }
}
```

## 高级命令行操作

### poppler-utils 高级功能

#### 使用边界框坐标提取文本
```bash
# 使用边界框坐标提取文本（对于结构化数据至关重要）
pdftotext -bbox-layout document.pdf output.xml

# XML 输出包含每个文本元素的精确坐标
```

#### 高级图像转换
```bash
# 转换为具有特定分辨率的 PNG 图像
pdftoppm -png -r 300 document.pdf output_prefix

# 转换特定页面范围（高分辨率）
pdftoppm -png -r 600 -f 1 -l 3 document.pdf high_res_pages

# 转换为 JPEG 并设置质量
pdftoppm -jpeg -jpegopt quality=85 -r 200 document.pdf jpeg_output
```

#### 提取嵌入式图像
```bash
# 提取所有嵌入式图像及其元数据
pdfimages -j -p document.pdf page_images

# 列出图像信息（不提取）
pdfimages -list document.pdf

# 以原始格式提取图像
pdfimages -all document.pdf images/img
```

### qpdf 高级功能

#### 复杂页面操作
```bash
# 将 PDF 分割成页面组
qpdf --split-pages=3 input.pdf output_group_%02d.pdf

# 使用复杂范围提取特定页面
qpdf input.pdf --pages input.pdf 1,3-5,8,10-end -- extracted.pdf

# 从多个 PDF 中合并特定页面
qpdf --empty --pages doc1.pdf 1-3 doc2.pdf 5-7 doc3.pdf 2,4 -- combined.pdf
```

#### PDF 优化和修复
```bash
# 为网络优化 PDF（线性化以进行流式传输）
qpdf --linearize input.pdf optimized.pdf

# 删除未使用的对象并压缩
qpdf --optimize-level=all input.pdf compressed.pdf

# 尝试修复损坏的 PDF 结构
qpdf --check input.pdf
qpdf --fix-qdf damaged.pdf repaired.pdf

# 显示详细的 PDF 结构以进行调试
qpdf --show-all-pages input.pdf > structure.txt
```

#### 高级加密
```bash
# 使用特定权限添加密码保护
qpdf --encrypt user_pass owner_pass 256 --print=none --modify=none -- input.pdf encrypted.pdf

# 检查加密状态
qpdf --show-encryption encrypted.pdf

# 移除密码保护（需要密码）
qpdf --password=secret123 --decrypt encrypted.pdf decrypted.pdf
```

## 高级 Python 技巧

### pdfplumber 高级功能

#### 使用精确坐标提取文本
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    page = pdf.pages[0]
    
    # 提取所有文本及其坐标
    chars = page.chars
    for char in chars[:10]:  # 前十个字符
        print(f"字符：'{char['text']}' 在 x:{char['x0']:.1f} y:{char['y0']:.1f}")
    
    # 通过边界框（左，上，右，下）提取文本
    bbox_text = page.within_bbox((100, 100, 400, 200)).extract_text()
```

#### 使用自定义设置提取复杂表格
```python
import pdfplumber
import pandas as pd

with pdfplumber.open("complex_table.pdf") as pdf:
    page = pdf.pages[0]
    
    # 使用自定义设置提取复杂布局的表格
    table_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
        "snap_tolerance": 3,
        "intersection_tolerance": 15
    }
    tables = page.extract_tables(table_settings)
    
    # 表格提取的视觉调试
    img = page.to_image(resolution=150)
    img.save("debug_layout.png")
```

### reportlab 高级功能

#### 使用表格创建专业报告
```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# 示例数据
data = [
    ['产品', 'Q1', 'Q2', 'Q3', 'Q4'],
    ['小部件', '120', '135', '142', '158'],
    ['小玩意', '85', '92', '98', '105']
]

# 创建 PDF 并添加表格
doc = SimpleDocTemplate("report.pdf")
elements = []

# 添加标题
styles = getSampleStyleSheet()
title = Paragraph("季度销售报告", styles['Title'])
elements.append(title)

# 添加具有高级样式的表格
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
elements.append(table)

doc.build(elements)
```

## 复杂工作流程

### 从 PDF 中提取图像/图像

#### 方法 1：使用 pdfimages（最快）
```bash
# 提取所有图像及其原始质量
pdfimages -all document.pdf images/img
```

#### 方法 2：使用 pypdfium2 + 图像处理
```python
import pypdfium2 as pdfium
from PIL import Image
import numpy as np

def extract_figures(pdf_path, output_dir):
    pdf = pdfium.PdfDocument(pdf_path)
    
    for page_num, page in enumerate(pdf):
        # 渲染高分辨率页面
        bitmap = page.render(scale=3.0)
        img = bitmap.to_pil()
        
        # 转换为 numpy 以进行处理
        img_array = np.array(img)
        
        # 简单图像检测（非白色区域）
        mask = np.any(img_array != [255, 255, 255], axis=2)
        
        # 找到轮廓并提取边界框
        #（这是简化的 - 真实实现需要更复杂的检测）
        
        # 保存检测到的图像
        # ... 实现取决于特定需求
```

### 具有错误处理的批量 PDF 处理
```python
import os
import glob
from pypdf import PdfReader, PdfWriter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def batch_process_pdfs(input_dir, operation='merge'):
    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))
    
    if operation == 'merge':
        writer = PdfWriter()
        for pdf_file in pdf_files:
            try:
                reader = PdfReader(pdf_file)
                for page in reader.pages:
                    writer.add_page(page)
                logger.info(f"已处理：{pdf_file}")
            except Exception as e:
                logger.error(f"无法处理 {pdf_file}：{e}")
                continue
        
        with open("batch_merged.pdf", "wb") as output:
            writer.write(output)
    
    elif operation == 'extract_text':
        for pdf_file in pdf_files:
            try:
                reader = PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                output_file = pdf_file.replace('.pdf', '.txt')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                logger.info(f"从：{pdf_file} 提取文本")
                
            except Exception as e:
                logger.error(f"无法从 {pdf_file} 提取文本：{e}")
                continue
```

### 高级 PDF 裁剪
```python
from pypdf import PdfWriter, PdfReader

reader = PdfReader("input.pdf")
writer = PdfWriter()

# 裁剪页面（左，下，右，上以点为单位）
page = reader.pages[0]
page.mediabox.left = 50
page.mediabox.bottom = 50
page.mediabox.right = 550
page.mediabox.top = 750

writer.add_page(page)
with open("cropped.pdf", "wb") as output:
    writer.write(output)
```

## 性能优化技巧

### 1. 对于大型 PDF
- 使用流式方法而不是将整个 PDF 加载到内存中
- 使用 `qpdf --split-pages` 分割大文件
- 使用 pypdfium2 逐页处理

### 2. 对于文本提取
- `pdftotext -bbox-layout` 对于纯文本提取最快
- 使用 pdfplumber 对于结构化数据和表格
- 避免在非常大的文档中使用 `pypdf.extract_text()`

### 3. 对于图像提取
- `pdfimages` 比渲染页面快得多
- 使用低分辨率进行预览，高分辨率用于最终输出

### 4. 对于表单填写
- pdf-lib 在维护表单结构方面优于大多数替代方案
- 在处理之前先验证表单字段

### 5. 内存管理
```python
# 分块处理 PDF
def process_large_pdf(pdf_path, chunk_size=10):
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    
    for start_idx in range(0, total_pages, chunk_size):
        end_idx = min(start_idx + chunk_size, total_pages)
        writer = PdfWriter()
        
        for i in range(start_idx, end_idx):
            writer.add_page(reader.pages[i])
        
        # 处理块
        with open(f"chunk_{start_idx//chunk_size}.pdf", "wb") as output:
            writer.write(output)
```

## 常见问题故障排除

### 加密 PDF
```python
#