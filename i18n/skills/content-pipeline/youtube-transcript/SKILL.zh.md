---
name: youtube-transcript
description: 当用户提供 YouTube URL 或要求从 YouTube 下载/获取/抓取字幕时，下载 YouTube 视频字幕。当用户想要转录或从 YouTube 视频中获取字幕/副标题时也适用。
allowed-tools: Bash,Read,Write
---

# YouTube 字幕下载器 (YouTube Transcript Downloader)

此技能帮助用户使用 yt-dlp 从 YouTube 视频中下载字幕（字幕/CC）。

## 何时使用此技能

当用户：
- 提供 YouTube URL 并希望获取字幕
- 请求“从 YouTube 下载字幕”
- 想要“获取字幕”或“获取字幕”
- 请求“转录 YouTube 视频”
- 需要 YouTube 视频的文本内容时
激活此技能

## 工作原理

### 优先顺序：
1. **检查 yt-dlp 是否已安装** - 如果需要则安装
2. **列出可用的字幕** - 查看实际可用内容
3. **首先尝试手动字幕** (`--write-sub`) - 最高质量
4. **回退到自动生成** (`--write-auto-sub`) - 通常可用
5. **最后手段：Whisper 转录** - 如果没有字幕存在（需要用户确认）
6. **确认下载** 并向用户显示文件保存位置
7. **可选** 如果用户想要纯文本，则清理 VTT 格式

## 安装检查

**重要**：始终首先检查 yt-dlp 是否已安装：

```bash
which yt-dlp || command -v yt-dlp
```

### 如果未安装

根据系统尝试自动安装：

**macOS (Homebrew)**：
```bash
brew install yt-dlp
```

**Linux (apt/Debian/Ubuntu)**：
```bash
sudo apt update && sudo apt install -y yt-dlp
```

**替代方案（pip - 在所有系统上均适用）**：
```bash
pip3 install yt-dlp
# 或
python3 -m pip install yt-dlp
```

**如果安装失败**：通知用户他们需要手动安装 yt-dlp 并提供来自 https://github.com/yt-dlp/yt-dlp#installation 的安装说明

## 检查可用字幕

**始终在尝试下载之前这样做**：

```bash
yt-dlp --list-subs "YOUTUBE_URL"
```

这显示没有下载任何内容的情况下可用的字幕类型。查找：
- 手动字幕（更好的质量）
- 自动生成字幕（通常可用）
- 可用语言

## 下载策略

### 选项1：手动字幕（首选）

首先尝试此方法 - 最高质量，由人类创建：

```bash
yt-dlp --write-sub --skip-download --output "OUTPUT_NAME" "YOUTUBE_URL"
```

### 选项2：自动生成字幕（回退）

如果手动字幕不可用：

```bash
yt-dlp --write-auto-sub --skip-download --output "OUTPUT_NAME" "YOUTUBE_URL"
```

这两个命令都会创建一个 `.vtt` 文件（WebVTT字幕格式）。

## 选项3：Whisper转录（最后手段）

**只有当手动和自动生成的字幕都不可用时才使用此选项**。

### 步骤1：显示文件大小并请求确认

```bash
# 获取音频文件大小估计
yt-dlp --print "%(filesize,filesize_approx)s" -f "bestaudio" "YOUTUBE_URL"

# 或获取持续时间以估计
yt-dlp --print "%(duration)s %(title)s" "YOUTUBE_URL"
```

**重要**：向用户显示文件大小并询问：“没有字幕可用。我可以下载音频（大约X MB）并使用Whisper进行转录。您想要继续吗？” 

**在继续之前等待用户确认**。

### 步骤2：检查Whisper安装

```bash
command -v whisper
```

如果没有安装，询问用户：“Whisper未安装。使用 `pip install openai-whisper` 安装它吗？（需要 ~1-3GB 用于模型）？这是一个一次性安装。” 

**在安装之前等待用户确认**。

如果批准，则安装：
```bash
pip3 install openai-whisper
```

### 步骤3：仅下载音频

```bash
yt-dlp -x --audio-format mp3 --output "audio_%(id)s.%(ext)s" "YOUTUBE_URL"
```

### 步骤4：使用Whisper进行转录

