<!--
本文件由智谱 AI 自动翻译生成
原文件: STRUCTURE.md
翻译时间: 2025-12-12 16:11:11
翻译模型: glm-4-flash
原文大小: 6,670 字符
-->

# 仓库结构

pypict-claude-skill 仓库的完整文件结构。

```
pypict-claude-skill/
├── .github/                          # GitHub 配置
│   ├── ISSUE_TEMPLATE/               # 问题模板
│   │   ├── bug_report.md             # 缺陷报告模板
│   │   └── feature_request.md        # 功能请求模板
│   ├── workflows/                    # GitHub Actions
│   │   └── ci.yml                    # 验证 CI 工作流程
│   ├── markdown-link-check-config.json  # 链接检查配置
│   └── pull_request_template.md      # PR 模板
│
├── examples/                         # 真实世界示例
│   ├── README.md                     # 示例概述
│   ├── atm-specification.md          # 自动柜员机系统规范
│   └── atm-test-plan.md              # 完整的自动柜员机测试计划（31 个测试用例）
│
├── references/                       # 参考文档
│   ├── pict_syntax.md                # PICT 语法参考（占位符）
│   └── examples.md                   # PICT 示例参考（占位符）
│
├── scripts/                          # 辅助脚本
│   ├── README.md                     # 脚本文档
│   └── pict_helper.py                # PICT 的 Python 工具（生成、格式化、解析）
│
├── .gitignore                        # Git 忽略规则
├── CHANGELOG.md                      # 版本历史
├── CONTRIBUTING.md                   # 贡献指南
├── LICENSE                           # 带有 PICT 和 pypict 程序员归因的 MIT 许可证
├── PUBLISHING.md                     # 在 GitHub 上发布的指南
├── QUICKSTART.md                     # 快速入门指南
├── README.md                         # 主要文档
└── SKILL.md                          # Claude 技能定义

```

## 文件描述

### 根目录

| 文件 | 目的 | 状态 |
|------|---------|--------|
| **README.md** | 仓库的主要文档，包含安装和使用说明 | ✅ 完成 |
| **SKILL.md** | Claude 技能定义，包含工作流程和最佳实践 | ✅ 完成 |
| **LICENSE** | 带有 PICT 和 pypict 程序员归因的 MIT 许可证 | ✅ 完成 |
| **CONTRIBUTING.md** | 贡献项目的指南 | ✅ 完成 |
| **CHANGELOG.md** | 版本历史和发布说明 | ✅ 完成 |
| **QUICKSTART.md** | 新用户的快速入门指南 | ✅ 完成 |
| **PUBLISHING.md** | 发布仓库的步骤指南 | ✅ 完成 |
| **.gitignore** | Python 和临时文件的 Git 忽略模式 | ✅ 完成 |

### .github/ 目录

| 文件 | 目的 | 状态 |
|------|---------|--------|
| **workflows/ci.yml** | CI/CD 的 GitHub Actions 工作流程 | ✅ 完成 |
| **ISSUE_TEMPLATE/bug_report.md** | 缺陷报告模板 | ✅ 完成 |
| **ISSUE_TEMPLATE/feature_request.md** | 功能请求模板 | ✅ 完成 |
| **pull_request_template.md** | PR 模板 | ✅ 完成 |
| **markdown-link-check-config.json** | 链接检查配置 | ✅ 完成 |

### examples/ 目录

| 文件 | 目的 | 状态 |
|------|---------|--------|
| **README.md** | 可用示例的概述 | ✅ 完成 |
| **atm-specification.md** | 完整的自动柜员机系统规范（11 个部分） | ✅ 完成 |
| **atm-test-plan.md** | 包含 PICT 模型和 31 个测试用例的完整测试计划 | ✅ 完成 |

### references/ 目录

| 文件 | 目的 | 状态 |
|------|---------|--------|
| **pict_syntax.md** | PICT 语法参考和语法 | 🚧 占位符 |
| **examples.md** | 按领域收集的 PICT 示例 | 🚧 占位符 |

### scripts/ 目录

| 文件 | 目的 | 状态 |
|------|---------|--------|
| **README.md** | 脚本文档 | ✅ 完成 |
| **pict_helper.py** | PICT 的 Python 工具（生成、格式化、解析） | 🚧 基本实现 |

## 文件关键特性

### README.md
- Claude Code CLI 和桌面安装说明
- 快速入门指南
- 自动柜员机示例摘要
- 对微软 PICT 和 pypict 的致谢
- 文档和资源链接

### SKILL.md
- 使用技能的完整工作流程
- 参数识别指南
- PICT 模型生成过程
- 约束编写最佳实践
- 预期输出确定
- 常见模式和示例

### examples/atm-test-plan.md
- 包含 8 个参数的完整 PICT 模型
- 16 个业务规则约束
- 31 个优化后的测试用例（从 25,920 种组合中）
- 覆盖率分析
- 测试执行指南
- 基于风险的优先级排序
- 可追溯性矩阵

### PUBLISHING.md
- 步骤指南，用于在 GitHub 上发布
- 仓库配置说明
- 发布创建过程
- 推广策略
- 维护指南

### CONTRIBUTING.md
- 贡献类型和指南
- 示例的文件结构
- 提交信息约定
- PR 流程
- 质量标准

## 文件统计

- **总文件数:** 18
- **Markdown 文档:** 14 个文件
- **Python 脚本:** 1 个文件
- **配置文件:** 3 个文件
- **完成文件:** 15 个（83%）
- **占位符文件:** 2 个（11%）
- **基本实现:** 1 个（6%）

## 文档覆盖率

| 类别 | 覆盖率 |
|----------|----------|
| 安装 | ✅ 完成 |
| 快速入门 | ✅ 完成 |
| 示例 | ✅ 1 个完成（ATM），更多计划中 |
| API/参考 | 🚧 占位符（待完成） |
| 贡献 | ✅ 完成 |
| 发布 | ✅ 完成 |

## 仓库的下一步步骤

### 短期（v1.1）
1. 完成 `references/pict_syntax.md` 中的完整 PICT 语法
2. 向 `references/examples.md` 添加更多示例
3. 增强 `pict_helper.py` 以实现完整的 pypict 集成
4. 添加更多真实世界示例

### 中期（v1.2-1.3）
1. 电子商务结账示例
2. API 测试示例
3. 移动应用配置示例
4. 与测试管理工具的集成

### 长期（v2.0+）
1. 高级约束模式库
2. 从代码自动生成测试用例
3. CI/CD 集成示例
4. 性能测试模板

## 贡献结构

当添加新文件时：

1. **示例**：添加到 `examples/`，包含规范和测试计划
2. **文档**：根据适当情况添加到根目录或 `references/`
3. **脚本**：添加到 `scripts/` 并更新 README
4. **模板**：添加到 `.github/ISSUE_TEMPLATE/` 或 `.github/`

## 维护清单

- [ ] 保持 CHANGELOG.md 更新
- [ ] 更新 README.md 中的新功能
- [ ] 向 examples/README.md 添加新示例
- [ ] 更新本文件中的文件计数
- [ ] 维护所有 markdown 文件中的链接
- [ ] 测试所有代码示例和命令
- [ ] 保持许可证归因最新

---

**仓库状态：** ✅ 准备发布

**最后更新：** 2025 年 10 月 19 日

**版本：** 1.0.0