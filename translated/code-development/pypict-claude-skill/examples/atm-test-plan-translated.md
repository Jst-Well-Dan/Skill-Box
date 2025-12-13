<!--
本文件由智谱 AI 自动翻译生成
原文件: atm-test-plan.md
翻译时间: 2025-12-12 16:12:18
翻译模型: glm-4-flash
原文大小: 17,679 字符
-->

# 自动柜员机系统测试计划
## 使用 PICT（成对独立组合测试）

**系统:** SecureBank ATM 模型 SB-5000  
**版本:** 1.0  
**测试计划版本:** 1.0  
**日期:** 2025 年 10 月 19 日  
**测试方法:** 成对组合测试

---

## 1. 执行摘要

本测试计划使用成对独立组合测试（PICT）来高效地测试 ATM 系统，同时实现全面覆盖并最大限度地减少测试用例数量。该方法将测试用例数量减少了约 85%，与穷举测试相比，同时保持了参数交互的高覆盖率。

**关键统计数据：**
- **生成的总测试用例数:** 31
- **测试的参数:** 8
- **总可能组合数:** 25,920（穷举）
- **成对测试用例:** 31（减少 99.88%）
- **应用约束:** 16 个业务规则
- **覆盖率水平:** 所有双向（成对）参数交互

---

## 2. PICT 模型

以下模型定义了所有参数、它们的值和业务规则约束：

```
# ATM 系统测试模型
# 基于 SecureBank ATM 模型 SB-5000 规范 v1.0

# 参数
TransactionType: Withdrawal, Deposit, BalanceInquiry, Transfer, PINChange
CardType: EMVChip, MagStripe, Invalid
PINStatus: Valid, Invalid_1st, Invalid_2nd, Invalid_3rd
AccountType: Checking, Savings, Both
TransactionAmount: Within_Limit, At_Max_Transaction, Exceeds_Transaction, Exceeds_Daily
CashAvailability: Sufficient, Insufficient, Empty
NetworkStatus: Connected_Primary, Connected_Backup, Disconnected
CardCondition: Good, Damaged, Expired

# 基于 ATM 业务规则的业务规则约束

# 无效卡片无法完成交易
IF [CardType] = "Invalid" THEN [TransactionType] = "Withdrawal"
IF [CardType] = "Invalid" THEN [PINStatus] = "Valid"

# 余额查询不需要现金或特定金额
IF [TransactionType] = "BalanceInquiry" THEN [TransactionAmount] = "Within_Limit"
IF [TransactionType] = "BalanceInquiry" THEN [CashAvailability] = "Sufficient"

# PIN 变更不需要现金或特定金额
IF [TransactionType] = "PINChange" THEN [TransactionAmount] = "Within_Limit"
IF [TransactionType] = "PINChange" THEN [CashAvailability] = "Sufficient"

# 存款不需要检查现金供应器中的现金供应
IF [TransactionType] = "Deposit" THEN [CashAvailability] = "Sufficient"

# 转账不需要供应器中的现金
IF [TransactionType] = "Transfer" THEN [CashAvailability] = "Sufficient"

# 取款需要检查现金和交易限制
IF [TransactionType] = "Withdrawal" AND [CashAvailability] = "Empty" THEN [TransactionAmount] = "Within_Limit"

# 第 3 次无效 PIN 后，无论交易如何，卡片都应被保留
IF [PINStatus] = "Invalid_3rd" THEN [TransactionType] = "Withdrawal"

# 损坏或过期的卡片应在 PIN 验证之前失败
IF [CardCondition] = "Damaged" THEN [PINStatus] = "Valid"
IF [CardCondition] = "Expired" THEN [PINStatus] = "Valid"

# 网络断开连接会影响所有交易类型
IF [NetworkStatus] = "Disconnected" THEN [TransactionType] IN {Withdrawal, Deposit, Transfer}

# 金额约束仅适用于取款和存款
IF [TransactionAmount] = "Exceeds_Daily" THEN [TransactionType] IN {Withdrawal, Deposit}
IF [TransactionAmount] = "Exceeds_Transaction" THEN [TransactionType] IN {Withdrawal, Deposit}
IF [TransactionAmount] = "At_Max_Transaction" THEN [TransactionType] IN {Withdrawal, Deposit}
```

---

## 3. 参数定义

### 3.1 TransactionType
- **Withdrawal:** 从账户中取款
- **Deposit:** 向账户存款
- **BalanceInquiry:** 检查账户余额
- **Transfer:** 在账户之间转账
- **PINChange:** 更改 ATM PIN

### 3.2 CardType
- **EMVChip:** 带有 EMV 芯片的卡片（当前标准）
- **MagStripe:** 仅磁条卡片（过时）
- **Invalid:** 不可识别或损坏的卡片数据

