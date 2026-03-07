---
name: vercel-deploy
description: 将应用程序和网站部署到 Vercel。当用户请求部署操作时，请使用此技能，例如“部署我的应用”、“将此部署到生产环境”、“创建预览部署”、“部署并发给我链接”或“推送此内容”。无需身份验证 - 返回预览 URL 和可认领的部署链接。
---

# Vercel Deploy

立即将任何项目部署到 Vercel。无需身份验证。

## 工作原理

1. 将您的项目打包成 tarball（排除 `node_modules` 和 `.git`）
2. 从 `package.json` 自动检测框架
3. 上传到部署服务
4. 返回 **预览 URL**（实时网站）和 **认领 URL**（转移到您的 Vercel 账户）

## 使用方法

```bash
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh [路径]
```

**参数：**
- `path` - 部署目录，或 `.tgz` 文件（默认为当前目录）

**示例：**

```bash
# 部署当前目录
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh

# 部署特定项目
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh /path/to/project

# 部署现有 tarball
bash /mnt/skills/user/vercel-deploy/scripts/deploy.sh /path/to/project.tgz
```

## 输出

```
准备部署...
检测到框架：nextjs
创建部署包...
部署...
✓ 部署成功！

预览 URL：https://skill-deploy-abc123.vercel.app
认领 URL：   https://vercel.com/claim-deployment?code=...
```

脚本还将 JSON 输出到 stdout 以供程序使用：

```json
{
  "previewUrl": "https://skill-deploy-abc123.vercel.app",
  "claimUrl": "https://vercel.com/claim-deployment?code=...",
  "deploymentId": "dpl_...",
  "projectId": "prj_..."
}
```

## 框架检测

脚本从 `package.json` 自动检测框架。支持的框架包括：

- **React**: Next.js, Gatsby, Create React App, Remix, React Router
- **Vue**: Nuxt, Vitepress, Vuepress, Gridsome
- **Svelte**: SvelteKit, Svelte, Sapper
- **其他前端**: Astro, Solid Start, Angular, Ember, Preact, Docusaurus
- **后端**: Express, Hono, Fastify, NestJS, Elysia, h3, Nitro
- **构建工具**: Vite, Parcel
- **更多**: Blitz, Hydrogen, RedwoodJS, Storybook, Sanity, 等。

对于没有 `package.json` 的静态 HTML 项目，框架设置为 `null`。

## 静态 HTML 项目

对于没有 `package.json` 的项目：
- 如果有一个非 `index.html` 命名的单个 `.html` 文件，它会被自动重命名
- 这确保了页面在根 URL (`/`) 上被服务

## 向用户展示结果

始终显示两个 URL：

```
✓ 部署成功！

预览 URL：https://skill-deploy-abc123.vercel.app
认领 URL：   https://vercel.com/claim-deployment?code=...

在预览 URL 中查看您的网站。
要将此部署转移到您的 Vercel 账户，请访问认领 URL。
```

## 故障排除

### 网络出口错误

如果由于网络限制（在 claude.ai 上很常见）部署失败，请告诉用户：

````
部署失败，因为网络限制。要修复此问题：

1. 前往 https://claude.ai/admin-settings/capabilities
2. 将 *.vercel.com 添加到允许的域
3. 再次尝试部署
```