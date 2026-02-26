<!--
本文件由智谱 AI 自动翻译生成
原文件: CLAUDE.md
翻译时间: 2025-12-12 16:11:26
翻译模型: glm-4-flash
原文大小: 9,157 字符
-->

# CLAUDE.md

本文件为在存储库中工作时使用 Claude 代码（claude.ai/code）提供指导。

## 存储库概述

这是 Claude 技能宝库，一个包含 47+ 实用 Claude 技能的精选集合，这些技能分布在 8 个类别中。存储库既是一个技能市场，也是一个管理和分发技能的框架。技能是模块化包，通过专业知识、工作流程和工具集成扩展 Claude 的功能。

## 存储库结构

```
awesome-claude-skills/
├── .claude-plugin/
│   └── marketplace.json          # 所有 47+ 技能的中央注册表
│
├── Category Directories/          # 按类别组织的技能
│   ├── business-marketing/
│   ├── collaboration-project-management/
│   ├── communication-writing/
│   ├── creative-media/
│   ├── data-analysis/
│   ├── development/
│   ├── document-processing/
│   ├── document-skills/          # 过时的 Office 文档技能
│   └── productivity-organization/
│
├── scripts/                       # 技能管理的 Python 自动化脚本
│   ├── fetch_external_skills.py  # 获取外部技能的主要协调器
│   ├── github_fetcher.py         # GitHub API 交互
│   ├── marketplace_updater.py    # 更新 marketplace.json
│   ├── skill_processor.py        # 验证和处理技能
│   └── utils.py                  # 公共工具
│
├── config/
│   └── external_skills_config.json  # 外部技能源配置
│
├── awesome-skills-showcase/      # React/Vite 网页展示应用程序
│   ├── src/                      # TypeScript/React 源代码
│   └── package.json              # Node.js 依赖项和脚本
│
└── requirements.txt              # Python 依赖项
```

## 技能结构

每个技能都遵循标准化的结构：

```
skill-name/
├── SKILL.md (必需)
│   ├── YAML 前置元数据与名称和描述
│   └── Markdown 指令
└── 可选目录：
    ├── scripts/      # 可执行代码（Python/Bash）
    ├── references/   # 需要时加载的文档
    └── assets/       # 模板、图像等。
```

YAML 前置元数据中的 `name` 和 `description` 是关键的 - 它们决定了 Claude 何时激活技能。

## Python 环境和脚本

### 依赖项

在运行脚本之前安装 Python 依赖项：
```bash
pip install -r requirements.txt
```

必需的包：
- `requests>=2.31.0` - 用于 GitHub API 的 HTTP 请求
- `python-frontmatter>=1.1.0` - 解析 SKILL.md 文件中的 YAML 前置元数据
- `PyYAML>=6.0.1` - YAML 解析
- `jsonschema>=4.20.0` - 验证 JSON 架构

### 获取外部技能

主要的自动化工具是 `fetch_external_skills.py`，它从外部 GitHub 存储库获取技能并将它们集成到市场中。

**基本用法：**
```bash
# 获取所有配置的技能
python scripts/fetch_external_skills.py --all

# 通过 ID 获取特定技能
python scripts/fetch_external_skills.py --skill markdown-to-epub-converter

# 干运行（模拟而不写入）
python scripts/fetch_external_skills.py --dry-run --all

# 强制重新获取现有技能
python scripts/fetch_external_skills.py --force --all

# 使用自定义配置文件
python scripts/fetch_external_skills.py --config path/to/config.json
```

**配置：**
外部技能在 `config/external_skills_config.json` 中定义。每个技能条目包括：
- `id` - 唯一标识符
- `github_url` - 源存储库 URL
- `repo_type` - 类型：`standalone`、`multi_skill`
- `target_folder` - 目标目录
- `category` - 市场类别
- `extraction_config` - 如何从存储库提取：
  - `full_repo` - 克隆整个存储库
  - `subfolder` - 提取特定子目录
  - `deep_nested` - 提取深层嵌套子目录

### 脚本架构

获取系统是模块化的：

1. **fetch_external_skills.py** - 主要协调器
   - 加载配置
   - 验证环境
   - 协调获取工作流程
   - 生成执行报告

2. **github_fetcher.py** - GitHub 交互
   - 处理 GitHub API 认证（使用 `GITHUB_TOKEN` 环境变量）
   - 通过 API 或 git 克隆下载存储库
   - 根据配置提取特定子目录

3. **skill_processor.py** - 技能验证
   - 验证 SKILL.md 结构和前置元数据
   - 检查必需的元数据（名称、描述）
   - 规范化技能元数据

