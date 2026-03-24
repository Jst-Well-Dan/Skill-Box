<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>

<p align="center">
  简体中文 | <a href="./README.en.md">English</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Plugins-39-blue?style=for-the-badge" alt="Plugins">
  <img src="https://img.shields.io/badge/Skills-68-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/分类-8-blue?style=for-the-badge" alt="Categories">
  <img src="https://img.shields.io/badge/平台-16+-green?style=for-the-badge" alt="Platforms">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>跨 AI Agent 的技能策展平台 — 跨平台兼容 · 场景驱动 · 持续进化</em>
</p>

---

## Skill Box 是什么？

**Skill Box** 是一个**跨 AI Agent 的技能策展平台**。它的价值不在于“收集”，而在于**筛选 + 整合 + 降低使用门槛**。

与按技术功能罗列技能的仓库不同，Skill Box 围绕**用户角色和真实工作流**组织技能——让你根据“想做什么”来找到所需技能，而非先搞懂“要调哪个 API”。

### 🎯 Skill Box 生态

| 组件 | 定位 | 链接 |
| :--- | :--- | :--- |
| **Skill Box** (本仓库) | 核心内容层 — 策展技能库 | 你在这里 |
| **Skill Box Website** | 展示层 — 可视化浏览技能 | [skill-box.zwtj.site](https://skill-box.zwtj.site/) |
| **Skillbox Studio** | 行动层 — 可视化安装工具 | [GitHub](https://github.com/Jst-Well-Dan/Skillbox-Studio) |

### 💡 为什么选 Skill Box？

- **跨平台兼容**：支持 **16+ AI Agent** — Claude Code, Cursor, Windsurf, Gemini CLI, Amp 等。
- **场景化分类**：按“你要做什么”分类，而非按底层功能分类。
- **完整工具链**：配套的 Website + Studio 工具，降低非技术用户的使用门槛。
- **双层质量标签**：每个技能清晰标注为 `🎖️ Curated`（作者亲测推荐）或 `🌐 Community`（质量合格收录）。

---

## 📋 技能分类

| 分类 | 说明 | 技能数 |
| :--- | :--- | :---: |
| **开发工具 (Dev Tools)** | 前端开发、测试、DevOps 及 AI 元技能 | 13 |
| **内容流水线 (Content Pipeline)** | 网页采集、视频下载、AI 内容创作及发布 | 16 |
| **Obsidian** | 适配 Obsidian 的视觉套件：Excalidraw、Mermaid 及 Canvas | 3 |
| **办公生产力 (Productivity)** | 文档处理 (Word/Excel/PDF)、Notion 及效率工具 | 13 |
| **视觉与创意 (Visual & Creative)** | 视觉艺术、图像处理及视频创作 | 10 |
| **商业分析师 (Business Analyst)** | 数据分析、财务建模、SEC 研究及发票处理 | 18 |
| **AI 元技能 (AI Meta)** | 技能创建指南及开发者成长分析 | 8 |
| **学习与研究 (Learning & Research)** | 深度阅读、知识管理、研究辅助 | 1 |

---

## 🌟 严选工作流 (Curated Workflows)

> *“不再是零散的工具，而是经过作者高频实战验证的专业闭环。”*

### 🎥 深度内容获取与创作 (Content & Media)
- **`jina-cli` & `content-harvester`** — 网页内容结构化的“眼睛”与视频/微信文章抓取三件套，是内容工程的基础设施。
- **`baoyu-content-creation-suite`** — 宝玉出品的全能创作套件，涵盖小红书、微信配图及各种专业信息图表生成。

### 📊 商业分析与办公自动化 (Business & Productivity)
- **`invoice-processor`** — 自动化发票处理，通过 AI 视觉将 PDF/图片发票批量提取至 Excel，告别手工录入。
- **`document-suite` & `md-to-pdf`** — Anthropic 官方办公全家桶与自建 Markdown 转 PDF 工具，打通文档输出的最后一环。
- **`notebooklm-integration`** — 深度文档分析利器，直接在 Agent 中查询 NotebookLM 笔记，确保回答有据可查。

### 📝 第二大脑与知识管理 (Second Brain)
- **`obsidian-toolkit`** — Obsidian 创始人 kepano 官方出品的权威技能包，涵盖 Markdown 深度编辑与自动化管理。

### 💻 前端开发与 AI 元能力 (Dev & Meta)
- **`anthropic-frontend-design` & `vercel-frontend-suite`** — 官方出品的前端设计与工程化工具，构建高质量 UI 与一键部署的基石。

---

## 🚀 快速开始

### 方式一：一键安装（推荐）

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### 方式二：使用 Skillbox Studio

下载 [Skillbox Studio](https://github.com/Jst-Well-Dan/Skillbox-Studio)，享受可视化的安装体验。

### 方式三：手动安装

将任意技能文件夹复制到你的 Agent 技能目录。确切路径请参考[平台兼容性](#%EF%B8%8F-支持的平台)章节。

### 使用技能

安装后，你的 AI Agent 会**自动识别**何时调用相关技能。例如：

- *"分析这个 PDF 并总结到 Word"* → 自动调用 **docx** + **pdf**
- *"抓取这个网页并分析其商业模式"* → 自动调用 **weixin-fetch** + **csv-data-summarizer**
- *"下载这个 YouTube 视频并提取字幕"* → 自动调用 **advanced-video-downloader** + **youtube-transcript**

---

## 📂 完整技能清单

<details>
<summary>点击展开 8 大分类 / 39 个插件 / 68 个技能完整列表</summary>

### 开发工具 Dev Tools（13 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `artifacts-builder` | 使用 React, Tailwind, shadcn/ui 构建多组件 HTML Artifacts | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `frontend-design` | 创建独特的生产级前端界面 | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `react-best-practices` | 来自 Vercel 工程团队的 React & Next.js 性能优化 | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 4 | `vercel-deploy` | 部署应用到 Vercel 并获取预览链接 | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 5 | `web-design-guidelines` | UI 代码审查，确保符合 Web 界面设计规范 | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 6 | `changelog-generator` | 从 git commit 自动生成变更日志 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `development-brainstorming` | 协作式技术设计头脑风暴 | [obra](https://github.com/obra/superpowers) |
| 8 | `git-pushing` | 使用 Conventional Commits 规范提交并推送 | [mhattingpete](https://github.com/mhattingpete) |
| 9 | `github` | 通过 gh CLI 进行 GitHub 操作：Issue, PR, CI, 代码审查 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 10 | `supabase-postgres-best-practices` | 来自 Supabase 的 Postgres 性能优化最佳实践 | [Supabase](https://github.com/supabase/agent-skills) |
| 11 | `md-to-pdf` | 批量将 Markdown 转为 PDF，支持 CJK 字符和图片嵌入 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 12 | `context7` | Context7 CLI and MCP setup for AI coding skills management. | [Context7](https://github.com/context7/cli) |
| 13 | `gstack` | Fast headless browser for QA testing and site dogfooding. | [Garryslist](https://github.com/gstack/gstack) |

---

### 内容流水线 Content Pipeline（16 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `weixin-fetch` | 抓取微信文章转为 Markdown，含破防爬逻辑 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 2 | `advanced-video-downloader` | 下载 YouTube, B站等 1000+ 平台视频 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 3 | `youtube-transcript` | 提取 YouTube 视频字幕 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 4 | `content-research-writer` | 基于调研且带有引用的高质量内容写作 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 5 | `baoyu-post-to-wechat` | 发布到微信公众号 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 6 | `baoyu-article-illustrator` | AI 文章配图生成 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 7 | `baoyu-cover-image` | 文章封面图生成（20 种风格） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 8 | `baoyu-slide-deck` | 专业幻灯片图片生成 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 9 | `baoyu-comic` | 知识漫画创作（多种画风） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 10 | `baoyu-infographic` | 专业信息图表（20 种布局 × 17 种风格） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 11 | `baoyu-image-gen` | 通过 OpenAI/Google 官方 API 生成图片 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 12 | `openai-whisper-api` | 通过 OpenAI Whisper API 进行语音转文字 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 13 | `sherpa-onnx-tts` | 离线本地文字转语音（保护隐私） | [OpenClaw](https://github.com/openclaw/openclaw) |
| 14 | `summarize` | URL/文件/YouTube 内容摘要提取 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 15 | `jina-cli` | 使用 Jina AI 进行网页内容读取与搜索 | [geekjourneyx](https://github.com/geekjourneyx/jina-cli) |
| 16 | `minimax-tts` | MiniMax TTS API for text-to-speech, voice cloning and voice design. | [MiniMax](https://github.com/minimax/tts) |

---

### Obsidian（3 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `excalidraw-diagram` | 为 Obsidian 生成 Excalidraw 架构图 | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 2 | `mermaid-visualizer` | 将文本转化为专业 Mermaid 图表 | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 3 | `obsidian-canvas-creator` | 创建 Obsidian Canvas 文件（思维导图与自由布局） | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |

---

### 办公生产力 Productivity（13 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `document-skills-docx` | Word 文档创建、编辑、修订跟踪 | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `document-skills-xlsx` | Excel 电子表格处理（含公式） | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `document-skills-pptx` | PowerPoint 演示文稿创建与编辑 | [Anthropic](https://github.com/anthropics/skills) |
| 4 | `document-skills-pdf` | PDF 操作、提取与表单填写 | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `notion` | Notion 知识管理集成 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 6 | `trello` | Trello 项目看板管理 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 7 | `nano-pdf` | 通过 nano-pdf CLI 进行自然语言 PDF 编辑 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 8 | `weather` | 实时天气查询（无需 API key） | [OpenClaw](https://github.com/openclaw/openclaw) |
| 9 | `obsidian-toolkit` | 专家级 Obsidian 工具箱：Markdown, Bases, CLI | [Steph Ango](https://github.com/kepano/obsidian-skills) |
| 10 | `notebooklm-integration` | 查询 Google NotebookLM 以获取有据可查的回答 | [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) |
| 11 | `Anthropic-brand-guidelines` | 应用 Anthropic 品牌色彩与字体规范 | [Anthropic](https://github.com/anthropics/skills) |
| 12 | `raffle-winner-picker` | 抽奖活动随机中奖者抽取 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 13 | `usfiscaldata` | 美国财政部财政数据访问 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |

---

### 视觉与创意 Visual & Creative（10 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `algorithmic-art` | 使用 p5.js 创作生成式算法艺术 | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `canvas-design` | 精美视觉艺术与海报创作 | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `image-enhancer` | 图像分辨率与清晰度增强 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 4 | `slack-gif-creator` | 为 Slack 优化的动图创作 | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `theme-factory` | 预设或自定义主题风格化 Artifacts | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `video-frames` | 通过 ffmpeg 提取视频帧与缩略图 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 7 | `remotion` | 基于 React 的视频创作（46 条最佳实践） | [Remotion](https://github.com/remotion-dev/skills) |
| 8 | `baoyu-xhs-images` | 小红书风格信息图系列生成 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 9 | `baoyu-compress-image` | 批量图片压缩与优化 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 10 | `matplotlib` | 出版级静态图表制作 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |

---

### 商业分析师 Business Analyst（18 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `csv-data-summarizer` | CSV 分析、摘要统计与快速可视化 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 2 | `excel-pivot-wizard` | Excel 数据透视表生成 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 3 | `excel-variance-analyzer` | 差异与偏差分析 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 4 | `excel-dcf-modeler` | DCF（现金流折现）估值金融模型 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 5 | `excel-lbo-modeler` | LBO（杠杆收购）分析金融模型 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 6 | `invoice-processor` | AI 视觉识别 PDF/图片发票提取至 Excel | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 7 | `plotly` | 交互式图表与仪表盘 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 8 | `seaborn` | 统计数据可视化 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 9 | `geopandas` | 地理空间数据分析与制图 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 10 | `networkx` | 网络/图论分析与可视化 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 11 | `sympy` | 符号数学计算 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 12 | `scientific-visualization` | 综合科学可视化工具包 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 13 | `statistical-analysis` | 标准化 EDA 与统计验证 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 14 | `edgartools` | SEC EDGAR 文件研究 (10-K/10-Q/8-K) | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 15 | `alpha-vantage` | 通过 Alpha Vantage API 获取实时行情 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 16 | `hedgefundmonitor` | 对冲基金风险监控与分析 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 17 | `excel-inventory` | 高级库存与存货管理 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 18 | `financial-report-pro` | 自动化财务报告与摘要 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |

---

### AI 元技能 AI Meta（8 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `skill-creator` | 编写高质量 Claude 技能的指南 | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `mcp-builder` | 编写 MCP（Model Context Protocol）服务器的指南 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 3 | `developer-growth-analysis` | 从对话历史中分析编码模式与成长空间 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 4 | `skill-seekers` | 将文档、仓库、PDF 转化为技能的通用预处理器 | [Yusuf Karaaslan](https://github.com/yusufkaraaslan/Skill_Seekers) |
| 5 | `prompt-optimizer` | 高阶系统提示词工程与优化 | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `skill-debugger` | 调试复杂 Agent 技能的综合工具 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 7 | `context-compressor` | 节省 Token 的上下文管理与压缩 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 8 | `token-estimator` | 精确的 Token 计数与成本估算 | [Anthropic](https://github.com/anthropics/skills) |

---

### 学习与研究 Learning & Research（1 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `notebooklm` | Expert guide and tools for Google NotebookLM CLI and MCP server. | [NotebookLM MCP](https://github.com/notebooklm/mcp) |

</details>

---

## 🖥️ 支持的平台

Skill Box 兼容 **16+ AI Agent**。可使用下方路径表手动配置，或使用一键工具。

**一键配置 (推荐):**
使用 [vercel-labs/add-skill](https://github.com/vercel-labs/add-skill) 进行交互式选择与自动安装。

<details>
<summary>点击展开完整兼容性列表</summary>

| AI Agent | 项目路径 | 全局路径 |
| :--- | :--- | :--- |
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` |
| **Trae** | `.trae/skills/` | `~/.trae/skills/` |
| **Gemini CLI** | `.gemini/skills/` | `~/.gemini/skills/` |
| **Roo Code** | `.roo/skills/` | `~/.roo/skills/` |
| **Antigravity** | `.agent/skills/` | `~/.gemini/antigravity/skills/` |
| **OpenClaw** | `skills/` | `~/.OpenClaw/skills/` |
| **Goose** | `.goose/skills/` | `~/.config/goose/skills/` |
| **OpenCode** | `.opencode/skills/` | `~/.config/opencode/skills/` |
| **Kilo Code** | `.kilocode/skills/` | `~/.kilocode/skills/` |
| **Kiro CLI** | `.kiro/skills/` | `~/.kiro/skills/` |
| **Amp** | `.agents/skills/` | `~/.config/agents/skills/` |
| **Codex** | `.codex/skills/` | `~/.codex/skills/` |
| **Droid** | `.factory/skills/` | `~/.factory/skills/` |

</details>

---

## 🤝 贡献与反馈

我们欢迎新技能、改进建议或 Bug 报告——每一份贡献都弥足珍贵。

- 🐛 发现 Bug？→ [提交 Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- 💡 有好主意？→ [发起 Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- ✍️ 想要贡献？→ 查看[技能创建指南](./no-code-builder/skill-creator/SKILL.md)

---

## 📜 致谢

Skill Box 站在开源社区巨人的肩膀上。感谢所有技能作者与来源仓库：

[Anthropic](https://github.com/anthropics/skills) · [Vercel Labs](https://github.com/vercel-labs/agent-skills) · [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) · [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) · [obra](https://github.com/obra/superpowers) · [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) · [OpenClaw](https://github.com/openclaw/openclaw) · [Supabase](https://github.com/supabase/agent-skills) · [Remotion](https://github.com/remotion-dev/skills) · [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) · [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) · [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) · [staruhub](https://github.com/staruhub/ClaudeSkills) · [Steph Ango (kepano)](https://github.com/kepano/obsidian-skills) · [Yusuf Karaaslan](https://github.com/yusufkaraaslan/Skill_Seekers)

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by <a href="https://github.com/Jst-Well-Dan">Jst-Well-Dan</a></em>
</p>