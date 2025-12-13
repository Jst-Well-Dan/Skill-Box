<!--
本文件由智谱 AI 自动翻译生成
原文件: colour-schemes.md
翻译时间: 2025-12-12 16:12:20
翻译模型: glm-4-flash
原文大小: 12,759 字符
-->

# D3.js 颜色方案和调色板推荐

数据可视化中颜色选择的全面指南。

## 内置分类颜色方案

### Category10（默认）

```javascript
d3.schemeCategory10
// ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
//  '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
```

**特点：**
- 10种不同的颜色
- 色盲友好
- 大多数分类数据的默认选择
- 平衡的饱和度和亮度

**使用场景：** 通用分类编码、图例项、多个数据系列

### Tableau10

```javascript
d3.schemeTableau10
```

**特点：**
- 优化数据可视化的10种颜色
- 专业外观
- 优秀的可区分性

**使用场景：** 商业仪表板、专业报告、演示文稿

### Accent

```javascript
d3.schemeAccent
// 8种高饱和度颜色
```

**特点：**
- 明亮、鲜艳的颜色
- 高对比度
- 现代美学

**使用场景：** 突出重要类别、现代网络应用程序

### Dark2

```javascript
d3.schemeDark2
// 8种较暗、柔和的颜色
```

**特点：**
- 暗色调
- 专业外观
- 适合深色背景

**使用场景：** 暗模式可视化、专业环境

### Paired

```javascript
d3.schemePaired
// 12种颜色，分为相似色调的配对
```

**特点：**
- 亮色和暗色变体的配对
- 适用于嵌套类别
- 12种不同的颜色

**使用场景：** 分组条形图、层次类别、前后比较

### Pastel1 & Pastel2

```javascript
d3.schemePastel1 // 9种颜色
d3.schemePastel2 // 8种颜色
```

**特点：**
- 柔软、低饱和度颜色
- 外观温和
- 适合大区域

**使用场景：** 背景颜色、细微分类、舒缓的视觉呈现

### Set1, Set2, Set3

```javascript
d3.schemeSet1 // 9种颜色 - 鲜艳
d3.schemeSet2 // 8种颜色 - 暗淡
d3.schemeSet3 // 12种颜色 - 浅色调
```

**特点：**
- Set1：高饱和度，最大区分度
- Set2：专业，平衡
- Set3：微妙，许多类别

**使用场景：** 根据视觉层次需求变化

## 顺序颜色方案

顺序方案使用单一色调或渐变将连续数据从低到高值映射。

### 单色调顺序

**蓝色：**
```javascript
d3.interpolateBlues
d3.schemeBlues[9] // 9步离散版本
```

**其他单色调选项：**
- `d3.interpolateGreens` / `d3.schemeGreens`
- `d3.interpolateOranges` / `d3.schemeOranges`
- `d3.interpolatePurples` / `d3.schemePurples`
- `d3.interpolateReds` / `d3.schemeReds`
- `d3.interpolateGreys` / `d3.schemeGreys`

**使用场景：**
- 简单热图
- 彩色图
- 密度图
- 单一指标可视化

### 多色调顺序

**Viridis（推荐）：**
```javascript
d3.interpolateViridis
```

**特点：**
- 感知均匀
- 色盲友好
- 打印安全
- 无视觉死区
- 感知亮度单调递增

**其他感知均匀选项：**
- `d3.interpolatePlasma` - 紫色到黄色
- `d3.interpolateInferno` - 黑色通过红色/橙色到白色
- `d3.interpolateMagma` - 黑色通过紫色到白色
- `d3.interpolateCividis` - 色盲优化

**色盲友好：**
```javascript
d3.interpolateTurbo // 类似彩虹但感知均匀
d3.interpolateCool  // 青色到洋红色
d3.interpolateWarm  // 橙色到黄色
```

**使用场景：**
- 科学可视化
- 医学成像
- 任何高精度数据可视化
- 可访问性可视化

### 传统顺序

**黄色-橙色-红色：**
```javascript
d3.interpolateYlOrRd
d3.schemeYlOrRd[9]
```

**黄色-绿色-蓝色：**
```javascript
d3.interpolateYlGnBu
d3.schemeYlGnBu[9]
```

**其他多色调：**
- `d3.interpolateBuGn` - 蓝到绿
- `d3.interpolateBuPu` - 蓝到紫
- `d3.interpolateGnBu` - 绿到蓝
- `d3.interpolateOrRd` - 橙到红
- `d3.interpolatePuBu` - 紫到蓝
- `d3.interpolatePuBuGn` - 紫到蓝绿
- `d3.interpolatePuRd` - 紫到红
- `d3.interpolateRdPu` - 红到紫
- `d3.interpolateYlGn` - 黄到绿
- `d3.interpolateYlOrBr` - 黄到橙棕色

