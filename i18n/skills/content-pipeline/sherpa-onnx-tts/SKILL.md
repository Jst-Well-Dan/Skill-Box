---
name: sherpa-onnx-tts
description: 基于 sherpa-onnx 的本地文本转语音（离线，无需云端）。支持多种语音模型，保护隐私且响应快速。
metadata:
  {
    "openclaw":
      {
        "emoji": "🗣️",
        "os": ["darwin", "linux", "win32"],
        "requires": { "env": ["SHERPA_ONNX_RUNTIME_DIR", "SHERPA_ONNX_MODEL_DIR"] },
        "install":
          [
            {
              "id": "download-runtime-macos",
              "kind": "download",
              "os": ["darwin"],
              "url": "https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-osx-universal2-shared.tar.bz2",
              "archive": "tar.bz2",
              "extract": true,
              "stripComponents": 1,
              "targetDir": "runtime",
              "label": "下载 sherpa-onnx 运行环境 (macOS)",
            },
            {
              "id": "download-runtime-linux-x64",
              "kind": "download",
              "os": ["linux"],
              "url": "https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-linux-x64-shared.tar.bz2",
              "archive": "tar.bz2",
              "extract": true,
              "stripComponents": 1,
              "targetDir": "runtime",
              "label": "下载 sherpa-onnx 运行环境 (Linux x64)",
            },
            {
              "id": "download-runtime-win-x64",
              "kind": "download",
              "os": ["win32"],
              "url": "https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-win-x64-shared.tar.bz2",
              "archive": "tar.bz2",
              "extract": true,
              "stripComponents": 1,
              "targetDir": "runtime",
              "label": "下载 sherpa-onnx 运行环境 (Windows x64)",
            },
            {
              "id": "download-model-lessac",
              "kind": "download",
              "url": "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-high.tar.bz2",
              "archive": "tar.bz2",
              "extract": true,
              "targetDir": "models",
              "label": "下载 Piper en_US lessac 语音模型 (high)",
            },
          ],
      },
  }
---

# sherpa-onnx-tts (本地离线语音合成)

使用 sherpa-onnx 离线命令行工具进行本地 TTS（文本转语音）。

## 安装步骤

1. 下载对应操作系统的运行环境（解压至 `~/.openclaw/tools/sherpa-onnx-tts/runtime`）。
2. 下载语音模型（解压至 `~/.openclaw/tools/sherpa-onnx-tts/models`）。

更新 `~/.openclaw/openclaw.json` 配置：

```json5
{
  skills: {
    entries: {
      "sherpa-onnx-tts": {
        env: {
          SHERPA_ONNX_RUNTIME_DIR: "~/.openclaw/tools/sherpa-onnx-tts/runtime",
          SHERPA_ONNX_MODEL_DIR: "~/.openclaw/tools/sherpa-onnx-tts/models/vits-piper-en_US-lessac-high",
        },
      },
    },
  },
}
```

封装脚本位于本技能文件夹内。可以直接运行，或将其添加至 PATH：

```bash
export PATH="{baseDir}/bin:$PATH"
```

## 使用方法

```bash
{baseDir}/bin/sherpa-onnx-tts -o ./tts.wav "你好，这是来自本地的语音合成。"
```

注意事项：

- 如果需要其他音色，可以从 sherpa-onnx 的 `tts-models` 发布页选择不同的模型。
- 如果模型目录中有多个 `.onnx` 文件，请设置 `SHERPA_ONNX_MODEL_FILE` 环境变量或传递 `--model-file` 参数。
- 您还可以通过 `--tokens-file` 或 `--data-dir` 来覆盖默认设置。
- Windows 用户：请运行 `node {baseDir}\\bin\\sherpa-onnx-tts -o tts.wav "你好内容"`。
