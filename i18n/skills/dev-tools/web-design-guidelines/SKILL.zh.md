---
name: web-design-guidelines
description: 审查 UI 代码以符合 Web 接口指南。在需要“审查我的 UI”、“检查可访问性”、“审计设计”、“审查 UX”或“检查我的网站是否符合最佳实践”时使用。
argument-hint: <文件或模式>
author: Vercel Labs
---

# Web 接口指南

审查文件是否符合 Web 接口指南。

## 工作原理

1. 从以下源 URL 获取最新指南
2. 读取指定的文件（或提示用户输入文件/模式）
3. 与获取的指南中的所有规则进行核对
4. 以简洁的 `文件:行` 格式输出结果

## 指南源

在每次审查之前获取新鲜指南：

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

使用 WebFetch 获取最新规则。获取的内容包含所有规则和输出格式说明。

## 使用方法

当用户提供文件或模式参数时：
1. 从上述源 URL 获取指南
2. 读取指定的文件
3. 应用获取的指南中的所有规则
4. 使用指南中指定的格式输出结果

如果没有指定文件，请询问用户要审查哪些文件。