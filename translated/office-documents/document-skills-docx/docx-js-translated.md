<!--
本文件由智谱 AI 自动翻译生成
原文件: docx-js.md
翻译时间: 2025-12-12 16:13:53
翻译模型: glm-4-flash
原文大小: 16,449 字符
-->

---

# DOCX 库教程

使用 JavaScript/TypeScript 生成 .docx 文件。

**重要提示：在开始之前，请阅读本文档的全文。** 文档中涵盖了关键的格式规则和常见错误，跳过部分可能导致文件损坏或渲染问题。

## 设置
假设 docx 已经全局安装
如果没有安装：`npm install -g docx`

```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun, Media, 
        Header, Footer, AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink, 
        InternalHyperlink, TableOfContents, HeadingLevel, BorderStyle, WidthType, TabStopType, 
        TabStopPosition, UnderlineType, ShadingType, VerticalAlign, SymbolRun, PageNumber,
        FootnoteReferenceRun, Footnote, PageBreak } = require('docx');

// 创建 & 保存
const doc = new Document({ sections: [{ children: [/* 内容 */] }] });
Packer.toBuffer(doc).then(buffer => fs.writeFileSync("doc.docx", buffer)); // Node.js
Packer.toBlob(doc).then(blob => { /* 下载逻辑 */ }); // 浏览器
```

## 文本与格式化
```javascript
// 重要提示：永远不要使用 \n 进行换行 - 总是使用单独的 Paragraph 元素
// ❌ 错误：new TextRun("行 1\n行 2")
// ✅ 正确：new Paragraph({ children: [new TextRun("行 1")] }), new Paragraph({ children: [new TextRun("行 2")] })

// 基本文本与所有格式选项
new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 200, after: 200 },
  indent: { left: 720, right: 720 },
  children: [
    new TextRun({ text: "粗体", bold: true }),
    new TextRun({ text: "斜体", italics: true }),
    new TextRun({ text: "下划线", underline: { type: UnderlineType.DOUBLE, color: "FF0000" } }),
    new TextRun({ text: "彩色", color: "FF0000", size: 28, font: "Arial" }), // Arial 默认
    new TextRun({ text: "高亮", highlight: "yellow" }),
    new TextRun({ text: "删除线", strike: true }),
    new TextRun({ text: "x2", superScript: true }),
    new TextRun({ text: "H2O", subScript: true }),
    new TextRun({ text: "小写字母", smallCaps: true }),
    new SymbolRun({ char: "2022", font: "Symbol" }), // 项目符号 •
    new SymbolRun({ char: "00A9", font: "Arial" })   // 版权 © - Arial 用于符号
  ]
})
```

## 样式与专业格式化

```javascript
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 24 } } }, // 12pt 默认
    paragraphStyles: [
      // 文档标题样式 - 覆盖内置标题样式
      { id: "Title", name: "Title", basedOn: "Normal",
        run: { size: 56, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, alignment: AlignmentType.CENTER } },
      // 重要提示：通过使用它们的精确 ID 覆盖内置标题样式
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, color: "000000", font: "Arial" }, // 16pt
        paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } }, // 必须用于 TOC
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, color: "000000", font: "Arial" }, // 14pt
        paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1 } },
      // 自定义样式使用您自己的 ID
      { id: "myStyle", name: "My Style", basedOn: "Normal",
        run: { size: 28, bold: true, color: "000000" },
        paragraph: { spacing: { after: 120 }, alignment: AlignmentType.CENTER } }
    ],
    characterStyles: [{ id: "myCharStyle", name: "My Char Style",
      run: { color: "FF0000", bold: true, underline: { type: UnderlineType.SINGLE } } }]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [
      new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun("文档标题")] }), // 使用覆盖的标题样式
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("标题 1")] }), // 使用覆盖的标题 1 样式
      new Paragraph({ style: "myStyle", children: [new TextRun("自定义段落样式")] }),
      new Paragraph({ children: [
        new TextRun("普通文本"),
        new TextRun({ text: "自定义字符样式", style: "myCharStyle" })
      ]})
    ]
  }]
});
```

