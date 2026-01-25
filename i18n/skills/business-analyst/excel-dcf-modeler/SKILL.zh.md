---
name: excel-dcf-modeler
description: |
  在 Excel 中构建现金流折现 (DCF) 估值模型。适用于创建 DCF 模型、计算企业价值或评估公司价值。
  支持 'excel dcf'、'构建 dcf 模型'、'计算企业价值' 等指令。
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---

# Excel DCF 估值建模器

## 概述

按照投资银行标准创建专业的 DCF 估值模型，包括 WACC（加权平均资本成本）计算和敏感性分析。

## 前提条件

- Excel 或兼容的电子表格软件
- 目标公司的历史财务数据
- 用于估算 WACC 的行业可比数据

## 指导说明

1. 创建假设表，包括营收增长、利润率、WACC 和终值增长率
2. 构建自由现金流预测（5 年预测期）
3. 使用戈登增长模型 (Gordon Growth Model) 计算终值
4. 将现金流和终值折现为现值
5. 求和得到企业价值 (EV)，减去净负债得到股权价值
6. 为关键假设添加敏感性分析表

## 输出结果

- 包含 4 个工作表的完整 DCF 模型：假设、预测、估值和敏感性
- 企业价值和每股股权价值
- 关于 WACC 和终值增长率的敏感性分析

## 错误处理

| 错误 | 原因 | 解决方案 |
|-------|-------|----------|
| 终值出现 #DIV/0! | WACC 等于终值增长率 | 终值增长率必须小于 WACC |
| FCF 为负 | 高资本支出或营运资金需求 | 审查假设，可能需要不同的模型 |
| 估值 (EV) 不切实际 | 极端的增长假设 | 参照行业可比公司进行基准测试 |

## 示例

**示例：为一家 SaaS 公司估值**
请求："为一家年收入 5000 万美元、增长率为 30% 的 SaaS 公司创建 DCF 模型"
结果：包含 5 年预测、12% WACC、3% 终值增长率及敏感性表的 4 表模型

**示例：并购估值分析**
请求："对收购目标进行 DCF 分析"
结果：包含协同效应调整、场景分析和每股估值的模型

## 相关资源

- [Damodaran 在线 DCF 资源](https://pages.stern.nyu.edu/~adamodar/)
- [WSO DCF 建模指南](https://www.wallstreetoasis.com/)
- `{baseDir}/references/dcf-formulas.md` 获取 Excel 公式模板
