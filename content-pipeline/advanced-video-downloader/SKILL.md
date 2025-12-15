---
name: advanced-video-downloader
description: Download videos from YouTube, Bilibili, TikTok and 1000+ platforms using yt-dlp. Use when user requests video download, provides video URLs, mentions saving/downloading videos, or needs batch downloads. Supports quality selection, audio extraction, playlist downloads, and cookie-based authentication.
---

# Advanced Video Downloader

## Overview

This skill provides comprehensive video downloading capabilities from 1000+ platforms including YouTube, Bilibili, TikTok, Twitter, Instagram, and more using the powerful yt-dlp tool.

## When to Use This Skill

Activate this skill when the user:
- Explicitly requests to download a video ("download this video", "下载视频")
- Provides video URLs from any platform
- Mentions saving videos for offline viewing
- Wants to extract audio from videos
- Needs to download multiple videos or playlists
- Asks about video quality options

## Core Capabilities

### 1. Single Video Download
Download individual videos from any supported platform with automatic quality selection.

**Example usage:**
```
User: "Download this YouTube video: https://youtube.com/watch?v=abc123"
User: "下载这个B站视频: https://bilibili.com/video/BV1xxx"
```

### 2. Batch & Playlist Download
Download multiple videos or entire playlists at once.

**Example usage:**
```
User: "Download all videos from this playlist"
User: "Download these 3 videos: [URL1], [URL2], [URL3]"
```

### 3. Audio Extraction
Extract audio only from videos, saving as MP3 or M4A.

**Example usage:**
```
User: "Download only the audio from this video"
User: "Convert this video to MP3"
```

### 4. Quality Selection
Choose specific video quality (4K, 1080p, 720p, etc.).

**Example usage:**
```
User: "Download in 4K quality"
User: "Get the 720p version to save space"
```

## Response Pattern

When a user requests video download:

### Step 1: Identify the Platform and URL(s)
```python
# Extract video URL(s) from user message
# Identify platform: YouTube, Bilibili, TikTok, etc.
```

### Step 2: Check Tool Availability
```bash
# Check if yt-dlp is installed
yt-dlp --version
```

### Step 3: Select Appropriate yt-dlp Command

Based on platform and requirements:
- **YouTube, Twitter, Instagram, TikTok**: Basic command works
- **Bilibili**: Basic command works for most videos
- **Quality selection**: Use `-f` with height filter
- **Audio only**: Use `-x --audio-format mp3`
- **Playlists**: Use playlist-specific output template

### Step 4: Execute Download

Use yt-dlp directly with appropriate options:

```bash
# Basic download (best quality MP4)
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "VIDEO_URL"

# Specific quality (1080p)
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --merge-output-format mp4 -o "%(title)s.%(ext)s" "VIDEO_URL"

# Audio only (MP3)
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "VIDEO_URL"

# With cookies file (for protected content)
yt-dlp --cookies cookies.txt -o "%(title)s.%(ext)s" "VIDEO_URL"

# Playlist download
yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "PLAYLIST_URL"
```

### Step 5: Report Results
After download completes, report:
- ✅ Video title and duration
- ✅ File size and format
- ✅ Save location
- ✅ Download speed and time taken
- ⚠️ Any warnings or quality limitations

**Example output:**
```
✅ Downloaded: "Video Title Here"
   Duration: 15:30
   Quality: 1080p MP4
   Size: 234 MB
   Location: ./Video Title Here.mp4
   Time: 45 seconds at 5.2 MB/s
```

## Platform-Specific Notes

### YouTube
- Fully supported by yt-dlp
- No authentication needed for public videos
- Supports all quality levels including 4K/8K

### Bilibili
- Supported by yt-dlp
- High-quality downloads may require login cookies
- Use `--cookies` with cookies.txt for member-only content

### Other Platforms
- Most platforms work well with yt-dlp
- Check `references/supported_platforms.md` for full list

## Handling Cookies for Protected Content

For platforms requiring authentication (Bilibili VIP, member-only content, etc.):

### Method 1: Export Cookies File (Recommended)
```bash
# Use browser extension "Get cookies.txt LOCALLY"
# Export cookies.txt, then:
yt-dlp --cookies cookies.txt "VIDEO_URL"
```

### Method 2: Manual Cookies File
```bash
# Create cookies.txt in Netscape format
# Use browser extension "Get cookies.txt LOCALLY"
# Then use with yt-dlp
yt-dlp --cookies cookies.txt "VIDEO_URL"
```

## Troubleshooting

### Issue: Video quality lower than expected
**Solution:**
1. Check if platform requires login for HD
2. Use `--cookies cookies.txt` for authenticated access
3. Explicitly specify quality with `-f` parameter

### Issue: Download very slow
**Solution:**
1. Check internet connection
2. Try different time of day (peak hours affect speed)
3. Use `--concurrent-fragments` for faster downloads

### Issue: "Video unavailable" or geo-restricted
**Solution:**
1. Video may be region-locked
2. Use proxy/VPN if legally permitted
3. Check if video is still available on platform

## Common Commands

### Quality Presets

```bash
# 4K (2160p)
yt-dlp -f "bestvideo[height<=2160]+bestaudio/best[height<=2160]" --merge-output-format mp4 "VIDEO_URL"

# 1080p (Full HD)
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --merge-output-format mp4 "VIDEO_URL"

# 720p (HD)
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4 "VIDEO_URL"

# 480p (SD)
yt-dlp -f "bestvideo[height<=480]+bestaudio/best[height<=480]" --merge-output-format mp4 "VIDEO_URL"
```

### Audio Extraction

```bash
# Extract as MP3
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "VIDEO_URL"

# Extract as M4A (better quality)
yt-dlp -x --audio-format m4a -o "%(title)s.%(ext)s" "VIDEO_URL"
```

### Batch Downloads

```bash
# Download multiple URLs from file
yt-dlp -a urls.txt

# Download playlist with custom naming
yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "PLAYLIST_URL"

# Download channel's videos
yt-dlp -o "%(uploader)s/%(title)s.%(ext)s" "CHANNEL_URL"
```

## References

### `references/supported_platforms.md`
Comprehensive list of 1000+ supported platforms with platform-specific notes and requirements.

### `references/quality_formats.md`
Detailed explanation of video formats, codecs, and quality selection strategies.

## Tips for Best Results

1. **Always specify quality if user has preference** - saves bandwidth and storage
2. **Batch downloads save time** - use playlist URLs when possible
3. **Audio extraction is faster** - recommend for podcast/music content
4. **Check file size before downloading** - warn user for very large files (>1GB)

## Sources

- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [yt-dlp Installation Guide](https://github.com/yt-dlp/yt-dlp#installation)