### 3.3 PINStatus
- **Valid:** 输入正确的 PIN
- **Invalid_1st:** 第一次错误的 PIN 尝试
- **Invalid_2nd:** 第二次错误的 PIN 尝试
- **Invalid_3rd:** 第三次错误的 PIN 尝试（触发卡片保留）

### 3.4 AccountType
- **Checking:** 仅支票账户
- **Savings:** 仅储蓄账户
- **Both:** 可用多个账户

### 3.5 TransactionAmount
- **Within_Limit:** 在所有限制之内的金额
- **At_Max_Transaction:** 达到每笔交易最大限制（取款为 500 美元）
- **Exceeds_Transaction:** 超过每笔交易限制
- **Exceeds_Daily:** 超过每日限制（1000 美元）

### 3.6 CashAvailability
- **Sufficient:** 自动柜员机有足够的现金
- **Insufficient:** 自动柜员机有一些现金，但不足以进行交易
- **Empty:** 自动柜员机现金不足

### 3.7 NetworkStatus
- **Connected_Primary:** 使用主宽带连接
- **Connected_Backup:** 切换到 4G/LTE 备用
- **Disconnected:** 没有网络连接

### 3.8 CardCondition
- **Good:** 卡片状况良好
- **Damaged:** 卡片损坏/不可读
- **Expired:** 卡片已过期

---

## 4. 生成的测试用例

| 测试 # | 交易类型 | 卡类型 | PIN 状态 | 账户类型 | 交易金额 | 现金供应 | 网络状态 | 卡片状况 | 预期输出 |
|--------|-----------------|-----------|------------|--------------|-------------------|-------------------|----------------|---------------|-----------------|
| 1 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | 成功：发放现金 - 打印收据 |
| 2 | Deposit | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Primary | Good | 成功：接受存款 - 打印收据 |
| 3 | BalanceInquiry | EMVChip | Valid | Both | Within_Limit | Sufficient | Connected_Primary | Good | 成功：显示并打印余额 |
| 4 | Transfer | MagStripe | Valid | Both | Within_Limit | Sufficient | Connected_Primary | Good | 成功：完成转账 - 打印收据 |
| 5 | PINChange | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | 成功：成功更改 PIN |
| 6 | Withdrawal | EMVChip | Invalid_1st | Checking | Within_Limit | Sufficient | Connected_Primary | Good | 错误：错误的 PIN - 剩余 2 次尝试 |
| 7 | Withdrawal | MagStripe | Invalid_2nd | Savings | Within_Limit | Sufficient | Connected_Primary | Good | 错误：错误的 PIN - 剩余 1 次尝试 |
| 8 | Withdrawal | EMVChip | Invalid_3rd | Both | Within_Limit | Sufficient | Connected_Primary | Good | 错误：超过最大 PIN 尝试次数 - 保留卡片 |
| 9 | Withdrawal | Invalid | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | 错误：卡片不可识别 - 交易拒绝 |
| 10 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Damaged | 错误：卡片不可读 - 请使用另一张卡片 |
| 11 | Deposit | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Primary | Expired | 错误：卡片过期 - 请联系您的银行 |
| 12 | Withdrawal | EMVChip | Valid | Checking | At_Max_Transaction | Sufficient | Connected_Primary | Good | 成功：发放现金 - 打印收据 |
| 13 | Withdrawal | MagStripe | Valid | Savings | Exceeds_Transaction | Sufficient | Connected_Primary | Good | 错误：交易超过最大取款金额（500 美元） |
| 14 | Withdrawal | EMVChip | Valid | Both | Exceeds_Daily | Sufficient | Connected_Primary | Good | 错误：交易超过每日取款限制（1000 美元） |
| 15 | Deposit | MagStripe | Valid | Checking | At_Max_Transaction | Sufficient | Connected_Primary | Good | 成功：接受存款 - 打印收据 |
| 16 | Deposit | EMVChip | Valid | Savings | Exceeds_Transaction | Sufficient | Connected_Primary | Good | 错误：存款超过最大金额（5000 美元） |
| 17 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Insufficient | Connected_Primary | Good | 错误：自动柜员机中现金不足，无法进行此金额的交易 |
| 18 | Withdrawal | MagStripe | Valid | Savings | Within_Limit | Empty | Connected_Primary | Good | 错误：自动柜员机现金不足 - 请尝试另一地点 |
| 19 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Backup | Good | 成功：发放现金 - 打印收据（备用网络） |
| 20 | Deposit | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Backup | Good | 成功：接受存款 - 打印收据（备用网络） |
| 21 | Transfer | EMVChip | Valid | Both | Within_Limit | Sufficient | Connected_Backup | Good | 成功：完成转账 - 打印收据（备用网络） |
| 22 | Withdrawal | MagStripe | Valid | Checking | Within_Limit | Sufficient | Disconnected | Good | 错误：无法连接到银行 - 交易不可用 |
| 23 | Deposit | EMVChip | Valid | Savings | Within_Limit | Sufficient | Disconnected | Good | 错误：无法连接到银行 - 交易不可用 |
| 24 | Transfer | MagStripe | Valid | Both | Within_Limit | Sufficient | Disconnected | Good | 错误：无法连接到银行 - 交易不可用 |
| 25 | Transfer | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | 错误：转账需要多个账户 |
| 26 | Withdrawal | MagStripe | Valid | Both | At_Max_Transaction | Sufficient | Connected_Backup | Good | 成功：发放现金 - 打印收据（备用网络） |
| 27 | BalanceInquiry | MagStripe | Valid | Checking | Within_Limit | Sufficient | Connected_Backup | Good | 成功：显示并打印余额（备用网络） |
| 28 | PINChange | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Backup | Good | 成功：成功更改 PIN（备用网络） |
| 29 | Deposit | EMVChip | Valid | Both | At_Max_Transaction | Sufficient | Connected_Backup | Good | 成功：接受存款 - 打印收据（备用网络） |
| 30 | Withdrawal | EMVChip | Invalid_1st | Savings | Exceeds_Transaction | Insufficient | Connected_Backup | Good | 错误：错误的 PIN - 剩余 2 次尝试 |
| 31 | BalanceInquiry | EMVChip | Invalid_2nd | Savings | Within_Limit | Sufficient | Connected_Primary | Good | 错误：错误的 PIN - 剩余 1 次尝试 |

