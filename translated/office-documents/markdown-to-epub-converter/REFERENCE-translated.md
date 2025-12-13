<!--
本文件由智谱 AI 自动翻译生成
原文件: REFERENCE.md
翻译时间: 2025-12-12 16:13:29
翻译模型: glm-4-flash
原文大小: 8,682 字符
-->

# Markdown 到 EPUB 技能 - 技术参考

扩展和自定义 Markdown 到 EPUB 技能的高级技术文档。

## 模块概述

### `markdown_processor.py`

解析 Markdown 并提取文档结构的核心模块。

#### 主要类

**MarkdownProcessor**
```python
processor = MarkdownProcessor()
result = processor.process(markdown_content)
```

方法：
- `process(markdown_content: str) -> Dict` - 解析 Markdown 并提取结构
- `_extract_frontmatter(content: str) -> str` - 提取 YAML 前置元数据
- `_extract_metadata(content: str)` - 从文档标题中提取元数据
- `_parse_chapters(content: str) -> List[Chapter]` - 解析为章节
- `_parse_sections(content: str, min_level: int) -> List[Section]` - 解析章节
- `_build_toc() -> List[Dict]` - 构建目录
- `markdown_to_html(markdown_text: str) -> str` - 将 Markdown 转换为 HTML
- `_render_inline(text: str) -> str` - 处理内联元素（粗体、斜体、链接）

#### 数据类

**EbookMetadata**
```python
metadata = EbookMetadata(
    title="My Book",
    author="John Doe",
    language="en",
    date="2025-01-15",
    identifier="unique-id"
)
```

**Chapter**
```python
chapter = Chapter(
    title="Chapter 1",
    content="Introduction text...",
    sections=[Section(...), ...],
    anchor="chapter-1"
)
```

**Section**
```python
section = Section(
    title="Section 1.1",
    level=2,
    content="Section content...",
    anchor="section-1-1"
)
```

### `epub_generator.py`

使用 ebooklib 创建和管理 EPUB 文件。

#### 主要类

**EPUBGenerator**
```python
generator = EPUBGenerator(metadata)
success = generator.generate(chapters, output_path)
```

方法：
- `generate(chapters: List[Chapter], output_path: str) -> bool` - 主要生成方法
- `_create_book()` - 初始化 EPUB 书籍对象
- `_add_chapters()` - 将章节添加到书籍
- `_render_chapter(chapter: Chapter) -> str` - 将章节渲染为 XHTML
- `_render_content(content: str) -> str` - 将 Markdown 内容渲染为 HTML
- `_add_style()` - 添加 CSS 样式
- `_add_toc()` - 生成目录
- `_write_epub(output_path: str)` - 将 EPUB 文件写入磁盘

**默认 CSS**
- 内置于 `EPUBGenerator.DEFAULT_CSS`
- 可通过子类化进行自定义
- 适用于所有屏幕尺寸的响应式设计

#### 方便函数

```python
# 从 Markdown 字符串创建 EPUB
create_epub_from_markdown(
    markdown_content: str,
    output_path: str,
    title: Optional[str] = None,
    author: Optional[str] = None
) -> bool
```

## HTML/XHTML 生成

### Markdown 到 HTML 转换

`markdown_to_html()` 方法将 Markdown 转换为语义 HTML：

```python
markdown = "# Title\n\nSome **bold** text"
html = MarkdownProcessor.markdown_to_html(markdown)
# 返回: <h1>Title</h1>\n<p>Some <strong>bold</strong> text</p>
```

### 支持的元素

- **标题**（H1-H6）：`# to ######`
- **强调**：`**bold**`, `*italic*`, `__bold__`, `_italic_`
- **链接**：`[text](url)`
- **列表**：`- item`, `* item`, `1. item`
- **代码**：`` `inline` ``, ` ``` ` ` ` (块)
- **引用**：`> quote`
- **水平线**：`---`, `***`, `___`

### 特殊处理

- HTML 转义：`&`, `<`, `>`, `"`, `'` 自动转义
- 代码块：内容被转义并保留原样
- 段落：双换行创建新的 `<p>` 标签
- 链接：正确编码的 href 属性

## EPUB 结构

### 生成的文件布局

```
metadata.opf          # 包含元数据
nav.xhtml             # EPUB3 导航
toc.ncx               # NCBI NCX（向后兼容）
OEBPS/
├── chap_001.xhtml    # 章节文件
├── chap_002.xhtml
├── ...
├── style/
│   └── main.css      # 内嵌样式表
└── [其他资源]
```

### 元数据字段

来自 `EbookMetadata`：
- **identifier**：唯一 ID（如果没有提供，自动生成 UUID）
- **title**：书籍标题（必需）
- **language**：语言代码（默认："en"）
- **author**：作者姓名
- **date**：出版日期（可选）

### 导航

