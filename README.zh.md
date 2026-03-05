<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>

<p align="center">
  <a href="./README.md">English</a> | 简体中文
</p>

<p align="center">
  <img src="https://img.shields.io/badge/技能-85-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/分类-7-blue?style=for-the-badge" alt="Categories">
  <img src="https://img.shields.io/badge/平台-16+-green?style=for-the-badge" alt="Platforms">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>跨 AI Agent 的技能策展平台 — 跨平台兼容 · 场景驱动 · 持续进化</em>
</p>

---

## Skill Box 是什么？

**Skill Box** 是一个**跨 AI Agent 的技能策展平台**。价值不在于"收集"，而在于**筛选 + 整合 + 降低使用门槛**。

与按底层技术功能罗列技能的仓库不同，Skill Box 围绕**用户角色和真实工作流**组织技能——让你根据"想做什么"来找到所需技能，而非先搞懂"要调哪个 API"。

### 🎯 Skill Box 生态

| 组件 | 定位 | 链接 |
| :--- | :--- | :--- |
| **Skill Box**（本仓库） | 核心内容层 — 策展技能库 | 你在这里 |
| **Skill Box Website** | 展示层 — 可视化浏览技能 | [skill-box.zwtj.site](https://skill-box.zwtj.site/) |
| **Skillbox Studio** | 行动层 — 可视化安装工具 | [GitHub](https://github.com/Jst-Well-Dan/Skillbox-Studio) |

### 💡 为什么选 Skill Box？

- **跨平台兼容**：支持 **16+ AI Agent** — Claude Code、Cursor、Windsurf、Gemini CLI、Amp 等
- **场景化分类**：按"你要做什么"分类，而非按底层功能分类
- **完整工具链**：配套的 Website + Studio 桌面工具，降低非技术用户的使用门槛
- **双层质量标签**：每个技能清晰标注为 `🎖️ Curated`（作者亲测推荐）或 `🌐 Community`（质量合格收录）

---

## 📋 技能分类

| 分类 | 说明 | 技能数 |
| :--- | :--- | :---: |
| **零代码构建 (No-Code Builder)** | 前端开发、测试、DevOps 工作流——无需深度编码 | 18 |
| **办公生产力 (Office & Productivity)** | Word/Excel/PPT/PDF 处理、Notion、Trello 及效率集成 | 10 |
| **内容流水线 (Content Pipeline)** | 网页采集、视频下载、AI 内容创作、TTS 及多平台分发 | 21 |
| **学习与研读 (Learning & Research)** | 深度阅读分析、Obsidian 联动、NotebookLM 及知识管理 | 4 |
| **视觉与创意 (Visual & Creative)** | 视觉设计、图像生成、视频制作、Excalidraw/Mermaid 图表 | 11 |
| **品牌与营销 (Brand & Marketing)** | 品牌规范、内部沟通及互动工具 | 3 |
| **商业分析师 (Business Analyst)** | 数据可视化、金融建模、SEC 研究及发票处理 | 18 |

---

## 🌟 严选工作流 (Curated Workflows)

> *“不再是零散的工具，而是经过作者高频实战验证的专业闭环。”*

### � 投行与商业分析工作流
> *结合 CFA 专业背景实战验证，将耗时的金融建模和财务数据提取自动化*
- **`alpha-vantage` & `edgartools`** — 终端直通美股财报 (10-K/10-Q) 与实时基本面分析
- **`excel-dcf-modeler` & `excel-lbo-modeler`** — 自动构建专业的 DCF（现金流折现）和 LBO（杠杆收购）估值模型
- **`invoice-processor`** — 通过 AI 视觉自动识别 PDF/图片发票，一键整理为 Excel 财务报表

### 📝 深度学习与第二大脑
> *个人知识管理 (PKM) 的核心链路，解决“读完就忘”和“笔记混乱”的痛点*
- **`deep-reading`** — 拒绝简单总结，套用麦肯锡、系统思维等 5 大思维模型对长文进行“逆向工程”
- **`obsidian`** — 通过命令行无缝管理本地 Obsidian 知识库，自动维护双向链接
- **`excalidraw-diagram`** — 将文字逻辑一键转化为 Obsidian 可用的 Excalidraw 架构图和思维导图

### �️ 深度内容采编
> *彻底解决复杂网页与封闭平台的内容抓取难题，高频创作者必备*
- **`web-fetch`** — 经过特殊优化的网页抓取器，完美破除防爬虫限制（完美支持微信公众号长文解析）
- **`advanced-video-downloader`** — 极速下载 YouTube、B站等 1000+ 平台的高质量视频与音频
- **`youtube-transcript`** — 无脑提取视频精准字幕，为你构建庞大的语料加工库

---

## 🚀 快速开始

### 方式一：一键安装（推荐）

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### 方式二：使用 Skillbox Studio

下载 [Skillbox Studio](https://github.com/Jst-Well-Dan/Skillbox-Studio)，享受可视化的点选安装体验。

### 方式三：手动安装

将任意技能文件夹复制到你的 Agent 技能目录即可。具体路径请参考下方的[平台兼容性](#%EF%B8%8F-支持的平台)章节。

### 使用技能

安装后，你的 AI Agent 会**自动识别**何时调用相关技能。例如：

- *"分析这个 PDF 并总结到 Word"* → 自动调用 **docx** + **pdf**
- *"抓取这个网页并分析其商业模式"* → 自动调用 **web-fetch** + **csv-data-summarizer**
- *"下载这个 YouTube 视频并提取字幕"* → 自动调用 **advanced-video-downloader** + **youtube-transcript**

---

## 📂 完整技能清单

<details>
<summary>点击展开 7 大分类 / 85 个技能完整列表</summary>

### 零代码构建 No-Code Builder（18 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `artifacts-builder` | 使用 React、Tailwind、shadcn/ui 构建多组件 HTML Artifacts | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `frontend-design` | 创建独特的生产级前端界面 | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `react-best-practices` | 来自 Vercel 工程团队的 React & Next.js 性能优化 | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 4 | `vercel-deploy` | 应用部署到 Vercel 并获取预览链接 | [Vercel Labs](https://github.com/vercel-labs/agent-skills) |
| 5 | `web-design-guidelines` | UI 代码审查与 Web 界面设计规范合规检查 | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `pypict-claude-skill` | PICT 组合测试用例设计 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `test-driven-development` | TDD 方法论：先写测试，再实现功能 | [obra](https://github.com/obra/superpowers) |
| 8 | `test-fixing` | 智能错误分组，系统性修复所有失败测试 | [mhattingpete](https://github.com/mhattingpete) |
| 9 | `webapp-testing` | 基于 Playwright 的 E2E Web 应用测试 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 10 | `changelog-generator` | 从 Git 提交自动生成变更日志 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 11 | `development-brainstorming` | 协作式技术设计头脑风暴 | [obra](https://github.com/obra/superpowers) |
| 12 | `git-pushing` | 使用 Conventional Commits 规范提交推送 | [mhattingpete](https://github.com/mhattingpete) |
| 13 | `github` | 通过 gh CLI 管理 Issue、PR、CI 及代码审查 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 14 | `skill-creator` | Claude 技能创建与更新指南 | [Anthropic](https://github.com/anthropics/skills) |
| 15 | `mcp-builder` | MCP（Model Context Protocol）服务端构建指南 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 16 | `developer-growth-analysis` | 从对话历史中分析编码模式与成长空间 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 17 | `terminal-title` | 根据当前任务自动更新终端窗口标题 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 18 | `supabase-postgres-best-practices` | 来自 Supabase 的 Postgres 性能优化最佳实践 | [Supabase](https://github.com/supabase/agent-skills) |

---

### 办公生产力 Office & Productivity（10 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `document-skills-docx` | Word 文档创建、编辑、修订跟踪 | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `document-skills-xlsx` | Excel 电子表格处理（含公式） | [Anthropic](https://github.com/anthropics/skills) |
| 3 | `document-skills-pptx` | PowerPoint 演示文稿创建与编辑 | [Anthropic](https://github.com/anthropics/skills) |
| 4 | `document-skills-pdf` | PDF 操作、提取与表单填写 | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `markdown-to-epub-converter` | Markdown 转 EPUB 电子书 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 6 | `file-organizer` | 智能文件整理（基于上下文理解） | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `nano-pdf` | 自然语言直接编辑 PDF（通过 nano-pdf CLI） | [OpenClaw](https://github.com/openclaw/openclaw) |
| 8 | `notion` | Notion 知识库管理集成 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 9 | `trello` | Trello 项目看板管理 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 10 | `weather` | 实时天气查询（无需 API Key） | [OpenClaw](https://github.com/openclaw/openclaw) |

---

### 内容流水线 Content Pipeline（21 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `web-fetch` | 网页内容抓取转 Markdown（含微信公众号支持） | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 2 | `advanced-video-downloader` | 下载 YouTube、B站等 1000+ 平台视频 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 3 | `youtube-transcript` | 提取 YouTube 视频字幕 | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 4 | `content-research-writer` | 基于调研与引用的高质量内容写作 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 5 | `baoyu-xhs-images` | 小红书风格信息图系列生成 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 6 | `baoyu-post-to-x` | 通过 Chrome 自动化发布到 X（Twitter） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 7 | `baoyu-post-to-wechat` | 发布到微信公众号 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 8 | `baoyu-article-illustrator` | AI 文章配图生成 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 9 | `baoyu-cover-image` | 文章封面图生成（20 种风格） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 10 | `baoyu-slide-deck` | 专业幻灯片图片生成 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 11 | `baoyu-comic` | 知识漫画创作（多种画风） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 12 | `baoyu-infographic` | 专业信息图表（20 种布局 × 17 种视觉风格） | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 13 | `baoyu-danger-gemini-web` | 通过 Gemini Web API 生成图文内容 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 14 | `baoyu-image-gen` | 通过 OpenAI/Google 官方 API 生成图片 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 15 | `baoyu-danger-x-to-markdown` | X（Twitter）推文转 Markdown | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 16 | `baoyu-url-to-markdown` | 网页内容转 Markdown | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 17 | `baoyu-compress-image` | 批量图片压缩与优化 | [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) |
| 18 | `openai-whisper-api` | 通过 OpenAI Whisper API 进行语音转文字 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 19 | `sherpa-onnx-tts` | 离线本地文字转语音（无需云 API） | [OpenClaw](https://github.com/openclaw/openclaw) |
| 20 | `summarize` | URL/文件/YouTube 内容摘要提取 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 21 | `xurl` | X (Twitter) CLI 命令行操作与发布 | [OpenClaw](https://github.com/openclaw/openclaw) |

---

### 学习与研读 Learning & Research（4 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `deep-reading` | 5 大思维模型深度分析（麦肯锡、系统思维等） | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 2 | `obsidian` | 通过 CLI 管理 Obsidian 知识库：搜索、创建、链接笔记 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 3 | `notebooklm-integration` | 查询 Google NotebookLM 获取有据可查的回答 | [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) |
| 4 | `family-history-research` | 家谱与家族史研究规划 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |

---

### 视觉与创意 Visual & Creative（11 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `excalidraw-diagram` | 为 Obsidian 生成 Excalidraw 图表 | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 2 | `mermaid-visualizer` | 文本转专业 Mermaid 图表 | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 3 | `obsidian-canvas-creator` | 创建 Obsidian Canvas（思维导图与自由布局） | [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) |
| 4 | `algorithmic-art` | 使用 p5.js 创作生成式算法艺术 | [Anthropic](https://github.com/anthropics/skills) |
| 5 | `canvas-design` | 精美静态视觉艺术与海报创作 | [Anthropic](https://github.com/anthropics/skills) |
| 6 | `image-enhancer` | 图像分辨率与清晰度增强 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 7 | `slack-gif-creator` | Slack 专用动图创作工具 | [Anthropic](https://github.com/anthropics/skills) |
| 8 | `theme-factory` | 预设或自定义主题风格化 Artifacts | [Anthropic](https://github.com/anthropics/skills) |
| 9 | `openai-image-gen` | 通过 OpenAI Images API 批量 AI 图片生成 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 10 | `video-frames` | 通过 ffmpeg 提取视频帧与缩略图 | [OpenClaw](https://github.com/openclaw/openclaw) |
| 11 | `remotion` | 基于 React 的视频创作（46 条最佳实践） | [Remotion](https://github.com/remotion-dev/skills) |

---

### 品牌与营销 Brand & Marketing（3 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `Anthropic-brand-guidelines` | 应用 Anthropic 官方品牌配色与字体规范 | [Anthropic](https://github.com/anthropics/skills) |
| 2 | `internal-comms` | 各类内部沟通文案撰写 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |
| 3 | `raffle-winner-picker` | 抽奖与赠品活动随机中奖者抽取 | [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) |

---

### 商业分析师 Business Analyst（18 个技能）

| # | 技能 | 说明 | 来源 |
| :--- | :--- | :--- | :--- |
| 1 | `csv-data-summarizer` | CSV 数据分析、汇总统计与快速可视化 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 2 | `excel-pivot-wizard` | Excel 数据透视表生成 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 3 | `excel-variance-analyzer` | 差异与偏差分析 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 4 | `excel-dcf-modeler` | DCF 估值金融模型 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 5 | `excel-lbo-modeler` | LBO 杠杆收购分析模型 | [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| 6 | `invoice-processor` | AI 视觉识别 PDF/图片发票提取至 Excel | [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box) |
| 7 | `matplotlib` | 出版级静态图表 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 8 | `seaborn` | 统计数据可视化 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 9 | `plotly` | 交互式图表与仪表盘 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 10 | `geopandas` | 地理空间数据分析与制图 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 11 | `networkx` | 网络/图论分析与可视化 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 12 | `sympy` | 符号数学计算 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 13 | `scientific-visualization` | 综合科学可视化工具包 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 14 | `statistical-analysis` | 标准化 EDA 与统计验证 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 15 | `edgartools` | SEC EDGAR 文件研究（10-K/10-Q/8-K） | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 16 | `alpha-vantage` | 通过 Alpha Vantage API 获取实时行情数据 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 17 | `hedgefundmonitor` | 对冲基金风险监控与分析 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |
| 18 | `usfiscaldata` | 美国财政部财政数据访问 | [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) |

</details>

---

## 🖥️ 支持的平台

Skill Box 技能兼容 **16+ AI Agent**。可使用下方路径表手动安装，或使用一键工具。

**一键配置工具（推荐）：**
使用 [vercel-labs/add-skill](https://github.com/vercel-labs/add-skill) 进行交互式选择与自动安装。

<details>
<summary>点击展开完整平台兼容性列表</summary>

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

## 🤝 贡献与反馈

欢迎提交新技能、改进建议或 Bug 报告——每一份贡献都弥足珍贵。

- 🐛 发现问题？→ [提交 Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- 💡 有新想法？→ [发起 Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- ✍️ 想要贡献？→ 查看[技能创建指南](./no-code-builder/skill-creator/SKILL.md)

---

## 📜 致谢

Skill Box 是站在开源社区巨人肩膀上的产物。特别感谢所有技能作者与来源仓库：

[Anthropic](https://github.com/anthropics/skills) · [Vercel Labs](https://github.com/vercel-labs/agent-skills) · [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills) · [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) · [obra](https://github.com/obra/superpowers) · [K-Dense-AI](https://github.com/K-Dense-AI/claude-scientific-skills) · [OpenClaw](https://github.com/openclaw/openclaw) · [Supabase](https://github.com/supabase/agent-skills) · [Remotion](https://github.com/remotion-dev/skills) · [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills) · [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) · [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill) · [staruhub](https://github.com/staruhub/ClaudeSkills)

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by <a href="https://github.com/Jst-Well-Dan">Jst-Well-Dan</a></em>
</p>
