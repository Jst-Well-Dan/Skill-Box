<!--
本文件由智谱 AI 自动翻译生成
原文件: examples.md
翻译时间: 2025-12-12 16:10:22
翻译模型: glm-4-flash
原文大小: 2,343 字符
-->

# PICT 示例参考

> **注意**：这是一个占位符文件。全面示例即将推出！
> 
> 目前，请查看[示例目录](../examples/)以获取完整的真实世界示例。

## 可用示例

### 完整示例
- **[ATM 系统测试](../examples/atm-specification.md)**：包含 31 个测试用例的全面银行 ATM 系统

### 即将推出

#### 软件测试
- 多参数功能测试
- API 端点测试
- 数据库查询验证
- 算法测试

#### 网络应用程序
- 表单验证
- 用户身份验证
- 电子商务结账
- 购物车操作

#### 配置测试
- 系统配置
- 功能标志
- 环境设置
- 浏览器兼容性

#### 移动测试
- 设备和操作系统组合
- 屏幕尺寸
- 网络条件
- 权限

## 模式库（即将推出）

### 常见约束模式

```
# 依赖约束
IF [FeatureA] = "Enabled" THEN [FeatureB] = "Enabled";

# 独立选项
IF [PaymentMethod] = "Cash" THEN [InstallmentPlan] = "None";

# 平台限制
IF [OS] = "iOS" THEN [Browser] IN {Safari, Chrome};

# 环境限制
IF [Environment] = "Production" THEN [LogLevel] <> "Debug";
```

### 边界值模式

```
# 数字边界
Age: 0, 17, 18, 64, 65, 100

# 尺寸类别
FileSize: 0KB, 1KB, 1MB, 100MB, 1GB

# 时间段
Duration: 0s, 1s, 30s, 60s, 3600s
```

### 负面测试模式

```
# 无效输入（某些 PICT 变体中使用 ~ 前缀）
Email: Valid, Invalid, Empty, TooLong
Password: Strong, Weak, Empty, SpecialChars

# 错误条件
NetworkStatus: Connected, Slow, Disconnected, Timeout
```

## 贡献示例

有示例要分享吗？我们非常乐意将其包括在内！

1. 按照在 [examples/README.md](../examples/README.md) 中的结构创建您的示例
2. 包含：
   - 原始规范
   - PICT 模型
   - 带有预期输出的测试用例
   - 学习要点
3. 提交一个拉取请求

有关详细信息，请参阅 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 外部资源

- [成对测试教程](https://www.pairwisetesting.com/)
- [NIST 组合测试资源](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software)
- [Microsoft PICT 示例](https://github.com/microsoft/pict/tree/main/doc)