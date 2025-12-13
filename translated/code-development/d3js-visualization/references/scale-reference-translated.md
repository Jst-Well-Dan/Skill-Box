<!--
本文件由智谱 AI 自动翻译生成
原文件: scale-reference.md
翻译时间: 2025-12-12 16:12:16
翻译模型: glm-4-flash
原文大小: 12,079 字符
-->

# D3.js 标度参考

全面指南，包括所有 d3 标度类型、示例和用例。

## 连续标度

### 线性标度

将连续输入域映射到连续输出范围，使用线性插值。

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range([0, 500]);

scale(50);  // 返回 250
scale(0);   // 返回 0
scale(100); // 返回 500

// 反转标度（从输出获取输入）
scale.invert(250); // 返回 50
```

**用例：**
- 定量数据最常见的标度
- 轴，条形长度，位置编码
- 温度，价格，计数，测量

**方法：**
- `.domain([min, max])` - 设置输入域
- `.range([min, max])` - 设置输出范围
- `.invert(value)` - 从输出值获取域值
- `.clamp(true)` - 将输出限制在范围边界内
- `.nice()` - 将域扩展到漂亮的整数值

### 幂标度

将连续输入映射到连续输出，使用指数转换。

```javascript
const sqrtScale = d3.scalePow()
  .exponent(0.5)  // 平方根
  .domain([0, 100])
  .range([0, 500]);

const squareScale = d3.scalePow()
  .exponent(2)  // 平方
  .domain([0, 100])
  .range([0, 500]);

// 平方根的简写
const sqrtScale2 = d3.scaleSqrt()
  .domain([0, 100])
  .range([0, 500]);
```

**用例：**
- 感知缩放（人类感知是非线性的）
- 面积编码（使用平方根将值映射到圆半径）
- 强调小或大值之间的差异

### 对数标度

将连续输入映射到连续输出，使用对数转换。

```javascript
const logScale = d3.scaleLog()
  .domain([1, 1000])  // 必须是正数
  .range([0, 500]);

logScale(1);    // 返回 0
logScale(10);   // 返回 ~167
logScale(100);  // 返回 ~333
logScale(1000); // 返回 500
```

**用例：**
- 跨越多个数量级的数据
- 人口，GDP，财富分布
- 对数轴
- 指数增长可视化

**重要提示：** 域值必须是严格正数（>0）。

### 时间标度

专门用于时间数据的线性标度。

```javascript
const timeScale = d3.scaleTime()
  .domain([new Date(2020, 0, 1), new Date(2024, 0, 1)])
  .range([0, 800]);

timeScale(new Date(2022, 0, 1)); // 返回 400

// 反转以获取日期
timeScale.invert(400); // 返回 mid-2022 的日期对象
```

**用例：**
- 时间序列可视化
- 时间轴
- 时间动画
- 基于日期的交互

**方法：**
- `.nice()` - 将域扩展到漂亮的时间间隔
- `.ticks(count)` - 生成间隔均匀的刻度值
- 所有线性标度方法都适用

### 离散标度

将连续输入映射到离散输出桶。

```javascript
const quantizeScale = d3.scaleQuantize()
  .domain([0, 100])
  .range(['low', 'medium', 'high']);

quantizeScale(25);  // 返回 'low'
quantizeScale(50);  // 返回 'medium'
quantizeScale(75);  // 返回 'high'

// 获取阈值值
quantizeScale.thresholds(); // 返回 [33.33, 66.67]
```

**用例：**
- 分箱连续数据
- 热图颜色
- 风险类别（低/中/高）
- 年龄组，收入区间

### 分位数标度

根据分位数将连续输入映射到离散输出。

```javascript
const quantileScale = d3.scaleQuantile()
  .domain([3, 6, 7, 8, 8, 10, 13, 15, 16, 20, 24]) // 样本数据
  .range(['low', 'medium', 'high']);

quantileScale(8);  // 根据分位数位置返回
quantileScale.quantiles(); // 返回分位数阈值
```

**用例：**
- 等大小组，无论分布如何
- 百分比分类
- 处理偏斜分布

### 阈值标度

将连续输入映射到离散输出，具有自定义阈值。

```javascript
const thresholdScale = d3.scaleThreshold()
  .domain([0, 10, 20])
  .range(['freezing', 'cold', 'warm', 'hot']);

