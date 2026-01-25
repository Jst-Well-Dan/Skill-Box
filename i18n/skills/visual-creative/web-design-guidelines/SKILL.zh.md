---
name: web-design-guidelines
description: 根据网页界面指南合规性审查 UI 代码。当被要求“审查我的 UI”、“检查无障碍性”、“审计设计”、“审查 UX”或“根据最佳实践检查我的网站”时使用。
argument-hint: <file-or-pattern>
---

# Web 接口指南

Review files for compliance with Web Interface Guidelines.

## 工作原理

1. 从以下源 URL 获取最新指南
2. 读取指定的文件（或提示用户输入文件/模式）
3. 与获取的指南中的所有规则进行比对
4. 以简洁的 `file:line` 格式输出结果

## 指南源

在每次审查之前获取最新指南：

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

使用 WebFetch 获取最新规则。获取的内容包含所有规则和输出格式说明。

## 使用方法

当用户提供文件或模式参数时：
1. 从上述源 URL 获取指南
2. 读取指定的文件
3. 应用获取指南中的所有规则
4. 使用指南中指定的格式输出结果

如果没有指定文件，请提示用户选择要审查的文件。