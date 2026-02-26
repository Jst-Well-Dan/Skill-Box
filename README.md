<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>

<p align="center">
  English | <a href="./README.zh.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Plugins-33-blue?style=for-the-badge" alt="Plugins">
  <img src="https://img.shields.io/badge/Skills-62-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/Version-v2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>Curated Practical Skills · Continuously Updated · Modular Refactor</em>
</p>

---

**Bridging Technical Divides, Empowering AI for Everyone**

From automated workflows to professional content creation, unlock the infinite possibilities of AI.

Skillbox is a curated collection of skills for Claude Code. We group related skills into powerful plugins to make installation and usage more efficient.

---

## 🔗 Important Links

- **Skillbox Official Site**: [https://skill-box.zwtj.site/](https://skill-box.zwtj.site/) - Browse available skills visually
- **Skillbox Studio**: [https://github.com/Jst-Well-Dan/Skillbox-Studio](https://github.com/Jst-Well-Dan/Skillbox-Studio) - Visual management tool

---

## Plugin Categories

| Category | Description | Plugins | Skills |
|------|------|:--------:|:--------:|
| **No-Code Builder** | Web development, testing, and automation workflows without writing code. | 8 | 17 |
| **Office Automation** | Unified processing suite for Word, Excel, PPT, and PDF. | 3 | 6 |
| **Content Pipeline** | Full workflow for web harvesting, video downloading, and AI content creation. | 5 | 16 |
| **Immersive Reading** | Deep reading analysis and action conversion. | 3 | 4 |
| **Visual & Creative** | Visual design, video production, Obsidian visualization, and theme styling. | 8 | 10 |
| **Brand & Marketing** | Brand guidelines, internal communications, and raffle tools. | 3 | 3 |
| **Business Analyst** | Data analysis toolkit, financial modeling, and invoice recognition. | 3 | 6 |

---

## 🌟 Featured Plugins

### 📥 Content Harvester (content-harvester)
> *One-stop harvesting for web and multi-media resources*
- **web-fetch**: Scrape web content into Markdown.
- **advanced-video-downloader**: Download videos from YouTube, Bilibili, and 1000+ other platforms.
- **youtube-transcript**: Extract YouTube transcripts automatically.

### 📊 Data Analysis Toolkit (data-analysis-toolkit)
> *From data cleaning to deep insights*
- **csv-data-summarizer**: One-click CSV summary and visualization.
- **excel-pivot-wizard**: Create advanced pivot tables and dashboards.
- **excel-variance-analyzer**: Root cause analysis for budget vs. actual variance.

### 📑 Document Suite (document-suite)
> *Unified handling for the entire Office suite*
- **docx / xlsx / pptx / pdf**: Create, edit, and analyze Word/Excel/PPT/PDF while preserving formatting.

### 🧠 Reading to Action (reading-to-action)
> *Transform high-quality input into actual output*
- **deep-reading-analyst**: Deep analysis of articles using 5 major mental models.
- **ship-learn-next**: Develop action-oriented learning and execution plans.

---

## 🚀 Quick Start

### Method 1: One-Click Install (Recommended)

Run the following command in your terminal to install the entire skill library:

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### Method 2: Install Specific Plugins

With the refactored structure, you can easily install functional groups. For example, to install the Office suite:

```bash
claude plugin add document-suite
```

### Using Skills

Once the plugin is installed, Claude will **automatically identify** when to call the relevant skills. For example:

- "Analyze this PDF and summarize it into Word" → Automatically calls **document-suite**
- "Scrape this webpage and analyze its business model" → Automatically calls **content-harvester** and **data-analysis-toolkit**

---

## 📂 Full List (v2.0)

<details>
<summary>Click to expand the detailed list of 33 plugins / 62 skills</summary>

### No-Code Builder

#### 1. frontend-builder
> End-to-end frontend development: design interfaces, build artifacts, follow best practices, and deploy.

**Included Skills:**
- `artifacts-builder` - Building frontend artifacts
- `frontend-design` - Frontend UI design
- `react-best-practices` - React best practices
- `vercel-deploy` - Deployment to Vercel
- `web-design-guidelines` - Web UI design guidelines compliance check

**Source:** [Anthropic](https://github.com/anthropics/skills) | [Vercel Labs](https://github.com/vercel-labs/agent-skills)

#### 2. testing-toolkit
> Complete testing toolkit: PICT design, TDD methodology, automated test fixing, and E2E testing.

**Included Skills:**
- `pypict` - PICT combinatorial test design
- `tdd` - Test Driven Development
- `test-fixing` - Automated test fixing
- `webapp-testing` - Web app end-to-end testing

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) | [obra](https://github.com/obra/superpowers) | [mhattingpete](https://github.com/mhattingpete)

#### 3. dev-workflow
> Streamline development: brainstorm features, push changes, and auto-generate changelogs.

**Included Skills:**
- `changelog-generator` - Automatic changelog generation
- `dev-brainstorming` - Development brainstorming
- `git-pushing` - Git commit and push

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) | [obra](https://github.com/obra/superpowers) | [mhattingpete](https://github.com/mhattingpete/claude-skills-marketplace)

#### 4. skill-creator
> Guide for creating and updating effective Claude skills.

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 5. mcp-builder
> Guide for creating high-quality MCP (Model Context Protocol) servers.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 6. developer-growth-analysis
> Identify coding patterns and growth areas from chat history.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 7. terminal-title
> Automatically updates terminal window title based on current task.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 8. supabase-postgres-best-practices
> Postgres performance optimization and best practices from Supabase: query performance, schema design, connection management, and security.

**Source:** [Supabase](https://github.com/supabase/agent-skills)

---

### Office Automation

#### 8. document-suite
> Complete office document toolkit: create, edit, and analyze Word, Excel, PowerPoint, and PDF.

**Included Skills:**
- `docx` - Word document processing
- `pdf` - PDF document processing
- `pptx` - PowerPoint processing
- `xlsx` - Excel spreadsheet processing

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 9. markdown-to-epub-converter
> Convert markdown documents and chat summaries into EPUB ebook files.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 10. file-organizer
> Intelligently organizes files and folders by understanding context.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### Content Pipeline

#### 11. content-harvester
> Complete content harvesting: scrape webpages, download videos, and extract YouTube transcripts.

**Included Skills:**
- `advanced-video-downloader` - Multi-platform video downloader
- `web-fetch` - Web scraping to Markdown
- `youtube-transcript` - YouTube transcript extraction

**Source:** [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box)

#### 12. content-research-writer
> Assists in writing high-quality content with research, citations, and section feedback.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 13. baoyu-content-creation-suite
> Complete content creation workflow: AI image generation, multi-platform publishing (Xiaohongshu/X/WeChat), article illustrations, slide decks, comics, and infographics.

**Included Skills:**
- `xhs-images` - Xiaohongshu image generation
- `post-to-x` - Post to X (Twitter)
- `post-to-wechat` - Post to WeChat Official Account
- `article-illustrator` - Article illustrations
- `cover-image` - Cover image generation
- `slide-deck` - Slide deck creation
- `comic` - Comic generation
- `infographic` - Infographic creation
- `gemini-web` - Gemini web search
- `image-gen` - AI image generation

**Source:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

#### 14. baoyu-x-to-markdown
> Convert X (Twitter) posts to Markdown format.

**Source:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

#### 15. baoyu-url-to-markdown
> Convert web page content to Markdown format.

**Source:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

---

### Immersive Reading

#### 16. reading-to-action
> Transform reading into results: deep multi-model analysis and actionable learning pathways.

**Included Skills:**
- `deep-reading-analyst` - Deep analysis using 5 mental models
- `ship-learn-next` - Learning action plans

**Source:** [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box)

#### 17. notebooklm-integration
> Query Google NotebookLM notebooks for source-grounded answers.

**Source:** [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill)

#### 18. family-history-research
> Assistance with planning family history and genealogy research projects.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### Visual & Creative

#### 19. obsidian-visual-suite
> Complete visualization toolkit for Obsidian: Excalidraw, Mermaid, and Canvas.

**Included Skills:**
- `excalidraw-diagram` - Excalidraw diagrams
- `mermaid-visualizer` - Mermaid visualization
- `obsidian-canvas-creator` - Obsidian Canvas

**Source:** [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills)

#### 20. algorithmic-art
> Creating algorithmic art using p5.js with seeded randomness.

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 21. canvas-design
> Create beautiful static visual art and posters.

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 22. image-enhancer
> Improves quality of images/screenshots by enhancing resolution and clarity.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 23. slack-gif-creator
> Toolkit for creating animated GIFs optimized for Slack.

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 24. theme-factory
> Toolkit for styling artifacts with preset or on-the-fly themes.

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 25. baoyu-compress-image
> Batch compress images and optimize file sizes.

**Source:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

#### 26. remotion-best-practices
> Comprehensive guide for Remotion video creation: React-based video production, animations, audio, captions, 3D content, and 46 best practices.

**Source:** [Remotion](https://github.com/remotion-dev/skills)

---

### Brand & Marketing

#### 27. anthropic-brand-guidelines
> Applies Anthropic's official brand colors and typography to any sort of artifact.

**Source:** [Anthropic](https://github.com/anthropics/skills)

#### 28. internal-comms
> Resources to help write all kinds of internal communications.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 29. raffle-winner-picker
> Picks random winners for giveaways, raffles, and contests.

**Source:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### Business Analyst

#### 30. data-analysis-toolkit
> Complete data analysis toolkit: CSV summarization, pivot tables, and variance analysis for comprehensive business data insights.

**Included Skills:**
- `csv-data-summarizer` - CSV data analysis and visualization
- `excel-pivot-wizard` - Excel pivot tables
- `excel-variance-analyzer` - Variance analysis

**Source:** [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)

#### 31. financial-modeling-suite
> Professional financial modeling suite for DCF valuation and LBO analysis. Perfect for investment banking and corporate finance.

**Included Skills:**
- `excel-dcf-modeler` - DCF valuation model
- `excel-lbo-modeler` - LBO analysis model

**Source:** [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)

#### 32. invoice-processor
> Automatically process invoices from PDFs/images to Excel using AI vision.

**Source:** [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box)

</details>

---

## Supported Platforms & Configuration

Skillbox skills are not only compatible with Claude Code but can also be installed in various other AI agents.

**One-Click Configuration Tool (Recommended)**
You can use the script provided by [vercel-labs/add-skill](https://github.com/vercel-labs/add-skill) for quick configuration, supporting interactive selection and automatic installation.

**Manual Path Reference**
If manual installation is required, please refer to the path configurations in the table below. Use the `-g` or `--global` flag to install to the global path.

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

---

## Contributions & Feedback

Welcome to submit new plugin ideas or improve existing skills!

- Found a bug? [Submit an Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- Have an idea? [Start a Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- Want to contribute? Check out the [Skill Creation Guide](./no-code-builder/skill-creator/SKILL.md)

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by Jst-Well-Dan</em>
</p>