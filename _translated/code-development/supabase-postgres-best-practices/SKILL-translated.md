---
name: supabase-postgres-best-practices
description: 来自 Supabase 的 Postgres 性能优化与最佳实践。在编写、审查或优化 Postgres 查询、架构设计或数据库配置时使用此技能。
license: MIT
metadata:
  author: supabase
  version: "1.1.0"
  organization: Supabase
  date: 2026年1月
  abstract: 为使用 Supabase 和 Postgres 的开发者提供的全面 Postgres 性能优化指南。包含 8 个类别的性能规则，按影响程度从关键（查询性能、连接管理）到增量（高级功能）排序。每条规则包括详细说明、错误 vs. 正确的 SQL 示例、查询计划分析以及指导自动化优化和代码生成的特定性能指标。
---

# Supabase Postgres 最佳实践

由 Supabase 维护的全面 Postgres 性能优化指南。包含 8 个类别的规则，按影响程度排序，以指导自动化查询优化和架构设计。

## 何时应用

在以下情况下参考这些指南：
- 编写 SQL 查询或设计架构时
- 实施索引或查询优化时
- 审查数据库性能问题时
- 配置连接池或扩缩容时
- 针对 Postgres 特定功能进行优化时
- 使用行级安全性 (RLS) 时

## 按优先级排序的规则类别

| 优先级 | 类别 | 影响 | 前缀 |
|----------|----------|--------|--------|
| 1 | 查询性能 (Query Performance) | 关键 (CRITICAL) | `query-` |
| 2 | 连接管理 (Connection Management) | 关键 (CRITICAL) | `conn-` |
| 3 | 安全性与 RLS (Security & RLS) | 关键 (CRITICAL) | `security-` |
| 4 | 架构设计 (Schema Design) | 高 (HIGH) | `schema-` |
| 5 | 并发与锁定 (Concurrency & Locking) | 中高 (MEDIUM-HIGH) | `lock-` |
| 6 | 数据访问模式 (Data Access Patterns) | 中 (MEDIUM) | `data-` |
| 7 | 监控与诊断 (Monitoring & Diagnostics) | 低中 (LOW-MEDIUM) | `monitor-` |
| 8 | 高级功能 (Advanced Features) | 低 (LOW) | `advanced-` |

## 如何使用

阅读各规则文件以获取详细说明和 SQL 示例：

```
references/query-missing-indexes.md
references/schema-partial-indexes.md
references/_sections.md
```

每个规则文件包含：
- 为什么要关注该规则的简要说明
- 错误的 SQL 示例及说明
- 正确的 SQL 示例及说明
- 可选的 EXPLAIN 输出或指标
- 额外的上下文和参考资料
- Supabase 特有的注意事项（如果适用）

## 参考资料

- https://www.postgresql.org/docs/current/
- https://supabase.com/docs
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
- https://supabase.com/docs/guides/auth/row-level-security
