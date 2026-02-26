<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:11:21
翻译模型: glm-4-flash
原文大小: 21,764 字符
-->

---
name: d3-viz
description: 使用 d3.js 创建交互式数据可视化。这项技能应在创建自定义图表、图形、网络图、地理可视化或任何需要精细控制视觉元素、过渡或交互的复杂 SVG 基于数据可视化时使用。无论在 React、Vue、Svelte、纯 JavaScript 或任何其他环境中，都可以使用此技能进行定制可视化，而超越标准图表库。
---

# D3.js 可视化

## 概述

这项技能提供了使用 d3.js 创建复杂、交互式数据可视化的指导。D3.js（数据驱动文档）擅长将数据绑定到 DOM 元素，并应用数据驱动的转换来创建具有精确控制每个视觉元素的定制、出版物质量的可视化。这些技术在任何 JavaScript 环境中都适用，包括纯 JavaScript、React、Vue、Svelte 和其他框架。

## 何时使用 d3.js

**使用 d3.js 的场景：**
- 需要独特视觉编码或布局的自定义可视化
- 具有复杂平移、缩放或刷行为的交互式探索
- 网络图/图形可视化（力导向布局、树状图、层次结构、弦图）
- 具有自定义投影的地理可视化
- 需要平滑、编排过渡的可视化
- 具有精细样式控制的高质量图形
- 标准库中不可用的新型图表

**考虑替代方案：**
- 3D 可视化 - 使用 Three.js 代替

## 核心工作流程

### 1. 设置 d3.js

在脚本顶部导入 d3：

```javascript
import * as d3 from 'd3';
```

或使用 CDN 版本（7.x）：

```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```

所有模块（刻度、轴、形状、过渡等）都可通过 `d3` 命名空间访问。

### 2. 选择集成模式

**模式 A：直接 DOM 操作（推荐用于大多数情况）**
使用 d3 选择 DOM 元素并 imperative 地操作它们。这在任何 JavaScript 环境中都有效：

```javascript
function drawChart(data) {
  if (!data || data.length === 0) return;

  const svg = d3.select('#chart'); // 通过 ID、类或 DOM 元素选择

  // 清除以前的内容
  svg.selectAll("*").remove();

  // 设置尺寸
  const width = 800;
  const height = 400;
  const margin = { top: 20, right: 30, bottom: 40, left: 50 };

  // 创建刻度、轴和绘制可视化
  // ... d3 代码 ...
}

// 当数据更改时调用
drawChart(myData);
```

**模式 B：声明式渲染（用于具有模板的框架）**
使用 d3 进行数据计算（刻度、布局），但通过您的框架渲染元素：

```javascript
function getChartElements(data) {
  const xScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.value)])
    .range([0, 400]);

  return data.map((d, i) => ({
    x: 50,
    y: i * 30,
    width: xScale(d.value),
    height: 25
  }));
}

// 在 React 中：{getChartElements(data).map((d, i) => <rect key={i} {...d} fill="steelblue" />)}
// 在 Vue 中：v-for 指令遍历返回的数组
// 在纯 JavaScript 中：从返回的数据手动创建元素
```

对于具有过渡、交互或利用 d3 完全功能的复杂可视化，请使用模式 A。对于更简单的可视化或当您的框架更喜欢声明式渲染时，请使用模式 B。

### 3. 结构化可视化代码

在您的绘图函数中遵循以下标准结构：

```javascript
function drawVisualization(data) {
  if (!data || data.length === 0) return;

  const svg = d3.select('#chart'); // 或传递选择器/元素
  svg.selectAll("*").remove(); // 清除以前的渲染

  // 1. 定义尺寸
  const width = 800;
  const height = 400;
  const margin = { top: 20, right: 30, bottom: 40, left: 50 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;

  // 2. 创建带有边距的主要组
  const g = svg.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  // 3. 创建刻度
  const xScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.x)])
    .range([0, innerWidth]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.y)])
    .range([innerHeight, 0]); // 注意：反转用于 SVG 坐标

  // 4. 创建并附加轴
  const xAxis = d3.axisBottom(xScale);
  const yAxis = d3.axisLeft(yScale);

  g.append("g")
    .attr("transform", `translate(0,${innerHeight})`)
    .call(xAxis);

  g.append("g")
    .call(yAxis);

  // 5. 绑定数据和创建视觉元素
  g.selectAll("circle")
    .data(data)
    .join("circle")
    .attr("cx", d => xScale(d.x))
    .attr("cy", d => yScale(d.y))
    .attr("r", 5)
    .attr("fill", "steelblue");
}

// 当数据更改时调用
drawVisualization(myData);
```

