<h1 align="center">Claude Skills Vault</h1>
<h3 align="center">Claude Skills 精选集</h3>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome" />
  </a>
  <a href="https://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square" alt="License: Apache-2.0" />
  </a>
  <img src="https://img.shields.io/badge/Skills-49-blue?style=flat-square" alt="49 Skills" />
</p>

<p align="center">
一个包含 <strong>49 个精选实用 Claude Skills</strong> 的扩展集合，用于提升 Claude.ai、Claude Code 和 Claude API 的生产力。
</p>

<p align="center">
  <em>基于 <a href="https://github.com/ComposioHQ/awesome-claude-skills">Awesome Claude Skills</a> 扩展，包含更多精选技能</em>
</p>

---

## 📊 快速统计

- **技能总数**: 49
- **分类数量**: 8
- **代码开发**: 11 个编程和开发技能
- **版本协作**: 6 个 Git 和代码审查工具
- **学习研究**: 7 个学习和知识管理工具
- **商务营销**: 7 个商务和营销工具
- **组织方式**: 按内容类型结构化，便于导航
- **特色**: 包含原项目精选技能 + 社区发现的优质扩展

---

## 📖 目录

- [什么是 Claude Skills?](#什么是-claude-skills)
- [项目结构](#项目结构)
- [按类别分类的技能](#按类别分类的技能)
  - [代码开发](#代码开发) (11 个技能)
  - [版本协作](#版本协作) (6 个技能)
  - [Office文档](#office文档) (6 个技能)
  - [内容创作](#内容创作) (3 个技能)
  - [学习研究](#学习研究) (7 个技能)
  - [创意媒体](#创意媒体) (7 个技能)
  - [商务营销](#商务营销) (7 个技能)
  - [数据分析](#数据分析) (2 个技能)
- [其他优秀的 Skills 项目](#其他优秀的-skills-项目)
- [快速开始](#快速开始)
- [安装](#安装)
- [创建技能](#创建技能)
- [贡献](#贡献)
- [资源](#资源)
- [许可证](#许可证)

---

## 什么是 Claude Skills?

Claude Skills 是可定制的工作流程，用于教 Claude 如何根据你的独特需求执行特定任务。Skills 使 Claude 能够在所有 Claude 平台（Claude.ai、Claude Code 和 Claude API）上以可重复、标准化的方式执行任务。

**主要优势：**
- ⚡ **一致性**：每次都以相同的方式执行任务
- 🎯 **专业化**：在特定领域拥有深厚的专业知识
- 🔄 **可重用性**：在不同项目中使用相同的技能
- 📚 **知识**：内置文档和最佳实践
- 🚀 **生产力**：自动化复杂的工作流程

---

## 项目结构

```
claude-skills-vault/
├── .claude-plugin/
│   └── marketplace.json          # 所有 49 个技能的注册表
│
├── business-marketing/            # 商务营销 (7 个技能)
├── collaboration-project-management/  # 版本协作 (部分)
├── communication-writing/         # 内容创作 + 学习研究 (部分)
├── creative-media/                # 创意媒体 (7 个技能)
├── data-analysis/                 # 数据分析 (2 个技能)
├── development/                   # 代码开发 + 版本协作 (部分)
├── document-processing/           # Office文档 (部分)
├── document-skills/               # Office文档 (Office 技能)
├── productivity-organization/     # Office文档 + 学习研究 (部分)
│
├── awesome-skills-showcase/       # Web 展示应用
├── config/                        # 配置文件
├── logs/                          # 日志文件
├── scripts/                       # Python 自动化脚本
│
├── README.md                      # 本文件
└── requirements.txt               # Python 依赖
```

**注**：技能按功能分类（见 marketplace.json），但文件夹结构保持原有组织形式。

---

## 按类别分类的技能

### 代码开发
*11 个软件开发、前端、后端、可视化和测试技能*

- **artifacts-builder** - 使用 React、Tailwind CSS 和 shadcn/ui 构建精美的多组件 Claude.ai HTML artifacts
- **d3js-visualization** - 使用 D3.js 创建交互式数据可视化
- **developer-growth-analysis** - 分析编码模式并识别改进领域
- **mcp-builder** - 为 LLM 集成创建高质量的 MCP（模型上下文协议）服务器
- **move-code-quality-skill** - 分析 Move 语言包的最佳实践和合规性
- **pypict-claude-skill** - 使用成对组合测试设计全面的测试用例
- **template-skill** - 新 Claude Skills 的模板和结构
- **terminal-title** - 自动更新终端窗口标题以反映当前任务
- **test-driven-development** - 先编写测试，观察它们失败，然后编写最少的代码使其通过
- **webapp-testing** - 使用 Playwright 测试 Web 应用程序进行 UI 验证

---

### 版本协作
*6 个 Git 版本控制、代码审查和分支管理技能*

- **changelog-generator** - 通过分析 git 提交历史自动创建面向用户的变更日志
- **finishing-a-development-branch** - 通过结构化工作流选项指导开发工作的完成
- **git-pushing** - 使用常规提交消息暂存、提交和推送 git 更改
- **review-implementing** - 系统地处理和实施代码审查反馈
- **test-fixing** - 运行测试并使用智能错误分组系统地修复所有失败的测试
- **using-git-worktrees** - 为特性开发创建隔离的 git worktrees

---

### Office文档
*6 个 Word、Excel、PowerPoint、PDF 文档处理技能*

- **document-skills-docx** - 创建、编辑和分析 Microsoft Word 文档
- **document-skills-pdf** - 处理 PDF 文档（提取、合并、注释）
- **document-skills-pptx** - 创建和编辑 PowerPoint 演示文稿
- **document-skills-xlsx** - 使用公式和图表操作 Excel 电子表格
- **file-organizer** - 根据上下文智能组织文件并查找重复项
- **markdown-to-epub-converter** - 将 markdown 文档转换为格式化的 EPUB 电子书文件

---

### 内容创作
*3 个写作、头脑风暴和内容提取技能*

- **article-extractor** - 从 URL 提取干净的文章内容，无广告或杂乱信息
- **brainstorming** - 通过协作提问将粗略的想法完善为成熟的设计
- **content-research-writer** - 通过研究、引用和反馈撰写高质量内容

---

### 学习研究
*7 个深度阅读、知识管理和学习工具*

- **deep-reading-analyst** - 使用 10+ 思维模型（SCQA、5W2H、批判性思维等）进行文章深度分析框架
- **family-history-research** - 规划家族史和家谱研究项目
- **meeting-insights-analyzer** - 分析会议记录以获取行为模式和见解
- **notebooklm-integration** - 查询 Google NotebookLM 笔记本以获得基于来源的答案
- **ship-learn-next** - 将学习内容转化为可操作的实施计划
- **skill-creator** - 创建有效 Claude Skills 的指导（适合所有用户）
- **tapestry** - 从 URL 统一提取内容和行动计划

---

### 创意媒体
*7 个图像、视频和设计创作技能*

- **canvas-design** - 使用设计原则创建精美的 PNG 和 PDF 视觉艺术
- **image-enhancer** - 增强专业演示的图像质量和分辨率
- **slack-gif-creator** - 创建针对 Slack 优化的动画 GIF
- **theme-factory** - 为 artifacts 应用专业字体和颜色主题
- **video-downloader** - 从 YouTube 和其他平台下载视频
- **youtube-transcript** - 下载 YouTube 视频转录和字幕

---

### 商务营销
*7 个商业运营、营销和业务工具*

- **brand-guidelines** - 应用 Anthropic 的品牌颜色和排版以实现一致的视觉识别
- **competitive-ads-extractor** - 从广告库中提取和分析竞争对手的广告
- **domain-name-brainstormer** - 生成创意域名并检查可用性
- **internal-comms** - 撰写内部通信（新闻简报、常见问题解答、状态报告）
- **invoice-organizer** - 组织发票和收据以进行税务准备
- **lead-research-assistant** - 通过外展策略识别和筛选高质量潜在客户
- **raffle-winner-picker** - 使用加密安全的随机性随机选择活动获胜者

---

### 数据分析
*2 个数据处理、分析和调试技能*

- **csv-data-summarizer** - 分析 CSV 文件并通过可视化生成洞察
- **root-cause-tracing** - 通过执行向后追踪错误以找到根本原因

---

## 其他优秀的 Skills 项目

除了本项目中的技能，我们还推荐以下优秀的 Claude Skills 项目：

### 🔬 科学与研究工具

**[Claude Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills)** - 由 K-Dense AI 维护
*一个包含 123+ 个专业科学计算和研究技能的综合性集合*

该项目专注于科学研究和数据科学领域，包括：
- **生物信息学**: Biopython, AlphaFold, Ensembl, PubMed 数据库
- **化学信息学**: RDKit, DeepChem, ChEMBL, PubChem, 分子分析
- **机器学习**: PyTorch Lightning, scikit-learn, transformers, stable-baselines3
- **数据科学**: Pandas, Polars, Dask, Vaex, 统计分析
- **可视化**: Matplotlib, Seaborn, Plotly, 科学可视化
- **物理与量子**: Qiskit, Cirq, PennyLane, QuTiP
- **天文学**: Astropy
- **系统生物学**: COBRA, 通路分析, 网络分析
- **临床研究**: ClinicalTrials, ClinVar, FDA 数据库

**为什么推荐：**
- ✅ 专业的科学领域覆盖
- ✅ 每个技能都有详细的参考文档
- ✅ 包含实际使用示例和最佳实践
- ✅ 持续更新和维护
- ✅ 适合研究人员、数据科学家和科学计算用户

**快速开始：**
```bash
git clone https://github.com/K-Dense-AI/claude-scientific-skills.git
cd claude-scientific-skills
```

---

如果你知道其他优秀的 Claude Skills 项目，欢迎提交 PR 添加到这里！

---

## 快速开始

### 前置要求

- Claude.ai 账户、Claude Code 安装或 Claude API 访问权限
- 对于 Python 脚本：Python 3.8+ 和 `requirements.txt` 中的依赖项

### 安装

1. **克隆仓库：**
   ```bash
   git clone https://github.com/Jst-Well-Dan/claude-skills-vault.git
   cd claude-skills-vault
   ```

2. **安装 Python 依赖（如果使用自动化脚本）：**
   ```bash
   pip install -r requirements.txt
   ```

3. **将技能添加到你的 Claude 环境：**

   **对于 Claude Code：**
   - 将所需的技能文件夹复制到你的项目中
   - Claude Code 将自动从 `.claude-plugin/marketplace.json` 文件检测技能

   **对于 Claude.ai：**
   - 导航到技能的文件夹
   - 复制 `SKILL.md` 的内容
   - 粘贴到你的 Claude.ai 对话中

   **对于 Claude API：**
   - 在系统提示或上下文中包含技能内容

### 使用技能

每个技能包含：
- `SKILL.md` - 主要技能定义和说明
- `references/` - 支持文档（如适用）
- `scripts/` - 辅助脚本（如适用）

**示例：使用 deep-reading-analyst 技能**
```bash
cd productivity-organization/deep-reading-analyst-skill
cat SKILL.md
```

---

## 创建技能

想创建你自己的 Claude Skill？使用 **skill-creator** 技能来指导你完成整个过程！

**技能的关键组成部分：**
- 带有 frontmatter 元数据（名称、描述）的 `SKILL.md`
- 清晰、可操作的说明
- 示例和用例
- 参考文档（可选）
- 辅助脚本（可选）

**最佳实践：**
- 专注于特定、明确定义的任务
- 包含清晰的激活触发器
- 提供具体示例
- 记录前置条件和依赖项
- 在不同的 Claude 平台上测试

查看 [skill-creator](./development/skill-creator/) 获取详细指导。

---

## 自动化脚本

位于 `scripts/` 中，这些 Python 工具帮助管理技能集合：

- **fetch_external_skills.py** - 从 GitHub 获取外部技能的编排器
- **github_fetcher.py** - GitHub API 交互和仓库下载
- **marketplace_updater.py** - 管理 marketplace.json 条目
- **skill_processor.py** - 验证和处理技能元数据
- **utils.py** - 通用工具函数

**配置：**
- `config/external_skills_config.json` - 外部技能源
- `logs/` - 执行日志

---

## 贡献

我们欢迎贡献！以下是你可以提供帮助的方式：

1. **添加新技能**：按照 `template-skill` 中的结构创建新技能
2. **改进现有技能**：提交带有增强功能或错误修复的 PR
3. **报告问题**：为错误或建议打开 issue
4. **分享使用示例**：通过分享你的用例帮助他人学习
5. **推荐其他项目**：分享你发现的优秀 Claude Skills 项目

**贡献指南：**
- 每个技能必须有带有适当 frontmatter 的 `SKILL.md`
- 遵循现有的类别结构
- 包含清晰的示例和文档
- 在不同的 Claude 平台上测试你的技能
- 添加新技能时更新 `marketplace.json`

---

## 资源

- **官方 Claude 文档**：[docs.anthropic.com](https://docs.anthropic.com)
- **Claude Skills 指南**：[docs.anthropic.com/claude/docs/skills](https://docs.anthropic.com/claude/docs/skills)
- **Composio 集成**：[composio.dev](https://composio.dev)
- **MCP 协议**：[modelcontextprotocol.io](https://modelcontextprotocol.io)

---

## 许可证

本项目采用 Apache License 2.0 许可 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

---

## 致谢

特别感谢所有贡献者和 Claude 社区构建和分享这些出色的技能！

**特色贡献者：**
- [@obra](https://github.com/obra) - 多个开发工作流程技能
- [@smerchek](https://github.com/smerchek) - Markdown 转 EPUB 转换器
- [@chrisvoncsefalvay](https://github.com/chrisvoncsefalvay) - D3.js 可视化
- [@coffeefuelbump](https://github.com/coffeefuelbump) - CSV 数据摘要器
- [@emaynard](https://github.com/emaynard) - 家族史研究
- 还有更多！请参阅各个技能以获取归属信息。

**推荐项目：**
- [K-Dense AI](https://github.com/K-Dense-AI) - Claude Scientific Skills 项目维护者

---

<p align="center">
  由 Claude 社区用 ❤️ 制作
</p>

<p align="center">
  <a href="https://github.com/Jst-Well-Dan/claude-skills-vault">⭐ 给这个仓库加星</a> •
  <a href="https://github.com/Jst-Well-Dan/claude-skills-vault/issues">报告错误</a> •
  <a href="https://github.com/Jst-Well-Dan/claude-skills-vault/issues">请求功能</a>
</p>
