<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>

<p align="center">
  <a href="./README.md">English</a> | 简体中文
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Plugins-33-blue?style=for-the-badge" alt="Plugins">
  <img src="https://img.shields.io/badge/Skills-68-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/Version-v2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>严选实战技能 · 持续更新</em>
</p>

---

**跨越技术分界，普启 AI 赋能**

从自动化工作流到专业内容创作，解锁 AI 的无限可能。

Skillbox 是一个精心整理的 Claude Code 技能合集。我们将相关的技能组合成功能强大的插件，让你的安装和使用更加高效。

---

## 🔗 相关链接

- **Skillbox 官网**: [https://skill-box.zwtj.site/](https://skill-box.zwtj.site/) - 更直观地查看已有技能
- **Skillbox Studio**: [https://github.com/Jst-Well-Dan/Skillbox-Studio](https://github.com/Jst-Well-Dan/Skillbox-Studio) - 可视化管理工具

---

## 插件分类

| 类别 | 说明 | 插件数量 | 包含技能 |
|------|------|:--------:|:--------:|
| **零代码构建** | 不写代码也能完成前端开发、测试与自动化工作流 | 7 | 15 |
| **办公自动化** | Word、Excel、PPT、PDF 统一处理套件 | 3 | 6 |
| **内容流水线** | 网页采集、视频下载、AI内容创作全流程 | 6 | 17 |
| **沉浸式研读** | 深度阅读分析与行动转化 | 3 | 4 |
| **视觉与创意** | 视觉设计、视频制作、Obsidian 可视化与主题美化 | 11 | 19 |
| **品牌与营销** | 品牌规范、内部沟通与抽奖工具 | 3 | 3 |
| **商业分析师** | 数据分析工具包、金融建模与发票识别 | 3 | 6 |

---

## 🌟 核心插件推荐

### 📥 内容采集器 (content-harvester)
> *一站式网页与多媒体资源采集*
- **web-fetch**: 抓取网页内容转成 Markdown
- **advanced-video-downloader**: 下载 YouTube、B站等 1000+ 平台视频
- **youtube-transcript**: 自动提取 YouTube 视频字幕

### 📊 数据分析工具包 (data-analysis-toolkit)
> *从数据清洗到深度洞察*
- **csv-data-summarizer**: CSV 数据一键摘要与可视化
- **excel-pivot-wizard**: 创建高级数据透视表与仪表板
- **excel-variance-analyzer**: 预算与实际差异根因分析

### 📑 办公文档套件 (document-suite)
> *Office 全家桶统一处理*
- **docx / xlsx / pptx / pdf**: 创建、编辑、分析 Word/Excel/PPT/PDF，保留格式。

### 🧠 阅读行动转化 (reading-to-action)
> *将高质量输入转化为实际产出*
- **deep-reading-analyst**: 5 大思维模型深度剖析文章
- **ship-learn-next**: 制定实战型的学习与行动计划

---

## 🚀 快速开始

### 方式一：一键安装（推荐）

在终端运行以下命令，即可安装整个技能库：

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### 方式二：安装特定插件

重构后，你可以更方便地安装功能组合。例如安装办公套件：

```bash
claude plugin add document-suite
```

### 使用技能

插件安装后，Claude 会**自动识别**何时调用相关技能。例如：

- "分析这个 PDF 并总结到 Word" → 自动调用 **document-suite**
- "抓取这个网页并分析其商业模式" → 自动调用 **content-harvester** 和 **data-analysis-toolkit**

---

## 📂 完整列表 (v2.0)

<details>
<summary>点击展开 33 个插件 / 68 个技能详细清单</summary>

### 零代码构建 (No-Code Builder)

#### 1. frontend-builder
> 端到端前端开发：界面设计、Artifacts 构建、最佳实践遵循及项目部署。

**包含技能:**
- `artifacts-builder` - 构建前端artifacts
- `frontend-design` - 前端界面设计
- `react-best-practices` - React最佳实践
- `vercel-deploy` - 部署到Vercel

**来源:** [Anthropic](https://github.com/anthropics/skills) | [Vercel Labs](https://github.com/vercel-labs/agent-skills)

#### 2. testing-toolkit
> 全方位测试工具箱：包含 PICT 测试设计、TDD 方法论、自动测试修复与 E2E 端到端测试。

**包含技能:**
- `pypict` - PICT组合测试 design
- `tdd` - 测试驱动开发
- `test-fixing` - 自动修复测试
- `webapp-testing` - Web应用端到端测试

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) | [obra](https://github.com/obra/superpowers) | [mhattingpete](https://github.com/mhattingpete)

#### 3. dev-workflow
> 优化开发流程：功能头脑风暴、代码提交推送，以及自动生成变更日志。

**包含技能:**
- `changelog-generator` - 自动生成变更日志
- `dev-brainstorming` - 开发头脑风暴
- `git-pushing` - Git提交推送

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills) | [obra](https://github.com/obra/superpowers) | [mhattingpete](https://github.com/mhattingpete/claude-skills-marketplace)

#### 4. skill-creator
> 创建与更新高效 Claude 技能的权威指南。

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 5. mcp-builder
> 创建高质量 MCP (Model Context Protocol) 服务端的开发指南。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 6. developer-growth-analysis
> 从对话历史中深度挖掘编程模式，识别开发者成长空间。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 7. terminal-title
> 根据当前执行的任务，自动更新终端窗口标题。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### 办公自动化 (Office Automation)

#### 8. document-suite
> 全能 Office 办公套件：轻松创建、编辑和分析 Word、Excel、PowerPoint 及 PDF。

**包含技能:**
- `docx` - Word文档处理
- `pdf` - PDF文档处理
- `pptx` - PowerPoint处理
- `xlsx` - Excel表格处理

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 9. markdown-to-epub-converter
> 将 Markdown 文档和对话摘要一键转换为 EPUB 电子书文件。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 10. file-organizer
> 智能文件整理助手：深度理解上下文，自动分类管理文件与文件夹。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### 内容流水线 (Content Pipeline)

#### 11. content-harvester
> 全能内容采集利器：网页抓取、视频下载及 YouTube 字幕快速提取。

**包含技能:**
- `advanced-video-downloader` - 多平台视频下载
- `web-fetch` - 网页抓取转Markdown
- `youtube-transcript` - YouTube字幕提取

**来源:** [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box)

#### 12. content-research-writer
> 辅助撰写高质量内容：涵盖调研、引用文献及段落实时反馈。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 13. baoyu-content-creation-suite
> 全流程内容创作套件：AI 以图生文、多平台发布（小红书/X/微信）、文章配图、幻灯片制作、漫画生成及信息图表。

**包含技能:**
- `xhs-images` - 小红书图片生成
- `post-to-x` - 发布到X平台
- `post-to-wechat` - 发布到微信公众号
- `article-illustrator` - 文章配图
- `cover-image` - 封面图生成
- `slide-deck` - 幻灯片制作
- `comic` - 漫画生成
- `infographic` - 信息图表
- `gemini-web` - Gemini网页搜索
- `image-gen` - AI图片生成

**来源:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

#### 14. baoyu-x-to-markdown
> 将 X (Twitter) 推文高效转换为 Markdown 格式。

**来源:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

#### 15. baoyu-url-to-markdown
> 将网页内容快速转换为 Markdown 格式。

**来源:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

---

### 沉浸式研读 (Immersive Reading)

#### 16. reading-to-action
> 将阅读转化为生产力：多模型深度分析及实战化学习路径。

**包含技能:**
- `deep-reading-analyst` - 5大思维模型深度分析
- `ship-learn-next` - 学习行动计划

**来源:** [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box)

#### 17. notebooklm-integration
> 调用 Google NotebookLM 笔记本，基于原始资料提供有据可查的回答。

**来源:** [PleasePrompto](https://github.com/PleasePrompto/notebooklm-skill)

#### 18. family-history-research
> 助力规划家谱与家族史研究项目。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### 视觉与创意 (Visual Creative)

#### 19. obsidian-visual-suite
> Obsidian 专属视觉增强套件：涵盖 Excalidraw、Mermaid 与 Canvas 画布。

**包含技能:**
- `excalidraw-diagram` - Excalidraw图表
- `mermaid-visualizer` - Mermaid可视化
- `obsidian-canvas-creator` - Obsidian画布

**来源:** [Axton Liu](https://github.com/axtonliu/axton-obsidian-visual-skills)

#### 20. algorithmic-art
> 使用 p5.js 与种子随机数创作富有美感的算法艺术。

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 21. canvas-design
> 创作精美的静态视觉艺术作品与海报。

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 22. image-enhancer
> 图像与截图修补利器：全面提升分辨率与清晰度。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 23. slack-gif-creator
> Slack 专用动图制作工具：专为 Slack 优化的 GIF 创作套件。

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 24. theme-factory
> Artifacts 风格化工厂：内置预设主题，亦可即时定制。

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 25. web-design-guidelines
> 依据 Web 界面设计指南 (WIG) 审核 UI 代码合规性。

**来源:** [Vercel Labs](https://github.com/vercel-labs/agent-skills)

#### 26. baoyu-compress-image
> 批量图像压缩与文件体积优化工具。

**来源:** [Jim Liu (宝玉)](https://github.com/JimLiu/baoyu-skills)

#### 27. remotion-best-practices
> Remotion 视频创作全面指南：基于 React 的视频生产、动画制作、音频处理、字幕添加及 3D 内容构建的 46 项最佳实践。

**来源:** [Remotion](https://github.com/remotion-dev/skills)

---

### 品牌与营销 (Brand Marketing)

#### 28. anthropic-brand-guidelines
> 为任何 Artifact 应用 Anthropic 官方品牌配色与字体规范。

**来源:** [Anthropic](https://github.com/anthropics/skills)

#### 29. internal-comms
> 助力各类内部沟通文案的撰写。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

#### 30. raffle-winner-picker
> 专为赠送、抽奖和竞赛设计的随机中奖者抽取工具。

**来源:** [ComposioHQ](https://github.com/ComposioHQ/awesome-claude-skills)

---

### 商业分析师 (Business Analyst)

#### 31. data-analysis-toolkit
> 全能数据分析工具包：包含 CSV 摘要、透视表及差异分析，提供全方位商业数据洞察。

**包含技能:**
- `csv-data-summarizer` - CSV数据分析与可视化
- `excel-pivot-wizard` - Excel数据透视表
- `excel-variance-analyzer` - 差异分析

**来源:** [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)

#### 32. financial-modeling-suite
> 专业金融建模套件：DCF 估值与 LBO 分析，完美适配投行与企业财务。

**包含技能:**
- `excel-dcf-modeler` - DCF估值模型
- `excel-lbo-modeler` - LBO分析模型

**来源:** [Jeremy Longshore](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)

#### 33. invoice-processor
> 发票自动化处理：利用 AI 视觉将 PDF/图片发票提取至 Excel。

**来源:** [Jst-Well-Dan](https://github.com/Jst-Well-Dan/Skill-Box)

</details>

---

## 支持的平台与配置

Skillbox 中的技能不仅适用于 Claude Code，还支持安装到多种 AI 代理（Agent）中。

**一键配置工具（推荐）**
可以使用 [vercel-labs/add-skill](https://github.com/vercel-labs/add-skill) 提供的脚本进行快速配置，支持交互式选择和自动安装。

**手动路径参考**
如果需要手动安装，请参考下表的路径配置。使用 `-g` 或 `--global` 参数可安装到全局路径。

| Agent 代理 | 项目路径 (Project Path) | 全局路径 (Global Path) |
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

## 贡献与反馈

欢迎提交新插件构想或改进现有技能！

- 发现问题？[提交 Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- 有新想法？[发起 Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- 想要贡献？查看 [技能创建指南](./no-code-builder/skill-creator/SKILL.md)

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by Jst-Well-Dan</em>
</p>