### 4. 实现响应式尺寸

使可视化适应容器尺寸：

```javascript
function setupResponsiveChart(containerId, data) {
  const container = document.getElementById(containerId);
  const svg = d3.select(`#${containerId}`).append('svg');

  function updateChart() {
    const { width, height } = container.getBoundingClientRect();
    svg.attr('width', width).attr('height', height);

    // 使用新尺寸重新绘制可视化
    drawChart(data, svg, width, height);
  }

  // 初始加载时更新
  updateChart();

  // 窗口尺寸变化时更新
  window.addEventListener('resize', updateChart);

  // 返回清理函数
  return () => window.removeEventListener('resize', updateChart);
}

// 使用：
// const cleanup = setupResponsiveChart('chart-container', myData);
// cleanup(); // 当组件卸载或元素删除时调用
```

或使用 ResizeObserver 进行更直接的容器监控：

```javascript
function setupResponsiveChartWithObserver(svgElement, data) {
  const observer = new ResizeObserver(() => {
    const { width, height } = svgElement.getBoundingClientRect();
    d3.select(svgElement)
      .attr('width', width)
      .attr('height', height);

    // 重新绘制可视化
    drawChart(data, d3.select(svgElement), width, height);
  });

  observer.observe(svgElement.parentElement);
  return () => observer.disconnect();
}
```

## 常见可视化模式

### 条形图

```javascript
function drawBarChart(data, svgElement) {
  if (!data || data.length === 0) return;

  const svg = d3.select(svgElement);
  svg.selectAll("*").remove();

  const width = 800;
  const height = 400;
  const margin = { top: 20, right: 30, bottom: 40, left: 50 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;

  const g = svg.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  const xScale = d3.scaleBand()
    .domain(data.map(d => d.category))
    .range([0, innerWidth])
    .padding(0.1);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.value)])
    .range([innerHeight, 0]);

  g.append("g")
    .attr("transform", `translate(0,${innerHeight})`)
    .call(d3.axisBottom(xScale));

  g.append("g")
    .call(d3.axisLeft(yScale));

  g.selectAll("rect")
    .data(data)
    .join("rect")
    .attr("x", d => xScale(d.category))
    .attr("y", d => yScale(d.value))
    .attr("width", xScale.bandwidth())
    .attr("height", d => innerHeight - yScale(d.value))
    .attr("fill", "steelblue");
}

// 使用：
// drawBarChart(myData, document.getElementById('chart'));
```

### 折线图

```javascript
const line = d3.line()
  .x(d => xScale(d.date))
  .y(d => yScale(d.value))
  .curve(d3.curveMonotoneX); // 平滑曲线

g.append("path")
  .datum(data)
  .attr("fill", "none")
  .attr("stroke", "steelblue")
  .attr("stroke-width", 2)
  .attr("d", line);
```

### 散点图

```javascript
g.selectAll("circle")
  .data(data)
  .join("circle")
  .attr("cx", d => xScale(d.x))
  .attr("cy", d => yScale(d.y))
  .attr("r", d => sizeScale(d.size)) // 可选：大小编码
  .attr("fill", d => colourScale(d.category)) // 可选：颜色编码
  .attr("opacity", 0.7);
```

### 弦图

弦图显示实体之间的关系，在圆形布局中，用带子表示它们之间的流动：

```javascript
function drawChordDiagram(data) {
  // 数据格式：包含源、目标和值的对象的数组
  // 示例：[{ source: 'A', target: 'B', value: 10 }, ...]

  if