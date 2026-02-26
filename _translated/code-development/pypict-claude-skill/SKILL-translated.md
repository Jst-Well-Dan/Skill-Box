<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:11:45
翻译模型: glm-4-flash
原文大小: 10,928 字符
-->

---
name: pict-test-designer
description: 使用 PICT (成对独立组合测试) 设计任何需求或代码的综合测试用例。分析输入，使用成对测试生成具有参数、值和约束的有效场景的 PICT 模型。输出 PICT 模型、测试用例的 Markdown 表格和预期结果。
---

# PICT 测试设计器

此技能通过 PICT (成对独立组合测试) 实现系统化测试用例设计。给定需求或代码，它分析系统以识别测试参数，生成具有适当约束的 PICT 模型，执行模型以生成成对测试用例，并以预期输出格式化结果。

## 何时使用此技能

在以下情况下使用此技能：
- 为具有多个输入参数的功能、功能或系统设计测试用例
- 为具有许多组合的配置创建测试套件
- 需要全面覆盖且测试用例最少
- 分析需求以识别测试场景
- 与具有多个条件路径的代码一起工作
- 为 API 端点、Web 表单或系统配置构建测试矩阵

## 工作流程

遵循以下过程进行测试设计：

### 1. 分析需求或代码

从用户的请求或代码中识别：
- **参数**：输入变量、配置选项、环境因素
- **值**：每个参数的可能值（使用等价类划分）
- **约束**：业务规则、技术限制、参数之间的依赖关系
- **预期结果**：不同组合应该发生什么

**示例分析：**

对于具有以下需求的登录功能：
- 用户可以使用用户名/密码登录
- 支持 2FA（开启/关闭）
- 在受信任设备上记住登录
- 3 次失败后限制速率

识别的参数：
- 凭据：有效、无效
- 双因素认证：开启、关闭
- 记住我：勾选、未勾选
- 前次失败：0、1、2、3、4

### 2. 生成 PICT 模型

创建一个具有以下内容的 PICT 模型：
- 清晰的参数名称
- 明确定义的值集（使用等价类划分和边界值）
- 无效组合的约束
- 解释业务规则的注释

**模型结构：**
```
# 参数定义
ParameterName: Value1, Value2, Value3

# 约束（如果有）
IF [Parameter1] = "Value" THEN [Parameter2] <> "OtherValue";
```

**有关以下内容，请参阅 references/pict_syntax.md：**
- 完整的语法参考
- 约束语法和运算符
- 高级功能（子模型、别名、负测试）
- 命令行选项
- 详细约束模式

**有关以下内容，请参阅 references/examples.md：**
- 按领域划分的完整真实世界示例
- 软件功能测试示例
- Web 应用程序、API 和移动测试示例
- 数据库和配置测试模式
- 认证、资源访问、错误处理的常见模式

### 3. 执行 PICT 模型

生成 PICT 模型文本并将其格式化以供用户使用。您可以直接使用 Python 代码来处理模型：

```python
# 定义参数和约束
parameters = {
    "OS": ["Windows", "Linux", "MacOS"],
    "Browser": ["Chrome", "Firefox", "Safari"],
    "Memory": ["4GB", "8GB", "16GB"]
}

constraints = [
    'IF [OS] = "MacOS" THEN [Browser] IN {Safari, Chrome}',
    'IF [Memory] = "4GB" THEN [OS] <> "MacOS"'
]

# 生成模型文本
model_lines = []
for param_name, values in parameters.items():
    values_str = ", ".join(values)
    model_lines.append(f"{param_name}: {values_str}")

if constraints:
    model_lines.append("")
    for constraint in constraints:
        if not constraint.endswith(';'):
            constraint += ';'
        model_lines.append(constraint)

model_text = "\n".join(model_lines)
print(model_text)
```

**使用辅助脚本（可选）：**
`scripts/pict_helper.py` 脚本提供用于模型生成和输出格式化的实用工具：

