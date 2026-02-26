<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:13:58
翻译模型: glm-4-flash
原文大小: 12,412 字符
-->

---
name: tapestry
description: 统一的内容提取和行动规划。当用户说 "tapestry <URL>"、"weave <URL>"、"help me plan <URL>"、"extract and plan <URL>"、"make this actionable <URL>" 或类似短语，表示他们想要提取内容并创建一个行动计划时使用。自动检测内容类型（YouTube 视频、文章、PDF）并相应处理。
allowed-tools: Bash,Read,Write
---

# Tapestry：统一的内容提取 + 行动规划

这是协调整个 Tapestry 工作流程的 **主技能**：
1. 从 URL 检测内容类型
2. 使用适当的技能提取内容
3. 自动创建 Ship-Learn-Next 行动计划

## 何时使用此技能

当用户：
- 说 "tapestry [URL]"
- 说 "weave [URL]"
- 说 "help me plan [URL]"
- 说 "extract and plan [URL]"
- 说 "make this actionable [URL]"
- 说 "turn [URL] into a plan"
- 提供一个 URL 并要求 "从中学到并实施"
- 想要完整的 Tapestry 工作流程（提取 → 规划）

**要关注的关键词**：tapestry、weave、plan、actionable、extract and plan、make a plan、turn into action

## 工作原理

### 完整工作流程：
1. **检测 URL 类型**（YouTube、文章、PDF）
2. **使用适当的技能提取内容**：
   - YouTube → youtube-transcript 技能
   - 文章 → article-extractor 技能
   - PDF → 下载并提取文本
3. **使用 ship-learn-next 技能创建行动计划**
4. **保存内容文件和计划文件**
5. **向用户展示摘要**

## URL 检测逻辑

### YouTube 视频

**检测模式**：
- `youtube.com/watch?v=`
- `youtu.be/`
- `youtube.com/shorts/`
- `m.youtube.com/watch?v=`

**操作**：使用 youtube-transcript 技能

### 网络文章/博客文章

**检测模式**：
- `http://` 或 `https://`
- NOT YouTube，NOT PDF
- 常见域名：medium.com、substack.com、dev.to、等。
- 任何 HTML 页面

**操作**：使用 article-extractor 技能

### PDF 文档

**检测模式**：
- URL 以 `.pdf` 结尾
- URL 返回 `Content-Type: application/pdf`

**操作**：下载并提取文本

### 其他内容

**后备方案**：
- 尝试 article-extractor（适用于大多数 HTML）
- 如果失败，通知用户不支持此类型

## 步骤-by-步骤工作流程

### 第 1 步：检测内容类型

```bash
URL="$1"

# 检查 YouTube
if [[ "$URL" =~ youtube\.com/watch || "$URL" =~ youtu\.be/ || "$URL" =~ youtube\.com/shorts ]]; then
    CONTENT_TYPE="youtube"

# 检查 PDF
elif [[ "$URL" =~ \.pdf$ ]]; then
    CONTENT_TYPE="pdf"

# 检查 URL 是否返回 PDF
elif curl -sI "$URL" | grep -i "Content-Type: application/pdf" > /dev/null; then
    CONTENT_TYPE="pdf"

# 默认为文章
else
    CONTENT_TYPE="article"
fi

echo "📍 Detected: $CONTENT_TYPE"
```

### 第 2 步：提取内容（按类型）

#### YouTube 视频

```bash
# 使用 youtube-transcript 技能工作流程
echo "📺 提取 YouTube 脚本..."

# 1. 检查 yt-dlp
if ! command -v yt-dlp &> /dev/null; then
    echo "安装 yt-dlp..."
    brew install yt-dlp
fi

# 2. 获取视频标题
VIDEO_TITLE=$(yt-dlp --print "%(title)s" "$URL" | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '')

# 3. 下载脚本
yt-dlp --write-auto-sub --skip-download --sub-langs en --output "temp_transcript" "$URL"

# 4. 转换为干净的文本（去重）
python3 -c "
import sys, re
seen = set()
vtt_file = 'temp_transcript.en.vtt'
try:
    with open(vtt_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
                clean = re.sub('<[^>]*>', '', line)
                clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
                if clean and clean not in seen:
                    print(clean)
                    seen.add(clean)
except FileNotFoundError:
    print('Error: Could not find transcript file', file=sys.stderr)
    sys.exit(1)
" > "${VIDEO_TITLE}.txt"

# 5. 清理
rm -f temp_transcript.en.vtt

CONTENT_FILE="${VIDEO_TITLE}.txt"
echo "✓ 保存脚本：$CONTENT_FILE"
```