- **NCX（导航控制文件）**：用于与旧读者的向后兼容
- **NAV（EPUB3 导航文档）**：EPUB3 读者的标准
- 自动从章节/章节层次结构生成

## 自定义

### 扩展类

**自定义样式**
```python
class CustomEPUBGenerator(EPUBGenerator):
    CUSTOM_CSS = """/* Your CSS here */"""

    def _add_style(self):
        # 自定义样式逻辑
        super()._add_style()
```

**自定义元数据**
```python
metadata = EbookMetadata()
metadata.title = "My Custom Title"
metadata.author = "Custom Author"
generator = EPUBGenerator(metadata)
```

**自定义 HTML 渲染**
```python
class CustomProcessor(MarkdownProcessor):
    @staticmethod
    def markdown_to_html(markdown_text):
        # 自定义转换逻辑
        return html
```

### 添加新的 Markdown 功能

1. 在 `MarkdownProcessor` 中扩展 `markdown_to_html()`
2. 添加对新 Markdown 语法的解析逻辑
3. 返回适当的 HTML 等价物
4. 使用 `test_epub_skill.py` 进行测试

示例 - 添加删除线支持：
```python
# 在 markdown_to_html()
text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
```

## 性能考虑

### 大型文档

- 处理是 O(n) 其中 n = 文档长度
- 内存使用：约 3-5 倍的 Markdown 源大小
- EPUB 生成通常小于 100ms 对于 100+ 页的文档

### 优化技巧

1. **批量处理**：一次运行处理多个文档
2. **章节拆分**：将非常大的文档拆分为较小的文件
3. **内容优化**：删除不必要的空白/格式
4. **懒加载**：按需生成 EPUB 而不是预先计算

## 调试

### 启用调试输出

```python
import logging
logging.basicConfig(level=logging.DEBUG)

processor = MarkdownProcessor()
result = processor.process(markdown_content)
```

### 常见问题

**空章节**
- 检查 Markdown 是否有正确的结构
- 验证没有章节完全为空的内容
- 使用 `_render_content()` 调试 HTML 输出

**无效的 XHTML**
- 验证所有标签都已正确关闭
- 检查是否有未转义的特殊字符
- 使用验证工具检查生成的 EPUB

**缺少目录**
- 确保章节/章节有正确的标题
- 验证锚点生成是否正确
- 检查是否已填充章节列表

## API 集成

### 与 Claude 技能一起使用

```python
# 在您的技能实现中
def generate_ebook(markdown_content, title=None, author=None):
    from epub_generator import create_epub_from_markdown

    success = create_epub_from_markdown(
        markdown_content,
        "output.epub",
        title=title,
        author=author
    )

    if success:
        # 返回 file_id 或流
        return read_epub_file("output.epub")
    else:
        return None
```

### 文件处理

该技能可以处理：
- 直接文件路径
- 通过 Files API 的文件内容
- Markdown 字符串
- 聊天消息内容

## 测试

### 单元测试

```python
# 测试 Markdown 解析
processor = MarkdownProcessor()
result = processor.process(test_markdown)
assert len(result['chapters']) == expected_count

# 测试 HTML 生成
html = MarkdownProcessor.markdown_to_html(test_content)
assert '<h1>' in html
assert '<strong>' in html
```

### 集成测试

```python
# 测试端到端 EPUB 生成
success = create_epub_from_markdown(
    markdown_content,
    test_output_path,
    title="Test",
    author="Tester"
)
assert success
assert Path(test_output_path).exists()
```

### 测试覆盖率

当前测试覆盖率：
- ✓ 多级标题的 Markdown 解析
- ✓ YAML 前置元数据提取
- ✓ HTML 生成和转义
- ✓ EPUB 文件创建
- ✓ 边界情况（空内容，特殊字符）
- ✓ 目录生成
- ✓ 大型文档（100+ 章节）

## 版本历史

**v1.0.0**（当前）
- 初次发布
- 完整的 Markdown 到 EPUB 转换
- YAML 前置元数据支持
- 自动目录生成
- EPUB3 兼容
- 完整的测试套件

## 未来路线图

**v1.1.0**（计划）
- 封面页生成
- 自定义 CSS 模板
- 图像嵌入

**v2.0.0**（未来）
- Kindle 格式支持 (.mobi, .azw3)
- 高级表格支持
- 脚注和交叉引用
- 实验性的 MCP 集成以支持封面图像

## 贡献

### 代码指南
- 遵循 PEP 8 风格指南
- 为所有函数添加文档字符串
- 包含类型提示
- 为新功能编写测试
- 更新此参考文档

### 添加功能
1. 创建功能分支
2. 实现并添加测试
3. 更新 SKILL.md 和 REFERENCE.md
4. 提交并附带测试结果

---

**最后更新**: 2025-01-16
**维护者**: 技能开发团队