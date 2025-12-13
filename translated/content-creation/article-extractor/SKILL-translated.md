<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:11:39
翻译模型: glm-4-flash
原文大小: 9,615 字符
-->

---
name: article-extractor
description: 从 URL（博客文章、教程）中提取干净的文本内容并保存为可读文本。当用户想要下载、提取或保存文章/博客文章的 URL 而不带广告、导航或杂乱内容时使用。
allowed-tools: Bash,Write
---

# 文章提取器

此技能从网络文章和博客文章中提取主要内容，删除导航、广告、新闻订阅注册和其他杂乱内容。保存干净的、可读的文本。

## 何时使用此技能

当用户：
- 提供文章/博客 URL 并想要文本内容
- 要求“下载这篇文章”
- 想要“从 [URL] 提取内容”
- 要求“将这篇博客文章保存为文本”
- 需要没有干扰的干净文章文本

## 工作原理

### 优先顺序：
1. **检查是否安装了工具**（reader 或 trafilatura）
2. **使用最佳可用工具下载和提取文章**
3. **清理内容**（删除额外空格，正确格式化）
4. **以文章标题作为文件名保存到文件**
5. **确认位置**并显示预览

## 安装检查

按以下顺序检查文章提取工具：

### 选项 1：reader（推荐 - Mozilla 的 Readability）

```bash
command -v reader
```

如果没有安装：
```bash
npm install -g @mozilla/readability-cli
# 或
npm install -g reader-cli
```

### 选项 2：trafilatura（基于 Python，非常好）

```bash
command -v trafilatura
```

如果没有安装：
```bash
pip3 install trafilatura
```

### 选项 3：后备方案（curl + 简单解析）

如果没有可用工具，使用基本的 curl + 文本提取（不太可靠但可行）

## 提取方法

### 方法 1：使用 reader（适用于大多数文章）

```bash
# 提取文章
reader "URL" > article.txt
```

**优点：**
- 基于 Mozilla 的 Readability 算法
- 极佳的去除杂乱内容
- 保留文章结构

### 方法 2：使用 trafilatura（适用于博客/新闻）

```bash
# 提取文章
trafilatura --URL "URL" --output-format txt > article.txt

# 或使用更多选项
trafilatura --URL "URL" --output-format txt --no-comments --no-tables > article.txt
```

**优点：**
- 非常准确的提取
- 适用于各种网站结构
- 处理多种语言

**选项：**
- `--no-comments`: 跳过评论部分
- `--no-tables`: 跳过数据表
- `--precision`: 优先考虑精确度
- `--recall`: 提取更多内容（可能包含一些噪声）

### 方法 3：后备方案（curl + 基本解析）

```bash
# 下载和提取基本内容
curl -s "URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            if tag in {'p', 'article', 'main', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
                self.in_content = True
        self.current_tag = tag

    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > article.txt
```

**注意：** 这不太可靠但可行。

## 提取标题

提取标题作为文件名：

### 使用 reader：
```bash
# reader 输出带有标题的 markdown，标题在顶部
TITLE=$(reader "URL" | head -n 1 | sed 's/^# //')
```

### 使用 trafilatura：
```bash
# 获取包括标题在内的元数据
TITLE=$(trafilatura --URL "URL" --json | python3 -c "import json, sys; print(json.load(sys.stdin)['title'])")
```

### 使用 curl（后备方案）：
```bash
TITLE=$(curl -s "URL" | grep -oP '<title>\K[^<]+' | sed 's/ - .*//' | sed 's/ | .*//')
```

## 文件名创建

为文件系统清理标题：

```bash
# 获取标题
TITLE="来自网站的文章标题"

# 为文件系统清理（删除特殊字符，限制长度）
FILENAME=$(echo "$TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<' '' | tr '>' '' | tr '|' '-' | cut -c 1-100 | sed 's/ *$//')

# 添加扩展名
FILENAME="${FILENAME}.txt"
```

## 完整工作流程