```bash
# 自动检测语言（推荐）
whisper audio_VIDEO_ID.mp3 --model base --output_format vtt

# 或指定已知语言
whisper audio_VIDEO_ID.mp3 --model base --language en --output_format vtt
```

**模型选项**（目前坚持使用`base`）：
- `tiny` - 最快，最不精确 (~1GB)
- `base` - 好的平衡 (~1GB) ← **使用此选项**
- `small` - 更好的准确性 (~2GB)
- `medium` - 非常好 (~5GB)
- `large` - 最佳准确性 (~10GB)

### 步骤5：清理

转录完成后，询问用户：“转录完成！您想要删除音频文件以节省空间吗？”

如果回答是：
```bash
rm audio_VIDEO_ID.mp3
```

## 获取视频信息

### 提取视频标题（用于文件名）

```bash
yt-dlp --print "%(title)s" "YOUTUBE_URL"
```

使用此方法根据视频标题创建有意义的文件名。清理标题以兼容文件系统：
- 将 `/` 替换为 `-`
- 替换可能引起问题的特殊字符
- 考虑使用清理后的版本：`$(yt-dlp --print "%(title)s" "URL" | tr '/' '-' | tr ':' '-')`

## 后处理

### 转换为纯文本（推荐）

YouTube自动生成的VTT文件包含**重复行**，因为字幕会随着重叠的时间戳逐个显示。在转换为纯文本时始终删除重复项，同时保留原始说话顺序。

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

### 使用视频标题进行完整后处理

```bash
# 获取视频标题
VIDEO_TITLE=$(yt-dlp --print "%(title)s" "YOUTUBE_URL" | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '')
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

echo "✓ Saved to: ${VIDEO_TITLE}.txt"

# 清理VTT文件
rm "$VTT_FILE"
echo "✓ Cleaned up temporary VTT file"
```

## 输出格式

- **VTT格式** (`.vtt`): 包含时间戳和格式，适用于视频播放器
- **纯文本** (`.txt`): 只包含文本内容，适用于阅读或分析

## 小贴士

- 文件名将是 `{output_name}.{language_code}.vtt`（例如，`transcript.en.vtt`）
- 大多数YouTube视频都有自动生成的英语字幕
- 一些视频可能有多种语言选项
- 如果自动字幕不可用，尝试使用 `--write-sub` 而不是 `--write-auto-sub` 以获取手动字幕

## 完整工作流程示例