#### 文章/博客文章

```bash
# 使用 article-extractor 技能工作流程
echo "📄 提取文章内容..."

# 1. 检查提取工具
if command -v reader &> /dev/null; then
    TOOL="reader"
elif command -v trafilatura &> /dev/null; then
    TOOL="trafilatura"
else
    TOOL="fallback"
fi

echo "使用：$TOOL"

# 2. 根据工具提取
case $TOOL in
    reader)
        reader "$URL" > temp_article.txt
        ARTICLE_TITLE=$(head -n 1 temp_article.txt | sed 's/^# //')
        ;;

    trafilatura)
        METADATA=$(trafilatura --URL "$URL" --json)
        ARTICLE_TITLE=$(echo "$METADATA" | python3 -c "import json, sys; print(json.load(sys.stdin).get('title', 'Article'))")
        trafilatura --URL "$URL" --output-format txt --no-comments > temp_article.txt
        ;;

    fallback)
        ARTICLE_TITLE=$(curl -s "$URL" | grep -oP '<title>\K[^<]+' | head -n 1)
        ARTICLE_TITLE=${ARTICLE_TITLE%% - *}
        curl -s "$URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'form'}
        self.in_content = False

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags and tag in {'p', 'article', 'main'}:
            self.in_content = True

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

# 3. 清理文件名
FILENAME=$(echo "$ARTICLE_TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | cut -c 1-80 | sed 's/ *$//')
CONTENT_FILE="${FILENAME}.txt"
mv temp_article.txt "$CONTENT_FILE"

echo "✓ 保存文章：$CONTENT_FILE"
```

#### PDF 文档

```bash
# 下载并提取 PDF
echo "📑 下载 PDF..."

# 1. 下载 PDF
PDF_FILENAME=$(basename "$URL")
curl -L -o "$PDF_FILENAME" "$URL"

# 2. 使用 pdftotext（如果可用）提取文本
if command -v pdftotext &> /dev/null; then
    pdftotext "$PDF_FILENAME" temp_pdf.txt
    CONTENT_FILE="${PDF_FILENAME%.pdf}.txt"
    mv temp_pdf.txt "$CONTENT_FILE"
    echo "✓ 从 PDF 中提取文本：$CONTENT_FILE"

    # 可选地保留原始 PDF
    echo "保留原始 PDF？(y/n)"
    read -r KEEP_PDF
    if [[ ! "$KEEP_PDF" =~ ^[Yy]$ ]]; then
        rm "$PDF_FILENAME"
    fi
else
    # pdftotext 未找到
    echo "⚠️  pdftotext 未找到。PDF 已下载但未提取。"
    echo "   使用：brew install poppler"
    CONTENT_FILE="$PDF_FILENAME"
fi
```

### 第 3 步：创建 Ship-Learn-Next 行动计划

**重要**：在提取内容后始终创建一个行动计划。

```bash
# 读取提取的内容
CONTENT_FILE="[从上一步]"
```

**创建计划的关键点**：
- 提取可操作的学习要点（而不仅仅是摘要）
- 定义一个具体的 4-8 周任务
- 创建 Rep 1（本周可交付）
- 设计 Reps 2-5（渐进式迭代）
- 将计划保存为 markdown 文件
- 使用格式：`Ship-Learn-Next Plan - [简短任务标题].md`

### 第 4 步：展示结果

向用户展示：
```
✅ Tapestry 工作流程完成！

📥 提取内容：
   ✓ [内容类型]：[标题]
   ✓ 保存到：[filename.txt]
   ✓ [X] 个单词提取

📋 创建行动计划：
   ✓ 任务：[任务标题]
   ✓ 保存到：Ship-Learn-Next Plan - [标题].md

🎯 你的任务：[一句话总结]

📍 Rep 1（本周）：[Rep 1 目标]

你将在何时交付 Rep 1？
```

## 完整 Tapestry 工作流程脚本

