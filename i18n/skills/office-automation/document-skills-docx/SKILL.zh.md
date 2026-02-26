---
name: docx
description: "综合的文档创建、编辑和分析，支持跟踪更改、注释、格式保留和文本提取。当Claude需要处理专业文档（.docx文件）时，用于：(1) 创建新文档，(2) 修改或编辑内容，(3) 处理跟踪更改，(4) 添加注释，或任何其他文档任务"
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX 创建、编辑和分析

## 概述

用户可能要求您创建、编辑或分析 .docx 文件的内容。.docx 文件本质上是一个包含 XML 文件和其他资源的 ZIP 存档，您可以读取或编辑这些资源。您有不同的工具和工作流程可供不同任务使用。

## 工作流程决策树

### 阅读和分析内容
使用以下“文本提取”或“原始 XML 访问”部分

### 创建新文档
使用“创建新的 Word 文档”工作流程

### 编辑现有文档
- **您自己的文档 + 简单更改**
  使用“基本 OOXML 编辑”工作流程

- **他人的文档**
  使用**“红笔批注工作流程”**（推荐默认）

- **法律、学术、商业或政府文档**
  使用**“红笔批注工作流程”**（必需）

## 阅读和分析内容

### 文本提取
如果您只需读取文档的文本内容，应使用 pandoc 将文档转换为 markdown。Pandoc 提供了出色的结构保留支持，并可以显示跟踪更改：

```bash
# 将文档转换为带有跟踪更改的 markdown
pandoc --track-changes=all path-to-file.docx -o output.md
# 选项：--track-changes=accept/reject/all
```

### 原始 XML 访问
您需要原始 XML 访问以获取注释、复杂格式、文档结构、嵌入媒体和元数据。对于这些功能中的任何一项，您都需要解压缩文档并读取其原始 XML 内容。

#### 解压缩文件
`python ooxml/scripts/unpack.py <office_file> <output_directory>`

#### 关键文件结构
* `word/document.xml` - 主要文档内容
* `word/comments.xml` - 在 document.xml 中引用的注释
* `word/media/` - 嵌入的图像和媒体文件
* 跟踪更改使用 `<w:ins>`（插入）和 `<w:del>`（删除）标签

## 创建新的 Word 文档

当从头开始创建新的 Word 文档时，请使用 **docx-js**，它允许您使用 JavaScript/TypeScript 创建 Word 文档。

### 工作流程
1. **必需 - 阅读整个文件**：从开始到结束完整地阅读 `docx-js.md`（约 500 行）。**永远不要在阅读此文件时设置任何范围限制**。在继续文档创建之前，请阅读完整文件内容以获取详细的语法、关键格式规则和最佳实践。
2. 使用 Document、Paragraph、TextRun 组件创建 JavaScript/TypeScript 文件（您可以假设所有依赖项都已安装，但如果没有，请参阅以下依赖项部分）
3. 使用 Packer.toBuffer() 导出为 .docx

## 编辑现有的 Word 文档

当编辑现有的 Word 文档时，请使用 **Document library**（一个用于 OOXML 操作的 Python 库）。该库自动处理基础设施设置，并提供用于文档操作的方法。对于复杂场景，您可以直接通过库访问底层 DOM。

### 工作流程
1. **必需 - 阅读整个文件**：从开始到结束完整地阅读 `ooxml.md`（约 600 行）。**永远不要在阅读此文件时设置任何范围限制**。阅读完整文件内容以获取 Document library API 和直接编辑文档文件的 XML 模式。
2. 解压缩文档：`python ooxml/scripts/unpack.py <office_file> <output_directory>`
3. 使用 Document library 创建并运行 Python 脚本（请参阅 ooxml.md 中的“Document Library”部分）
4. 打包最终文档：`python ooxml/scripts/pack.py <input_directory> <office_file>`

Document library 提供了用于常见操作的高级方法和直接 DOM 访问，以处理复杂场景。

## 文档审查的红笔批注工作流程

此工作流程允许您在实现 OOXML 之前使用 markdown 规划全面的跟踪更改。

**关键**：为了实现完整的跟踪更改，您必须系统地实施所有更改。

**批量策略**：将相关更改分组为每批 3-10 个更改。这使调试变得可管理，同时保持效率。在移动到下一个之前测试每个批量。

**原则：最小、精确的编辑**
在实现跟踪更改时，仅标记实际更改的文本。重复未更改的文本会使编辑难以审查，并显得不专业。将替换拆分为：[未更改的文本] + [删除] + [插入] + [未更改的文本]。通过从原始中提取 `<w:r>` 元素并重新使用它来保留原始运行中的 RSID，以保留未更改文本的原始 RSID。

示例 - 将句子中的“30 天”更改为“60 天”：
```python
# 不好 - 替换整个句子
'<w:del><w:r><w:delText>The term is 30 days.</w:delText></w:r></w:del><w:ins><w:r><w:t>The term is 60 days.</w:t></w:r></w:ins>'

# 好 - 仅标记更改的内容，保留原始 <w:r> 以供未更改的文本使用
'<w:r w:rsidR="00AB12CD"><w:t>The term is </w:t></w:r><w:del><w:r><w:delText>30</w:delText></w:r></w:del><w:ins><w:r><w:t>60</w:t></w:r></w:ins><w:r w:rsidR="00AB12CD"><w:t> days.</w:t></w:r>'
```