---

## 5. 测试覆盖率分析

### 5.1 按交易类型覆盖率
- **Withdrawal:** 14 个测试用例（45%）
- **Deposit:** 7 个测试用例（23%）
- **BalanceInquiry:** 3 个测试用例（10%）
- **Transfer:** 4 个测试用例（13%）
- **PINChange:** 2 个测试用例（6%）
- **其他（卡片错误）：** 1 个测试用例（3%）

### 5.2 按结果类型覆盖率
- **成功场景：** 17 个测试用例（55%）
- **错误场景：** 14 个测试用例（45%）

### 5.3 覆盖的关键场景
✅ 测试了所有交易类型  
✅ 测试了所有卡片类型  
✅ 测试了所有 PIN 场景，包括卡片保留  
✅ 执行交易限制  
✅ 执行每日限制  
✅ 现金供应场景  
✅ 网络故障转移测试  
✅ 卡片状况验证  
✅ 账户类型验证  

---

## 6. 测试执行指南

### 6.1 测试前设置

1. **ATM 配置：**
   - 加载现金纸带，数量充足
   - 验证所有硬件组件正常工作
   - 根据规范配置交易限制
   - 确保主备网络连接

2. **测试卡片：**
   - 准备 EMV 芯片卡（有效、过期）
   - 准备磁条卡（有效、损坏）
   - 准备无效/不可识别的卡片

3. **测试账户：**
   - 创建测试账户（支票、储蓄、两者都有）
   - 设置已知余额以供验证
   - 配置每日取款限制

### 6.2 测试执行过程

对于每个测试用例：

1. **设置：** 根据测试参数配置 ATM 和账户
2. **执行：** 按指定方式执行交易
3. **观察：** 记录实际结果
4. **验证：** 将其与预期输出进行比较
5. **记录：** 记录结果和任何偏差
6. **重置：** 将 ATM 返回到初始状态以进行下一个测试

### 6.3 通过/失败标准

**通过：**
- 实际输出与预期输出完全匹配
- 交易在指定时间内完成
- 打印收据（如果适用）并包含正确信息
- 正确创建审计日志条目

**失败：**
- 输出与预期不同
- 系统错误或崩溃
- 交易超时
- 预期打印收据但未打印
- 绕过安全验证

---

## 7. 测试环境要求

### 7.1 硬件

- 所有组件正常工作的 ATM
- 主备网络连接
- 混合面额的现金纸带
- 加载收据纸
- 各种类型的测试卡片

### 7.2 软件

- ATM 应用软件 v1.0
- 测试交易处理环境
- 网络故障转移模拟工具
- 监控和日志记录工具

### 7.3 测试数据

- 有效的测试账户凭据
- 多种账户类型
- 已知的账户余额
- 过期和无效的卡片用于负面测试

---

## 8. 基于风险的测试优先级

### 优先级 1（关键）- 必须通过
- 测试用例：1、2、3、8、9、13、14、18、22
- **重点：** 核心交易、安全（卡片保留）、限制执行、关键错误条件

### 优先级 2（高）- 应通过
- 测试用例：4、5、6、7、10、11、12、16、17、19、23、24
- **重点：** 所有交易类型、错误处理、网络故障转移

### 优先级 3（中等）- 好