```bash
ARTICLE_URL="https://example.com/article"

# 检查工具
if command -v reader &> /dev/null; then
    TOOL="reader"
    echo "使用 reader（Mozilla Readability）"
elif command -v trafilatura &> /dev/null; then
    TOOL="trafilatura"
    echo "使用 trafilatura"
else
    TOOL="fallback"
    echo "使用后备方法（可能不太准确）"
fi

# 提取文章
case $TOOL in
    reader)
        # 获取内容
        reader "$ARTICLE_URL" > temp_article.txt

        # 获取标题（# 后的第一行 markdown）
        TITLE=$(head -n 1 temp_article.txt | sed 's/^# //')
        ;;

    trafilatura)
        # 从元数据获取标题
        METADATA=$(trafilatura --URL "$ARTICLE_URL" --json)
        TITLE=$(echo "$METADATA" | python3 -c "import json, sys; print(json.load(sys.stdin).get('title', 'Article'))")

        # 获取干净的内容
        trafilatura --URL "$ARTICLE_URL" --output-format txt --no-comments > temp_article.txt
        ;;

    fallback)
        # 获取标题
        TITLE=$(curl -s "$ARTICLE_URL" | grep -oP '<title>\K[^<]+' | head -n 1)
        TITLE=${TITLE%% - *}  # 移除网站名称
        TITLE=${TITLE%% | *}  # 移除网站名称（另一种方式）

        # 获取内容（基本提取）
        curl -s "$ARTICLE_URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'form'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            if tag in {'p', 'article', 'main'}:
                self.in_content = True
        if tag in {'h1', 'h2', 'h3'}:
            self.content.append('\n')

    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > temp_article.txt
        ;;
esac

# 清理文件名
FILENAME=$(echo "$TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<>' '' | tr '|' '-' | cut -c 1-80 | sed 's/ *$//' | sed 's/^ *//')
FILENAME="${FILENAME}.txt"

# 移动到最终文件名
mv temp_article.txt "$FILENAME"

# 显示结果
echo "✓ 提取文章：$TITLE"
echo "✓ 保存到：$FILENAME"
echo ""
echo "预览（前 10 行）："
head -n 10 "$FILENAME"
```

## 错误处理

### 常见问题

**1. 工具未安装**
- 尝试备用工具（reader → trafilatura → 后备方案）
- 提供安装：使用“npm install -g reader-cli”安装 reader

**2. 需要付费墙或登录**
- 提取工具可能会失败
- 通知用户：“这篇文章需要认证。无法提取。”

**3. 无效的 URL**
- 检查 URL 格式
- 尝试使用和没有重定向的

**4. 未提取内容**
- 网站可能使用大量的 JavaScript
- 尝试后备方法
- 如果提取失败，通知用户

**5. 标题中包含特殊字符**
- 为文件系统清理标题
- 移除：`/`, `:`, `?`, `"`, `<`, `>`, `|`
- 用 `-` 或移除

## 输出格式

### 保存的文件包含：
- 文章标题（如果可用）
- 作者（如果工具可用）
- 主要文章文本
- 标题部分
- 没有导航、广告或杂乱内容

### 什么被移除：
- 导航菜单
- 广告和促销内容
- 新闻订阅注册表单
- 相关文章侧边栏
- 评论部分（可选）
- 社交媒体按钮
- 隐私政策通知

## 提高结果的最佳实践

**1. 使用 reader 提取大多数文章**
- 最佳全面工具
- 基于 Firefox 阅读视图
- 在大多数新闻网站和博客上工作

**2. 使用 trafilatura 提取：**
- 学术文章
- 新闻网站
- 布局复杂的博客
- 非英语内容

**3. 后备方法限制：**
- 可能包含一些噪声
- 段落检测不太准确
- 对于简单网站来说比没有好

**4. 检查提取质量：**
- 总是向用户显示预览（前 10-15 行）
- 询问是否正确
- 如果需要，尝试不同的工具

## 示例用法

**简单提取：**
```bash
# 用户：“提取 https://example.com/article”
reader "https://example.com/article" > temp.txt
TITLE=$(head -n 1 temp.txt | sed 's/^# //')
FILENAME="$(echo "$TITLE" | tr '/' '-').txt"
mv temp.txt "$FILENAME"
echo "✓ 保存到：$FILENAME"
```

**带有错误处理：**
```bash
if ! reader "$URL" > temp.txt 2>/dev/null; then
    if command -v trafilatura &> /dev/null; then
        trafilatura --URL "$URL" --output-format txt > temp.txt
    else
        echo "错误：无法提取文章。安装 reader 或 trafilatura。"
        exit 1
    fi
fi
```

## 最佳实践

- ✅ 总是在提取后显示预览（前 10 行）
- ✅ 在保存之前验证提取是否成功
- ✅ 为文件系统兼容性清理文件名
- ✅ 如果主要方法失败，尝试后备方法
- ✅ 通知用户使用了哪个工具
- ✅ 保持文件名长度合理（< 100 个字符）

## 提取后

向用户显示：
1. “✓ 提取：[文章标题]”
2. “✓ 保存到：[文件名]”
3. 显示预览（前 10-15 行）
4. 文件大小和位置

询问是否需要：
- “您是否希望我也从这个中创建一个 Ship-Learn-Next 计划？”（如果使用 ship-learn-next 技能）
- “我应该提取另一篇文章吗？”