```bash
# 从 JSON 配置生成模型
python scripts/pict_helper.py generate config.json

# 将 PICT 工具输出格式化为 Markdown 表格
python scripts/pict_helper.py format output.txt

# 将 PICT 输出解析为 JSON
python scripts/pict_helper.py parse output.txt
```

**要生成实际的测试用例，用户可以：**
1. 将 PICT 模型保存到文件（例如，`model.txt`）
2. 使用在线 PICT 工具，例如：
   - https://pairwise.yuuniworks.com/
   - https://pairwise.teremokgames.com/
3. 或在本地安装 PICT（请参阅 references/pict_syntax.md）

### 4. 确定预期输出

对于每个生成的测试用例，根据以下内容确定预期结果：
- 业务需求
- 代码逻辑
- 有效/无效组合

为每个测试用例创建预期输出的列表。

### 5. 格式化完整的测试套件

向用户提供以下内容：
1. **PICT 模型** - 包含参数和约束的完整模型
2. **Markdown 表格** - 以表格格式显示的测试用例，带有测试编号
3. **预期输出** - 每个测试用例的预期结果

## 输出格式

以以下结构呈现结果：

````markdown
## PICT 模型

```
# 参数
Parameter1: Value1, Value2, Value3
Parameter2: ValueA, ValueB

# 约束
IF [Parameter1] = "Value1" THEN [Parameter2] = "ValueA";
```

## 生成的测试用例

| 测试编号 | Parameter1 | Parameter2 | 预期输出 |
| --- | --- | --- | --- |
| 1 | Value1 | ValueA | 成功 |
| 2 | Value2 | ValueB | 成功 |
| 3 | Value1 | ValueB | 错误：无效组合 |
...

## 测试用例摘要

- 总测试用例数：N
- 覆盖率：成对（所有双向组合）
- 应用约束：N
````

## 最佳实践

### 参数识别

**好的：**
- 使用描述性名称：`AuthMethod`、`UserRole`、`PaymentType`
- 应用等价类划分：`FileSize: 小、中、大` 而不是 `FileSize: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
- 包含边界值：`Age: 0, 17, 18, 65, 66`
- 添加错误测试的负值：`Amount: ~-1, 0, 100, ~999999`

**避免：**
- 通用名称：`Param1`、`Value1`、`V1`
- 值过多而没有划分
- 缺少边缘情况

### 约束编写

**好的：**
- 记录理由：`# Safari 仅在 MacOS 上可用`
- 从简单开始，逐步增加
- 测试约束是否按预期工作

**避免：**
- 过度约束（消除了太多有效组合）
- 约束不足（生成无效测试用例）
- 没有明确文档的复杂嵌套逻辑

### 预期输出定义

**具体明确：**
- "登录成功，用户被重定向到仪表板"
- "HTTP 400：无效凭据错误"
- "2FA 提示显示"

**不模糊：**
- "工作"
- "错误"
- "成功"

### 可扩展性

对于大型参数集：
- 使用子模型来分组相关参数和不同的顺序
- 考虑为不相关的功能创建单独的测试套件
- 从顺序 2（成对）开始，对于关键组合增加
- 典型的成对测试将测试用例减少 80-90%，与穷举测试相比

## 常见模式

### Web 表单测试

```python
parameters = {
    "Name": ["Valid", "Empty", "TooLong"],
    "Email": ["Valid", "Invalid", "Empty"],
    "Password": ["Strong", "Weak", "Empty"],
    "Terms": ["Accepted", "NotAccepted"]
}

constraints = [
    'IF [Terms] = "NotAccepted" THEN [Name] = "Valid"',  # 测试验证即使条款未接受
]
```

### API 端点测试

