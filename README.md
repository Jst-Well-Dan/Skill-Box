<p align="center">
  <img src="./_logo/Skillbox-with-words 1.svg" alt="Skillbox Logo" width="600">
</p>


<p align="center">
  <img src="https://img.shields.io/badge/Plugins-33-blue?style=for-the-badge" alt="Plugins">
  <img src="https://img.shields.io/badge/Skills-61-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/Version-v2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>严选实战技能 · 持续更新 · 模块化重构版</em>
</p>

---

**跨越技术分界，普启 AI 赋能**

从自动化工作流到专业内容创作，解锁 AI 的无限可能。

Skillbox 是一个精心整理的 Claude Code 技能合集，并在 v2.0 中完成了**插件化 (Plugin) 重构**。我们将相关的技能组合成功能强大的插件，让你的安装和使用更加高效。

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
| **内容流水线** | 网页采集、视频下载、AI内容创作全流程 | 6 | 18 |
| **沉浸式研读** | 深度阅读分析与行动转化 | 3 | 4 |
| **视觉与创意** | 视觉设计、视频制作、Obsidian 可视化与主题美化 | 9 | 11 |
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
<summary>点击展开 33 个插件 / 61 个技能详细清单</summary>

### 零代码构建 (No-Code Builder)
- **frontend-builder**: `artifacts-builder`, `frontend-design`, `react-best-practices`, `vercel-deploy`
- **testing-toolkit**: `pypict`, `tdd`, `test-fixing`, `webapp-testing`
- **dev-workflow**: `changelog-generator`, `dev-brainstorming`, `git-pushing`
- **skill-creator**: 技能创建指南
- **mcp-builder**: MCP 服务器构建指南
- **developer-growth-analysis**: 编码模式与成长分析
- **terminal-title**: 终端标题自动更新

### 办公自动化 (Office Automation)
- **document-suite**: `docx`, `pdf`, `pptx`, `xlsx`
- **markdown-to-epub-converter**: Markdown 转电子书
- **file-organizer**: 智能文件整理

### 内容流水线 (Content Pipeline)
- **content-harvester**: `video-downloader`, `web-fetch`, `youtube-transcript`
- **content-research-writer**: 研究型写作助手
- **baoyu-content-creation-suite**: `xhs-images`, `post-to-x`, `post-to-wechat`, `article-illustrator`, `cover-image`, `slide-deck`, `comic`, `infographic`, `gemini-web`, `image-gen` (来源: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills))
- **baoyu-x-to-markdown**: X推文转Markdown (来源: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills))
- **baoyu-url-to-markdown**: 网页转Markdown (来源: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills))

### 沉浸式研读 (Immersive Reading)
- **reading-to-action**: `deep-reading`, `ship-learn-next`
- **notebooklm-integration**: Google NotebookLM 集成
- **family-history-research**: 家族史研究规划

### 视觉与创意 (Visual Creative)
- **obsidian-visual-suite**: `excalidraw`, `mermaid`, `obsidian-canvas`
- **algorithmic-art**: 算法艺术创作
- **canvas-design**: 海报与画布设计
- **image-enhancer**: 图片增强与清晰化
- **slack-gif-creator**: Slack 动图制作
- **theme-factory**: 主题工厂（10+ 预设）
- **web-design-guidelines**: 设计规范检查
- **baoyu-compress-image**: 图片批量压缩 (来源: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills))
- **remotion-best-practices**: Remotion视频制作 (46个最佳实践) (来源: [remotion-dev/skills](https://github.com/remotion-dev/skills))

### 品牌与营销 (Brand Marketing)
- **anthropic-brand-guidelines**: Anthropic 品牌设计规范
- **internal-comms**: 内部沟通模板
- **raffle-winner-picker**: 随机抽奖工具

### 商业分析师 (Business Analyst)
- **data-analysis-toolkit**: `csv-summarizer`, `pivot-wizard`, `variance-analyzer`
- **financial-modeling-suite**: `dcf-modeler`, `lbo-modeler`
- **invoice-processor**: 发票识别处理

</details>

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