**专业字体组合：**
- **Arial (标题) + Arial (正文)** - 最广泛支持的，干净且专业
- **Times New Roman (标题) + Arial (正文)** - 经典衬线标题与现代无衬线正文
- **Georgia (标题) + Verdana (正文)** - 优化于屏幕阅读，优雅的对比

**关键样式原则：**
- **覆盖内置样式**：使用精确的 ID，如 "Heading1"、"Heading2"、"Heading3" 来覆盖 Word 的内置标题样式
- **HeadingLevel 常量**：`HeadingLevel.HEADING_1` 使用 "Heading1" 样式，`HeadingLevel.HEADING_2` 使用 "Heading2" 样式，等等
- **包含 outlineLevel**：将 `outlineLevel: 0` 设置为 H1，`outlineLevel: 1` 设置为 H2，等等，以确保 TOC 正确工作
- **使用自定义样式**而不是内联格式以保持一致性
- **使用 `styles.default.document.run.font` 设置默认字体** - Arial 是广泛支持的
- **使用不同的字体大小**来建立视觉层次（标题 > 标题 > 正文）
- **使用适当的间距**使用 `before` 和 `after` 段落间距
- **谨慎使用颜色**：默认使用黑色（000000）和灰色阴影用于标题和副标题（标题 1、标题 2 等）
- **设置一致的页边距**（1440 = 1 英寸）

## 列表（始终使用正确的列表 - 永远不要使用 Unicode 项目符号）
```javascript
// 项目符号 - 总是使用编号配置，而不是 Unicode 符号
// 重要提示：使用 LevelFormat.BULLET 常量，而不是字符串 "bullet"
const doc = new Document({
  numbering: {
    config: [
      { reference: "bullet-list",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "first-numbered-list",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "second-numbered-list", // 不同的引用 = 重新开始计数
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }
    ]
  },
  sections: [{
    children: [
      // 项目符号列表项
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("第一个项目符号")] }),
      new Paragraph({ numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("第二个项目符号")] }),
      // 编号列表项
      new Paragraph({ numbering: { reference: "first-numbered-list", level: 0 },
        children: [new TextRun("第一个编号项")] }),
      new Paragraph({ numbering: { reference: "first-numbered-list", level: 0 },
        children: [new TextRun("第二个编号项")] }),
      // ⚠️ 重要提示：不同的引用 = 独立的列表，重新开始计数
      // 相同的引用 = 继续编号（1, 2, 3... 然后是 4, 5, 6...）
      new Paragraph({ numbering: { reference: "second-numbered-list", level: 0 },
        children: [new TextRun("再次从 1 开始（因为不同的引用）")] })
    ]
  }]
});

// ⚠️ 重要编号规则：每个引用创建一个独立的编号列表
// - 相同的引用 = 继续编号（1, 2, 3... 然后是 4, 5, 6...）
// - 不同的引用 = 从 1 重新开始计数（1, 2, 3... 然后是 1, 2, 3...）
为每个单独的编号部分使用唯一的引用名称！

// ⚠️ 重要提示：永远不要使用 Unicode 项目符号 - 它们创建的列表无法正常工作
// new TextRun("• 项目")           // 错误
// new SymbolRun({ char: "2022" }) // 错误
// ✅ 总是使用带有 LevelFormat.BULLET 的编号配置来创建真正的 Word 列表
```

