<!--
本文件由智谱 AI 自动翻译生成
原文件: ooxml.md
翻译时间: 2025-12-12 16:12:22
翻译模型: glm-4-flash
原文大小: 23,562 字符
-->

---

# Office Open XML 技术参考

**重要：在开始之前，请阅读本完整文档。** 本文档涵盖以下内容：
- [技术指南](#技术指南) - 架构合规性规则和验证要求
- [文档内容模式](#文档内容模式) - 标题、列表、表格、格式化等的 XML 模式
- [文档库（Python）](#文档库-python) - 使用自动基础设施设置推荐的 OOXML 操作方法
- [跟踪更改（红线标记）](#跟踪更改-红线标记) - 实现跟踪更改的 XML 模式

## 技术指南

### 架构合规性
- **`<w:pPr>` 中的元素顺序**：`<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`
- **空白**：在具有前导/尾随空白的 `<w:t>` 元素中添加 `xml:space='preserve'`
- **Unicode**：在 ASCII 内容中转义字符：`"` 变为 `&#8220;`
  - **字符编码参考**：花括号引号 `""` 变为 `&#8220;&#8221;`，撇号 `'` 变为 `&#8217;`，破折号 `—` 变为 `&#8212;`
- **跟踪更改**：使用 `<w:del>` 和 `<w:ins>` 标签，并带有 `w:author="Claude"`，在 `<w:r>` 元素外部
  - **关键**：`<w:ins>` 使用 `</w:ins>` 关闭，`<w:del>` 使用 `</w:del>` 关闭 - 永远不要混合
  - **RSID 必须是 8 位十六进制数**：使用类似 `00AB1234` 的值（仅限 0-9、A-F 字符）
  - **trackRevisions 位置**：在 settings.xml 中在 `<w:proofState>` 之后添加 `<w:trackRevisions/>`
- **图像**：添加到 `word/media/`，在 `document.xml` 中引用，设置尺寸以防止溢出

## 文档内容模式

### 基本结构
```xml
<w:p>
  <w:r><w:t>文本内容</w:t></w:r>
</w:p>
```

### 标题和样式
```xml
<w:p>
  <w:pPr>
    <w:pStyle w:val="Title"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:r><w:t>文档标题</w:t></w:r>
</w:p>

<w:p>
  <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
  <w:r><w:t>章节标题</w:t></w:r>
</w:p>
```

### 文本格式化
```xml
<!-- 粗体 -->
<w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>粗体</w:t></w:r>
<!-- 斜体 -->
<w:r><w:rPr><w:i/><w:iCs/></w:rPr><w:t>斜体</w:t></w:r>
<!-- 下划线 -->
<w:r><w:rPr><w:u w:val="single"/></w:rPr><w:t>下划线</w:t></w:r>
<!-- 高亮 -->
<w:r><w:rPr><w:highlight w:val="yellow"/></w:rPr><w:t>高亮</w:t></w:r>
```

### 列表
```xml
<!-- 有序列表 -->
<w:p>
  <w:pPr>
    <w:pStyle w:val="ListParagraph"/>
    <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
    <w:spacing w:before="240"/>
  </w:pPr>
  <w:r><w:t>第一项</w:t></w:r>
</w:p>

<!-- 在 1 处重新开始编号列表 - 使用不同的 numId -->
<w:p>
  <w:pPr>
    <w:pStyle w:val="ListParagraph"/>
    <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
    <w:spacing w:before="240"/>
  </w:pPr>
  <w:r><w:t>新列表项 1</w:t></w:r>
</w:p>

<!-- 项目符号列表（级别 2） -->
<w:p>
  <