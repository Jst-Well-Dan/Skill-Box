---
name: excalidraw-diagram
description: 从文本内容生成 Excalidraw 图表，用于 Obsidian。当用户请求创建图表、流程图、思维导图或 Excalidraw 格式的可视化表示时使用。在“Excalidraw”、“画图”、“流程图”、“思维导图”、“可视化”、“diagram”等触发时启动。
metadata:
  version: 1.1.0
---

# Excalidraw Diagram Generator

从文本内容创建 Excalidraw 图表，输出 Obsidian 准备好的 `.md` 文件。

## 工作流程

1. 分析内容 - 识别概念、关系、层次结构
2. 选择图表类型（见下文）
3. 生成 Excalidraw JSON
4. 生成带有 Excalidraw 前置信息的 Obsidian 准备好的 `.md` 文件
5. **自动保存到当前工作目录**
6. 通知用户文件路径并确认保存成功

## 输出格式

**必须严格按照以下结构输出，不得有任何修改：**

```markdown
---
excalidraw-plugin: parsed
tags: [excalidraw]
---
==⚠  在此文档的「更多选项」菜单中切换到 EXCALIDRAW 视图。⚠== 您可以使用命令面板中的命令「解压缩当前 Excalidraw 文件」来解压缩绘图数据。更多信息请检查插件设置下的「保存」

# Excalidraw Data

## Text Elements
%%
## Drawing
\`\`\`json
{JSON 完整数据}
\`\`\`
%%
```

**关键要点：**
- 前置信息必须包含 `tags: [excalidraw]`
- 警告信息必须完整
- JSON 必须被 `%%` 标记包围
- 不能使用 `excalidraw-plugin: parsed` 以外的其他前置信息设置

## 图表类型与选择指南

选择合适的图表形式，以提升理解力和视觉吸引力。

| 类型 | 英文 | 使用场景 | 做法 |
|------|------|---------|------|
| **流程图** | Flowchart | 步骤说明、工作流程、任务执行顺序 | 用箭头连接各步骤，清晰表达流程走向 |
| **思维导图** | Mind Map | 概念发散、主题分类、灵感捕捉 | 以中心为核心向外发散，放射状结构 |
| **层级图** | Hierarchy | 组织结构、内容分级、系统拆解 | 自上而下或自左至右构建层级节点 |
| **关系图** | Relationship | 要素之间的影响、依赖、互动 | 图形间用连线表示关联，箭头与说明 |
| **对比图** | Comparison | 两种以上方案或观点的对照分析 | 左右两栏或表格形式，标明比较维度 |
| **时间线图** | Timeline | 事件发展、项目进度、模型演化 | 以时间为轴，标出关键时间点与事件 |
| **矩阵图** | Matrix | 双维度分类、任务优先级、定位 | 建立 X 与 Y 两个维度，坐标平面安置 |
| **自由布局** | Freeform | 内容零散、灵感记录、初步信息收集 | 无需结构限制，自由放置图块与箭头 |

## 设计规则

### 文本与格式
- **所有文本元素必须使用** `fontFamily: 5`（Excalifont 手写字体）
- **文本中的双引号替换规则**：`"` 替换为 `『』`
- **文本中的圆括号替换规则**：`()` 替换为 `「」`
- **字体大小规则**：
  - 标题：24-28px
  - 副标题：18-20px
  - 正文/说明：14-16px
- **行高**：所有文本使用 `lineHeight: 1.25`

### 布局与设计
- **画布范围**：建议所有元素在 0-1200 x 0-800 区域内
- **元素间距**：确保元素间距适当，整体布局美观
- **层次清晰**：使用不同颜色和形状区分不同层级的信息
- **图形元素**：适当使用矩形框、圆形、箭头等元素来组织信息

### 色彩调色板
- **标题颜色**：`#1e40af`（深蓝）
- **副标题/连接线**：`#3b82f6`（亮蓝）
- **正文文字**：`#374151`（灰色）
- **强调/重点**：`#f59e0b`（金色）
- **其他配色**：建议使用和谐的配色方案，避免过多颜色

参考：[references/excalidraw-schema.md](references/excalidraw-schema.md)

## JSON 结构

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://github.com/zsviczian/obsidian-excalidraw-plugin",
  "elements": [...],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

## 元素模板

每个元素都需要以下字段：

```json
{
  "id": "unique-id",
  "type": "rectangle",
  "x": 100, "y": 100,
  "width": 200, "height": 50,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid|dashed",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a1",
  "roundness": {"type": 3},
  "seed": 123456789,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1751928342106,
  "link": null,
  "locked": false
}
```

