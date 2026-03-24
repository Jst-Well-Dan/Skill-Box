---
name: video-frames
description: 使用 ffmpeg 从视频中提取帧或短视频片段。支持按时间戳截取图片，适用于视频预览和 UI 分析。
homepage: https://ffmpeg.org
metadata:
  {
    "openclaw":
      {
        "emoji": "🎞️",
        "requires": { "bins": ["ffmpeg"] },
        "install":
          [
            {
              "id": "brew",
              "kind": "brew",
              "formula": "ffmpeg",
              "bins": ["ffmpeg"],
              "label": "安装 ffmpeg (brew)",
            },
          ],
      },
  }
---

# 视频帧提取 (Video Frames)

从视频中提取单帧，或创建用于检查的快速缩略图。

## 快速开始

提取第一帧：

```bash
{baseDir}/scripts/frame.sh /path/to/video.mp4 --out /tmp/frame.jpg
```

提取特定时间点的帧：

```bash
{baseDir}/scripts/frame.sh /path/to/video.mp4 --time 00:00:10 --out /tmp/frame-10s.jpg
```

## 注意事项

- 在询问“这里发生了什么？”时，优先使用 `--time` 参数。
- 使用 `.jpg` 格式进行快速共享；使用 `.png` 格式获取高清 UI 帧。
- 此工具依赖 `ffmpeg` 命令行工具。