```python
parameters = {
    "HTTPMethod": ["GET", "POST", "PUT", "DELETE"],
    "Authentication": ["Valid", "Invalid", "Missing"],
    "ContentType": ["JSON", "XML", "FormData"],
    "PayloadSize": ["Empty", "Small", "Large"]
}

constraints = [
    'IF [HTTPMethod] = "GET" THEN [PayloadSize] = "Empty"',
    'IF [Authentication] = "Missing" THEN [HTTPMethod] IN {GET, POST}'
]
```

### 配置测试

```python
parameters = {
    "Environment": ["Dev", "Staging", "Production"],
    "CacheEnabled": ["True", "False"],
    "LogLevel": ["Debug", "Info", "Error"],
    "Database": ["SQLite", "PostgreSQL", "MySQL"]
}

constraints = [
    'IF [Environment] = "Production" THEN [LogLevel] <> "Debug"',
    'IF [Database] = "SQLite" THEN [Environment] = "Dev"'
]
```

## 故障排除

### 没有生成测试用例

- 检查约束不是过度限制性的
- 验证约束语法（必须以 `;` 结尾）
- 确保参数名称在约束中与定义匹配（使用 `[ParameterName]`）

### 测试用例过多

- 验证使用顺序 2（成对）而不是更高顺序
- 考虑拆分为子模型
- 检查是否可以将参数分离为独立的测试套件

### 输出中的无效组合

- 添加缺失的约束
- 验证约束逻辑是否正确
- 检查是否需要使用 `NOT` 或 `<>` 运算符

### 脚本错误

- 确保 pypict 已安装：`pip install pypict --break-system-packages`
- 检查 Python 版本（3.7+）
- 验证模型语法是否有效

## 参考资料

- **references/pict_syntax.md** - 完整的 PICT 语法参考，包括语法和运算符
- **references/examples.md** - 按不同领域划分的完整真实世界示例
- **scripts/pict_helper.py** - 用于模型生成和输出格式化的 Python 实用工具
- [PICT GitHub 仓库](https://github.com/microsoft/pict) - 官方 PICT 文档
- [pypict 文档](https://github.com/kmaehashi/pypict) - Python 绑定文档
- [在线 PICT 工具](https://pairwise.yuuniworks.com/) - 基于网络的 PICT 生成器

## 示例

### 示例 1：简单函数测试

**用户请求**："为除法函数设计测试，该函数接受两个数字并返回结果。"

**分析**：
- 参数：被除数（数字）、除数（数字）
- 值：使用等价类划分和边界值
  - 数字：负数、零、正数、大数值
- 约束：除以零是无效的
- 预期输出：结果或错误

**PICT 模型**：
```
Dividend: -10, 0, 10, 1000
Divisor: ~0, -5, 1, 5, 100

IF [Divisor] = "0" THEN [Dividend] = "10";
```

**测试用例**：

| 测试编号 | 被除数 | 除数 | 预期输出 |
| --- | --- | --- | --- |
| 1 | 10 | 0 | 错误：除以零 |
| 2 | -10 | 1 | -10.0 |
| 3 | 0 | -5 | 0.0 |
| 4 | 1000 | 5 | 200.0 |
| 5 | 10 | 100 | 0.1 |

### 示例 2：电子商务结账

**用户请求**："为具有支付方式、运输选项和用户类型的结账流程设计测试。"

**分析**：
- 支付：信用卡、PayPal、银行转账（根据用户类型有限制）
- 运输：标准、快递、隔夜
- 用户：访客、注册用户、高级用户
- 约束：访客不能使用银行转账，高级用户获得免费快递

**PICT 模型**：
```
PaymentMethod: CreditCard, PayPal, BankTransfer
ShippingMethod: Standard, Express, Overnight
UserType: Guest, Registered, Premium

IF [UserType] = "Guest" THEN [PaymentMethod] <> "BankTransfer";
IF [UserType] = "Premium" AND [ShippingMethod] = "Express" THEN [PaymentMethod] IN {CreditCard, PayPal};
```

**输出**：12-15 个测试用例，涵盖所有有效的支付/运输/用户组合，以及预期的成本和结果。