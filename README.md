<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>

<p align="center">
  English | <a href="./README.zh.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Skills-85-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/Categories-7-blue?style=for-the-badge" alt="Categories">
  <img src="https://img.shields.io/badge/Platforms-16+-green?style=for-the-badge" alt="Platforms">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>A Curated Skill Collection for AI Agents — Cross-Platform · Scenario-Driven · Continuously Evolving</em>
</p>

---

## What is Skill Box?

**Skill Box** is a **cross-AI-Agent skill curation platform**. Its value lies not in "collecting", but in **filtering + integrating + lowering the barrier to use**.

Unlike repositories that simply list skills by technical function, Skill Box organizes skills around **user roles and real workflows** — so you find what you need by thinking about *what you want to accomplish*, not *what API to call*.

### 🎯 The Skill Box Ecosystem

| Component | Role | Link |
| :--- | :--- | :--- |
| **Skill Box** (this repo) | Core content layer — the curated skill library | You are here |
| **Skill Box Website** | Discovery layer — browse skills visually | [skill-box.zwtj.site](https://skill-box.zwtj.site/) |
| **Skillbox Studio** | Action layer — visual installation tool | [GitHub](https://github.com/Jst-Well-Dan/Skillbox-Studio) |

### 💡 Why Skill Box?

- **Cross-platform**: Works with **16+ AI Agents** — Claude Code, Cursor, Windsurf, Gemini CLI, Amp, and more
- **Scenario-driven categories**: Organized by what you *do*, not what skills *are*
- **Complete toolchain**: Website + Desktop Studio lower the barrier for non-technical users
- **Quality tiers**: Every skill is clearly labeled as `🎖️ Curated` (author-verified) or `🌐 Community` (quality-checked)

---

## 📋 Skill Categories

| Category | Description | Skills |
| :--- | :--- | :---: |
| **No-Code Builder** | Frontend development, testing, DevOps workflows — build without deep coding | 18 |
| **Office & Productivity** | Word/Excel/PPT/PDF processing, Notion, Trello, and productivity integrations | 10 |
| **Content Pipeline** | Web scraping, video downloading, AI content creation, TTS, and multi-platform publishing | 21 |
| **Learning & Research** | Deep reading analysis, Obsidian integration, NotebookLM, and knowledge management | 4 |
| **Visual & Creative** | Visual design, image generation, video production, Excalidraw/Mermaid diagrams | 11 |
| **Brand & Marketing** | Brand guidelines, internal communications, and engagement tools | 3 |
| **Business Analyst** | Data visualization, financial modeling, SEC research, and invoice processing | 18 |

---

## 🌟 Curated Workflows

> *“Not just atomic tools—these are end-to-end, battle-tested solutions verified in daily practice.”*

### 💼 Investment Banking & Finance
> *Automating time-consuming financial modeling and SEC data extraction.*
- **`alpha-vantage` & `edgartools`** — Terminal-native SEC filings (10-K/10-Q) extraction and fundamental analysis
- **`excel-dcf-modeler` & `excel-lbo-modeler`** — Auto-build professional DCF (Discounted Cash Flow) and LBO (Leveraged Buyout) financial models
- **`invoice-processor`** — AI vision recognition to process PDF/image invoices directly into formatted Excel ledgers

### 📝 Deep Learning & Second Brain
> *The core Personal Knowledge Management (PKM) loop.*
- **`deep-reading`** — Beyond summaries: Reverse-engineer long-form content using 5 mental models (e.g., McKinsey Framework, Systems Thinking)
- **`obsidian`** — Manage your local Obsidian vault via CLI, maintaining bidirectional Wikilinks seamlessly
- **`excalidraw-diagram`** — Instantly transform structural text logic into interactive Obsidian Excalidraw diagrams and mind maps

### 🕸️ Content Harvesting Pipeline
> *Bypassing walled gardens and closed platforms.*
- **`web-fetch`** — Highly optimized scraper that bypasses anti-bot measures (Perfect parsing for WeChat Official Articles)
- **`advanced-video-downloader`** — High-speed video/audio extraction from YouTube, Bilibili, and 1000+ platforms
- **`youtube-transcript`** — Effortlessly extract high-accuracy video transcripts for your text processing corpus

---

## 🚀 Quick Start

### Method 1: One-Click Install (Recommended)

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### Method 2: Use Skillbox Studio

Download [Skillbox Studio](https://github.com/Jst-Well-Dan/Skillbox-Studio) for a visual, point-and-click installation experience.

### Method 3: Manual Installation

Copy any skill folder into your agent's skill directory. See the [Platform Compatibility](#-supported-platforms) section below for paths.

### Using Skills

Once installed, your AI agent will **automatically identify** when to invoke relevant skills. For example:

- *"Analyze this PDF and summarize it into Word"* → Calls **docx** + **pdf**
- *"Scrape this webpage and analyze its business model"* → Calls **web-fetch** + **csv-data-summarizer**
- *"Download this YouTube video and extract the transcript"* → Calls **advanced-video-downloader** + **youtube-transcript**

---

## 📂 Full Skill List

<details>
<summary>Click to expand the complete list of 85 skills across 7 categories</summary>

### No-Code Builder (18 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `artifacts-builder` | Build multi-component HTML artifacts with React, Tailwind, shadcn/ui | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `frontend-design` | Create distinctive, production-grade frontend interfaces | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `react-best-practices` | React & Next.js performance optimization from Vercel Engineering | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 4 | `vercel-deploy` | Deploy applications to Vercel with preview URLs | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 5 | `web-design-guidelines` | UI code review for Web Interface Guidelines compliance | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `pypict-claude-skill` | PICT combinatorial test case design | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `test-driven-development` | TDD methodology: write tests first, then implement | [obra](https://github.com/obra/superpowers) |
| 8 | `test-fixing` | Systematically fix all failing tests with smart error grouping | [mhattingpete](https://github.com/mhattingpete) |
| 9 | `webapp-testing` | E2E web app testing with Playwright | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 10 | `changelog-generator` | Auto-generate changelogs from git commits | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 11 | `development-brainstorming` | Collaborative technical design brainstorming | [obra](https://github.com/obra/superpowers) |
| 12 | `git-pushing` | Stage, commit, and push with conventional messages | [mhattingpete](https://github.com/mhattingpete) |
| 13 | `github` | GitHub operations via gh CLI: issues, PRs, CI, code review | [OpenClaw](https://github.com/openclaw/openclaw) |
| 14 | `skill-creator` | Guide for creating effective Claude skills | [Anthropic](https://github.com/anthropics/skills) |
| 15 | `mcp-builder` | Guide for building MCP (Model Context Protocol) servers | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 16 | `developer-growth-analysis` | Identify coding patterns and growth areas from chat history | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 17 | `terminal-title` | Auto-update terminal window title based on current task | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 18 | `supabase-postgres-best-practices` | Postgres performance optimization from Supabase | [Supabase](https://github.com/supabase/agent-skills) |

---

### Office & Productivity (10 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `document-skills-docx` | Word document creation, editing, tracked changes | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `document-skills-xlsx` | Excel spreadsheet processing with formulas | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `document-skills-pptx` | PowerPoint creation and editing | [Anthropic](https://github.com/anthropics/skills) |
| 4 | `document-skills-pdf` | PDF manipulation, extraction, and form filling | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `markdown-to-epub-converter` | Convert Markdown to EPUB ebook files | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 6 | `file-organizer` | Intelligent file organization by context | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `nano-pdf` | Natural language PDF editing via nano-pdf CLI | [OpenClaw](https://github.com/openclaw/openclaw) |
| 8 | `notion` | Notion knowledge management integration | [OpenClaw](https://github.com/openclaw/openclaw) |
| 9 | `trello` | Trello project board management | [OpenClaw](https://github.com/openclaw/openclaw) |
| 10 | `weather` | Real-time weather queries (no API key needed) | [OpenClaw](https://github.com/openclaw/openclaw) |

---

### Content Pipeline (21 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `web-fetch` | Scrape web content to Markdown (incl. WeChat articles) | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 2 | `advanced-video-downloader` | Download videos from YouTube, Bilibili, 1000+ platforms | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 3 | `youtube-transcript` | Extract YouTube video transcripts | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 4 | `content-research-writer` | Research-backed content writing with citations | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 5 | `baoyu-xhs-images` | Xiaohongshu (RedNote) infographic series | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 6 | `baoyu-post-to-x` | Post to X (Twitter) via Chrome automation | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 7 | `baoyu-post-to-wechat` | Post to WeChat Official Account | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 8 | `baoyu-article-illustrator` | AI article illustration generation | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 9 | `baoyu-cover-image` | Article cover image generation (20 styles) | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 10 | `baoyu-slide-deck` | Professional slide deck image generation | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 11 | `baoyu-comic` | Knowledge comic creation (multiple art styles) | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 12 | `baoyu-infographic` | Professional infographics (20 layouts × 17 styles) | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 13 | `baoyu-danger-gemini-web` | Image & text generation via Gemini Web API | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 14 | `baoyu-image-gen` | Image generation via OpenAI/Google official APIs | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 15 | `baoyu-danger-x-to-markdown` | Convert X (Twitter) posts to Markdown | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 16 | `baoyu-url-to-markdown` | Convert web pages to Markdown | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 17 | `baoyu-compress-image` | Batch image compression and optimization | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 18 | `openai-whisper-api` | Speech-to-text via OpenAI Whisper API | [OpenClaw](https://github.com/openclaw/openclaw) |
| 19 | `sherpa-onnx-tts` | Offline local text-to-speech (privacy-friendly) | [OpenClaw](https://github.com/openclaw/openclaw) |
| 20 | `summarize` | URL/file/YouTube content summarization | [OpenClaw](https://github.com/openclaw/openclaw) |
| 21 | `xurl` | X (Twitter) CLI operations and publishing | [OpenClaw](https://github.com/openclaw/openclaw) |

---

### Learning & Research (4 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `deep-reading` | Deep analysis using 5 mental models (McKinsey, Systems Thinking, etc.) | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 2 | `obsidian` | Manage Obsidian vaults: search, create, link notes via CLI | [OpenClaw](https://github.com/openclaw/openclaw) |
| 3 | `notebooklm-integration` | Query Google NotebookLM for source-grounded answers | [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) |
| 4 | `family-history-research` | Family history and genealogy research planning | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |

---

### Visual & Creative (11 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `excalidraw-diagram` | Generate Excalidraw diagrams for Obsidian | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 2 | `mermaid-visualizer` | Transform text into professional Mermaid diagrams | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 3 | `obsidian-canvas-creator` | Create Obsidian Canvas files (MindMap & freeform) | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 4 | `algorithmic-art` | Generative algorithmic art with p5.js | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `canvas-design` | Beautiful static visual art and poster creation | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `image-enhancer` | Enhance image resolution and clarity | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `slack-gif-creator` | Animated GIF creation optimized for Slack | [Anthropic](https://github.com/anthropics/skills) |
| 8 | `theme-factory` | Style artifacts with preset or custom themes | [Anthropic](https://github.com/anthropics/skills) |
| 9 | `openai-image-gen` | Batch AI image generation via OpenAI Images API | [OpenClaw](https://github.com/openclaw/openclaw) |
| 10 | `video-frames` | Video frame and thumbnail extraction via ffmpeg | [OpenClaw](https://github.com/openclaw/openclaw) |
| 11 | `remotion` | React-based video creation with 46 best practices | [Remotion](https://github.com/remotion-dev/skills) |

---

### Brand & Marketing (3 skills)

| # | Skill | Description | Source |
| :--- | :--- | :--- | :--- |
| 1 | `Anthropic-brand-guidelines` | Apply Anthropic's brand colors and typography | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `internal-comms` | Write various internal communications | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 3 | `raffle-winner-picker` | Random winner selection for giveaways and contests | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |

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
| 7 | `matplotlib` | Publication-quality static charts | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 8 | `seaborn` | Statistical data visualization | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 9 | `plotly` | Interactive charts and dashboards | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 10 | `geopandas` | Geospatial data analysis and mapping | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 11 | `networkx` | Network/graph analysis and visualization | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 12 | `sympy` | Symbolic mathematics computation | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 13 | `scientific-visualization` | Comprehensive scientific visualization toolkit | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 14 | `statistical-analysis` | Standardized EDA and statistical validation | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 15 | `edgartools` | SEC EDGAR filings research (10-K/10-Q/8-K) | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 16 | `alpha-vantage` | Real-time market data via Alpha Vantage API | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 17 | `hedgefundmonitor` | Hedge fund risk monitoring and analysis | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 18 | `usfiscaldata` | US Treasury fiscal data access | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |

</details>

---

## 🖥️ Supported Platforms

Skill Box skills are compatible with **16+ AI Agents**. Use the path table below for manual installation, or try the one-click tool.

**One-Click Configuration Tool (Recommended):**
Use [vercel-labs/add-skill](https://github.com/vercel-labs/add-skill) for interactive selection and automatic installation.

<details>
<summary>Click to expand the full platform compatibility table</summary>

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
| **Clawdbot** | `skills/` | `~/.clawdbot/skills/` |
| **Goose** | `.goose/skills/` | `~/.config/goose/skills/` |
| **OpenCode** | `.opencode/skills/` | `~/.config/opencode/skills/` |
| **Kilo Code** | `.kilocode/skills/` | `~/.kilocode/skills/` |
| **Kiro CLI** | `.kiro/skills/` | `~/.kiro/skills/` |
| **Amp** | `.agents/skills/` | `~/.config/agents/skills/` |
| **Codex** | `.codex/skills/` | `~/.codex/skills/` |
| **Droid** | `.factory/skills/` | `~/.factory/skills/` |

</details>

---

## 🤝 Contributing

We welcome contributions! Whether it's a new skill, an improvement, or a bug report — every bit helps.

- 🐛 Found a bug? → [Submit an Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- 💡 Have an idea? → [Start a Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- ✍️ Want to contribute? → Check out the [Skill Creation Guide](./no-code-builder/skill-creator/SKILL.md)

---

## 📜 Acknowledgements

Skill Box is built on the shoulders of the open-source community. Special thanks to all skill authors and source repositories:

[Anthropic](https://github.com/anthropics/skills) · [Vercel Labs](https://github.com/vercel-labs/agent-skills) · [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) · [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) · [obra](https://github.com/obra/superpowers) · [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) · [OpenClaw](https://github.com/openclaw/openclaw) · [Supabase](https://github.com/supabase/agent-skills) · [Remotion](https://github.com/remotion-dev/skills) · [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) · [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) · [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) · [staruhub](https://github.com/staruhub/ClaudeSkills)

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by <a href="https://github.com/Jst-Well-Dan">Jst-Well-Dan</a></em>
</p>