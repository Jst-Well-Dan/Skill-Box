---
title: 在 WHERE 和 JOIN 列上添加索引
impact: 关键 (CRITICAL)
impactDescription: 在大型表上可提升 100-1000 倍的查询速度
tags: 索引, 性能, 顺序扫描, 查询优化
---

## 在 WHERE 和 JOIN 列上添加索引

对未建立索引的列进行过滤或连接查询会导致全表扫描。随着数据量的增长，查询速度会呈指数级下降。

**不正确（大表上的顺序扫描）：**

```sql
-- customer_id 上没有索引，导致全表扫描
select * from orders where customer_id = 123;

-- EXPLAIN 显示：Seq Scan on orders (cost=0.00..25000.00 rows=100 width=85)
```

**正确（索引扫描）：**

```sql
-- 在频繁过滤的列上创建索引
create index orders_customer_id_idx on orders (customer_id);

select * from orders where customer_id = 123;

-- EXPLAIN 显示：Index Scan using orders_customer_id_idx (cost=0.42..8.44 rows=100 width=85)
```

对于 JOIN 列，务必在外部键（foreign key）一侧建立索引：

```sql
-- 为引用列建立索引
create index orders_customer_id_idx on orders (customer_id);

select c.name, o.total
from customers c
join orders o on o.customer_id = c.id;
```

参考资料：[查询优化 (Query Optimization)](https://supabase.com/docs/guides/database/query-optimization)