thresholdScale(-5);  // 返回 'freezing'
thresholdScale(5);   // 返回 'cold'
thresholdScale(15);  // 返回 'warm'
thresholdScale(25);  // 返回 'hot'
```

**用例：**
- 自定义断点
- 成绩界限（A，B，C，D，F）
- 温度类别
- 空气质量指数

## 顺序标度

### 顺序颜色标度

将连续输入映射到连续颜色渐变。

```javascript
const colourScale = d3.scaleSequential(d3.interpolateBlues)
  .domain([0, 100]);

colourScale(0);   // 返回最浅蓝色
colourScale(50);  // 返回中等蓝色
colourScale(100); // 返回最深蓝色
```

**可用插值器：**

**单色调：**
- `d3.interpolateBlues`，`d3.interpolateGreens`，`d3.interpolateReds`
- `d3.interpolateOranges`，`d3.interpolatePurples`，`d3.interpolateGreys`

**多色调：**
- `d3.interpolateViridis`，`d3.interpolateInferno`，`d3.interpolateMagma`
- `d3.interpolatePlasma`，`d3.interpolateWarm`，`d3.interpolateCool`
- `d3.interpolateCubehelixDefault`，`d3.interpolateTurbo`

**用例：**
- 热图，分形图
- 连续数据可视化
- 温度，海拔，密度

### 分裂颜色标度

将连续输入映射到具有中点的分裂颜色渐变。

```javascript
const divergingScale = d3.scaleDiverging(d3.interpolateRdBu)
  .domain([-10, 0, 10]);

divergingScale(-10); // 返回红色
divergingScale(0);   // 返回白色/中性
divergingScale(10);  // 返回蓝色
```

**可用插值器：**
- `d3.interpolateRdBu` - 从红色到蓝色
- `d3.interpolateRdYlBu` - 红色，黄色，蓝色
- `d3.interpolateRdYlGn` - 红色，黄色，绿色
- `d3.interpolatePiYG` - 粉红色，黄色，绿色
- `d3.interpolateBrBG` - 棕色，蓝绿色
- `d3.interpolatePRGn` - 紫色，绿色
- `d3.interpolatePuOr` - 紫色，橙色
- `d3.interpolateRdGy` - 红色，灰色
- `d3.interpolateSpectral` - 彩虹光谱

**用例：**
- 有意义的中点数据（零，平均值，中性）
- 正负值
- 上下比较
- 相关矩阵

### 顺序分位数标度

将顺序颜色与分位数映射相结合。

```javascript
const sequentialQuantileScale = d3.scaleSequentialQuantile(d3.interpolateBlues)
  .domain([3, 6, 7, 8, 8, 10, 13, 15, 16, 20, 24]);

// 根据分位数位置映射
```

**用例：**
- 感知均匀分箱
- 处理异常值
- 偏斜分布

## 序数标度

### 带状标度

将离散输入映射到连续带（矩形），具有可选填充。

```javascript
const bandScale = d3.scaleBand()
  .domain(['A', 'B', 'C', 'D'])
  .range([0, 400])
  .padding(0.1);

bandScale('A');           // 返回起始位置（例如，0）
bandScale('B');           // 返回起始位置（例如，110）
bandScale.bandwidth();    // 返回每个带的宽度（例如，95）
bandScale.step();         // 返回包括填充的总步长
bandScale.paddingInner(); // 返回带之间的内部填充（0-1）
bandScale.paddingOuter(); // 返回边缘的填充（0-1）
```

**用例：**
- 条形图（最常见用例）
- 分组元素
- 类别轴
- 热图单元格

**填充选项：**
- `.padding(value)` - 设置内部和外部填充（0-1）
- `.paddingInner(value)` - 带之间的填充（0-1）
- `.paddingOuter(value)` - 边缘的填充（0-1）
- `.align(value)` - 带的对齐（0-1，默认 0.5）

### 点标度

将离散输入映射到连续点（无宽度）。

```javascript
const pointScale = d3.scalePoint()
  .domain(['A', 'B', 'C', 'D'])
  .range([0, 400])
  .padding(0.5);

pointScale('A'); // 返回位置（例如，50）
pointScale('B'); // 返回位置（例如，150）
pointScale('C'); // 返回位置（例如，250）
pointScale('D'); // 返回位置（例如，350）
pointScale.step(); // 返回点之间的距离
```

**用例：**
- 线形图类别 x 轴
- 散点图与类别轴
- 网络图中的节点位置
- 任何类别定位

### 序数颜色标度

将离散输入映射到离散输出（颜色，形状等）。

```javascript
const colourScale = d3.scaleOrdinal(d3.schemeCategory10);

colourScale('apples');  // 返回第一种颜色
colourScale('oranges'); // 返回第二种颜色
colourScale('apples');  // 返回相同的第一个颜色（一致）

