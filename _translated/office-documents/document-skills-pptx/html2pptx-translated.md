<!--
本文件由智谱 AI 自动翻译生成
原文件: html2pptx.md
翻译时间: 2025-12-12 16:13:14
翻译模型: glm-4-flash
原文大小: 19,836 字符
-->

---

# HTML 到 PowerPoint 指南

使用 `html2pptx.js` 库将 HTML 幻灯片转换为 PowerPoint 演示文稿，并保持准确的定位。

## 目录

1. [创建 HTML 幻灯片](#creating-html-slides)
2. [使用 html2pptx 库](#using-the-html2pptx-library)
3. [使用 PptxGenJS](#using-pptxgenjs)

---

## 创建 HTML 幻灯片

每个 HTML 幻灯片都必须包含正确的身体尺寸：

### 布局尺寸

- **16:9**（默认）：`width: 720pt; height: 405pt`
- **4:3**：`width: 720pt; height: 540pt`
- **16:10**：`width: 720pt; height: 450pt`

### 支持的元素

- `<p>`、`<h1>`-`<h6>` - 带样式的文本
- `<ul>`、`<ol>` - 列表（切勿使用手动项目符号 •、-、*）
- `<b>`、`<strong>` - 加粗文本（内联格式）
- `<i>`、`<em>` - 斜体文本（内联格式）
- `<u>` - 下划线文本（内联格式）
- `<span>` - 带 CSS 样式的内联格式（加粗、斜体、下划线、颜色）
- `<br>` - 换行
- `<div>` with bg/border - 变成形状
- `<img>` - 图片
- `class="placeholder"` - 图表预留空间（返回 `{ id, x, y, w, h }`）

### 重要的文本规则

**所有文本都必须在 `<p>`、`<h1>`-`<h6>`、`<ul>` 或 `<ol>` 标签内：**
- ✅ 正确：`<div><p>文本在这里</p></div>`
- ❌ 错误：`<div>文本在这里</div>` - **文本将不会出现在 PowerPoint 中**
- ❌ 错误：`<span>文本</span>` - **文本将不会出现在 PowerPoint 中**
- `<div>` 或 `<span>` 中没有文本标签的文本将被静默忽略

**切勿使用手动项目符号符号（•、-、* 等）** - 使用 `<ul>` 或 `<ol>` 列表代替

**仅使用在互联网上普遍可用的字体：**
- ✅ 互联网安全字体：`Arial`、`Helvetica`、`Times New Roman`、`Georgia`、`Courier New`、`Verdana`、`Tahoma`、`Trebuchet MS`、`Impact`、`Comic Sans MS`
- ❌ 错误：`'Segoe UI'`、`'SF Pro'`、`'Roboto'`、自定义字体 - **可能会引起渲染问题**

### 样式

- 在身体上使用 `display: flex` 以防止边距折叠破坏溢出验证
- 使用 `margin` 进行间距（填充包含在大小中）
- 内联格式：使用 `<b>`、`<i>`、`<u>` 标签或带有 CSS 样式的 `<span>`（加粗、斜体、下划线、颜色）
  - `<span>` 支持：`font-weight: bold`、`font-style: italic`、`text-decoration: underline`、`color: #rrggbb`
  - `<span>` 不支持：`margin`、`padding`（在 PowerPoint 文本运行中不受支持）
  - 示例：`<span style="font-weight: bold; color: #667eea;">加粗蓝色文本</span>`
- Flexbox 工作正常 - 位置从渲染布局计算得出
- 使用带 `#` 前缀的十六进制颜色在 CSS 中
- **文本对齐**：当需要时使用 CSS `text-align`（`center`、`right` 等）作为 PptxGenJS 对文本格式化的提示，如果文本长度略有不同

### 形状样式（仅限 DIV 元素）

**重要提示：背景、边框和阴影仅在 `<div>` 元素上工作，不在文本元素（`<p>`、`<h1>`-`<h6>`、`<ul>`、`<ol>`）上**

- **背景**：CSS `background` 或 `background-color` 仅在 `<div>` 元素上
  - 示例：`<div style="background: #f0f0f0;">` - 创建具有背景的形状
- **边框**：CSS `border` 在 `<div>` 元素上转换为 PowerPoint 形状边框
  - 支持均匀边框：`border: 2px solid #333333`
  - 支持部分边框：`border-left`、`border-right`、`border-top`、`border-bottom`（渲染为线形状）
  - 示例：`<div style="border-left: 8pt solid #E76F51;">`
- **边框半径**：CSS `border-radius` 在 `<div>` 元素上为圆角
  - `border-radius: 50%` 或更高创建圆形形状
  - 百分比 <50% 相对于形状的较小维度计算
  - 支持 px 和 pt 单位（例如，`border-radius: 8pt;`、`border-radius: 12px;`)
  - 示例：`<div style="border-radius: 25%;">` 在 100x200px 矩形上 = 25% 的 100px = 25px 半径
- **盒阴影**：CSS `box-shadow` 在 `<div>` 元素上转换为 PowerPoint 阴影
  - 仅支持外部阴影（内嵌阴影被忽略以防止损坏）
  - 示例：`<div style="box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);">`
  - 注意：内嵌/内部阴影不受 PowerPoint 支持，将被跳过

### 图标和渐变

- **重要提示：切勿使用 CSS 渐变（`linear-gradient`、`radial-gradient`）** - 它们无法转换为 PowerPoint
- **始终首先使用 Sharp 创建渐变/图标 PNG，然后将其引用到 HTML 中**
- 对于渐变：将 SVG 渲染为 PNG 背景图像
- 对于图标：将 react-icons SVG 渲染为 PNG 图像
- 所有视觉效果都必须在 HTML 渲染之前作为位图图像预先渲染

**使用 Sharp 渲染图标：**

```javascript
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const sharp = require('sharp');
const { FaHome } = require('react-icons/fa');

async function rasterizeIconPng(IconComponent, color, size = "256", filename) {
  const svgString = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color: `#${color}`, size: size })
  );

  // 使用 Sharp 将 SVG 转换为 PNG
  await sharp(Buffer.from(svgString))
    .png()
    .toFile(filename);

  return filename;
}

// 使用：在 HTML 中使用之前渲染图标
const iconPath = await rasterizeIconPng(FaHome, "4472c4", "256", "home-icon.png");
// 然后在 HTML 中引用：`<img src="home-icon.png" style="width: 40pt; height: 40pt;">`
```

**使用 Sharp 渲染渐变：**

```javascript
const sharp = require('sharp');

async function createGradientBackground(filename) {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="562.5">
    <defs>
      <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#COLOR1"/>
        <stop offset="100%" style="stop-color:#COLOR2"/>
      </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#g)"/>
  </svg>`;

  await sharp(Buffer.from(svg))
    .png()
    .toFile(filename);

  return filename;
}

// 使用：在 HTML 中创建渐变背景之前
const bgPath = await createGradientBackground("gradient-bg.png");
// 然后在 HTML 中：`<body style="background-image: url('gradient-bg.png');">`
```

### 示例

```html
<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  background: #f5f5f5; font-family: Arial, sans-serif;
  display: flex;
}
.content { margin: 30pt; padding: 40pt; background: #ffffff; border-radius: 8pt; }
h1 { color: #2d3748; font-size: 32pt; }
.box {
  background: #70ad47; padding: 20pt; border: 3px solid #5a8f37;
  border-radius: 12pt; box-shadow: 3px 3px 10px rgba(0, 0,