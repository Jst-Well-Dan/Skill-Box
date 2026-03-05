---
name: obsidian-cli
description: 使用 Obsidian CLI 与 Obsidian 库进行交互，执行读取、创建、搜索、管理笔记、任务、属性等操作。还支持插件和主题开发，包括重新加载插件、运行 JavaScript、捕捉错误、截屏和检查 DOM。当用户要求与其 Obsidian 库交互、管理笔记、搜索内容、从命令行执行库操作或开发调试插件和主题时使用。
---

# Obsidian CLI

使用 `obsidian` CLI 与正在运行的 Obsidian 实例交互。需要 Obsidian 处于打开状态。

## 命令参考

运行 `obsidian help` 查看所有可用命令。

## 语法

**参数** 使用 `=` 赋值。带空格的值需要加引号：
`obsidian create name="我的笔记" content="你好世界"`

**标志** 是布尔开关：
`obsidian create name="我的笔记" silent overwrite`

## 常见模式

```bash
obsidian read file="我的笔记"
obsidian search query="搜索词" limit=10
obsidian daily:read
obsidian property:set name="status" value="done" file="我的笔记"
```

## 插件开发

1. **重新加载插件**: `obsidian plugin:reload id=my-plugin`
2. **检查错误**: `obsidian dev:errors`
3. **截屏验证**: `obsidian dev:screenshot path=screenshot.png`