// 自定义范围
const customScale = d3.scaleOrdinal()
  .domain(['cat1', 'cat2', 'cat3'])
  .range(['#FF6B6B', '#4ECDC4', '#45B7D1']);
```

**内置颜色方案：**

**类别：**
- `d3.schemeCategory10` - 10 种颜色
- `d3.schemeAccent` - 8 种颜色
- `d3.schemeDark2` - 8 种颜色
- `d3.schemePaired` - 12 种颜色
- `d3.schemePastel1` - 9 种颜色
- `d3.schemePastel2` - 8 种颜色
- `d3.schemeSet1` - 9 种颜色
- `d3.schemeSet2` - 8 种颜色
- `d3.schemeSet3` - 12 种颜色
- `d3.schemeTableau10` - 10 种颜色

**用例：**
- 类别颜色
- 图例项
- 多系列图表
- 网络节点类型

## 标度工具

### 漂亮域

将域扩展到漂亮的整数值。

```javascript
const scale = d3.scaleLinear()
  .domain([0.201, 0.996])
  .nice();

scale.domain(); // 返回 [0.2, 1.0]

// 与计数（近似刻度数）
const scale2 = d3.scaleLinear()
  .domain([0.201, 0.996])
  .nice(5);
```

### 限制

将输出限制在范围边界内。

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range([0, 500])
  .clamp(true);

scale(-10); // 返回 0（限制）
scale(150); // 返回 500（限制）
```

### 复制标度

创建独立的副本。

```javascript
const scale1 = d3.scaleLinear()
  .domain([0, 100])
  .range([0, 500]);

const scale2 = scale1.copy();
// scale2 与 scale1 独立
```

### 刻度生成

为轴生成漂亮的刻度值。

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range([0, 500]);

scale.ticks(10);        // 生成 ~10 个刻度
scale.tickFormat(10);   // 获取刻度格式函数
scale.tickFormat(10, ".2f"); // 自定义格式（2 位小数）

// 时间标度刻度
const timeScale = d3.scaleTime()
  .domain([new Date(2020, 0, 1), new Date(2024, 0, 1)]);

timeScale.ticks(d3.timeYear);      // 每年刻度
timeScale.ticks(d3.timeMonth, 3);  // 每 3 个月一次
timeScale.tickFormat(5, "%Y-%m");  // 格式为年-月
```

## 颜色空间和插值

### RGB 插值

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range(["blue", "red"]);
// 默认：RGB 插值
```

### HSL 插值

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range(["blue", "red"])
  .interpolate(d3.interpolateHsl);
// 更平滑的颜色过渡
```

### Lab 插值

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range(["blue", "red"])
  .interpolate(d3.interpolateLab);
// 感知均匀
```

### HCL 插值

```javascript
const scale = d3.scaleLinear()
  .domain([0, 100])
  .range(["blue", "red"])
  .interpolate(d3.interpolateHcl);
// 感知均匀，具有色调
```

## 常见模式

### 带有自定义中点的分裂标度

```javascript
const scale = d3.scaleLinear()
  .domain([min, midpoint, max])
  .range(["red", "white", "blue"])
  .interpolate(d3.interpolateHcl);
```

### 多停止渐变标度

```javascript
const scale = d3.scaleLinear()
  .domain([0, 25, 50, 75, 100])
  .range(["#d53e4f", "#fc8d59", "#fee08b", "#e6f598", "#66c2a5"]);
```

### 圆形半径标度（感知）

```javascript
const radiusScale = d3.scaleSqrt()
  .domain([0, d3.max(data, d => d.value)])
  .range([0, 50]);

// 与圆形一起使用
circle.attr("r", d => radiusScale(d.value));
```

### 基于数据范围的自适应标度

```javascript
function createAdaptiveScale(data) {
  const extent = d3.extent(data);
  const range = extent[1] - extent[0];
  
  // 如果数据跨度超过 2 个数量级，则使用对数标度
  if (extent[1] / extent[0] > 100) {
    return d3.scaleLog()
      .domain(extent)
      .range([0, width]);
  }
  
  // 否则使用线性
  return d3.scaleLinear()
    .domain(extent)
    .range([0, width]);
}
```

### 带有显式类别的颜色标度

```javascript
const colourScale = d3.scaleOrdinal()
  .domain(['Low Risk', 'Medium Risk', 'High Risk'])
  .range(['#2ecc71', '#f39c12', '#e74c3c'])
  .unknown('#95a5a6'); // 未知值的后备
```