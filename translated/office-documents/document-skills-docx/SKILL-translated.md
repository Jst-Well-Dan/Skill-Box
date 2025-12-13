<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:13:31
翻译模型: glm-4-flash
原文大小: 10,150 字符
-->

---
name: docx
description: "综合的文档创建、编辑和分析，支持跟踪更改、注释、格式保留和文本提取。当Claude需要处理专业文档（.docx文件）时，用于：(1) 创建新文档，(2) 修改或编辑内容，(3) 处理跟踪更改，(4) 添加注释，或任何其他文档任务"
license: 专有。LICENSE.txt包含完整条款
---

# DOCX 创建、编辑和分析

## 概述

用户可能要求您创建、编辑或分析 .docx 文件的内容。.docx 文件本质上是一个包含 XML 文件和其他资源的 ZIP 存档，您可以读取或编辑。您有不同工具和工作流程可供不同任务使用。

## 工作流程决策树

### 阅读和分析内容
使用以下“文本提取”或“原始 XML 访问”部分

### 创建新文档
使用“创建新的 Word 文档”工作流程

### 编辑现有文档
- **您自己的文档 + 简单更改**
  使用“基本 OOXML 编辑”工作流程

- **他人的文档**
  使用**“红线工作流程”**（推荐默认）

- **法律、学术、商业或政府文档**
  使用**“红线工作流程”**（必需）

## 阅读和分析内容

### 文本提取
如果您只需要读取文档的文本内容，应使用 pandoc 将文档转换为 markdown。Pandoc 提供了出色的保留文档结构支持，并可以显示跟踪更改：

```bash
# 将文档转换为 markdown 并显示跟踪更改
pandoc --track-changes=all path-to-file.docx -o output.md
# 选项：--track-changes=accept/reject/all
```

### 原始 XML 访问
您需要原始 XML 访问以：注释、复杂格式、文档结构、嵌入媒体和元数据。对于这些功能中的任何一项，您都需要解包文档并读取其原始 XML 内容。

#### 解包文件
`python ooxml/scripts/unpack.py <office_file> <output_directory>`

#### 关键文件结构
* `word/document.xml` - 主要文档内容
* `word/comments.xml` - 在 document.xml 中引用的注释
* `word/media/` - 嵌入的图像和媒体文件
* 跟踪更改使用 `<w:ins>`（插入）和 `<w:del>`（删除）标签

## 创建新的 Word 文档

从零开始创建新的 Word 文档时，请使用 **docx-js**，它允许您使用 JavaScript/TypeScript 创建 Word 文档。

### 工作流程
1. **必需 - 读取整个文件**：从头到尾完整阅读[`docx-js.md`](docx-js.md)（约 500 行）。**永远不要在阅读此文件时设置任何范围限制**。在开始创建文档之前，请阅读完整文件内容，以获取详细的语法、关键格式规则和最佳实践。
2. 使用 Document、Paragraph、TextRun 组件创建 JavaScript/TypeScript 文件（您可以假设所有依赖项都已安装，但如果未安装，请参阅以下依赖项部分）
3. 使用 Packer.toBuffer() 导出为 .docx

## 编辑现有的 Word 文档

当编辑现有的 Word 文档时，请使用 **Document library**（一个用于 OOXML 操作的 Python 库）。该库自动处理基础设施设置，并提供用于文档操作的方法。对于复杂场景，您可以直接通过库访问底层 DOM。

### 工作流程
1. **必需 - 读取整个文件**：从头到尾完整阅读[`ooxml.md`](ooxml.md)（约 600 行）。**永远不要在阅读此文件时设置任何范围限制**。阅读完整文件内容以获取 Document library API 和直接编辑文档文件的 XML 模式。
2. 解包文档：`python ooxml/scripts/unpack.py <office_file> <output_directory>`
3. 使用 Document library 创建并运行 Python 脚本（请参阅 ooxml.md 中的“Document Library”部分）
4. 打包最终文档：`python ooxml/scripts/pack.py <input_directory> <office_file>`

Document library 提供了用于常见操作的高级方法和直接 DOM 访问，用于复杂场景。

## 文档审查的红线工作流程

此工作流程允许您在实现 OOXML 之前使用 markdown 计划全面的跟踪更改。

**关键**：对于完整的跟踪更改，您必须系统地实施所有更改。

**批量策略**：将相关更改分组为 3-10 个更改的批次。这使调试变得可管理，同时保持效率。在移动到下一个批次之前测试每个批次。

**原则：最小、精确的编辑**
在实施跟踪更改时，仅标记实际更改的文本。重复未更改的文本会使编辑难以审查，并显得不专业。将替换拆分为：[未更改的文本] + [删除] + [插入] + [未更改的文本]。通过从原始中提取 `<w:r>` 元素并重新使用它来保留原始运行的原 RSID，以保留未更改的文本。

示例 - 将句子中的“30 天”更改为“60 天”：
```python
# 不好 - 替换整个句子
'<w:del><w:r><w:delText>30 天。</w:delText></w:r></w:del><w:ins><w:r><w:t>60 天。</w:t></w:r></w:ins>'

# 好 - 仅标记更改的内容，保留原始 <w:r> 以便未更改的文本
'<w:r w:rsidR="00AB12CD"><w:t>30 天</w:t></w:r><w:del><w:r><w:delText>30</w:delText></w:r></w:del><w:ins><w:r><w:t>60</w:t></w:r></w:ins><w:r w:rsidR="00AB12CD"><w:t> 天。</w:t></w:r>'
```

### 跟踪更改工作流程