## 表格
```javascript
// 完整的表格，包括边距、边框、标题和项目符号
const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

new Table({
  columnWidths: [4680, 4680], // ⚠️ 重要提示：在表格级别设置列宽 - 值在 DXA（二十分之一点）
  margins: { top: 100, bottom: 100, left: 180, right: 180 }, // 一次性设置所有单元格
  rows: [
    new TableRow({
      tableHeader: true,
      children: [
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA }, // 也设置每个单元格的宽度
          // ⚠️ 重要提示：始终使用 ShadingType.CLEAR 以防止 Word 中的黑色背景。
          shading: { fill: "D5E8F0", type: ShadingType.CLEAR }, 
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ 
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: "标题", bold: true, size: 22 })]
          })]
        }),
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA }, // 也设置每个单元格的宽度
          shading: { fill: "D5E8F0", type: ShadingType.CLEAR },
          children: [new Paragraph({ 
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: "项目符号", bold: true, size: 22 })]
          })]
        })
      ]
    }),
    new TableRow({
      children: [
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA }, // 也设置每个单元格的宽度
          children: [new Paragraph({ children: [new TextRun("常规数据")] })]
        }),
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA }, // 也设置每个单元格的宽度
          children: [
            new Paragraph({ 
              numbering: { reference: "bullet-list", level: 0 },
              children: [new TextRun("第一个项目符号")] 
            }),
            new Paragraph({ 
              numbering: { reference: "bullet-list", level: 0 },
              children: [new TextRun("第二个项目符号")] 
            })
          ]
        })
      ]
    })
  ]
})
```

**重要提示：表格宽度与边框**
- 使用 `columnWidths: [width1, width2, ...]` 数组以及每个单元格上的 `width: { size: X, type: WidthType.DXA }`
- DXA（二十分之一点）的值：1440 = 1 英寸，信纸可用宽度 = 9360 DXA（带有 1 英寸边距）
- 将边框应用于单个 `TableCell` 元素，而不是 `Table` 本身

**预计算列宽（信纸大小，带有 1 英寸边距 = 9360 DXA 总计）：**
- **2 列：** `columnWidths: [4680, 4680]`（等宽）
- **3 列：** `columnWidths: [3120, 3120, 3120]`（等宽）

## 链接与导航
```javascript
// 目录（需要标题） - 重要提示：仅使用 HeadingLevel，而不是自定义样式
// ❌ 错误：new Paragraph({ heading: HeadingLevel.HEADING_1, style: "customHeader", children: [new TextRun("标题")] })
// ✅ 正确：new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("标题")] })
new TableOfContents("目录", { hyperlink: true, headingStyleRange: "1-3" }),

// 外部链接
new Paragraph({
  children: [new ExternalHyperlink({
    children: [new TextRun({ text: "Google", style: "Hyperlink" })],
    link: "https://www.google.com"
  })]
}),

// 内部链接与书签
new Paragraph({
  children: [new InternalHyperlink({
    children: [new TextRun({ text: "转到部分", style: "Hyperlink" })],
    anchor: "section1"
  })]
}),
new Paragraph({
  children: [new TextRun("部分内容")],
  bookmark: { id: "section1", name: "section1" }
}),
```

## 图片与媒体
```javascript
// 基本图片，包括大小与位置
// 重要提示：始终指定 'type' 参数 - 它是必需的，用于 ImageRun
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new ImageRun({
    type: "png", // 新要求：必须指定图像类型（png、jpg、jpeg、gif、bmp、svg）
    data: fs.readFileSync("image.png"),
    transformation: { width: 200, height: 150, rotation: 0 }, // 旋转角度
    altText: { title: "Logo", description: "公司标志", name: "Name" } // 重要提示：所有三个字段都是必需的
  })]
})
```

## 分页符
```javascript
// 手动分页符
new Paragraph({ children: [new PageBreak()] }),

// 在段落之前分页符
new Paragraph({
  pageBreakBefore: true,
  children: [new TextRun("这将在新页面上开始")]
})

// ⚠️ 重要提示：永远不要单独使用 PageBreak - 它将创建 Word 无法打开的无效 XML
// ❌ 错误：new PageBreak() 
// ✅ 正确：new Paragraph({ children: [new PageBreak()] })
```

## 页眉/页脚与页面设置
```javascript
const doc = new Document({
  sections: [{
    properties: {
      page: {
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }, // 1440 = 1 英寸
        size: { orientation: PageOrientation.L