4. **marketplace_updater.py** - 注册表管理
   - 更新 `.claude-plugin/marketplace.json`
   - 将新技能与现有技能合并
   - 维护市场架构

## 网页展示应用程序

`awesome-skills-showcase/` 目录包含一个用于浏览技能的 React/Vite 网页应用程序。

### 开发命令

```bash
# 导航到展示目录
cd awesome-skills-showcase

# 安装依赖项（如果尚未安装）
pnpm install

# 启动开发服务器（默认：http://localhost:5173）
pnpm dev

# 为生产构建
pnpm build

# TypeScript 类型检查
pnpm build  # 包括 tsc -b

# 代码检查
pnpm lint

# 预览生产构建
pnpm preview
```

### 技术堆栈

- **React 19.2** - UI 框架
- **TypeScript** - 类型安全
- **Vite 7** - 构建工具和开发服务器
- **Tailwind CSS 3.4** - 样式
- **Radix UI** - 无头 UI 组件
- **shadcn/ui patterns** - UI 组件模式
- **Lucide React** - 图标

## 市场注册表

`.claude-plugin/marketplace.json` 文件是中央注册表。它遵循此架构：

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "awesome-claude-skills",
  "version": "1.0.0",
  "description": "...",
  "owner": { "name": "...", "email": "..." },
  "plugins": [
    {
      "name": "skill-name",
      "description": "当何时使用此技能...",
      "source": "./category/skill-folder",
      "category": "category-name"
    }
  ]
}
```

当手动添加新技能时，请确保：
1. 技能目录包含有效的 `SKILL.md`，其中包含前置元数据
2. `source` 路径相对于存储库根目录
3. `description` 清楚地说明 Claude 应何时使用该技能
4. 技能放置在适当的类别目录中

## 创建新技能

使用 `skill-creator` 技能（在 `development/skill-creator/` 中）进行指导。关键原则：

1. **必需**：包含 `name` 和 `description` 的 YAML 前置元数据的 `SKILL.md`
2. **描述质量**：具体说明 Claude 应何时使用该技能（使用第三人称）
3. **渐进式披露**：保持 SKILL.md 精简（最多 5k 字），使用 `references/` 进行详细文档
4. **脚本用于确定性任务**：当相同的代码被反复重写时，将可执行代码放在 `scripts/`
5. **资产用于输出**：使用 `assets/` 用于模板、图像或用于输出的文件（不加载到上下文中）

模板结构可在 `development/template-skill/` 中找到。

## Git 工作流程

**当前分支**：master
**主分支**：master（用于 PR）

提交更改时：
- 通过 `git log` 检查最近的提交来遵循常规提交风格
- 如同最近的提交所示，包括合著者归属
- 除非明确请求，否则不要提交以跳过测试或钩子

## 常见开发模式

### 手动添加新技能

1. 在适当的类别文件夹中创建技能目录
2. 编写包含正确前置元数据的 `SKILL.md`
3. 根据需要添加可选的 `scripts/`、`references/` 或 `assets/`
4. 将新条目更新到 `.claude-plugin/marketplace.json`
5. 通过在 Claude Code 中使用它来测试技能激活

### 从外部来源获取技能

1. 将技能配置添加到 `config/external_skills_config.json`
2. 运行：`python scripts/fetch_external_skills.py --skill <skill-id>`
3. 验证技能是否被正确地获取到正确的类别目录
4. 确认 `marketplace.json` 已更新

### 修改展示网页应用程序

1. 导航到 `awesome-skills-showcase/`
2. 运行 `pnpm dev` 以进行热重载开发
3. 编辑 `src/` 中的 TypeScript/React 文件
4. 在提交之前使用 `pnpm build` 进行构建

## 重要文件

- **marketplace.json** - 中央注册表，不要破坏 JSON 结构
- **external_skills_config.json** - 自动化技能获取的配置
- **requirements.txt** - 自动化脚本的 Python 依赖项
- **SKILL.md 文件** - 每个技能的定义，必须具有有效的 YAML 前置元数据
- **README.md** - 公共文档，保持与实际技能数量同步

## 类别

1. **development** - 软件开发、测试、代码质量（14 个技能）
2. **productivity-organization** - 任务管理、文档处理（10 个技能）
3. **communication-writing** - 内容创作、研究（6 个技能）
4. **creative-media** - 视觉内容、视频、创意工作（6 个技能）
5. **business-marketing** - 业务运营、营销（5 个技能）
6. **collaboration-project-management** - 团队协作、版本控制（3 个技能）
7. **data-analysis** - 数据分析和调试（2 个技能）
8. **document-processing** - 文档转换（1 个技能）

添加新技能时，将它们放置在最合适的类别中，如果需要，可以创建新类别。