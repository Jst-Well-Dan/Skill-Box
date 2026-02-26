<!--
本文件由智谱 AI 自动翻译生成
原文件: CONTRIBUTING.md
翻译时间: 2025-12-12 16:10:46
翻译模型: glm-4-flash
原文大小: 5,479 字符
-->

# 向 pypict-claude-skill 贡献

感谢您对 PICT 测试设计器 Claude 技能的贡献兴趣！本文档提供了贡献的指南和说明。

## 贡献方式

### 1. 添加示例
- 来自不同领域的真实世界测试场景
- 行业特定的测试模式
- 复杂约束场景
- 边界情况和高级用法

### 2. 改进文档
- 修复错别字或解释不清的地方
- 添加教程或指南
- 翻译文档
- 改进代码注释

### 3. 提升技能
- 优化测试用例生成
- 添加新的约束模式
- 改进预期输出确定
- 扩展领域支持

### 4. 报告问题
- 缺陷报告
- 功能请求
- 文档空白
- 用户体验改进

### 5. 分享用例
- 关于使用该技能的博客文章
- 视频教程
- 工作坊材料
- 成功故事

## 入门指南

### 分支和克隆

1. 在 GitHub 上分支仓库
2. 本地克隆您的分支：
   ```bash
   git clone https://github.com/yourusername/pypict-claude-skill.git
   cd pypict-claude-skill
   ```

3. 添加上游仓库：
   ```bash
   git remote add upstream https://github.com/originalowner/pypict-claude-skill.git
   ```

### 创建分支

创建一个描述性的分支名称：
```bash
git checkout -b feature/add-ecommerce-example
# 或
git checkout -b fix/typo-in-readme
# 或
git checkout -b docs/improve-installation-guide
```

## 贡献指南

### 行为准则

- 尊重和包容
- 欢迎新手
- 专注于建设性反馈
- 帮助他人学习和成长

### 质量标准

#### 对于示例
- 包含完整的规范/需求
- 提供清晰的 PICT 模型
- 生成全面的测试用例
- 添加预期输出
- 记录关键学习点
- 遵循现有的示例结构

#### 对于文档
- 使用清晰、简洁的语言
- 在需要时包含代码示例
- 测试所有命令和代码片段
- 遵循 Markdown 最佳实践
- 检查拼写和语法

#### 对于技能改进
- 在可能的情况下保持向后兼容性
- 添加注释解释复杂逻辑
- 更新文档以反映更改
- 包含演示新功能的示例
- 在提交前彻底测试

### 文件结构

当添加示例时：
```
examples/
├── your-example-name/
│   ├── README.md           # 概述和学习点
│   ├── specification.md    # 原始需求
│   ├── pict-model.txt     # 生成的 PICT 模型
│   └── test-plan.md       # 完整的测试计划
└── README.md              # 更新以列出您的示例
```

### 提交信息

编写清晰、描述性的提交信息：

```bash
# 推荐
git commit -m "添加电子商务结账测试示例"
git commit -m "修复安装说明中的错别字"
git commit -m "改进负测试的约束生成"

# 不理想
git commit -m "更新文件"
git commit -m "修复东西"
git commit -m "WIP"
```

### 提交请求过程

1. **更新文档** 如果您更改了功能
2. **添加测试/示例** 如果您添加了功能
3. **更新 README.md** 如果您添加了示例或重大功能
4. **确保质量**：
   - 检查错别字
   - 测试所有示例
   - 验证 Markdown 是否正确渲染
   - 确保链接正常工作

5. **提交 PR** 并提供清晰的描述：
   ```markdown
   ## 描述
   简要描述此 PR 做了什么
   
   ## 变更类型
   - [ ] 缺陷修复
   - [ ] 新功能
   - [ ] 文档更新
   - [ ] 示例添加
   
   ## 测试
   如何测试此变更？
   
   ## 相关问题
   修复 #123
   ```

6. **及时、专业地回应反馈**

## 示例贡献流程

### 添加新示例

1. 创建您的分支：
   ```bash
   git checkout -b example/api-testing
   ```

2. 将您的文件添加到 `examples/`：
   ```bash
   mkdir examples/api-testing
   # 创建您的规范、模型和测试计划
   ```

3. 更新 `examples/README.md`：
   ```markdown
   ## API 测试示例
   展示 PICT 测试用于 REST API 端点...
   ```

4. 提交您的更改：
   ```bash
   git add examples/api-testing/
   git add examples/README.md
   git commit -m "添加 REST API 测试示例"
   ```

5. 推送到您的分支：
   ```bash
   git push origin example/api-testing
   ```

6. 在 GitHub 上创建提交请求

### 修复文档

1. 创建您的分支：
   ```bash
   git checkout -b docs/clarify-installation
   ```

2. 进行您的更改

3. 提交并推送到您的分支：
   ```bash
   git commit -m "澄清 Windows 用户安装步骤"
   git push origin docs/clarify-installation
   ```

4. 创建提交请求

## 审查流程

1. **自动检查**（如果已配置）将运行
2. **维护者审查**通常在 1-2 周内
3. **反馈和迭代**可能被要求
4. **批准和合并**一旦所有标准都满足

## 认可

贡献者将被：
- 列在仓库的贡献者中
- 在发布说明中提及（对于重大贡献）
- 在适当的地方进行信用

## 有问题？

- 为一般问题打开一个问题
- 使用 `question` 标记您的问题
- 请耐心等待 - 我们都是志愿者！

## 许可证

通过贡献，您同意您的贡献将根据 MIT 许可证进行许可。

## 感谢！

每个贡献，无论大小，都有助于使此技能对每个人来说都更好。我们感谢您的时间和努力！ 🙏