<!--
本文件由智谱 AI 自动翻译生成
原文件: pict_syntax.md
翻译时间: 2025-12-12 16:10:16
翻译模型: glm-4-flash
原文大小: 1,915 字符
-->

# PICT 语法参考

> **注意**：这是一个占位符文件。完整的语法文档即将推出！
> 
> 目前，请参考官方 PICT 文档：
> - [GitHub 上的 Microsoft PICT](https://github.com/microsoft/pict)
> - [PICT 用户指南](https://github.com/microsoft/pict/blob/main/doc/pict.md)

## 快速参考

### 基本模型结构

```
# 参数
ParameterName: Value1, Value2, Value3
AnotherParameter: ValueA, ValueB, ValueC

# 约束（可选）
IF [ParameterName] = "Value1" THEN [AnotherParameter] <> "ValueA";
```

### 参数定义

```
ParameterName: Value1, Value2, Value3, ...
```

### 约束语法

```
IF <condition> THEN <condition>;
```

### 操作符

- `=` - 等于
- `<>` - 不等于
- `>` - 大于
- `<` - 小于
- `>=` - 大于等于
- `<=` - 小于等于
- `IN` - 集合成员
- `AND` - 逻辑与
- `OR` - 逻辑或
- `NOT` - 逻辑非

### 示例约束

```
# 简单约束
IF [OS] = "MacOS" THEN [Browser] <> "IE";

# 多个条件
IF [Environment] = "Production" AND [LogLevel] = "Debug" THEN [Approved] = "False";

# 集合成员
IF [UserRole] = "Guest" THEN [Permission] IN {Read, None};
```

## 即将推出

详细的文档将包括：
- 完整的语法规范
- 高级功能（子模型、别名、播种）
- 负面测试模式
- 权重规范
- 排序规范
- 每个功能的示例

## 贡献

如果您想帮助完成此文档：
1. 分叉存储库
2. 向此文件添加内容
3. 提交拉取请求

有关指南，请参阅 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 外部资源

- [官方 PICT 文档](https://github.com/microsoft/pict/blob/main/doc/pict.md)
- [pypict 文档](https://github.com/kmaehashi/pypict)
- [成对测试解释](https://www.pairwisetesting.com/)