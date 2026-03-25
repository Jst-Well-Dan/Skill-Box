# Skill-Box Plugin 重构设计方案

> 创建日期：2026-01-24
> 版本：1.0
> 状态：规划中

---

## 📋 目录

1. [背景与动机](#背景与动机)
2. [现状分析](#现状分析)
3. [重构目标](#重构目标)
4. [设计原则](#设计原则)
5. [重构方案](#重构方案)
6. [各分类详细规划](#各分类详细规划)
7. [实施路径](#实施路径)
8. [预期效果](#预期效果)

---

## 背景与动机

### 问题起源

在分析 **baoyu-skills** 的设计模式时，发现其采用了一种更为合理的 Plugin 组织方式：

```json
// baoyu-skills 的 marketplace.json 结构
{
  "plugins": [
    {
      "name": "content-skills",
      "description": "Content generation and publishing skills",
      "skills": [
        "./skills/baoyu-xhs-images",
        "./skills/baoyu-post-to-x",
        "./skills/baoyu-post-to-wechat",
        "./skills/baoyu-article-illustrator",
        "./skills/baoyu-cover-image",
        "./skills/baoyu-slide-deck",
        "./skills/baoyu-comic",
        "./skills/baoyu-infographic"
      ]
    },
    {
      "name": "ai-generation-skills",
      "skills": ["./skills/baoyu-danger-gemini-web", "./skills/baoyu-image-gen"]
    },
    {
      "name": "utility-skills",
      "skills": [
        "./skills/baoyu-danger-x-to-markdown",
        "./skills/baoyu-compress-image",
        "./skills/baoyu-url-to-markdown"
      ]
    }
  ]
}
```

这种设计的**核心优势**：
- 🔗 **依赖关系管理**：相关 Skills 被组合在同一 Plugin 中，用户安装一个 Plugin 即可获得完整的工作流能力
- 📦 **用户体验优化**：减少用户选择成本，不需要逐个安装相关 Skills
- 🎯 **语义化分组**：根据功能用途而非技术类别进行分组

### 当前问题

Skill-Box 当前采用 **"一个 Skill = 一个 Plugin"** 的模式：

```json
{
  "plugins": [
    { "name": "docx", "skills": ["./office-automation/document-skills-docx"] },
    { "name": "pdf", "skills": ["./office-automation/document-skills-pdf"] },
    { "name": "pptx", "skills": ["./office-automation/document-skills-pptx"] },
    { "name": "xlsx", "skills": ["./office-automation/document-skills-xlsx"] }
  ]
}
```

**问题表现**：
1. ❌ Plugin 数量过多（当前 50+ 个 Plugins）
2. ❌ 相关功能分散，用户需要逐个安装
3. ❌ 无法体现 Skills 之间的协同关系
4. ❌ 工作流被人为割裂

---

## 现状分析

### 当前分类结构统计

| 分类文件夹 | 文件夹名称 | Skills 数量 | 当前 Plugins 数量 |
|-----------|-----------|------------|------------------|
| 1 | `brand-marketing` | 5 | 5 |
| 2 | `business-analyst` | 6 | 6 |
| 3 | `content-pipeline` | 4 | 4 |
| 4 | `immersive-reading` | 5 | 5 |
| 5 | `no-code-builder` | 15 | 15 |
| 6 | `office-automation` | 6 | 6 |
| 7 | `visual-creative` | 9 | 9 |
| **合计** | **7个分类** | **50 个 Skills** | **50 个 Plugins** |

### 各分类 Skills 清单

#### 1. brand-marketing（品牌营销）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| Anthropic-brand-guidelines | 品牌风格指南 | 独立 |
| competitive-ads-extractor | 竞品广告提取 | 独立 |
| domain-name-brainstormer | 域名创意生成 | 独立 |
| internal-comms | 内部沟通写作 | 独立 |
| raffle-winner-picker | 抽奖中奖者选择 | 独立 |

#### 2. business-analyst（商业分析）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| csv-data-summarizer | CSV 数据分析 | 🔗 数据分析组 |
| invoice-processor | 发票处理 | 独立 |
| excel-dcf-modeler | DCF 估值模型 | 🔗 Excel 金融建模组 |
| excel-lbo-modeler | LBO 杠杆收购模型 | 🔗 Excel 金融建模组 |
| excel-pivot-wizard | 数据透视表 | 🔗 Excel 数据分析组 |
| excel-variance-analyzer | 方差分析 | 🔗 Excel 数据分析组 |

#### 3. content-pipeline（内容生产线）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| advanced-video-downloader | 视频下载 | 🔗 内容采集组 |
| content-research-writer | 内容研究写作 | 独立 |
| web-fetch | 网页抓取 | 🔗 内容采集组 |
| youtube-transcript | YouTube 字幕下载 | 🔗 内容采集组 |

#### 4. immersive-reading（沉浸阅读）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| deep-reading-analyst-skill | 深度阅读分析 | 🔗 阅读分析组 |
| family-history-research | 家谱研究 | 独立 |
| meeting-insights-analyzer | 会议洞察分析 | 🔗 阅读分析组 |
| notebooklm-integration | NotebookLM 集成 | 独立 |
| ship-learn-next | 学习行动转化 | 🔗 阅读分析组 |

#### 5. no-code-builder（无代码构建）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| artifacts-builder | Artifacts 构建器 | 🔗 前端开发组 |
| changelog-generator | 变更日志生成 | 🔗 开发工作流组 |
| developer-growth-analysis | 开发者成长分析 | 独立 |
| development-brainstorming | 开发头脑风暴 | 🔗 开发工作流组 |
| frontend-design | 前端设计 | 🔗 前端开发组 |
| git-pushing | Git 推送 | 🔗 开发工作流组 |
| mcp-builder | MCP 服务器构建 | 独立 |
| pypict-claude-skill | PICT 测试设计 | 🔗 测试工具组 |
| react-best-practices | React 最佳实践 | 🔗 前端开发组 |
| skill-creator | Skill 创建器 | 独立 |
| terminal-title | 终端标题 | 独立 |
| test-driven-development | TDD 测试驱动开发 | 🔗 测试工具组 |
| test-fixing | 测试修复 | 🔗 测试工具组 |
| vercel-deploy-claimable | Vercel 部署 | 🔗 前端开发组 |
| webapp-testing | Web 应用测试 | 🔗 测试工具组 |

#### 6. office-automation（办公自动化）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| document-skills-docx | Word 文档处理 | 🔗 文档处理组 |
| document-skills-pdf | PDF 文档处理 | 🔗 文档处理组 |
| document-skills-pptx | PPT 演示处理 | 🔗 文档处理组 |
| document-skills-xlsx | Excel 表格处理 | 🔗 文档处理组 |
| markdown-to-epub-converter | Markdown 转 EPUB | 🔗 文档转换组 |
| file-organizer | 文件整理器 | 独立 |

#### 7. visual-creative（视觉创意）
| Skills | 功能描述 | 关联度分析 |
|--------|---------|-----------|
| algorithmic-art | 算法艺术 | 独立 |
| canvas-design | 画布设计 | 独立 |
| excalidraw-diagram | Excalidraw 图表 | 🔗 Obsidian 可视化组 |
| image-enhancer | 图片增强 | 独立 |
| mermaid-visualizer | Mermaid 可视化 | 🔗 Obsidian 可视化组 |
| obsidian-canvas-creator | Obsidian Canvas 创建 | 🔗 Obsidian 可视化组 |
| slack-gif-creator | Slack GIF 创建 | 独立 |
| theme-factory | 主题工厂 | 独立 |
| web-design-guidelines | Web 设计指南 | 独立 |

---

## 重构目标

### 核心目标

1. **减少 Plugin 数量**：从 50 个减少到约 25-30 个
2. **保留分类结构**：继续使用 7 个分类文件夹组织 Skills
3. **优化用户体验**：相关 Skills 组合安装，降低选择成本
4. **保持灵活性**：独立 Skills 仍可单独作为 Plugin

### 量化指标

| 指标 | 当前值 | 目标值 |
|-----|-------|-------|
| Plugin 总数 | 50 | 25-30 |
| 平均每个 Plugin 的 Skills 数 | 1 | 1.5-2 |
| 组合型 Plugin 占比 | 0% | 40-50% |

---

## 设计原则

### 1. 工作流优先原则

> 如果用户需要 A、B、C 三个 Skills 一起存在才能完成完整工作流，则应将它们组合到同一个 Plugin

**示例**：
- `web-fetch` + `youtube-transcript` + `advanced-video-downloader` → **内容采集 Plugin**
- `docx` + `pdf` + `pptx` + `xlsx` → **文档处理 Plugin**

### 2. 功能依赖原则

> 如果 Skill A 的输出是 Skill B 的输入，则应考虑组合

**示例**：
- YouTube 字幕下载 → 内容分析 → 行动转化

### 3. 技术同源原则

> 使用相同底层技术栈的 Skills 可以组合

**示例**：
- 所有 Excel 金融建模 Skills（DCF、LBO）使用相同的 openpyxl 基础
- 所有 Obsidian 可视化 Skills 面向同一目标平台

### 4. 保持独立原则

> 功能单一、无明显关联的 Skills 保持独立

**示例**：
- `algorithmic-art` - 算法艺术创作，独立使用
- `family-history-research` - 家谱研究，独立使用

---

## 重构方案

### Plugin 重组规划

#### 1. brand-marketing（品牌营销）- 5 Plugins → 5 Plugins

> ⚡ **保持原状**：此分类的 Skills 相对独立，无明显组合需求

| Plugin 名称 | 包含 Skills | 说明 |
|------------|------------|------|
| anthropic-brand-guidelines | anthropic-brand-guidelines | 独立 |
| competitive-ads-extractor | competitive-ads-extractor | 独立 |
| domain-name-brainstormer | domain-name-brainstormer | 独立 |
| internal-comms | internal-comms | 独立 |
| raffle-winner-picker | raffle-winner-picker | 独立 |

---

#### 2. business-analyst（商业分析）- 6 Plugins → 3 Plugins ✨

| Plugin 名称 | 包含 Skills | 设计理由 |
|------------|------------|---------|
| **data-analysis-toolkit** | csv-data-summarizer, excel-pivot-wizard, excel-variance-analyzer | 数据分析全流程：从 CSV 处理到数据透视分析和方差分析 |
| **financial-modeling-suite** | excel-dcf-modeler, excel-lbo-modeler | 金融估值建模：DCF 和 LBO 模型经常一起使用进行企业估值 |
| invoice-processor | invoice-processor | 发票处理功能独立，场景特定 |

```json
// 新的 Plugin 结构
{
  "name": "data-analysis-toolkit",
  "description": "Complete data analysis toolkit: CSV summarization, pivot tables, and variance analysis for comprehensive business data insights.",
  "skills": [
    "./business-analyst/csv-data-summarizer",
    "./business-analyst/excel-pivot-wizard",
    "./business-analyst/excel-variance-analyzer"
  ]
},
{
  "name": "financial-modeling-suite",
  "description": "Professional financial modeling suite for DCF valuation and LBO analysis. Perfect for investment banking, private equity, and corporate finance professionals.",
  "skills": [
    "./business-analyst/excel-dcf-modeler",
    "./business-analyst/excel-lbo-modeler"
  ]
}
```

---

#### 3. content-pipeline（内容生产线）- 4 Plugins → 2 Plugins ✨

| Plugin 名称 | 包含 Skills | 设计理由 |
|------------|------------|---------|
| **content-harvester** | advanced-video-downloader, web-fetch, youtube-transcript | 内容采集工作流：网页抓取 → 视频下载 → 字幕提取，经常配合使用 |
| content-research-writer | content-research-writer | 内容研究写作是独立的创作流程 |

```json
{
  "name": "content-harvester",
  "description": "Complete web content harvesting pipeline: scrape webpages, download videos from 1000+ platforms, and extract YouTube transcripts. Everything you need to capture online content.",
  "skills": [
    "./content-pipeline/advanced-video-downloader",
    "./content-pipeline/web-fetch",
    "./content-pipeline/youtube-transcript"
  ]
}
```

---

#### 4. immersive-reading（沉浸阅读）- 5 Plugins → 3 Plugins ✨

| Plugin 名称 | 包含 Skills | 设计理由 |
|------------|------------|---------|
| **reading-to-action** | deep-reading-analyst-skill, meeting-insights-analyzer, ship-learn-next | 阅读 → 分析 → 行动转化的完整工作流 |
| notebooklm-integration | notebooklm-integration | NotebookLM 集成需要特定环境，独立维护 |
| family-history-research | family-history-research | 家谱研究是特定场景，独立使用 |

```json
{
  "name": "reading-to-action",
  "description": "Transform reading into results: deep content analysis, meeting insights extraction, and actionable learning conversion using proven frameworks.",
  "skills": [
    "./immersive-reading/deep-reading-analyst-skill",
    "./immersive-reading/meeting-insights-analyzer",
    "./immersive-reading/ship-learn-next"
  ]
}
```

---

#### 5. no-code-builder（无代码构建）- 15 Plugins → 9 Plugins ✨

| Plugin 名称 | 包含 Skills | 设计理由 |
|------------|------------|---------|
| **frontend-builder** | artifacts-builder, frontend-design, react-best-practices, vercel-deploy-claimable | 前端开发全流程：设计 → 构建 → 优化 → 部署 |
| **testing-toolkit** | pypict-claude-skill, test-driven-development, test-fixing, webapp-testing | 测试工具套件：设计 → 开发 → 修复 → E2E测试 |
| **dev-workflow** | changelog-generator, development-brainstorming, git-pushing | 开发工作流：规划 → 提交 → 记录 |
| skill-creator | skill-creator | Skill 创建功能独立 |
| mcp-builder | mcp-builder | MCP 构建功能独立 |
| developer-growth-analysis | developer-growth-analysis | 开发者分析功能独立 |
| terminal-title | terminal-title | 终端工具功能独立 |

```json
{
  "name": "frontend-builder",
  "description": "End-to-end frontend development suite: design high-quality interfaces, build complex artifacts, follow React best practices, and deploy to Vercel with one click.",
  "skills": [
    "./no-code-builder/artifacts-builder",
    "./no-code-builder/frontend-design",
    "./no-code-builder/react-best-practices",
    "./no-code-builder/vercel-deploy-claimable"
  ]
},
{
  "name": "testing-toolkit",
  "description": "Complete testing toolkit: PICT test design, TDD methodology, automated test fixing, and web application testing with Playwright.",
  "skills": [
    "./no-code-builder/pypict-claude-skill",
    "./no-code-builder/test-driven-development",
    "./no-code-builder/test-fixing",
    "./no-code-builder/webapp-testing"
  ]
},
{
  "name": "dev-workflow",
  "description": "Streamline your development workflow: brainstorm features, push changes with proper commits, and auto-generate changelogs.",
  "skills": [
    "./no-code-builder/changelog-generator",
    "./no-code-builder/development-brainstorming",
    "./no-code-builder/git-pushing"
  ]
}
```

---

#### 6. office-automation（办公自动化）- 6 Plugins → 3 Plugins ✨

| Plugin 名称 | 包含 Skills | 设计理由 |
|------------|------------|---------|
| **document-suite** | document-skills-docx, document-skills-pdf, document-skills-pptx, document-skills-xlsx | 办公文档全家桶：Word、PDF、PPT、Excel 统一处理 |
| markdown-to-epub-converter | markdown-to-epub-converter | 文档转换独立功能 |
| file-organizer | file-organizer | 文件整理独立功能 |

```json
{
  "name": "document-suite",
  "description": "Complete office document toolkit: create, edit, and analyze Word, Excel, PowerPoint, and PDF documents with full formatting support, tracked changes, and formulas.",
  "skills": [
    "./office-automation/document-skills-docx",
    "./office-automation/document-skills-pdf",
    "./office-automation/document-skills-pptx",
    "./office-automation/document-skills-xlsx"
  ]
}
```

---

#### 7. visual-creative（视觉创意）- 9 Plugins → 7 Plugins ✨

| Plugin 名称 | 包含 Skills | 设计理由 |
|------------|------------|---------|
| **obsidian-visual-suite** | excalidraw-diagram, mermaid-visualizer, obsidian-canvas-creator | Obsidian 可视化套件：三种可视化方式面向同一平台 |
| algorithmic-art | algorithmic-art | 算法艺术独立创作 |
| canvas-design | canvas-design | 画布设计独立功能 |
| image-enhancer | image-enhancer | 图片增强独立功能 |
| slack-gif-creator | slack-gif-creator | Slack 动图独立功能 |
| theme-factory | theme-factory | 主题工厂独立功能 |
| web-design-guidelines | web-design-guidelines | Web 设计指南独立功能 |

```json
{
  "name": "obsidian-visual-suite",
  "description": "Complete visualization toolkit for Obsidian: create Excalidraw diagrams, Mermaid flowcharts, and interactive Canvas mind maps from any text content.",
  "skills": [
    "./visual-creative/excalidraw-diagram",
    "./visual-creative/mermaid-visualizer",
    "./visual-creative/obsidian-canvas-creator"
  ]
}
```

---

## 重构前后对比总结

### 数量变化

| 分类 | 重构前 Plugins | 重构后 Plugins | 减少数量 |
|-----|---------------|---------------|---------|
| brand-marketing | 5 | 5 | 0 |
| business-analyst | 6 | 3 | -3 |
| content-pipeline | 4 | 2 | -2 |
| immersive-reading | 5 | 3 | -2 |
| no-code-builder | 15 | 9 | -6 |
| office-automation | 6 | 3 | -3 |
| visual-creative | 9 | 7 | -2 |
| **合计** | **50** | **32** | **-18** |

### 新增组合型 Plugins（9 个）

1. **data-analysis-toolkit** - 数据分析工具包
2. **financial-modeling-suite** - 金融建模套件
3. **content-harvester** - 内容采集器
4. **reading-to-action** - 阅读行动转化
5. **frontend-builder** - 前端构建器
6. **testing-toolkit** - 测试工具包
7. **dev-workflow** - 开发工作流
8. **document-suite** - 文档处理套件
9. **obsidian-visual-suite** - Obsidian 可视化套件

---

## 实施路径

### Phase 1: 准备阶段（1天）

- [ ] 备份当前 `marketplace.json`
- [ ] 创建新的 `marketplace.json` 模板
- [ ] 确认所有 Skills 路径正确

### Phase 2: 核心重构（2天）

- [ ] 实施 `office-automation` 重构（最简单，风险最低）
- [ ] 实施 `business-analyst` 重构
- [ ] 实施 `content-pipeline` 重构
- [ ] 实施 `visual-creative` 重构

### Phase 3: 复杂重构（2天）

- [ ] 实施 `no-code-builder` 重构（Skills 最多）
- [ ] 实施 `immersive-reading` 重构
- [ ] 确认 `brand-marketing` 无需变化

### Phase 4: 验证阶段（1天）

- [ ] 验证所有 Plugin 加载正常
- [ ] 测试组合 Plugins 的功能完整性
- [ ] 更新 README.md 文档
- [ ] 更新 Skill 翻译文件

---

## 预期效果

### 用户体验提升

1. **减少选择困难**：Plugin 数量从 50 个减少到 32 个
2. **工作流完整性**：安装一个 Plugin 即可获得完整工作流
3. **语义化分组**：Plugin 名称清晰表达功能用途

### 维护效率提升

1. **统一管理**：相关 Skills 在同一 Plugin 中统一版本管理
2. **快速定位**：通过 Plugin 层级快速找到相关 Skills
3. **文档简化**：组合 Plugin 的文档可以展示完整工作流

### 扩展性保障

1. **保留分类结构**：7 个分类文件夹继续用于组织 Skill 源码
2. **灵活组合**：未来可以根据需要调整 Plugin 组合
3. **向后兼容**：独立 Skills 仍可被单独引用

---

## 附录：完整的新 marketplace.json 结构

```json
{
  "name": "Skill-Box",
  "version": "2.0.0",
  "description": "An collection of practical skills that transforms your AI assistant from a generalist into a powerful specialist.",
  "owner": {
    "name": "Jst-Well-Dan",
    "url": "https://github.com/Jst-Well-Dan/Skill-Box"
  },
  "plugins": [
    // ===== brand-marketing (5 Plugins) =====
    { "name": "anthropic-brand-guidelines", "skills": ["./brand-marketing/Anthropic-brand-guidelines"] },
    { "name": "competitive-ads-extractor", "skills": ["./brand-marketing/competitive-ads-extractor"] },
    { "name": "domain-name-brainstormer", "skills": ["./brand-marketing/domain-name-brainstormer"] },
    { "name": "internal-comms", "skills": ["./brand-marketing/internal-comms"] },
    { "name": "raffle-winner-picker", "skills": ["./brand-marketing/raffle-winner-picker"] },

    // ===== business-analyst (3 Plugins) =====
    { 
      "name": "data-analysis-toolkit",
      "description": "Complete data analysis toolkit: CSV summarization, pivot tables, and variance analysis.",
      "skills": [
        "./business-analyst/csv-data-summarizer",
        "./business-analyst/excel-pivot-wizard",
        "./business-analyst/excel-variance-analyzer"
      ]
    },
    { 
      "name": "financial-modeling-suite",
      "description": "Professional financial modeling suite for DCF valuation and LBO analysis.",
      "skills": [
        "./business-analyst/excel-dcf-modeler",
        "./business-analyst/excel-lbo-modeler"
      ]
    },
    { "name": "invoice-processor", "skills": ["./business-analyst/invoice-processor"] },

    // ===== content-pipeline (2 Plugins) =====
    { 
      "name": "content-harvester",
      "description": "Complete web content harvesting: scrape webpages, download videos, extract YouTube transcripts.",
      "skills": [
        "./content-pipeline/advanced-video-downloader",
        "./content-pipeline/web-fetch",
        "./content-pipeline/youtube-transcript"
      ]
    },
    { "name": "content-research-writer", "skills": ["./content-pipeline/content-research-writer"] },

    // ===== immersive-reading (3 Plugins) =====
    { 
      "name": "reading-to-action",
      "description": "Transform reading into results: deep analysis, meeting insights, and actionable learning.",
      "skills": [
        "./immersive-reading/deep-reading-analyst-skill",
        "./immersive-reading/meeting-insights-analyzer",
        "./immersive-reading/ship-learn-next"
      ]
    },
    { "name": "notebooklm-integration", "skills": ["./immersive-reading/notebooklm-integration"] },
    { "name": "family-history-research", "skills": ["./immersive-reading/family-history-research"] },

    // ===== no-code-builder (9 Plugins) =====
    { 
      "name": "frontend-builder",
      "description": "End-to-end frontend development: design, build, optimize, and deploy.",
      "skills": [
        "./no-code-builder/artifacts-builder",
        "./no-code-builder/frontend-design",
        "./no-code-builder/react-best-practices",
        "./no-code-builder/vercel-deploy-claimable"
      ]
    },
    { 
      "name": "testing-toolkit",
      "description": "Complete testing toolkit: PICT design, TDD, test fixing, and Playwright testing.",
      "skills": [
        "./no-code-builder/pypict-claude-skill",
        "./no-code-builder/test-driven-development",
        "./no-code-builder/test-fixing",
        "./no-code-builder/webapp-testing"
      ]
    },
    { 
      "name": "dev-workflow",
      "description": "Streamline development: brainstorm, commit, and auto-generate changelogs.",
      "skills": [
        "./no-code-builder/changelog-generator",
        "./no-code-builder/development-brainstorming",
        "./no-code-builder/git-pushing"
      ]
    },
    { "name": "skill-creator", "skills": ["./no-code-builder/skill-creator"] },
    { "name": "mcp-builder", "skills": ["./no-code-builder/mcp-builder"] },
    { "name": "developer-growth-analysis", "skills": ["./no-code-builder/developer-growth-analysis"] },
    { "name": "terminal-title", "skills": ["./no-code-builder/terminal-title"] },

    // ===== office-automation (3 Plugins) =====
    { 
      "name": "document-suite",
      "description": "Complete office document toolkit: Word, Excel, PowerPoint, and PDF.",
      "skills": [
        "./office-automation/document-skills-docx",
        "./office-automation/document-skills-pdf",
        "./office-automation/document-skills-pptx",
        "./office-automation/document-skills-xlsx"
      ]
    },
    { "name": "markdown-to-epub-converter", "skills": ["./office-automation/markdown-to-epub-converter"] },
    { "name": "file-organizer", "skills": ["./office-automation/file-organizer"] },

    // ===== visual-creative (7 Plugins) =====
    { 
      "name": "obsidian-visual-suite",
      "description": "Complete visualization for Obsidian: Excalidraw, Mermaid, and Canvas.",
      "skills": [
        "./visual-creative/excalidraw-diagram",
        "./visual-creative/mermaid-visualizer",
        "./visual-creative/obsidian-canvas-creator"
      ]
    },
    { "name": "algorithmic-art", "skills": ["./visual-creative/algorithmic-art"] },
    { "name": "canvas-design", "skills": ["./visual-creative/canvas-design"] },
    { "name": "image-enhancer", "skills": ["./visual-creative/image-enhancer"] },
    { "name": "slack-gif-creator", "skills": ["./visual-creative/slack-gif-creator"] },
    { "name": "theme-factory", "skills": ["./visual-creative/theme-factory"] },
    { "name": "web-design-guidelines", "skills": ["./visual-creative/web-design-guidelines"] }
  ]
}
```

---

> 📝 **注意**：此文档为规划方案，实际实施时需要根据测试结果进行调整。
