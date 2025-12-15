<p align="center">
  <img src="https://img.shields.io/badge/Skills-40+-orange?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

# Skillbox 全域技能库

> **Load Skills, Level Up.** 技能加载实力进阶

<p align="center">
  <em>严选实战技能 · 持续更新</em>
</p>

---

**跨越技术分界，普启 AI 赋能**

从自动化工作流到专业内容创作，解锁 AI 的无限可能。

Skillbox 是一个精心整理的 Claude Code 技能合集，专为**非技术人员**设计。无需编程基础，即装即用，让你的 AI 助手瞬间变身各领域专家。

---

## 技能分区

| 类别 | 说明 | 技能数量 |
|------|------|:--------:|
| **零代码构建** | 不写代码也能创建网页、应用、测试用例 | 12 |
| **办公自动化** | Word、Excel、PPT、PDF 一键处理 | 6 |
| **内容流水线** | 抓取网页、下载视频、提取字幕 | 4 |
| **沉浸式研读** | 深度阅读、会议分析、笔记整理 | 6 |
| **视觉与创意** | 海报设计、GIF 制作、图片增强 | 7 |
| **品牌与营销** | 品牌规范、广告分析、域名创意 | 6 |
| **商业分析师** | 数据分析、CSV 处理、可视化 | 1 |

---

## 热门技能推荐

### 办公自动化
| 技能 | 能帮你做什么 |
|------|-------------|
| **docx** | 创建、编辑 Word 文档，支持批注和修订 |
| **xlsx** | Excel 数据分析，公式计算，图表生成 |
| **pptx** | 制作演示文稿，添加备注和布局 |
| **pdf** | PDF 合并拆分、表单填写、文字提取 |
| **markdown-to-epub** | 把文章转成电子书，可传到 Kindle 阅读 |

### 视觉与创意
| 技能 | 能帮你做什么 |
|------|-------------|
| **canvas-design** | 设计海报、宣传图、PNG/PDF 输出 |
| **slack-gif-creator** | 制作 Slack 表情动图 |
| **theme-factory** | 10 种预设主题，一键美化文档 |
| **image-enhancer** | 截图增强，提升清晰度 |

### 内容流水线
| 技能 | 能帮你做什么 |
|------|-------------|
| **web-fetch** | 抓取网页内容转成 Markdown |
| **youtube-transcript** | 下载 YouTube 视频字幕 |
| **video-downloader** | 下载 YouTube、B站等平台视频 |

### 沉浸式研读
| 技能 | 能帮你做什么 |
|------|-------------|
| **deep-reading-analyst** | 用 5 种思维模型深度分析文章 |
| **meeting-insights** | 分析会议录音，发现沟通问题 |
| **notebooklm** | 连接 Google NotebookLM，引用笔记回答问题 |

### 品牌与营销
| 技能 | 能帮你做什么 |
|------|-------------|
| **domain-name-brainstormer** | 头脑风暴域名创意并检查可用性 |
| **competitive-ads-extractor** | 分析竞争对手广告策略 |
| **raffle-winner-picker** | 从名单中随机抽奖 |

---

## 快速开始

### 方式一：一键安装（推荐）

在终端运行：

```bash
claude plugin install Jst-Well-Dan/Skill-Box
```

### 方式二：本地安装

下载仓库到本地后，运行：

```bash
claude plugin marketplace add ./Skill-Box
```

### 使用技能

技能市场安装后，需要使用/plugin 命令添加技能。
添加技能后，Claude 会**自动识别**何时使用。例如：

- 你说："帮我分析这个 Excel 文件" → 自动使用 **xlsx** 技能
- 你说："把这篇文章做个深度分析" → 自动使用 **deep-reading-analyst** 技能
- 你说："帮我设计一张海报" → 自动使用 **canvas-design** 技能

---

## 目录结构

```
Skillbox/
├── no-code-builder/        # 零代码构建
├── office-automation/      # 办公自动化
├── content-pipeline/       # 内容流水线
├── immersive-reading/      # 沉浸式研读
├── visual-creative/        # 视觉与创意
├── brand-marketing/        # 品牌与营销
├── business-analyst/       # 商业分析师
└── .claude-plugin/
    └── marketplace.json    # 技能注册表
```

---

