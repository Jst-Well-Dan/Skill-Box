---
name: openai-whisper-api
description: 通过 OpenAI 音频转录 API (Whisper) 转录语音。支持多种音频格式，可提供提示以优化转录效果。
homepage: https://platform.openai.com/docs/guides/speech-to-text
metadata:
  {
    "openclaw":
      {
        "emoji": "☁️",
        "requires": { "bins": ["curl"], "env": ["OPENAI_API_KEY"] },
        "primaryEnv": "OPENAI_API_KEY",
      },
  }
---

# OpenAI Whisper API (音频转录)

通过 OpenAI 的 `/v1/audio/transcriptions` 端点转录音频文件。

## 快速开始

```bash
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a
```

默认设置：

- 模型 (Model): `whisper-1`
- 输出 (Output): `<输入文件名>.txt`

## 常用参数

```bash
{baseDir}/scripts/transcribe.sh /path/to/audio.ogg --model whisper-1 --out /tmp/transcript.txt
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --language zh
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --prompt "演讲者姓名：彼得，丹尼尔"
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --json --out /tmp/transcript.json
```

## API 密钥

设置 `OPENAI_API_KEY` 环境变量，或在 `~/.openclaw/openclaw.json` 中配置：

```json5
{
  skills: {
    "openai-whisper-api": {
      apiKey: "在此输入您的 OpenAI 密钥",
    },
  },
}
```