### 跟踪更改工作流程

1. **获取 markdown 表示形式**：将文档转换为 markdown，同时保留跟踪更改：
   ```bash
   pandoc --track-changes=all path-to-file.docx -o current.md
   ```

2. **识别和分组更改**：审查文档，并识别所有需要的更改，将它们组织成逻辑批量：

   **位置方法**（用于在 XML 中查找更改）：
   - 部分或标题编号（例如，“第 3.2 部分”，“第 IV 条”）
   - 如果编号，则段落标识符
   - 使用唯一周围文本的 grep 模式
   - 文档结构（例如，“第一段”，“签名块”）
   - **不要使用 markdown 行号** - 它们不映射到 XML 结构

   **批量组织**（每批 3-10 个相关更改）：
   - 按部分：例如，“第 2 部分的批量 1：修订”，“第 5 部分的批量 2：更新”
   - 按类型：例如，“批量 1：日期更正”，“批量 2：当事人名称更改”
   - 按复杂性：从简单的文本替换开始，然后处理复杂的结构更改
   - 顺序：例如，“批量 1：第 1-3 页”，“批量 2：文档前半部分”

3. **阅读文档和解压缩**：
   - **必需 - 阅读整个文件**：从开始到结束完整地阅读 `ooxml.md`（约 600 行）。**永远不要在阅读此文件时设置任何范围限制**。阅读完整文件内容以获取 Document library API 和直接编辑文档文件的 XML 模式。
   - **解压缩文档**：`python ooxml/scripts/unpack.py <file.docx> <dir>`
   - **注意建议的 RSID**：解压缩脚本将建议一个用于跟踪更改的 RSID。复制此 RSID 以在步骤 4b 中使用。

4. **按批量实施更改**：逻辑地分组更改（按部分、按类型或按邻近性）并在单个脚本中一起实施它们。此方法：
   - 使调试更容易（较小的批量 = 更容易隔离错误）
   - 允许增量进度
   - 保持效率（批量大小为 3-10 个更改效果很好）

   **建议的批量分组**：
   - 按文档部分（例如，“第 3 部分的更改”，“定义”，“终止条款”）
   - 按更改类型（例如，“日期更改”，“当事人名称更新”，“法律术语替换”）
   - 按邻近性（例如，“第 1-3 页的更改”，“文档前半部分的更改”）

   对于每个相关更改的批量：

   **a. 将文本映射到 XML**：在 `word/document.xml` 中 grep 文本以验证文本如何跨 `<w:r>` 元素拆分。

   **b. 创建并运行脚本**：使用 `get_node` 查找节点，实施更改，然后 `doc.save()`。请参阅 ooxml.md 中的“Document Library”部分以获取模式。

   **注意**：始终在编写脚本之前 grep `word/document.xml` 以获取当前行号并验证文本内容。行号在每次脚本运行后会更改。

5. **打包文档**：在所有批量完成后，将解压缩目录转换回 .docx：
   ```bash
   python ooxml/scripts/pack.py unpacked reviewed-document.docx
   ```

6. **最终验证**：对完整的文档进行综合检查：
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

要可视分析 Word 文档，请使用两步过程将其转换为图像：

1. **将 DOCX 转换为 PDF**：
   ```bash
   soffice --headless --convert-to pdf document.docx
   ```

2. **将 PDF 页转换为 JPEG 图像**：
   ```bash
   pdftoppm -jpeg -r 150 document.pdf page
   ```
   这将创建类似 `page-1.jpg`、`page-2.jpg` 等的文件。

选项：
- `-r 150`：设置分辨率为 150 DPI（调整质量/大小平衡）
- `-jpeg`：输出 JPEG 格式（如果首选 PNG，则使用 `-png`）
- `-f N`：要转换的第一页（例如，`-f 2` 从第 2 页开始）
- `-l N`：要转换的最后一页（例如，`-l 5` 停止在第 5 页）
- `page`：输出文件的文件名前缀

示例用于特定范围：
```bash
pdftoppm -jpeg -r 150 -f 2 -l 5 document.pdf page  # 仅转换第 2-5 页
```

## 代码风格指南
**重要**：在生成 DOCX 操作的代码时：
- 编写简洁的代码
- 避免冗长的变量名称和重复操作
- 避免不必要的打印语句

## 依赖项

必需的依赖项（如果不可用，请安装）：

- **pandoc**：`sudo apt-get install pandoc`（用于文本提取）
- **docx**：`npm install -g docx`（用于创建新文档）
- **LibreOffice**：`sudo apt-get install libreoffice`（用于 PDF 转换）
- **Poppler**：`sudo apt-get install poppler-utils`（用于 pdftoppm 将 PDF 转换为图像）
- **defusedxml**：`pip install defusedxml`（用于安全的 XML 解析）