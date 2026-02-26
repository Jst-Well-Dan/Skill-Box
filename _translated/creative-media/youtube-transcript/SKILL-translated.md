<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:12:32
翻译模型: glm-4-flash
原文大小: 13,697 字符
-->

---
name: youtube-transcript
description: 当用户提供 YouTube URL 或请求从 YouTube 下载/获取/检索字幕时，下载 YouTube 视频字幕。当用户想要转录或从 YouTube 视频获取字幕时也使用。
allowed-tools: Bash,Read,Write
---

# YouTube 字幕下载器

此技能帮助使用 yt-dlp 从 YouTube 视频下载字幕（字幕/字幕）。

## 何时使用此技能

当用户：
- 提供 YouTube URL 并想要字幕
- 请求“从 YouTube 下载字幕”
- 想要“获取字幕”或“获取字幕”
- 请求“转录 YouTube 视频”
- 需要从 YouTube 视频获取文本内容时
激活此技能

## 工作原理

### 优先顺序：
1. **检查 yt-dlp 是否已安装** - 如有需要则安装
2. **列出可用的字幕** - 看看实际有什么可用
3. **首先尝试手动字幕** (`--write-sub`) - 最高的质量
4. **回退到自动生成** (`--write-auto-sub`) - 通常可用
5. **最后的手段：Whisper 转录** - 如果没有字幕（需要用户确认）
6. **确认下载** 并向用户显示文件保存位置
7. **可选地清理** VTT 格式，如果用户想要纯文本

## 安装检查

**重要**：始终首先检查 yt-dlp 是否已安装：

```bash
which yt-dlp || command -v yt-dlp
```

### 如果未安装

根据系统尝试自动安装：

**macOS (Homebrew)**:
```bash
brew install yt-dlp
```

**Linux (apt/Debian/Ubuntu)**:
```bash
sudo apt update && sudo apt install -y yt-dlp
```

**替代方案（pip - 适用于所有系统）**:
```bash
pip3 install yt-dlp
# 或
python3 -m pip install yt-dlp
```

**如果安装失败**：通知用户他们需要手动安装 yt-dlp 并提供来自 https://github.com/yt-dlp/yt-dlp#installation 的安装说明

## 检查可用的字幕

**始终首先这样做** 在尝试下载之前：

```bash
yt-dlp --list-subs "YOUTUBE_URL"
```

这显示了没有下载任何内容的情况下可用的字幕类型。查找：
- 手动字幕（更好的质量）
- 自动生成字幕（通常可用）
- 可用语言

## 下载策略

### 选项 1：手动字幕（首选）

首先尝试此选项 - 最高的质量，由人类创建：

```bash
yt-dlp --write-sub --skip-download --output "OUTPUT_NAME" "YOUTUBE_URL"
```

### 选项 2：自动生成字幕（回退）

如果手动字幕不可用：

```bash
yt-dlp --write-auto-sub --skip-download --output "OUTPUT_NAME" "YOUTUBE_URL"
```

这两个命令都会创建一个 `.vtt` 文件（WebVTT 字幕格式）。

## 选项 3：Whisper 转录（最后的手段）

**只有当手动和自动生成的字幕都不可用时才使用。**

### 第 1 步：显示文件大小并请求确认

```bash
# 获取音频文件大小估计
yt-dlp --print "%(filesize,filesize_approx)s" -f "bestaudio" "YOUTUBE_URL"

# 或获取持续时间以估计
yt-dlp --print "%(duration)s %(title)s" "YOUTUBE_URL"
```

**重要**：向用户显示文件大小并询问：“没有可用的字幕。我可以下载音频（约 X MB）并使用 Whisper 进行转录。您想继续吗？”

**在继续之前等待用户确认。**

### 第 2 步：检查 Whisper 安装

```bash
command -v whisper
```

如果没有安装，向用户询问：“Whisper 未安装。使用 `pip install openai-whisper` 安装它（需要 ~1-3GB 用于模型）？这是一个一次性安装。”

**在安装之前等待用户确认。**

如果批准安装：
```bash
pip3 install openai-whisper
```

### 第 3 步：仅下载音频

```bash
yt-dlp -x --audio-format mp3 --output "audio_%(id)s.%(ext)s" "YOUTUBE_URL"
```

### 第 4 步：使用 Whisper 转录

```bash
# 自动检测语言（推荐）
whisper audio_VIDEO_ID.mp3 --model base --output_format vtt

# 或指定已知语言
whisper audio_VIDEO_ID.mp3 --model base --language en --output_format vtt
```

