<!--
本文件由智谱 AI 自动翻译生成
原文件: GEMINI.md
翻译时间: 2025-12-12 16:11:08
翻译模型: glm-4-flash
原文大小: 4,375 字符
-->

---

# Gemini 项目背景：技能盒与展示

本文档概述了“技能盒”项目，其结构和关键开发工作流程。目标是帮助 Gemini 代理了解项目，以便在未来任务中应用。

## 项目概述

该仓库是一个用于管理和展示大型语言模型 AI “技能”集合的综合系统。用户的目的是为普通观众创建引人入胜的非技术演示。

项目主要包括以下两部分：

1. **技能管理系统（Python）：** 位于 `/scripts` 目录的一系列 Python 脚本，负责从外部 GitHub 仓库检索技能，处理其元数据，并将它们聚合到中央 `marketplace.json` 文件中。
2. **技能展示（React Web App）：** 位于 `/awesome-skills-showcase` 的现代 Web 应用程序，用于展示市场中的技能。它使用 Vite、React、TypeScript 构建，并使用 Tailwind CSS 进行样式设计。

## 关键组件与数据流

整个系统围绕一个清晰的数据管道进行设计：

1. **配置 (`config/external_skills_config.json`):** 一个主 JSON 文件，定义了要包含的所有技能列表。每个条目包含 GitHub URL、本地目标文件夹、类别和描述。

2. **检索 (`scripts/fetch_external_skills.py`):** 此脚本读取主配置文件，并从 GitHub 下载相应的技能仓库或子文件夹到正确的目录（例如，`/development`、`/data-analysis`）。它需要一个 `GITHUB_TOKEN` 环境变量。

3. **处理 (`scripts/skill_processor.py` & `scripts/marketplace_updater.py`):**
    * 在检索后，脚本处理下载的技能目录。
    * 它读取每个技能文件夹内的 `SKILL.md` 文件，该文件包含 YAML 前置块中的元数据。
    * 然后 `marketplace_updater.py` 脚本将此元数据与主配置信息合并，生成单个统一的 `/marketplace.json` 文件。此文件充当所有技能的中央数据库。

4. **展示 (`/awesome-skills-showcase`):**
    * 此 React 应用程序作为技能市场的前端。
    * 在运行或构建应用程序之前，一个 `sync` 脚本 (`scripts/sync-marketplace.js`) 将根 `marketplace.json` 文件复制到应用程序的 `src` 目录。
    * 应用程序随后加载此本地 `marketplace.json` 以渲染技能列表、其类别和描述。

---

## 构建和运行

### 1. 技能管理（Python）

要更新技能数据库，需要运行 Python 脚本。

**先决条件：**
* Python 3
* 安装依赖项：`pip install -r requirements.txt`
* 设置 `GITHUB_TOKEN` 环境变量为有效的 GitHub 个人访问令牌。

**工作流程：**

```bash
# 1. 从 GitHub 检索技能
python scripts/fetch_external_skills.py

# 2. 使用新技能更新 marketplace.json
# （假设有一个主脚本协调此操作，例如 main.py 或类似）
# 占位符用于运行完整更新管道的确切命令。
# TODO：记录运行完整市场更新命令的确切命令。
```

### 2. 技能展示（Web App）

要运行前端展示应用程序。

**先决条件：**
* Node.js 和 `pnpm`

**工作流程（从 `awesome-skills-showcase` 目录开始）：**

```bash
# 导航到 Web 应用程序目录
cd awesome-skills-showcase

# 安装依赖项
pnpm install

# 运行开发服务器（自动同步 marketplace.json）
pnpm dev

# 为生产构建
pnpm build
```

---

## 开发约定

* **添加新技能：**
    1. 在 `config/external_skills_config.json` 中添加新条目。
    2. 运行 Python 检索和处理脚本以下载技能并更新 `marketplace.json`。
    3. 验证技能是否正确显示在展示 Web 应用程序中。

* **技能结构：** 每个技能都是一个自包含的目录。最重要的文件是 `SKILL.md`，它定义了技能的目的并包含其 `name`、`description` 等的 YAML 前置块。

* **Web 应用组件：** 展示应用程序使用现代 React 模式构建，利用 `radix-ui` 和 `shadcn/ui` 原则的组件，并使用 Tailwind CSS 进行样式设计。新的 UI 功能应遵循此约定。