```bash
VIDEO_URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 获取视频标题用于文件名
VIDEO_TITLE=$(yt-dlp --print "%(title)s" "$VIDEO_URL" | tr '/' '_' | tr ':' '-' | tr '?' '' | tr '"' '')
OUTPUT_NAME="transcript_temp"

# ============================================
# 第一步：检查yt-dlp是否安装
# ============================================
if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp not found, attempting to install..."
    if command -v brew &> /dev/null; then
        brew install yt-dlp
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y yt-dlp
    else
        pip3 install yt-dlp
    fi
fi

# ============================================
# 第二步：列出可用字幕
# ============================================
echo "Checking available subtitles..."
yt-dlp --list-subs "$VIDEO_URL"

# ============================================
# 第三步：首先尝试手动字幕
# ============================================
echo "Attempting to download manual subtitles..."
if yt-dlp --write-sub --skip-download --output "$OUTPUT_NAME" "$VIDEO_URL" 2>/dev/null; then
    echo "✓ Manual subtitles downloaded successfully!"
    ls -lh ${OUTPUT_NAME}.*
else
    # ============================================
    # 第四步：回退到自动生成
    # ============================================
    echo "Manual subtitles not available. Trying auto-generated..."
    if yt-dlp --write-auto-sub --skip-download --output "$OUTPUT_NAME" "$VIDEO_URL" 2>/dev/null; then
        echo "✓ Auto-generated subtitles downloaded successfully!"
        ls -lh ${OUTPUT_NAME}.*
    else
        # ============================================
        # 第五步：最后手段 - Whisper转录
        # ============================================
        echo "⚠ No subtitles available for this video."

        # 获取文件大小
        FILE_SIZE=$(yt-dlp --print "%(filesize_approx)s" -f "bestaudio" "$VIDEO_URL")
        DURATION=$(yt-dlp --print "%(duration)s" "$VIDEO_URL")
        TITLE=$(yt-dlp --print "%(title)s" "$VIDEO_URL")

        echo "Video: $TITLE"
        echo "Duration: $((DURATION / 60)) minutes"
        echo "Audio size: ~$((FILE_SIZE / 1024 / 1024)) MB"
        echo ""
        echo "Would you like to download and transcribe with Whisper? (y/n)"
        read -r RESPONSE

        if [[ "$RESPONSE" =~ ^[Yy]$ ]]; then
            # 检查Whisper
            if ! command -v whisper &> /dev/null; then
                echo "Whisper not installed. Install now? (requires ~1-3GB) (y/n)"
                read -r INSTALL_RESPONSE
                if [[ "$INSTALL_RESPONSE" =~ ^[Yy]$ ]]; then
                    pip3 install openai-whisper
                else
                    echo "Cannot proceed without Whisper. Exiting."
                    exit 1
                fi
            fi

            # 下载音频
            echo "Downloading audio..."
            yt-dlp -x --audio-format mp3 --output "audio_%(id)s.%(ext)s" "$VIDEO_URL"

            # 获取实际的音频文件名
            AUDIO_FILE=$(ls audio_*.mp3 | head -n 1)

            # 转录
            echo "Transcribing with Whisper (this may take a few minutes)..."
            whisper "$AUDIO_FILE" --model base --output_format vtt

            # 清理
            echo "Transcription complete! Delete audio file? (y/n)"
            read -r CLEANUP_RESPONSE
            if [[ "$CLEANUP_RESPONSE" =~ ^[Yy]$ ]]; then
                rm "$AUDIO_FILE"
                echo "Audio file deleted."
            fi

            ls -lh *.vtt
        else
            echo "Transcription cancelled."
            exit 0
        fi
    fi
fi

# ============================================
# 第六步：转换为可读格式并去除重复项
# ============================================
VTT_FILE=$(ls ${OUTPUT_NAME}*.vtt 2>/dev/null || ls *.vtt | head -n 1)
if [ -f "$VTT_FILE" ]; then
    echo "Converting to readable format and removing duplicates..."
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
    echo "✓ Saved to: ${VIDEO_TITLE}.txt"

    # 清理临时VTT文件
    rm "$VTT_FILE"
    echo "✓ Cleaned up temporary VTT file"
else
    echo "⚠ No VTT file found to convert"
fi

echo "✓ Complete!"
```

**注意**：此完整工作流程处理所有场景，并进行适当的错误检查和在每个决策点上的用户提示。

## 错误处理

### 常见问题和解决方案：

**1. yt-dlp未安装**
- 根据系统尝试自动安装（Homebrew/apt/pip）
- 如果安装失败，提供手动安装链接
- 在继续之前验证安装

**2. 没有字幕可用**
- 首先列出可用的字幕以确认
- 尝试使用 `--write-sub` 和 `--write-auto-sub`
- 如果两者都失败，提供Whisper转录选项
- 在下载音频之前向用户显示文件大小并请求确认

**3. 无效或私有视频**
- 检查URL是否为正确格式：`https://www.youtube.com/watch?v=VIDEO_ID`
- 一些视频可能是私有的、受年龄限制或受地域限制
- 通知用户yt-dlp的具体错误

**4. Whisper安装失败**
- 可能需要系统依赖项（ffmpeg，rust）
- 提供备选方案：“使用 `pip3 install openai-whisper` 手动安装”
- 检查可用磁盘空间（模型需要 1-10GB，取决于大小）

**5. 下载中断或失败**
- 检查互联网连接
- 验证有足够的磁盘空间
- 如果出现SSL问题，尝试使用 `--no-check-certificate` 再次尝试

**6. 多种字幕语言**
- 默认情况下，yt-dlp下载所有可用的语言
- 可以使用 `--sub-langs en` 仅指定英语
- 首先使用 `--list-subs` 列出

### 最佳实践：

- ✅ 在尝试下载之前始终检查可用的内容（`--list-subs`）
- ✅ 在进行下一步之前在每个步骤中验证成功
- ✅ 在进行大型下载之前询问用户（音频文件，Whisper模型）
- ✅ 在处理完成后清理临时文件
- ✅ 在每个阶段提供关于正在发生什么的清晰反馈
- ✅ 以有帮助的消息优雅地处理错误