**模型选项**（现在坚持使用 `base`）：
- `tiny` - 最快，最不准确 (~1GB)
- `base` - 良好的平衡 (~1GB) ← **使用此选项**
- `small` - 更好的准确性 (~2GB)
- `medium` - 非常好 (~5GB)
- `large` - 最佳准确性 (~10GB)

### 第 5 步：清理

转录完成后，询问用户：“转录完成！您想删除音频文件以节省空间吗？”

如果同意：
```bash
rm audio_VIDEO_ID.mp3
```

## 获取视频信息

### 提取视频标题（用于文件名）

```bash
yt-dlp --print "%(title)s" "YOUTUBE_URL"
```

使用此信息根据视频标题创建有意义的文件名。为文件系统兼容性清理标题：
- 将 `/` 替换为 `-`
- 替换可能引起问题的特殊字符
- 考虑使用清理版本：`$(yt-dlp --print "%(title)s" "URL" | tr '/' '-' | tr ':' '-')`

## 后处理

### 转换为纯文本（推荐）

YouTube 的自动生成 VTT 文件包含 **重复的行**，因为字幕会随着重叠的时间戳逐渐显示。在转换为纯文本时始终去重，同时保留原始的说话顺序。

```bash
python3 -c "
import sys, re
seen = set()
with open('transcript.en.vtt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
            clean = re.sub('<[^>]*>', '', line)
            clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
            if clean and clean not in seen:
                print(clean)
                seen.add(clean)
" > transcript.txt
```

### 使用视频标题完成后处理

```bash
# 获取视频标题
VIDEO_TITLE=$(yt-dlp --print "%(title)s" "YOUTUBE_URL" | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '')

# 查找 VTT 文件
VTT_FILE=$(ls *.vtt | head -n 1)

# 转换并去重
python3 -c "
import sys, re
seen = set()
with open('$VTT_FILE', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
            clean = re.sub('<[^>]*>', '', line)
            clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
            if clean and clean not in seen:
                print(clean)
                seen.add(clean)
" > "${VIDEO_TITLE}.txt"

echo "✓ 保存到：${VIDEO_TITLE}.txt"

# 清理 VTT 文件
rm "$VTT_FILE"
echo "✓ 清理了临时 VTT 文件"
```

## 输出格式

- **VTT 格式** (`.vtt`): 包含时间戳和格式，适用于视频播放器
- **纯文本** (`.txt`): 仅文本内容，适用于阅读或分析

## 小贴士

- 文件名将是 `{output_name}.{language_code}.vtt`（例如，`transcript.en.vtt`）
- 大多数 YouTube 视频都有自动生成的英语字幕
- 一些视频可能有多种语言选项
- 如果自动字幕不可用，尝试 `--write-sub` 以获取手动字幕

## 完整工作流程示例