## 常见问题

### Q: 什么是 Claude Code？
Claude Code 是 Anthropic 推出的命令行 AI 编程助手。虽然名字里有"Code"，但它不只是写代码——它可以帮你处理文档、分析数据、管理文件等各种任务。

### Q: 技能会自动更新吗？
不会。你需要手动 `git pull` 来获取最新技能。

### Q: 我能创建自己的技能吗？
可以！使用 **skill-creator** 技能，它会指导你一步步创建自定义技能。

### Q: 技能安全吗？
本仓库所有技能都经过审核。技能本质上是一组说明文档和脚本，你可以随时查看源码。

---

## 完整技能清单

<details>
<summary>点击展开全部 41 个技能</summary>

### 零代码构建 (no-code-builder)
- **artifacts-builder** - 创建复杂的多组件 HTML 应用
- **changelog-generator** - 从 Git 提交自动生成更新日志
- **developer-growth-analysis** - 分析编码习惯，生成成长报告
- **development-brainstorming** - 软件设计头脑风暴
- **frontend-design** - 创建高质量前端界面
- **git-pushing** - 自动提交和推送代码
- **mcp-builder** - 创建 MCP 服务器集成外部服务
- **pypict-claude-skill** - 使用 PICT 设计测试用例
- **terminal-title** - 自动更新终端窗口标题
- **test-driven-development** - 测试驱动开发指南
- **test-fixing** - 自动修复失败的测试
- **webapp-testing** - 使用 Playwright 测试网页应用

### 办公自动化 (office-automation)
- **docx** - Word 文档创建与编辑
- **xlsx** - Excel 电子表格处理
- **pptx** - PowerPoint 演示文稿制作
- **pdf** - PDF 文档操作
- **file-organizer** - 智能文件整理
- **markdown-to-epub-converter** - Markdown 转电子书

### 内容流水线 (content-pipeline)
- **advanced-video-downloader** - 多平台视频下载
- **content-research-writer** - 内容研究与写作助手
- **web-fetch** - 网页内容抓取
- **youtube-transcript** - YouTube 字幕下载

### 沉浸式研读 (immersive-reading)
- **deep-reading-analyst** - 深度阅读分析框架
- **family-history-research** - 家族历史研究规划
- **meeting-insights-analyzer** - 会议洞察分析
- **notebooklm** - NotebookLM 集成
- **ship-learn-next** - 学习内容转行动计划
- **skill-creator** - 技能创建指南

### 视觉与创意 (visual-creative)
- **algorithmic-art** - 算法艺术创作
- **canvas-design** - 画布设计
- **image-enhancer** - 图片增强
- **slack-gif-creator** - Slack GIF 制作
- **theme-factory** - 主题工厂
- **video-downloader** - 视频下载
- **advanced-video-downloader** - 高级视频下载

### 品牌与营销 (brand-marketing)
- **Anthropic-brand-guidelines** - Anthropic 品牌规范
- **brand-guidelines** - 品牌规范应用
- **competitive-ads-extractor** - 竞品广告分析
- **domain-name-brainstormer** - 域名创意生成
- **internal-comms** - 内部沟通模板
- **raffle-winner-picker** - 随机抽奖

### 商业分析师 (business-analyst)
- **csv-data-summarizer** - CSV 数据分析可视化

</details>

---

## 贡献与反馈

欢迎提交新技能或改进现有技能！

- 发现问题？[提交 Issue](https://github.com/Jst-Well-Dan/Skill-Box/issues)
- 有新想法？[发起 Discussion](https://github.com/Jst-Well-Dan/Skill-Box/discussions)
- 想贡献技能？查看 [技能创建指南](./immersive-reading/skill-creator/SKILL.md)

---

## 致谢

本项目部分技能引用自社区贡献者，感谢以下作者的开源分享：

| 技能 | 作者 | 来源 |
|------|------|------|
| **git-pushing** | mhattingpete | [GitHub](https://github.com/mhattingpete) |
| **test-fixing** | mhattingpete | [GitHub](https://github.com/mhattingpete) |

---

## 许可证

MIT License - 自由使用、修改和分发

---

<p align="center">
  <b>Load Skills, Level Up.</b><br>
  <em>by Jst-Well-Dan</em>
</p>
