<!--
本文件由智谱 AI 自动翻译生成
原文件: QUICKSTART.md
翻译时间: 2025-12-12 16:11:00
翻译模型: glm-4-flash
原文大小: 5,596 字符
-->

# 快速入门指南

在5分钟内开始使用 PICT 测试设计器！

## 安装（选择一种）

### 选项 1：个人安装（所有项目）

```bash
# 克隆到您的个人技能目录
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer

# 重新启动 Claude Code - 技能现在可在所有项目中使用
```

### 选项 2：特定项目安装

```bash
# 从您的项目目录
git clone https://github.com/omkamal/pypict-claude-skill.git .claude/skills/pict-test-designer

# 重新启动 Claude Code - 技能仅在此项目中可用
```

### 选项 3：手动下载

1. 从：`https://github.com/omkamal/pypict-claude-skill` 下载 ZIP 文件
2. 解压到 `~/.claude/skills/pict-test-designer`（个人）或 `.claude/skills/pict-test-designer`（项目）
3. 重新启动 Claude Code

## 您的第一个测试计划（3 步）

### 步骤 1：启动 Claude Code

打开您的终端或 Claude Code 桌面版

### 步骤 2：描述您的系统

只需告诉 Claude 您想测试的内容：

```
我需要测试一个登录功能，以下是我的要求：
- 用户可以使用电子邮件和密码登录
- 支持 2FA（启用/禁用）
- “记住我”复选框选项
- 3 次失败尝试后的速率限制

你能使用 pict-test-designer 技能设计测试用例吗？
```

### 步骤 3：获取您的测试用例！

Claude 将自动：
1. ✅ 分析您的需求
2. ✅ 识别测试参数和值
3. ✅ 生成具有约束的 PICT 模型
4. ✅ 创建优化的测试用例
5. ✅ 提供预期输出

## 示例输出

您将收到：

### 1. PICT 模型
```
电子邮件：有效，无效，空
密码：有效，无效，空
双因素认证：启用，禁用
记住我：勾选，未勾选
失败尝试：0，1，2，3

IF [失败尝试] = "3" THEN [电子邮件] = "有效"；
```

### 2. 测试用例表

| 测试 # | 电子邮件 | 密码 | 2FA | 记住 | 失败 | 预期输出 |
|--------|-------|----------|-----|----------|--------|-----------------|
| 1 | Valid | Valid | Enabled | Checked | 0 | 成功：使用 2FA 提示登录 |
| 2 | Valid | Invalid | Disabled | Unchecked | 1 | 错误：密码错误（剩余 2 次尝试） |
| ... | ... | ... | ... | ... | ... | ... |

### 3. 摘要
- 总组合数：432
- PICT 测试用例：15
- 减少：96.5%

## 真实世界示例

### 尝试 ATM 示例

```
使用 pict-test-designer 技能，分析 examples/atm-specification.md 中的 ATM 规范，并显示测试覆盖率
```

这演示了一个复杂的系统，具有：
- 8 个参数
- 25,920 种可能的组合
- 只需 31 个测试用例！

## 常见用例

### 测试网页表单
```
为以下注册表单设计测试用例：
- 名称（必填，最多 50 个字符）
- 电子邮件（必填，必须为有效格式）
- 电话（可选，10 位数字）
- 国家（下拉菜单，5 个选项）
- 条款复选框（必填）
```

### 测试 API 端点
```
我需要测试一个 REST API 端点，该端点：
- 接受 GET、POST、PUT、DELETE 方法
- 需要身份验证（有效令牌，无效令牌，缺少令牌）
- 返回 JSON、XML 或错误
- 有速率限制

设计测试用例。
```

### 测试系统配置
```
使用以下配置测试我们的应用程序部署：
- 环境：开发，预发布，生产
- 数据库：MySQL，PostgreSQL，SQLite
- 缓存：启用/禁用
- SSL：启用/禁用
- 日志级别：调试，信息，错误

约束条件：生产必须不使用 SQLite 或调试日志
```

## 最佳实践提示

### ✅ 做这件事
- 清楚地描述您的需求
- 提及任何业务规则或约束
- 指定不同值的意义
- 如有需要，请要求特定的输出格式

### ❌ 避免这样做
- 太模糊：测试我的应用程序
- 缺乏上下文：为登录创建测试用例
- 缺少约束：未提及参数之间的依赖关系

## 下一步

1. **用您自己的系统尝试** - 从一个简单的功能开始
2. **查看示例** - 查看示例 [ATM 示例](examples/)
3. **阅读完整文档** - 查看 [SKILL.md](SKILL.md)
4. **根据您的需求定制** - 修改参数和约束
5. **分享您的结果** - 考虑为项目做出贡献！

## 获取帮助

- **有问题？** 在 GitHub 上打开 [问题](https://github.com/yourusername/pypict-claude-skill/issues)
- **示例？** 查看示例 [示例目录](examples/)
- **文档？** 阅读文档 [SKILL.md](SKILL.md) 和 [README.md](README.md)

## 高级用法

### 生成更多测试用例

一旦您有了 PICT 模型，您可以使用：

1. **使用在线工具**：
   - https://pairwise.yuuniworks.com/
   - https://pairwise.teremokgames.com/

2. **本地安装 PICT**：
   ```bash
   # Windows：从 GitHub 下载
   # https://github.com/microsoft/pict/releases
   
   # Linux/Mac：使用 pypict
   pip install pypict
   ```

3. **修改模型**：
   - 添加更多参数
   - 改变约束
   - 调整值
   - 重新生成测试用例

### 导出至测试管理工具

生成的测试用例可以：
- 复制到 Excel/CSV
- 导入到 JIRA、TestRail、Azure Test Plans
- 转换为自动化测试脚本
- 用于文档

## 成功故事

> “我们正在测试一个配置密集型的系统，有数百种可能的组合。使用 PICT 测试设计器，我们将测试套件从 500 多个测试减少到只有 45 个测试，同时保持了相同的覆盖率。这为我们节省了数周的时间！” - 质量保证团队领导

## 下一步计划

- 将此技能添加到您的常规测试工作流程中
- 在不同类型的系统上尝试
- 与您的团队分享示例
- 向项目贡献改进

**祝您测试愉快！ 🚀**