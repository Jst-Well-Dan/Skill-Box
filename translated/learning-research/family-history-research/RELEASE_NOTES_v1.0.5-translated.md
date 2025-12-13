<!--
本文件由智谱 AI 自动翻译生成
原文件: RELEASE_NOTES_v1.0.5.md
翻译时间: 2025-12-12 16:11:55
翻译模型: glm-4-flash
原文大小: 4,553 字符
-->

# 版本 1.0.5：文档重组

本次发布重新组织了项目结构，使指导文档与研究参考更好地对齐，使用户更容易找到全面的方法资源。

## 新增功能

### 文档结构重组

**将指导文件移动到 `references/` 目录**
- `research-log-guidance.md` - 从 `assets/templates/` 移动到 `references/`
- `research-plan-guidance.md` - 从 `assets/templates/` 移动到 `references/`

**更新 SKILL.md 参考**
- 纠正了对已迁移指导文档的引用
- 改善了模板和指导之间的导航

**这次重组的好处：**
- 指导文档与其它参考材料分组
- 模板（在 `assets/templates/`）和参考（在 `references/`）之间的区别更清晰
- 用户寻求详细方法时的信息架构更好
- 更容易维护和更新文档

## 重组后的结构

```
genealogy-research-skill/
├── assets/templates/          # 简化、实用的模板
│   ├── research-plan-template.md
│   ├── research-log-template.md
│   ├── citation-template.md
│   └── evidence-analysis-template.md
│
├── references/                # 综合参考文档
│   ├── research-plan-guidance.md
│   ├── research-log-guidance.md
│   ├── citation-templates.md
│   ├── evidence-evaluation.md
│   ├── gps-guidelines.md
│   └── research-strategies.md
│
├── SKILL.md                   # 主要技能定义
├── README.md                  # 安装和概述
└── CHANGELOG.md               # 版本历史
```

## 为什么这很重要

### 改善的信息架构

用户现在有一个更清晰的架构：
- **模板** (`assets/templates/`) - 快速、实用的日常工作工具
- **参考** (`references/`) - 全面的方法和详细指导

### 更好的用户体验

当用户需要：
- **快速指导**：从简化的模板开始
- **详细方法**：咨询同一 `references/` 目录中的参考文档

这反映了在 v1.0.3 和 v1.0.4 中引入的将简化模板与详细指导分离的成功做法。

## 专业标准

所有文档继续支持：
- **家谱证明标准 (GPS)** - 合理详尽的研究并记录
- **证据解释** - 完整和准确的引用
- **家谱认证委员会 (BCG)** - 专业方法

## 安装

### 快速开始

1. 下载最新版本：`family-history-planning-v1.0.5.zip`
2. 解压 ZIP 文件
3. **Claude.ai 用户**：在设置 > 能力中启用技能，然后上传技能文件夹
4. **Claude Code 用户**：将 `family-history-planning` 文件夹移动到 `~/.claude/skills/`
5. 开始使用：只需询问 Claude 关于家谱研究！

### 完整说明

请参阅 [README.md](https://github.com/emaynard/claude-family-history-research-skill/blob/main/README.md#installation) 以获取完整的安装说明。

## 这个技能的功能

家谱研究规划技能为 Claude 提供了以下专业知识的支持：
- **研究规划** - 按照 GPS 标准创建结构化的研究计划
- **引用创建** - 为 14+ 种来源类型生成正确格式的家谱引用
- **证据分析** - 系统地分析和解决家谱证据中的冲突
- **研究文档** - 创建专业的调查日志和文档

## 更新日志

### 版本 1.0.5 更改
- 将指导文档重组到 `references/` 目录
- 更新 SKILL.md 参考以反映新的文档位置
- 改善项目结构以获得更好的信息架构
- 更新 GitHub Actions 发布工作流程

### 之前版本的相关更改
请参阅 [完整更新日志](https://github.com/emaynard/claude-family-history-research-skill/blob/main/CHANGELOG.md) 以获取完整的版本历史。

## 支持

- **问题**：在 [GitHub Issues](https://github.com/emaynard/claude-family-history-research-skill/issues) 中报告错误或请求功能
- **文档**：请参阅 [README.md](https://github.com/emaynard/claude-family-history-research-skill/blob/main/README.md)
- **专业标准**：参考 GPS、证据解释和 BCG 资源
- **负责任的 AI**：了解更多信息请访问 [CRAIGEN.org](https://craigen.org)

---

**完整更新日志**：https://github.com/emaynard/claude-family-history-research-skill/compare/v1.0.4...v1.0.5