<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>

<p align="center">
  简体中文 | English
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Skills-78-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/Categories-7-blue?style=for-the-badge" alt="Categories">
  <img src="https://img.shields.io/badge/Platforms-16+-green?style=for-the-badge" alt="Platforms">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>Cross-Agent Skill Curation Platform — Multi-platform Compatible · Scenario-Driven · Continuously Evolving</em>
</p>

---

## What is Skill Box?

**Skill Box** is a **cross-AI Agent skill curation platform**. Its value lies not in "collection," but in **filtering + integration + lowering barriers to entry**.

Unlike repositories that list skills by technical function, Skill Box organizes skills around **user roles and real workflows**—allowing you to find what you need based on "what you want to do," rather than understanding "which API to call."

### 🎯 Skill Box Ecosystem

| Component | Position | Link |
| :--- | :--- | :--- |
| **Skill Box** (This Repo) | Core Content Layer — Curated Skill Library | You are here |
| **Skill Box Website** | Display Layer — Visualized Browsing | [skill-box.zwtj.site](https://skill-box.zwtj.site/) |
| **Skillbox Studio** | Action Layer — Visual Installation Tool | [GitHub](https://github.com/Jst-Well-Dan/Skillbox-Studio) |

### 💡 Why Skill Box?

- **Multi-platform Compatibility**: Supports **16+ AI Agents** — Claude Code, Cursor, Windsurf, Gemini CLI, Amp, etc.
- **Scenario-based Categorization**: Organized by "what you do," not backend functions.
- **Complete Toolchain**: Complementary Website + Studio tools to reduce entry barriers for non-technical users.
- **Dual-layer Quality Tags**: Each skill is clearly marked as `🎖️ Curated` (author-recommended) or `🌐 Community` (quality-verified).

---

## 📋 Categories

| Category | Description | Skills |
| :--- | :--- | :---: |
| **Dev Tools** | Frontend development, testing, DevOps, and AI meta-skills | 11 |
| **Content Pipeline** | Web scraping, video downloading, AI content creation, and publishing | 15 |
| **Obsidian** | Visual suits for Obsidian: Excalidraw, Mermaid, and Canvas | 3 |
| **Productivity** | Document processing (Word/Excel/PDF), Notion, and efficiency tools | 13 |
| **Visual & Creative** | Visual art, image processing, and video creation | 10 |
| **Business Analyst** | Data visualization, financial modeling, and SEC research | 18 |
| **AI Meta** | Skill creation guides and developer growth analysis | 8 |

---

## 🌟 Curated Workflows

> *"Not just scattered tools, but professional closed loops verified by frequency in real-world practice."*

### 📊 Investment Banking & Business Analysis
> *Verified by CFA professional background, automating time-consuming financial modeling and data extraction.*
- **`alpha-vantage` & `edgartools`** — direct access to US SEC filings (10-K/10-Q) and real-time fundamentals.
- **`excel-dcf-modeler` & `excel-lbo-modeler`** — autogenerate professional valuation models.
- **`invoice-processor`** — extract data from PDF/image invoices to Excel via AI vision.

### 📝 Deep Learning & Second Brain
> *Core link for Personal Knowledge Management (PKM), solving the "read and forget" pain point.*
- **`obsidian-toolkit`** — The ultimate Obsidian workflow: CLI, Markdown guides, and automatic Bases views.
- **`excalidraw-diagram`** — Convert text logic into Obsidian-ready Excalidraw diagrams.

### 🎥 Deep Content Harvesting
> *Solve content extraction hurdles on complex web and closed platforms.*
- **`weixin-fetch`** — Optimized WeChat article scraper with anti-bot bypass.
- **`advanced-video-downloader`** — High-speed downloads from YouTube, Bilibili, and 1000+ platforms.
- **`youtube-transcript`** — Extract precise transcripts to build your knowledge base.

---

## 🚀 Quick Start

### Option 1: One-click Install (Recommended)

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### Option 2: Using Skillbox Studio

Download [Skillbox Studio](https://github.com/Jst-Well-Dan/Skillbox-Studio) for a visualized one-click installation experience.

### Option 3: Manual Installation

Copy any skill folder to your Agent's skill directory. Refer to the [Platform Compatibility](#-supported-platforms) section for paths.

### Usage

After installation, your AI Agent will **automatically identify** when to call relevant skills. For example:

- *"Analyze this PDF and summarize to Word"* → calls **docx** + **pdf**
- *"Scrape this page and analyze business model"* → calls **weixin-fetch** + **csv-data-summarizer**
- *"Download this YouTube video and get transcript"* → calls **advanced-video-downloader** + **youtube-transcript**

---

## 📂 Full Skill List

<details>
<summary>Click to expand / 78 skills total</summary>

### Dev Tools (11 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `artifacts-builder` | Build multi-component HTML artifacts with React, Tailwind, shadcn/ui | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `frontend-design` | Create distinctive, production-grade frontend interfaces | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `react-best-practices` | React & Next.js performance optimization from Vercel Engineering | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 4 | `vercel-deploy` | Deploy applications to Vercel with preview URLs | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 5 | `web-design-guidelines` | UI code review for Web Interface Guidelines compliance | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 6 | `changelog-generator` | Auto-generate changelogs from git commits | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `development-brainstorming` | Collaborative technical design brainstorming | [obra](https://github.com/obra/superpowers) |
| 8 | `git-pushing` | Stage, commit, and push with conventional messages | [mhattingpete](https://github.com/mhattingpete) |
| 9 | `github` | GitHub operations via gh CLI: issues, PRs, CI, code review | [OpenClaw](https://github.com/openclaw/openclaw) |
| 10 | `supabase-postgres-best-practices` | Postgres performance optimization from Supabase | [Supabase](https://github.com/supabase/agent-skills) |
| 11 | `md-to-pdf` | Batch convert Markdown to PDF with CJK support and image embedding | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |

---

### Content Pipeline (15 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `weixin-fetch` | Scrape WeChat articles to Markdown with anti-bot bypass | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 2 | `advanced-video-downloader` | Download videos from YouTube, Bilibili, 1000+ platforms | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 3 | `youtube-transcript` | Extract YouTube video transcripts | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 4 | `content-research-writer` | Research-backed content writing with citations | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 5 | `baoyu-post-to-wechat` | Post to WeChat Official Account | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 6 | `baoyu-article-illustrator` | AI article illustration generation | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 7 | `baoyu-cover-image` | Article cover image generation (20 styles) | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 8 | `baoyu-slide-deck` | Professional slide deck image generation | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 9 | `baoyu-comic` | Knowledge comic creation (multiple art styles) | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 10 | `baoyu-infographic` | Professional infographics (20 layouts × 17 styles) | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 11 | `baoyu-image-gen` | Image generation via OpenAI/Google official APIs | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 12 | `openai-whisper-api` | Speech-to-text via OpenAI Whisper API | [OpenClaw](https://github.com/openclaw/openclaw) |
| 13 | `sherpa-onnx-tts` | Offline local text-to-speech (privacy-friendly) | [OpenClaw](https://github.com/openclaw/openclaw) |
| 14 | `summarize` | URL/file/YouTube content summarization | [OpenClaw](https://github.com/openclaw/openclaw) |
| 15 | `jina-cli` | Web content reader and search using Jina AI | [geekjourneyx](https://github.com/geekjourneyx/jina-cli) |

---

### Obsidian (3 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `excalidraw-diagram` | Generate Excalidraw diagrams for Obsidian | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 2 | `mermaid-visualizer` | Transform text into professional Mermaid diagrams | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 3 | `obsidian-canvas-creator` | Create Obsidian Canvas files (MindMap & freeform) | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |

---

### Productivity (13 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `document-skills-docx` | Word document creation, editing, tracked changes | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `document-skills-xlsx` | Excel spreadsheet processing with formulas | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `document-skills-pptx` | PowerPoint creation and editing | [Anthropic](https://github.com/anthropics/skills) |
| 4 | `document-skills-pdf` | PDF manipulation, extraction, and form filling | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `notion` | Notion knowledge management integration | [OpenClaw](https://github.com/openclaw/openclaw) |
| 6 | `trello` | Trello project board management | [OpenClaw](https://github.com/openclaw/openclaw) |
| 7 | `nano-pdf` | Natural language PDF editing via nano-pdf CLI | [OpenClaw](https://github.com/openclaw/openclaw) |
| 8 | `weather` | Real-time weather queries (no API key needed) | [OpenClaw](https://github.com/openclaw/openclaw) |
| 9 | `obsidian-toolkit` | Premium agent toolkit for Obsidian: Markdown, Bases, CLI | [Steph Ango](https://github.com/kepano/obsidian-skills) |
| 10 | `notebooklm-integration` | Query Google NotebookLM for source-grounded answers | [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) |
| 11 | `Anthropic-brand-guidelines` | Apply Anthropic's brand colors and typography | [Anthropic](https://github.com/anthropics/skills) |
| 12 | `raffle-winner-picker` | Random winner selection for giveaways and contests | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 13 | `usfiscaldata` | US Treasury fiscal data access | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |

---

### Visual & Creative (10 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `algorithmic-art` | Generative algorithmic art with p5.js | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `canvas-design` | Beautiful static visual art and poster creation | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `image-enhancer` | Enhance image resolution and clarity | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 4 | `slack-gif-creator` | Animated GIF creation optimized for Slack | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `theme-factory` | Style artifacts with preset or custom themes | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `video-frames` | Video frame and thumbnail extraction via ffmpeg | [OpenClaw](https://github.com/openclaw/openclaw) |
| 7 | `remotion` | React-based video creation with 46 best practices | [Remotion](https://github.com/remotion-dev/skills) |
| 8 | `baoyu-xhs-images` | Xiaohongshu (RedNote) infographic series | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 9 | `baoyu-compress-image` | Batch image compression and optimization | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 10 | `matplotlib` | Publication-quality static charts | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |

---

### Business Analyst (18 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `csv-data-summarizer` | CSV analysis, summary stats, and quick visualizations | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 2 | `excel-pivot-wizard` | Excel pivot table generation | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 3 | `excel-variance-analyzer` | Variance and deviation analysis | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 4 | `excel-dcf-modeler` | DCF valuation financial model | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 5 | `excel-lbo-modeler` | LBO analysis financial model | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 6 | `invoice-processor` | PDF/image invoice extraction to Excel via AI vision | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 7 | `plotly` | Interactive charts and dashboards | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 8 | `seaborn` | Statistical data visualization | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 9 | `geopandas` | Geospatial data analysis and mapping | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 10 | `networkx` | Network/graph analysis and visualization | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 11 | `sympy` | Symbolic mathematics computation | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 12 | `scientific-visualization` | Comprehensive scientific visualization toolkit | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 13 | `statistical-analysis` | Standardized EDA and statistical validation | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 14 | `edgartools` | SEC EDGAR filings research (10-K/10-Q/8-K) | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 15 | `alpha-vantage` | Real-time market data via Alpha Vantage API | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 16 | `hedgefundmonitor` | Hedge fund risk monitoring and analysis | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 17 | `excel-inventory` | Advanced inventory and stock management | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 18 | `financial-report-pro` | Automated financial reporting and summaries | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |

---

### AI Meta (8 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `skill-creator` | Guide for creating effective Claude skills | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `mcp-builder` | Guide for building MCP (Model Context Protocol) servers | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 3 | `developer-growth-analysis` | Identify coding patterns and growth areas from chat history | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 4 | `skill-seekers` | Universal preprocessor to turn docs, repos, and PDFs into AI skills | [Yusuf Karaaslan](https://github.com/yusufkaraaslan/Skill_Seekers) |
| 5 | `prompt-optimizer` | Advanced system prompt engineering & optimization | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `skill-debugger` | Comprehensive tool for debugging complex agent skills | [OpenClaw](https://github.com/openclaw/openclaw) |
| 7 | `context-compressor` | Token-saving context management and compression | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 8 | `token-estimator` | Precise token counting and cost estimation | [Anthropic](https://github.com/anthropics/skills) |

</details>

---

## 🖥️ Supported Platforms

Skill Box is compatible with **16+ AI Agents**. Use the path table below for manual configuration or use one-click tools.

**One-click Configuration (Recommended):**
Use [vercel-labs/add-skill](https://github.com/vercel-labs/add-skill) for interactive selection and automatic setup.

<details>
<summary>Click to expand complete compatibility list</summary>

| AI Agent | Project Path | Global Path |
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

## 🤝 Contribution & Feedback

We welcome new skills, improvement suggestions, or bug reports—every contribution counts.

- 🐛 Found a bug? → [Submit an Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- 💡 Have an idea? → [Start a Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- ✍️ Want to contribute? → Check out the [Skill Creation Guide](./no-code-builder/skill-creator/SKILL.md)

---

## 📜 Acknowledgments

Skill Box stands on the shoulders of the open-source community. Special thanks to all skill authors and source repositories:

[Anthropic](https://github.com/anthropics/skills) · [Vercel Labs](https://github.com/vercel-labs/agent-skills) · [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) · [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) · [obra](https://github.com/obra/superpowers) · [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) · [OpenClaw](https://github.com/openclaw/openclaw) · [Supabase](https://github.com/supabase/agent-skills) · [Remotion](https://github.com/remotion-dev/skills) · [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) · [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) · [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) · [staruhub](https://github.com/staruhub/ClaudeSkills) · [Steph Ango (kepano)](https://github.com/kepano/obsidian-skills) · [Yusuf Karaaslan](https://github.com/yusufkaraaslan/Skill_Seekers)

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by <a href="https://github.com/Jst-Well-Dan">Jst-Well-Dan</a></em>
</p>