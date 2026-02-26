---
name: advanced-video-downloader
description: 从YouTube、Bilibili、TikTok和1000+平台下载和转录视频。当用户请求视频下载、转录（字幕提取）或转换视频为文本/Markdown时使用。支持质量选择、音频提取、播放列表下载、基于Cookie的认证和通过SiliconFlow API（免费转录）的AI转录。
---

# Advanced Video Downloader

## 概述

本技能提供从1000+平台（包括YouTube、Bilibili、TikTok、Twitter、Instagram等）的综合视频下载和转录功能。它结合了以下功能：
- **yt-dlp**：强大的视频下载工具
- **SiliconFlow API**：免费AI转录，将视频转换为Markdown

## 何时使用此技能

当用户：
- 明确请求下载视频（“下载这个视频”，“下载视频”）
- 提供任何平台的视频URL
- 提到保存视频以供离线观看
- 希望从视频中提取音频
- 需要下载多个视频或播放列表
- 询问视频质量选项
- 请求视频转录（“转录视频”，“提取字幕”，“视频转文字”）
- 希望在单个工作流程中下载和转录视频

## 核心功能

### 1. 单个视频下载
从任何支持的平台上自动选择质量下载单个视频。

**示例用法：**
```plaintext
用户： "下载这个YouTube视频：https://youtube.com/watch?v=abc123"
用户： "下载这个B站视频：https://bilibili.com/video/BV1xxx"
```

### 2. 批量下载和播放列表下载
一次性下载多个视频或整个播放列表。

**示例用法：**
```plaintext
用户： "下载这个播放列表中的所有视频"
用户： "下载这些3个视频：[URL1]，[URL2]，[URL3]"
```

### 3. 音频提取
仅从视频中提取音频，保存为MP3或M4A。

**示例用法：**
```plaintext
用户： "仅下载这个视频的音频"
用户： "将这个视频转换为MP3"
```

### 4. 质量选择
选择特定的视频质量（4K、1080p、720p等）。

**示例用法：**
```plaintext
用户： "以4K质量下载"
用户： "获取720p版本以节省空间"
```

### 5. 视频音频转录
使用SiliconFlow的免费AI转录API将视频或音频文件转换为Markdown文本。

**示例用法：**
```plaintext
用户： "将这个视频转录为文本" / "转录这个视频"
用户： "下载并转录这个YouTube视频"
用户： "将这个音频转成文字"
用户： "从这个MP4文件中提取字幕"
```

**支持格式：**
- 音频：MP3、WAV、M4A、FLAC、AAC、OGG、OPUS、WMA
- 视频：MP4、AVI、MOV、MKV、FLV、WMV、WEBM、M4V

## 响应模式

当用户请求视频下载时：

### 第1步：识别平台和URL
```python
# 从用户消息中提取视频URL
# 识别平台：YouTube、Bilibili、TikTok等
```

### 第2步：检查工具可用性
```bash
# 检查yt-dlp是否已安装
yt-dlp --version
```

### 第3步：选择适当的yt-dlp命令

根据平台和需求：
- **YouTube、Twitter、Instagram、TikTok**：基本命令有效
- **Bilibili**：基本命令对大多数视频有效
- **质量选择**：使用`-f`与高度过滤器
- **仅音频**：使用`-x --audio-format mp3`
- **播放列表**：使用特定播放列表的输出模板

### 第4步：执行下载

使用yt-dlp直接使用适当的选项：

```bash
# 基本下载（最佳质量MP4）
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "VIDEO_URL"

# 特定质量（1080p）
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --merge-output-format mp4 -o "%(title)s.%(ext)s" "VIDEO_URL"

# 仅音频（MP3）
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "VIDEO_URL"

# 使用cookie文件（用于受保护的内容）
yt-dlp --cookies cookies.txt -o "%(title)s.%(ext)s" "VIDEO_URL"

# 播放列表下载
yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "PLAYLIST_URL"
```

### 第5步：报告结果
下载完成后，报告以下内容：
- ✅ 视频标题和持续时间
- ✅ 文件大小和格式
- ✅ 保存位置
- ✅ 下载速度和时间
- ⚠️ 任何警告或质量限制

**示例输出：**
```plaintext
✅ 下载完成：“视频标题在这里”
   持续时间：15:30
   质量：1080p MP4
   大小：234 MB
   位置：./Video Title Here.mp4
   时间：45秒，5.2 MB/s
```

## 转录响应模式

当用户请求视频/音频转录时：

### 第1步：检查先决条件
```bash
# 验证SiliconFlow API密钥是否可用
echo $SILICONFLOW_API_KEY
# 或用户必须通过--api-key参数提供
```

**API密钥设置：**
- 从：https://cloud.siliconflow.cn/account/ak 获取免费API密钥
- 将`.env.example`复制到`.env`并添加您的API密钥
- 或设置环境变量：`SILICONFLOW_API_KEY=sk-xxx`

### 第2步：验证文件
确保文件存在且是支持的格式（音频或视频）。

### 第3步：执行转录
使用捆绑的脚本`scripts/transcribe_siliconflow.py`：

```bash
# 基本转录
python scripts/transcribe_siliconflow.py --file video.mp4 --api-key sk-xxx

# 使用自定义输出路径
python scripts/transcribe_siliconflow.py --file audio.mp3 --output transcript.md --api-key sk-xxx

# 使用环境变量进行API密钥
python scripts/transcribe_siliconflow.py --file video.mp4
```

