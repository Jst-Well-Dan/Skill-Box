---
name: supabase-postgres-best-practices
description: 来自 Supabase 的 Postgres 性能优化和最佳实践。在编写、审查或优化 Postgres 查询、架构设计或数据库配置时使用此技能。
license: MIT
metadata:
  author: supabase
  version: "1.1.0"
  organization: Supabase
  date: January 2026
  abstract: 为使用 Supabase 和 Postgres 的开发者提供的全面 Postgres 性能优化指南。包含涵盖 8 个类别的性能规则，按影响程度从关键（查询性能、连接管理）到增量（高级功能）排序。每条规则都包括详细说明、错误与正确 SQL 示例、查询计划分析以及特定性能指标，以指导自动化优化和代码生成。
---

# Supabase Postgres 最佳实践

由 Supabase 维护的全面 Postgres 性能优化指南。包含涵盖 8 个类别的规则，按影响程度排序，以指导自动化查询优化和架构设计。

## 何时应用

在以下情况参考这些指南：
- 编写 SQL 查询或设计架构时
- 实施索引或查询优化时
- 审查数据库性能问题时
- 配置连接池或扩缩容时
- 为 Postgres 特定功能进行优化时
- 处理行级安全性 (RLS) 时

## 按优先级排序的规则类别

| 优先级 | 类别 | 影响 | 前缀 |
|----------|----------|--------|--------|
| 1 | 查询性能 | 关键 (CRITICAL) | `query-` |
| 2 | 连接管理 | 关键 (CRITICAL) | `conn-` |
| 3 | 安全与 RLS | 关键 (CRITICAL) | `security-` |
| 4 | 架构设计 | 高 (HIGH) | `schema-` |
| 5 | 并发与锁定 | 中高 (MEDIUM-HIGH) | `lock-` |
| 6 | 数据访问模式 | 中 (MEDIUM) | `data-` |
| 7 | 监控与诊断 | 低中 (LOW-MEDIUM) | `monitor-` |
| 8 | 高级功能 | 低 (LOW) | `advanced-` |

## 如何使用

阅读各个规则文件以获取详细说明和 SQL 示例：

```
references/query-missing-indexes.md
references/schema-partial-indexes.md
references/_sections.md
```

每个规则文件包含：
- 说明其重要性的简短解释
- 带有解释的错误 SQL 示例
- 带有解释的正确 SQL 示例
- 可选的 EXPLAIN 输出或指标
- 附加背景信息和参考资料
- Supabase 特定说明（如果适用）

## 参考资料

- https://www.postgresql.org/docs/current/
- https://supabase.com/docs
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
- https://supabase.com/docs/guides/auth/row-level-security