文本元素添加：
```json
{
  "text": "显示文本",
  "rawText": "显示文本",
  "fontSize": 20,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": null,
  "originalText": "显示文本",
  "autoResize": true,
  "lineHeight": 1.25
}
```

参见 [references/excalidraw-schema.md](references/excalidraw-schema.md) 了解所有元素类型。

---

## 其他技术要求

### 文本元素处理
- `## Text Elements` 部分在 Markdown 中**必须留空**，仅用 `%%` 作为分隔符
- Obsidian ExcaliDraw 插件会根据 JSON 数据**自动填充文本元素**
- 不需要手动列出所有文本内容

### 坐标与布局
- **坐标系统**：左上角为原点 (0,0)
- **推荐范围**：所有元素在 0-1200 x 0-800 像素范围内
- **元素 ID**：每个元素需要唯一的 `id`（可以是字符串，如「title」「box1」等）
- **Index 字段**：建议使用字母数字 (a1, a2, a3...)

### 所有元素所需字段
```json
{
  "id": "unique-identifier",
  "type": "rectangle|text|arrow|ellipse|diamond",
  "x": 100, "y": 100,
  "width": 200, "height": 50,
  "angle": 0,
  "strokeColor": "#color-hex",
  "backgroundColor": "transparent|#color-hex",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid|dashed",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a1",
  "roundness": {"type": 3},
  "seed": 123456789,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1751928342106,
  "link": null,
  "locked": false
}
```

### 文本特定属性
文本元素 (type: "text") 需要额外属性：
```json
{
  "text": "显示文本",
  "rawText": "显示文本",
  "fontSize": 20,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": null,
  "originalText": "显示文本",
  "autoResize": true,
  "lineHeight": 1.25
}
```

### appState 配置
```json
"appState": {
  "gridSize": null,
  "viewBackgroundColor": "#ffffff"
}
```

### files 字段
```json
"files": {}
```

## 实现说明

### 自动保存与文件生成工作流程

当生成 Excalidraw 图表时，**必须自动执行以下步骤**：

#### 1. 选择合适的图表类型
- 根据用户提供的内容特性，参考上方 「Diagram Types & Selection Guide」 表
- 分析内容的核心诉求，选择最合适的可视化形式

#### 2. 生成有意义的文件名
- 格式：`[主题].[类型].md`
- 例如：`内容创作流程.flowchart.md`、`Axton商业模式.relationship.md`
- 优先使用中文以提高清晰度

#### 3. 使用 Write 工具自动保存文件
- **保存位置**：当前工作目录（自动检测环境变量）
- **完整路径**：`{current_directory}/[filename].md`
- 这样可以实现灵活迁移，无需硬编码路径

#### 4. 确保 Markdown 结构完全正确
**必须按以下格式生成**（不能有任何修改）：

```markdown
---
excalidraw-plugin: parsed
tags: [excalidraw]
---
==⚠  在此文档的「更多选项」菜单中切换到 EXCALIDRAW 视图。⚠== 您可以使用命令面板中的命令「解压缩当前 Excalidraw 文件」来解压缩绘图数据。更多信息请检查插件设置下的「保存」

# Excalidraw Data

## Text Elements
%%
## Drawing
\`\`\`json
{完整的 JSON 数据}
\`\`\`
%%
```

#### 5. JSON 数据要求
- ✅ 包含完整的 Excalidraw JSON 结构
- ✅ 所有文本元素使用 `fontFamily: 5`
- ✅ 文本中的 `"` 替换为 `『』`
- ✅ 文本中的 `()` 替换为 `「」`
- ✅ JSON 格式必须有效，通过语法检查
- ✅ 所有元素有唯一的 `id`
- ✅ 包含 `appState` 和 `files: {}` 字段

#### 6. 用户反馈与确认
向用户报告：
- ✅ 图表已生成
- 📍 精确的保存位置
- 📖 如何在 Obsidian 中查看
- 🎨 图表的设计选择说明（选择了什么类型的图表、为什么）
- ❓ 是否需要调整或修改

### 示例输出信息
```
✅ Excalidraw 图已自动生成！

📍 保存位置：
Axton_2026商业模式.relationship.md

🎨 图表选择说明：
我选择了「关系图」来表现三大产品线之间的转化关系，用箭头展示用户的升级路径，以及它们如何共同构成完整的商业闭环。

📖 使用方法：
1. 在 Obsidian 中打开此文件
2. 点击右上角「更多选项」菜单
3. 选择「切换到 EXCALIDRAW 视图」
4. 即可看到可视化的商业模式全景

需要调整吗？比如改变布局、添加更多细节或调整配色，直接告诉我！
```