---
name: json-canvas
description: 创建和编辑 JSON Canvas 文件 (.canvas)，支持节点、边、组和连接。当处理 .canvas 文件、创建视觉画布、思维导图、流程图或用户提到 Obsidian 中的 Canvas 文件时使用。
---

# JSON Canvas 技能

## 文件结构

`.canvas` 文件包含 `nodes` 和 `edges` 两个顶层数组。

## 常用工作流

1. **创建新画布**: 使用 `{"nodes": [], "edges": []}` 初始化。
2. **添加节点**: 生成 16 位 16 进制 ID，指定类型 (`text`, `file`, `link`, `group`) 和位置。
3. **连接节点**: 创建边，引用 `fromNode` 和 `toNode` 的 ID。

## 节点属性

| 属性 | 是否必需 | 类型 | 描述 |
|-----------|----------|------|-------------|
| `id` | 是 | string | 唯一 16 位 16 进制标识符 |
| `type` | 是 | string | `text`, `file`, `link`, 或 `group` |
| `x`, `y` | 是 | integer | 像素位置 |
| `width`, `height` | 是 | integer | 像素宽高 |

## 节点类型

- **Text (文本)**: 包含 Markdown 内容。
- **File (文件)**: 引用库内文件。
- **Link (链接)**: 引用外部 URL。
- **Group (组)**: 用于组织其他节点的容器。