```bash
#!/bin/bash

# Tapestry：提取内容 + 创建行动计划
# 使用方法：tapestry <URL>

URL="$1"

if [ -z "$URL" ]; then
    echo "使用方法：tapestry <URL>"
    exit 1
fi

echo "🧵 Tapestry 工作流程开始..."
echo "URL：$URL"
echo ""

# 第 1 步：检测内容类型
if [[ "$URL" =~ youtube\.com/watch || "$URL" =~ youtu\.be/ || "$URL" =~ youtube\.com/shorts ]]; then
    CONTENT_TYPE="youtube"
elif [[ "$URL" =~ \.pdf$ ]] || curl -sI "$URL" | grep -iq "Content-Type: application/pdf"; then
    CONTENT_TYPE="pdf"
else
    CONTENT_TYPE="article"
fi

echo "📍 Detected: $CONTENT_TYPE"
echo ""

# 第 2 步：提取内容
case $CONTENT_TYPE in
    youtube)
        echo "📺 提取 YouTube 脚本..."
        # [YouTube 提取代码见上方]
        ;;

    article)
        echo "📄 提取文章..."
        # [文章提取代码见上方]
        ;;

    pdf)
        echo "📑 下载 PDF..."
        # [PDF 提取代码见上方]
        ;;
esac

echo ""

# 第 3 步：创建行动计划
echo "🚀 创建 Ship-Learn-Next 行动计划..."
# [使用 ship-learn-next 技能创建计划]

echo ""
echo "✅ Tapestry 工作流程完成！"
echo "📥 内容：$CONTENT_FILE"
echo "📋 计划：Ship-Learn-Next Plan - [标题].md"
echo ""
echo "🎯 下一步：查看你的行动计划并交付 Rep 1！"
```

## 错误处理

### 常见问题：

**1. 不支持 URL 类型**
- 尝试文章提取作为后备方案
- 如果失败： "无法从此 URL 类型提取内容"

**2. 未提取内容**
- 检查 URL 是否可访问
- 尝试其他提取方法
- 通知用户："提取失败。URL 可能需要身份验证。"

**3. 工具未安装**
- 当可能时自动安装（yt-dlp、reader、trafilatura）
- 如果自动安装失败，提供安装说明
- 当有后备方案时使用

**4. 空或无效的内容**
- 在创建计划之前验证文件是否有内容
- 如果提取失败，不要创建计划
- 向用户展示预览

## 最佳实践

- ✅ 总是显示检测到的内容 ("📍 Detected: youtube")
- ✅ 显示每个步骤的进度
- ✅ 保存内容文件和计划文件
- ✅ 展示提取内容的预览（前 10 行）
- ✅ 自动创建计划（不要询问）
- ✅ 在结束时展示清晰的摘要
- ✅ 提出承诺问题："你将在何时交付 Rep 1？"

## 使用示例

### 示例 1：YouTube 视频（使用 "tapestry"）

```
用户：tapestry https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude：
🧵 Tapestry 工作流程开始...
📍 Detected: youtube
📺 提取 YouTube 脚本...
✓ 保存脚本：Never Gonna Give You Up.txt

🚀 创建行动计划...
✓ 任务：Master Video Production
✓ 保存计划：Ship-Learn-Next Plan - Master Video Production.md

✅ 完成！你将在何时交付 Rep 1？
```

### 示例 2：文章（使用 "weave"）

```
用户：weave https://example.com/how-to-build-saas

Claude：
🧵 Tapestry 工作流程开始...
📍 Detected: article
📄 提取文章...
✓ 使用 reader（Mozilla Readability）
✓ 保存文章：How to Build a SaaS.txt

🚀 创建行动计划...
✓ 任务：Build a SaaS MVP
✓ 保存计划：Ship-Learn-Next Plan - Build a SaaS MVP.md

✅ 完成！你将在何时交付 Rep 1？
```

### 示例 3：PDF（使用 "help me plan"）

```
用户：help me plan https://example.com/research-paper.pdf

Claude：
🧵 Tapestry 工作流程开始...
📍 Detected: pdf
📑 下载 PDF...
✓ 下载：research-paper.pdf
✓ 提取文本：research-paper.txt

🚀 创建行动计划...
✓ 任务：Apply Research Findings
✓ 保存计划：Ship-Learn-Next Plan - Apply Research Findings.md

✅ 完成！你将在何时交付 Rep 1？
```

## 依赖项

此技能协调其他技能，因此需要：

**对于 YouTube：**
- yt-dlp（自动安装）
- Python 3（用于去重）

**对于文章：**
- reader（npm）OR trafilatura（pip）
- 如果两者都不可用，则回退到基本的 curl

**对于 PDF：**
- curl（内置）
- pdftotext（可选 - 来自 poppler 包）
  - 安装：`brew install poppler`（macOS）
  - 安装：`apt install poppler-utils`（Linux）

**对于规划：**
- 无其他要求（使用内置工具）

## 哲学

**Tapestry 将学习内容编织成行动。**

统一的工作流程确保您不仅消费内容，而且始终创建一个实施计划。这将被动学习转变为主动构建。

提取 → 规划 → 交付 → 学习 → 下一步。

这就是 Tapestry 的方式。