**使用场景：** 传统数据可视化，熟悉的颜色关联（温度、植被、水）

## 分离颜色方案

分离方案使用两种不同的色调突出中心值周围的偏差。

### 红蓝（温度）

```javascript
d3.interpolateRdBu
d3.schemeRdBu[11]
```

**特点：**
- 直观的温度隐喻
- 强烈对比
- 清晰的正负区分

**使用场景：** 温度、盈亏、高于/低于平均值、相关性

### 红黄蓝

```javascript
d3.interpolateRdYlBu
d3.schemeRdYlBu[11]
```

**特点：**
- 三色渐变
- 通过黄色更柔和的过渡
- 更多的视觉步骤

**使用场景：** 当极端值需要强调且中间需要可见性时

### 其他分离方案

**交通灯：**
```javascript
d3.interpolateRdYlGn // 红色（不好）到绿色（好）
```

**光谱（彩虹）：**
```javascript
d3.interpolateSpectral // 全光谱
```

**其他选项：**
- `d3.interpolateBrBG` - 棕色到蓝绿色
- `d3.interpolatePiYG` - 粉红色到黄绿色
- `d3.interpolatePRGn` - 紫色到绿色
- `d3.interpolatePuOr` - 紫色到橙色
- `d3.interpolateRdGy` - 红到灰

**使用场景：** 根据语义意义和可访问性需求选择

## 色盲友好调色板

### 一般指南

1. **避免红绿色组合**（最常见的色盲）
2. **使用蓝橙色分离**代替红绿色
3. **添加纹理或图案**作为冗余编码
4. **使用模拟工具测试**

### 推荐的色盲安全方案

**分类：**
```javascript
// Okabe-Ito 调色板（色盲安全）
const okabePalette = [
  '#E69F00', // 橙色
  '#56B4E9', // 天蓝色
  '#009E73', // 蓝绿色
  '#F0E442', // 黄色
  '#0072B2', // 蓝色
  '#D55E00', // 朱红色
  '#CC79A7', // 红紫色
  '#000000'  // 黑色
];

const colourScale = d3.scaleOrdinal()
  .domain(categories)
  .range(okabePalette);
```

**顺序：**
```javascript
// 使用 Viridis、Cividis 或 Blues
d3.interpolateViridis  // 最佳整体
d3.interpolateCividis  // 优化 CVD
d3.interpolateBlues    // 简单、安全
```

**分离：**
```javascript
// 使用蓝橙色而不是红绿色
d3.interpolateBrBG
d3.interpolatePuOr
```

## 自定义颜色调色板

### 创建自定义顺序

```javascript
const customSequential = d3.scaleLinear()
  .domain([0, 100])
  .range(['#e8f4f8', '#006d9c']) // 淡蓝到深蓝
  .interpolate(d3.interpolateLab); // 感知均匀
```

### 创建自定义分离

```javascript
const customDiverging = d3.scaleLinear()
  .domain([0, 50, 100])
  .range(['#ca0020', '#f7f7f7', '#0571b0']) // 红色、灰色、蓝色
  .interpolate(d3.interpolateLab);
```

### 创建自定义分类

```javascript
// 品牌颜色
const brandPalette = [
  '#FF6B6B', // 主要红色
  '#4ECDC4', // 次要青色
  '#45B7D1', // 次要蓝色
  '#FFA07A', // 强调珊瑚色
  '#98D8C8'  // 强调薄荷色
];

const colourScale = d3.scaleOrdinal()
  .domain(categories)
  .range(brandPalette);
```

## 语义颜色关联

### 通用的颜色含义

**红色：**
- 危险、错误、负面
- 高温
- 债务、亏损

**绿色：**
- 成功、正面
- 成长、植被
- 盈利、收益

**蓝色：**
- 信任、平静
- 水、冷
- 信息、中性

**黄色/橙色：**
- 警告、注意
- 能量、温暖
- 注意力

**灰色：**
- 中性、不活跃
- 缺失数据
- 背景

### 上下文特定的调色板

**金融：**
```javascript
const financialColours = {
  profit: '#27ae60',
  loss: '#e74c3c',
  neutral: '#95a5a6',
  highlight: '#3498db'
};
```

**温度：**
```javascript
const temperatureScale = d3.scaleSequential(d3.interpolateRdYlBu)
  .domain([40, -10]); // 热到冷（反转）
```

**交通/状态：**
```javascript
const statusColours = {
  success: '#27ae60',
  warning: '#f39c12',
  error: '#e74c3c',
  info: '#3498db',
  neutral: '#95a5a6'
};
```

## 可访问性最佳实践

### 对比度

确保颜色和背景之间的对比度足够：

```javascript
// 良好的对比度示例
const highContrast = {
  background: '#ffffff',
  text: '#2c3e50',
  primary: '#3498db',
  secondary: '#e74c3c'
};
```

