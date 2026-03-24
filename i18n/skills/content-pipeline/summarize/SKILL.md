---
name: summarize
description: 从 URL、播客和本地文件中总结或提取文本/转录（“转录此 YouTube/视频”的绝佳备选方案）。支持多种模型和 API 提供商。
homepage: https://summarize.sh
metadata:
  {
    "openclaw":
      {
        "emoji": "🧾",
        "requires": { "bins": ["summarize"] },
        "install":
          [
            {
              "id": "brew",
              "kind": "brew",
              "formula": "steipete/tap/summarize",
              "bins": ["summarize"],
              "label": "安装 summarize (brew)",
            },
          ],
      },
  }
---

# 内容总结 (Summarize)

快速总结 URL、本地文件和 YouTube 链接的命令行工具。

## 何时使用 (触发短语)

当用户询问以下任何内容时，请立即使用此技能：

- “使用 summarize.sh”
- “这个链接/视频讲了什么？”
- “总结这个 URL/文章”
- “转录这个 YouTube/视频”（尽力提取转录，无需 `yt-dlp`）

## 快速开始

```bash
summarize "https://example.com" --model google/gemini-3-flash-preview
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto
```

## YouTube：总结 vs 转录

尽力转录（仅限 URL）：

```bash
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto --extract-only
```

如果用户要求的转录内容过于庞大，请先返回简要总结，然后询问需要展开哪个章节或时间段。

## 模型与密钥

为所选提供商设置 API 密钥：

- OpenAI: `OPENAI_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`
- xAI: `XAI_API_KEY`
- Google: `GEMINI_API_KEY` (别名: `GOOGLE_GENERATIVE_AI_API_KEY`, `GOOGLE_API_KEY`)

如果未设置，默认模型为 `google/gemini-3-flash-preview`。

## 常用参数

- `--length short|medium|long|xl|xxl|<字符数>` (长度控制)
- `--max-output-tokens <数量>` (最大输出长度)
- `--extract-only` (仅提取内容，不总结 - 仅限 URL)
- `--json` (机器可读格式)
- `--firecrawl auto|off|always` (备用提取方案)
- `--youtube auto` (如果设置了 `APIFY_API_TOKEN`，则使用 Apify 备用)

## 配置信息

可选配置文件：`~/.summarize/config.json`

```json
{ "model": "openai/gpt-5.2" }
```

可选服务：

- `FIRECRAWL_API_KEY` 用于处理屏蔽的网站。
- `APIFY_API_TOKEN` 用于 YouTube 提取备选。