```bash
VIDEO_URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 获取视频标题用于文件名
VIDEO_TITLE=$(yt-dlp --print "%(title)s" "$VIDEO_URL" | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '')
OUTPUT_NAME="transcript_temp"

# ============================================
# 第 1 步：检查 yt-dlp 是否安装
# ============================================
if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp 未找到，尝试安装..."
    if command -v brew &> /dev/null; then
        brew install yt-dlp
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y yt-dlp
    else
        pip3 install yt-dlp
    fi
fi

# ============================================
# 第 2 步：列出可用的字幕
# ============================================
echo "检查可用的字幕..."
yt-dlp --list-subs "$VIDEO_URL"

# ============================================
# 第 3 步：首先尝试手动字幕
# ============================================
echo "尝试下载手动字幕..."
if yt-dlp --write-sub --skip-download --output "$OUTPUT_NAME" "$VIDEO_URL" 2>/dev/null; then
    echo "✓ 手动字幕下载成功！"
    ls -lh ${OUTPUT_NAME}.*
else
    # ============================================
    # 第 4 步：回退到自动生成
    # ============================================
    echo "手动字幕不可用。尝试自动生成..."
    if yt-dlp --write-auto-sub --skip-download --output "$OUTPUT_NAME" "$VIDEO_URL" 2>/dev/null; then
        echo "✓ 自动生成字幕下载成功！"
        ls -lh ${OUTPUT_NAME}.*
    else
        # ============================================
        # 第 5 步：最后的手段 - Whisper 转录
        # ============================================
        echo "⚠ 此视频没有可用的字幕。"

        # 获取文件大小
        FILE_SIZE=$(yt-dlp --print "%(filesize_approx)s" -f "bestaudio" "$VIDEO_URL")
        DURATION=$(yt-dlp --print "%(duration)s" "$VIDEO_URL")
        TITLE=$(yt-dlp --print "%(title)s" "$VIDEO_URL")

        echo "视频：$TITLE"
        echo "持续时间：$((DURATION / 60)) 分钟"
        echo "音频大小：~$((FILE_SIZE / 1024 / 1024)) MB"
        echo ""
        echo "您想下载并使用 Whisper 进行转录吗？(y/n)"
        read -r RESPONSE

        if [[ "$RESPONSE" =~ ^[Yy]$ ]]; then
            # 检查 Whisper
            if ! command -v whisper &> /dev/null; then
                echo "Whisper 未安装。使用 `pip3 install openai-whisper` 安装它（需要 ~1-3GB）？这是一个一次性安装。"
                read -r INSTALL_RESPONSE
                if [[ "$INSTALL_RESPONSE" =~ ^[Yy]$ ]]; then
                    pip3 install openai-whisper
                else
                    echo "没有 Whisper 无法继续。退出。"
                    exit 1
                fi
            fi

            # 下载音频
            echo "下载音频..."
            yt-dlp -x --audio-format mp3 --output "audio_%(id)s.%(ext)s" "$VIDEO_URL"

            # 获取实际的音频文件名
            AUDIO_FILE=$(ls audio_*.mp3 | head -n 1)

            # 转录
            echo "使用 Whisper 进行转录（这可能需要几分钟）..."
            whisper "$AUDIO_FILE" --model base --output_format vtt

            # 清理
            echo "转录完成！删除音频文件吗？(y/n)"
            read -r CLEANUP_RESPONSE
            if [[ "$CLEANUP_RESPONSE" =~ ^[Yy]$ ]]; then
                rm "$AUDIO_FILE"
                echo "音频文件已删除。"
            fi

            ls -lh *.vtt
        else
            echo "转录已取消。"
            exit 0
        fi
    fi
fi

# ============================================
# 第 6 步：转换为可读的纯文本并去重
# ============================================
VTT_FILE=$(ls ${OUTPUT_NAME}*.vtt 2>/dev/null || ls *.vtt | head -n 1)
if [ -f "$VTT_FILE" ]; then
    echo "转换为可读格式并去除重复项..."
    python3 -c "
import sys, re
seen = set()
with open('$VTT_FILE', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:') and '-->' not in line:
            clean = re.sub('<[^>]*>', '', line)
            clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
            if clean and clean not in seen:
                print(clean)
                seen.add(clean)
" > "${VIDEO_TITLE}.txt"
    echo "✓ 保存到：${VIDEO_TITLE}.txt"

    # 清理临时 VTT 文件
    rm "$VTT_FILE"
    echo "✓ 清理了临时 VTT 文件"
else
    echo "⚠ 未找到 VTT 文件以进行转换"
fi

echo "✓ 完成！"
```

**注意**：此完整工作流程处理所有场景，具有适当的错误检查并在每个决策点进行用户提示。

## 错误处理

### 常见问题和解决方案：

**1. yt-dlp 未安装**
- 根据系统尝试自动安装（Homebrew/apt/pip）
- 如果安装失败，提供手动安装链接
- 在继续之前验证安装

**2. 没有字幕可用**
- 首先列出可用的字幕以确认
- 尝试 `--write-sub` 和 `--write-auto-sub`
- 如果两者都失败，提供 Whisper 转录选项
- 在下载音频之前显示文件大小并请求用户确认

**3. 无效或私有视频**
- 检查 URL 是否为正确格式：`https://www.youtube.com/watch?v=VIDEO_ID`
- 一些视频可能是私有的、受年龄限制或地理封锁
- 通知用户 yt-dlp 的具体错误

**4. Whisper 安装失败**
- 可能需要系统依赖项（ffmpeg，rust）
- 提供替代方案：“手动安装：`pip3 install openai-whisper`”
- 检查可用磁盘空间（模型需要 1-10GB，取决于大小）

**5. 下载中断或失败**
- 检查互联网连接
- 验证有足够的磁盘空间
- 如果出现 SSL 问题，尝试使用 `--no-check-certificate` 再次尝试

**6. 多种字幕语言**
- 默认情况下，yt-dlp 下载所有可用的语言
- 可以使用 `--sub-langs en` 仅指定英语
- 使用 `--list-subs` 首先列出

### 最佳实践：

- ✅ 在尝试下载之前始终检查可用性 (`--list-subs`)
- ✅ 在进行下一步之前验证每个步骤的成功
- ✅ 在大型下载之前请求用户确认（音频文件，Whisper 模型）
- ✅ 在处理完成后清理临时文件
- ✅ 在每个阶段提供清晰的反馈
- ✅ 以有用的消息优雅地处理错误