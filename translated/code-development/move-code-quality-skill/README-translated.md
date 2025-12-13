<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:10:32
翻译模型: glm-4-flash
原文大小: 3,289 字符
-->

---

# Move 代码质量检查器 - Claude 代码技能

一个 Claude 代码技能，它分析 Move 语言包与官方 [Move 书籍代码质量检查清单](https://move-book.com/guides/code-quality-checklist/)，帮助您编写更好、更易于维护的 Move 代码。

## 概述

此技能扩展了 Claude 代码，具有对 Move 语言最佳实践的深入知识，提供：

- **针对 10+ 类最佳实践的自动化代码质量分析**
- **来自 Move 书籍的具体、可操作的推荐，并附有示例**
- **Move 2024 版本合规性检查**
- **包清单验证**
- **函数签名和结构分析**
- **测试最佳实践审查**

## 检查内容

该技能从多个维度分析您的 Move 代码：

1. **代码组织** - 格式一致性
2. **包清单** - 版本要求、依赖项、命名地址
3. **导入和模块** - 现代语法、命名约定
4. **结构体** - 能力模式、事件命名、动态字段
5. **函数** - 可见性修饰符、可组合性、参数顺序
6. **函数体** - 方法链式调用、字符串操作、集合
7. **选项和循环宏** - 现代惯用模式
8. **测试** - 属性使用、断言、清理模式
9. **文档** - 注释质量和完整性

## 安装

### 从 Claude 代码

```bash
# 克隆到您的 Claude 技能目录
git clone https://github.com/1NickPappas/move-code-quality-skill ~/.claude/skills/move-code-quality
```

### 手动安装

1. 如果不存在，创建技能目录：
   ```bash
   mkdir -p ~/.claude/skills
   ```

2. 将此技能克隆或复制到技能目录：
   ```bash
   cd ~/.claude/skills
   git clone https://github.com/1NickPappas/move-code-quality-skill
   ```

3. 当您使用 Move 代码时，Claude 代码将自动加载此技能

## 使用方法

当您使用 Move 代码时，该技能会自动激活。您也可以显式调用它：

```
分析此 Move 包的代码质量问题
```

```
根据 Move 代码质量检查清单审查此模块
```

```
检查此代码是否遵循 Move 2024 最佳实践
```

## 示例

该技能根据 Move 书籍的示例提供具体的反馈：

- **之前**：`use my_package::{Self};`
- **之后**：`use my_package;`
- **原因**：避免冗余 Self 导入

- **之前**：`public entry fun transfer(...);`
- **之后**：`public fun transfer(...);`
- **原因**：公共函数对 PTB 更具可组合性

## 要求

- Claude 代码 CLI
- Move 2024 版本项目
- 对 Move 语言的初步了解

## 贡献

我们欢迎贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 获取详细信息。

## 许可证

本项目采用 MIT 许可证 - 请参阅 [LICENSE](LICENSE) 文件获取详细信息。

## 资源

- [Move 书籍代码质量检查清单](https://move-book.com/guides/code-quality-checklist/)
- [Move 语言文档](https://move-language.github.io/move/)
- [Claude 代码技能文档](https://docs.claude.com/claude-code)

## 致谢

此技能基于 [The Move Book](https://move-book.com/) 的全面代码质量指南，由 Move 社区提供。