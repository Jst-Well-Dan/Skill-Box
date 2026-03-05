---
name: obsidian-bases
description: 创建和编辑 Obsidian Bases (.base 文件)，支持视图、过滤器、公式和汇总。当处理 .base 文件、创建笔记的数据库式视图，或用户提到 Obsidian 中的 Bases、表格视图、卡片视图、过滤器或公式时使用。
---

# Obsidian Bases 技能

## 工作流

1. **创建文件**：在库中创建一个具有有效 YAML 内容的 `.base` 文件。
2. **定义范围**：添加 `filters` 来选择显示的笔记（通过标签、文件夹、属性或日期）。
3. **添加公式**（可选）：在 `formulas` 部分定义计算属性。
4. **配置视图**：添加一个或多个视图（`table`、`cards`、`list` 或 `map`），并用 `order` 指定要显示的属性。
5. **验证**：确认 YAML 格式正确。

## 过滤器语法

```yaml
# AND - 所有条件必须为真
filters:
  and:
    - 'status == "done"'
    - 'priority > 3'

# OR - 任意条件为真
filters:
  or:
    - 'file.hasTag("book")'
    - 'file.hasTag("article")'
```

## 公式语法

```yaml
formulas:
  # 简单算术
  total: "price * quantity"
  # 条件逻辑
  status_icon: 'if(done, "✅", "⏳")'
  # 距离创建日期有多少天
  days_old: '(now() - file.ctime).days'
```

## 视图类型

- **Table (表格)**: 传统的行和列。
- **Cards (卡片)**: 适合展示图片或摘要。
- **List (列表)**: 简单的垂直列表。
- **Map (地图)**: 标记地理位置。

## 汇总公式

支持 `Average`, `Min`, `Max`, `Sum`, `Median`, `Earliest`, `Latest` 等。