1. **获取 markdown 表示形式**：将文档转换为 markdown 并保留跟踪更改：
   ```bash
   pandoc --track-changes=all path-to-file.docx -o current.md
   ```

2. **识别和分组更改**：审查文档并识别所有需要的更改，将它们组织成逻辑批次：

   **位置方法**（用于在 XML 中查找更改）：
   - 部分标题编号（例如，“第 3.2 部分”，“第 IV 条”）
   - 如果编号，则段落标识符
   - 带有独特周围文本的 grep 模式
   - 文档结构（例如，“第一段”，“签名块”）
   - **不要使用 markdown 行号** - 它们不映射到 XML 结构

   **批量组织**（每个批次 3-10 个相关更改）：
   - 按部分：例如，“第 2 部分的修正批次”，“第 5 部分的更新批次”
   - 按类型：例如，“第 1 批次：日期更正”，“第 2 批次：当事人名称更改”
   - 按复杂性：从简单的文本替换开始，然后处理复杂的结构更改
   - 顺序：例如，“第 1 批次：第 1-3 页”，“第 2 批次：第 4-6 页”

   对于每个相关更改批次：

   **a. 将文本映射到 XML**：在 `word/document.xml` 中 grep 文本以验证文本如何拆分到 `<w:r>` 元素中。

   **b. 创建并运行脚本**：使用 `get_node` 查找节点，实施更改，然后 `doc.save()`。请参阅 ooxml.md 中的**“Document Library”**部分以获取模式。

   **注意**：始终在编写脚本之前 grep `word/document.xml` 以获取当前行号并验证文本内容。行号在每次脚本运行后会发生变化。

3. **阅读文档和拆包**：
   - **必需 - 读取整个文件**：从头到尾完整阅读[`ooxml.md`](ooxml.md)（约 600 行）。**永远不要在阅读此文件时设置任何范围限制**。特别关注“Document Library”和“跟踪更改模式”部分。
   - **拆包文档**：`python ooxml/scripts/unpack.py <file.docx> <dir>`
   - **注意建议的 RSID**：拆包脚本将建议一个用于跟踪更改的 RSID。复制此 RSID 以在步骤 4b 中使用。

4. **在批次中实施更改**：逻辑地分组更改（按部分、按类型或按邻近性）并在单个脚本中一起实施它们。这种方法：
   - 使调试更容易（较小的批次更容易隔离错误）
   - 允许渐进式进步
   - 保持效率（3-10 个更改的批次大小效果良好）

   **建议的批量分组**：
   - 按文档部分（例如，“第 3 部分的更改”，“定义”，“终止条款”）
   - 按更改类型（例如，“日期更改”，“当事人名称更新”，“法律术语替换”）
   - 按邻近性（例如，“第 1-3 页的更改”，“文档前半部分的更改”）

   对于每个相关更改批次：

   **a. 将文本映射到 XML**：在 `word/document.xml` 中 grep 文本以验证文本如何拆分到 `<w:r>` 元素中。

   **b. 创建并运行脚本**：使用 `get_node` 查找节点，实施更改，然后 `doc.save()`。请参阅 ooxml.md 中的**“Document Library”**部分以获取模式。

   **注意**：始终在编写脚本之前 grep `word/document.xml` 以获取当前行号并验证文本内容。行号在每次脚本运行后会发生变化。

5. **打包文档**：在所有批次完成后，将拆包目录转换回 .docx：
   ```bash
   python ooxml/scripts/pack.py unpacked reviewed-document.docx
   ```

6. **最终验证**：对完整文档进行全面的检查：
   - 将最终文档转换为 markdown：
     ```bash
     pandoc --track-changes=all reviewed-document.docx -o verification.md
     ```
   - 验证所有更改是否正确应用：
     ```bash
     grep "original phrase" verification.md  # 应该找不到它
     grep "replacement phrase" verification.md  # 应该找到它
     ```
   - 检查是否引入了任何意外的更改


## 将文档转换为图像

要直观地分析 Word 文档，请使用两步过程将其转换为图像：

1. **将 DOCX 转换为 PDF**：
   ```bash
   soffice --headless --convert-to pdf document.docx
   ```

2. **将 PDF 页转换为 JPEG 图像**：
   ```bash
   pdftoppm -jpeg -r 150 document.pdf page
   ```
   这将创建类似 `page-1.jpg`、`page-2.jpg` 等文件。

选项：
- `-r 150`：设置分辨率为 150 DPI（调整质量/大小平衡）
- `-jpeg`：输出 JPEG 格式（如果首选 PNG，请使用 `-png`）
- `-f N`：要转换的第一页（例如，`-f 2` 从第 2 页开始）
- `-l N`：要转换的最后一页（例如，`-l 5` 停止在第 5 页）
- `page`：输出文件的名称前缀

示例用于特定范围：
```bash
pdftoppm -jpeg -r 150 -f 2 -l 5 document.pdf page  # 仅转换第 2-5 页
```

## 代码风格指南
**重要**：在生成 DOCX 操作的代码时：
- 编写简洁的代码
- 避免冗长的变量名称和冗余操作
- 避免不必要的打印语句

## 依赖项

必需的依赖项（如果不可用，请安装）：

- **pandoc**：`sudo apt-get install pandoc`（用于文本提取）
- **docx**：`npm install -g docx`（用于创建新文档）
- **LibreOffice**：`sudo apt-get install libreoffice`（用于 PDF 转换）
- **Poppler**：`sudo apt-get install poppler-utils`（用于 pdftoppm 将 PDF 转换为图像）
- **defusedxml**：`pip install defusedxml`（用于安全的 XML 解析）