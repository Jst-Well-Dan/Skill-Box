<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:10:29
翻译模型: glm-4-flash
原文大小: 3,065 字符
-->

---
name: artifacts-builder
description: 一套使用现代前端 Web 技术（React、Tailwind CSS、shadcn/ui）创建复杂、多组件 claude.ai HTML 艺术品的工具。用于需要状态管理、路由或 shadcn/ui 组件的复杂艺术品 - 不适用于简单的单文件 HTML/JSX 艺术品。
license: 详细条款请参阅 LICENSE.txt
---

# 艺术品构建器

要构建强大的前端 claude.ai 艺术品，请按照以下步骤操作：
1. 使用 `scripts/init-artifact.sh` 初始化前端仓库
2. 通过编辑生成的代码开发您的艺术品
3. 使用 `scripts/bundle-artifact.sh` 将所有代码打包成一个单独的 HTML 文件
4. 向用户展示艺术品
5. （可选）测试艺术品

**技术栈**：React 18 + TypeScript + Vite + Parcel（打包）+ Tailwind CSS + shadcn/ui

## 设计与风格指南

非常重要：为了避免所谓的“AI 混乱”，请避免使用过多的居中布局、紫色渐变、均匀的圆角和 Inter 字体。

## 快速入门

### 第 1 步：初始化项目

运行初始化脚本以创建一个新的 React 项目：
```bash
bash scripts/init-artifact.sh <项目名称>
cd <项目名称>
```

这将创建一个完全配置的项目，包括：
- ✅ React + TypeScript（通过 Vite）
- ✅ Tailwind CSS 3.4.1 与 shadcn/ui 主题系统
- ✅ 路径别名（`@/`）已配置
- ✅ 预安装 40 多个 shadcn/ui 组件
- ✅ 包含所有 Radix UI 依赖项
- ✅ Parcel 已配置用于打包（通过 .parcelrc）
- ✅ Node 18+ 兼容性（自动检测并固定 Vite 版本）

### 第 2 步：开发您的艺术品

要构建艺术品，请编辑生成的文件。有关指导，请参阅下文的 **常见开发任务**。

### 第 3 步：打包成单个 HTML 文件

要将 React 应用程序打包成一个单独的 HTML 艺术品：
```bash
bash scripts/bundle-artifact.sh
```

这将创建 `bundle.html` - 一个包含所有 JavaScript、CSS 和依赖项的内联艺术品。此文件可以直接在 Claude 对话中作为艺术品共享。

**要求**：您的项目必须在根目录中有一个 `index.html` 文件。

**脚本执行的操作**：
- 安装打包依赖项（parcel、@parcel/config-default、parcel-resolver-tspaths、html-inline）
- 创建具有路径别名支持的 `.parcelrc` 配置
- 使用 Parcel 构建（无源映射）
- 使用 html-inline 将所有资源内联到单个 HTML 文件中

### 第 4 步：与用户共享艺术品

最后，在对话中将打包的 HTML 文件与用户共享，以便他们可以将其作为艺术品查看。

### 第 5 步：测试/可视化艺术品（可选）

注意：这是一个完全可选的步骤。仅在必要时或被要求时执行。

要测试/可视化艺术品，请使用可用的工具（包括其他技能或内置工具，如 Playwright 或 Puppeteer）。通常，避免在艺术品准备好之前进行测试，因为这会在请求和完成的艺术品可见之间增加延迟。如果需要或出现问题时，在展示艺术品后进行测试。

## 参考

- **shadcn/ui 组件**：https://ui.shadcn.com/docs/components