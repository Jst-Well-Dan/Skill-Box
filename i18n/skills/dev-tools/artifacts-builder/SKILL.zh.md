---
name: artifacts-builder
description: 使用现代前端 Web 技术（React、Tailwind CSS、shadcn/ui）创建复杂的、多组件的 claude.ai HTML Artifacts 的工具套件。适用于需要状态管理、路由或 shadcn/ui 组件的复杂 Artifacts - 而不是简单的单文件 HTML/JSX Artifacts。
license: Complete terms in LICENSE.txt
---

# Artifacts Builder

要构建强大的前端 claude.ai 文件，请按照以下步骤操作：
1. 使用 `scripts/init-artifact.sh` 初始化前端仓库
2. 通过编辑生成的代码来开发您的文件
3. 使用 `scripts/bundle-artifact.sh` 将所有代码打包成一个单独的 HTML 文件
4. 向用户展示文件
5. （可选）测试文件

**技术栈**：React 18 + TypeScript + Vite + Parcel（打包）+ Tailwind CSS + shadcn/ui

## 设计与风格指南

非常重要：为了避免所谓的“AI slop”，请避免使用过多的居中布局、紫色渐变、统一的圆角和 Inter 字体。

## 快速入门

### 第 1 步：初始化项目

运行初始化脚本以创建一个新的 React 项目：
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

这将创建一个完全配置的项目，包括：
- ✅ React + TypeScript（通过 Vite）
- ✅ Tailwind CSS 3.4.1 与 shadcn/ui 主题系统
- ✅ 路径别名 (`@/`) 已配置
- ✅ 预装 40 多个 shadcn/ui 组件
- ✅ 包含所有 Radix UI 依赖项
- ✅ Parcel 已配置用于打包（通过 .parcelrc）
- ✅ Node 18+ 兼容性（自动检测并固定 Vite 版本）

### 第 2 步：开发您的文件

要构建文件，请编辑生成的文件。有关指导，请参阅下文的 **常见开发任务**。

### 第 3 步：打包到单个 HTML 文件

要将 React 应用程序打包成单个 HTML 文件：
```bash
bash scripts/bundle-artifact.sh
```

这将创建 `bundle.html` - 一个包含所有 JavaScript、CSS 和依赖项的内联自包含文件。此文件可以直接在 Claude 对话中作为文件分享。

**要求**：您的项目必须在根目录中有一个 `index.html` 文件。

**脚本执行的操作**：
- 安装打包依赖项（parcel、@parcel/config-default、parcel-resolver-tspaths、html-inline）
- 创建带有路径别名支持的 `.parcelrc` 配置
- 使用 Parcel 构建（无源映射）
- 使用 html-inline 将所有资源内联到单个 HTML 文件中

### 第 4 步：与用户分享文件

最后，将打包的 HTML 文件在对话中与用户分享，以便他们可以将其作为文件查看。

### 第 5 步：测试/可视化文件（可选）

注意：这是一个完全可选的步骤。只有当有必要或被要求时才执行。

要测试/可视化文件，请使用可用的工具（包括其他技能或内置工具，如 Playwright 或 Puppeteer）。通常，避免在文件准备就绪之前测试文件，因为这会在请求和最终文件可见之间增加延迟。如果需要或出现问题时，请在展示文件后进行测试。

## 参考

- **shadcn/ui 组件**：https://ui.shadcn.com/docs/components