**WCAG 指南：**
- 正常文本：4.5:1 最小
- 大号文本：3:1 最小
- UI 组件：3:1 最小

### 冗余编码

永远不要仅依靠颜色传达信息：

```javascript
// 添加图案或形状
const symbols = ['circle', 'square', 'triangle', 'diamond'];

// 添加文本标签
// 使用线型（实线、虚线、点线）
// 使用大小编码
```

### 测试

测试视觉呈现的色盲：

- Chrome DevTools（渲染 > 模拟视觉缺陷）
- 色彩橙（免费桌面应用程序）
- Coblis（在线模拟器）

## 专业颜色推荐

### 数据新闻

```javascript
// 守护者风格
const guardianPalette = [
  '#005689', // 守护者蓝色
  '#c70000', // 守护者红色
  '#7d0068', // 守护者粉色
  '#951c75', // 守护者紫色
];

// FT 风格
const ftPalette = [
  '#0f5499', // FT 蓝色
  '#990f3d', // FT 红色
  '#593380', // FT 紫色
  '#262a33', // FT 黑色
];
```

### 学术/科学

```javascript
// 自然期刊风格
const naturePalette = [
  '#0071b2', // 蓝色
  '#d55e00', // 朱红色
  '#009e73', // 绿色
  '#f0e442', // 黄色
];

// 使用 Viridis 进行连续数据
const scientificScale = d3.scaleSequential(d3.interpolateViridis);
```

### 企业/商业

```javascript
// 专业、保守
const corporatePalette = [
  '#003f5c', // 深蓝色
  '#58508d', // 紫色
  '#bc5090', // 紫红色
  '#ff6361', // 珊瑚色
  '#ffa600'  // 橙色
];
```

## 动态颜色选择

### 基于数据范围

```javascript
function selectColourScheme(data) {
  const extent = d3.extent(data);
  const hasNegative = extent[0] < 0;
  const hasPositive = extent[1] > 0;
  
  if (hasNegative && hasPositive) {
    // 分离：数据跨越零
    return d3.scaleSequentialSymlog(d3.interpolateRdBu)
      .domain([extent[0], 0, extent[1]]);
  } else {
    // 顺序：全部为正或全部为负
    return d3.scaleSequential(d3.interpolateViridis)
      .domain(extent);
  }
}
```

### 基于类别数量

```javascript
function selectCategoricalScheme(categories) {
  const n = categories.length;
  
  if (n <= 10) {
    return d3.scaleOrdinal(d3.schemeTableau10);
  } else if (n <= 12) {
    return d3.scaleOrdinal(d3.schemePaired);
  } else {
    // 对于许多类别，使用顺序与量化
    return d3.scaleQuantize()
      .domain([0, n - 1])
      .range(d3.quantize(d3.interpolateRainbow, n));
  }
}
```

## 避免的常见颜色错误

1. **彩虹渐变用于顺序数据**
   - 问题：不是感知均匀的，难以阅读
   - 解决方案：使用 Viridis、Blues 或其他均匀方案

2. **红绿色用于分离（色盲）**
   - 问题：8% 的男性无法区分
   - 解决方案：使用蓝橙色或紫绿色

3. **过多的分类颜色**
   - 问题：难以区分和记忆
   - 解决方案：限制为 5-8 个类别，使用分组

4. **对比度不足**
   - 问题：可读性差
   - 解决方案：测试对比度比率，使用深色在浅色背景上

5. **文化不一致的颜色**
   - 问题：混淆语义意义
   - 解决方案：研究目标受众的颜色关联

6. **反转温度尺度**
   - 问题：反直觉（红色 = 冷）
   - 解决方案：红色/橙色 = 热，蓝色 = 冷

## 快速参考指南

**需要显示...**

- **类别（≤10）：** `d3.schemeCategory10` 或 `d3.schemeTableau10`
- **类别（>10）：** `d3.schemePaired` 或分组类别
- **顺序（通用）：** `d3.interpolateViridis`
- **顺序（科学）：** `d3.interpolateViridis` 或 `d3.interpolatePlasma`
- **顺序（温度）：** `d3.interpolateRdYlBu`（反转）
- **分离（零）：** `d3.interpolateRdBu` 或 `d3.interpolateBrBG`
- **分离（好/坏）：** `d3.interpolateRdYlGn`（反转）
- **色盲安全（分类）：** Okabe-Ito 调色板（如上所示）
- **色盲安全（顺序）：** `d3.interpolateCividis` 或 `d3.interpolateBlues`
- **色盲安全（分离）：** `d3.interpolatePuOr` 或 `d3.interpolateBrBG`

**始终记住：**
1. 测试色盲
2. 确保足够的对比度
3. 适当地使用语义颜色
4. 添加冗余编码（图案、标签）
5. 简单（颜色越少 = 可视化越清晰）