### 第4步：报告转录结果
```plaintext
✅ 转录完成！
   文件：video.mp4
   输出：2025-01-15-video.md
   大小：12.5 KB

   预览：
   --------------------------------------------------
   [转录文本的前200个字符...]
   --------------------------------------------------
```

## 组合工作流程：下载 + 转录

对于“下载并转录此视频”之类的请求：

```bash
# 第1步：下载视频
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "VIDEO_URL"

# 第2步：转录下载的文件
python scripts/transcribe_siliconflow.py --file "Downloaded Video Title.mp4" --api-key sk-xxx
```

## 平台特定说明

### YouTube
- 由yt-dlp完全支持
- 公共视频无需身份验证
- 支持所有质量级别，包括4K/8K

### Bilibili
- 由yt-dlp支持
- 高质量下载可能需要登录cookie
- 使用`--cookies`与cookies.txt进行会员专属内容的下载

### 其他平台
- 大多数平台与yt-dlp配合良好
- 查看`references/supported_platforms.md`获取完整的平台列表

## 处理受保护内容的Cookie

对于需要身份验证的平台（Bilibili VIP、会员专属内容等）：

### 方法1：导出Cookie文件（推荐）
```bash
# 使用浏览器扩展“Get cookies.txt LOCALLY”
# 导出cookies.txt，然后：
yt-dlp --cookies cookies.txt "VIDEO_URL"
```

### 方法2：手动Cookie文件
```bash
# 创建Netscape格式的cookies.txt
# 使用浏览器扩展“Get cookies.txt LOCALLY”
# 然后与yt-dlp一起使用
yt-dlp --cookies cookies.txt "VIDEO_URL"
```

## 故障排除

### 问题：视频质量低于预期
**解决方案：**
1. 检查平台是否需要登录才能获得高清
2. 使用`--cookies cookies.txt`进行认证访问
3. 使用`-f`参数明确指定质量

### 问题：下载速度非常慢
**解决方案：**
1. 检查互联网连接
2. 尝试在一天中的不同时间（高峰时段会影响速度）
3. 使用`--concurrent-fragments`进行更快下载

### 问题：“视频不可用”或地理限制
**解决方案：**
1. 视频可能被区域锁定
2. 如果合法允许，使用代理/VPN
3. 检查视频是否仍在平台上可用

### 问题：转录API密钥错误
**解决方案：**
1. 验证API密钥以`sk-`开头
2. 从：https://cloud.siliconflow.cn/account/ak 获取免费密钥
3. 设置环境变量：`SILICONFLOW_API_KEY=sk-xxx`

### 问题：转录返回空文本
**解决方案：**
1. 检查音频/视频是否有清晰的语音
2. 验证文件格式是否受支持
3. 文件可能太短或仅包含音乐

## 常见命令

### 质量预设

```bash
# 4K（2160p）
yt-dlp -f "bestvideo[height<=2160]+bestaudio/best[height<=2160]" --merge-output-format mp4 "VIDEO_URL"

# 1080p（全高清）
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --merge-output-format mp4 "VIDEO_URL"

# 720p（高清）
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4 "VIDEO_URL"

# 480p（标清）
yt-dlp -f "bestvideo[height<=480]+bestaudio/best[height<=480]" --merge-output-format mp4 "VIDEO_URL"
```

### 音频提取

```bash
# 提取为MP3
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "VIDEO_URL"

# 提取为M4A（更好的质量）
yt-dlp -x --audio-format m4a -o "%(title)s.%(ext)s" "VIDEO_URL"
```

### 批量下载

```bash
# 从文件中下载多个URL
yt-dlp -a urls.txt

# 使用自定义命名下载播放列表
yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "PLAYLIST_URL"

# 下载频道的视频
yt-dlp -o "%(uploader)s/%(title)s.%(ext)s" "CHANNEL_URL"
```

## 捆绑资源

### 配置

#### `.env.example`
环境变量的模板。将其复制到`.env`并添加您的SiliconFlow API密钥。

### 脚本

#### `scripts/transcribe_siliconflow.py`
使用SiliconFlow的免费API的AI转录脚本。

**用法：**
```bash
python scripts/transcribe_siliconflow.py --file <audio/video> [--api-key <key>] [--output <path>]
```

**参数：**
- `--file, -f`: 输入音频/视频文件（必需）
- `--api-key, -k`: SiliconFlow API密钥（或使用`SILICONFLOW_API_KEY`环境变量）
- `--output, -o`: 输出Markdown文件路径（默认：`YYYY-MM-DD-filename.md`）
- `--model, -m`: 要使用的模型（默认：`FunAudioLLM/SenseVoiceSmall`）

### 参考

#### `references/supported_platforms.md`
1000+支持平台的完整列表，包括平台特定说明和要求。

#### `references/quality_formats.md`
视频格式、编解码器和质量选择策略的详细说明。

## 优化结果的技巧

1. **始终指定质量，如果用户有偏好** - 节省带宽和存储空间
2. **批量下载节省时间** - 当可能时使用播放列表URL
3. **音频提取更快** - 对于播客/音乐内容推荐
4. **在下载前检查文件大小** - 警告用户非常大（>1GB）的文件
5. **转录对于清晰的音频效果最好** - 考虑首先提取音频以获得更好的结果

## 来源

- [yt-dlp 文档](https://github.com/yt-dlp/yt-dlp)
- [yt-dlp 安装指南](https://github.com/yt-dlp/yt-dlp#installation)
- [SiliconFlow API 文档](https://docs.siliconflow.cn/)
- [SiliconFlow 免费API密钥](https://cloud.siliconflow.cn/account/ak)