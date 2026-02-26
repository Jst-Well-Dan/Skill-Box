---
name: excel-lbo-modeler
description: |
  在Excel中构建具有债务计划和IRR分析的杠杆收购（LBO）模型。
  用于构建LBO交易或分析私募股权回报。
  使用短语“excel lbo”、“构建lbo模型”、“计算pe回报”等触发。
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---

# Excel LBO Modeler

## 概述

创建具有债务结构、摊销计划和私募股权交易回报分析的杠杆收购模型。

## 先决条件

- Excel或兼容的电子表格软件
- 目标公司财务数据
- 债务条款表参数
- 入场/退出倍数假设

## 指令

1. 设置交易结构（购买价格、债务/股权分割）
2. 为每个部分（高级、夹层等）构建债务计划
3. 创建包含债务偿还的运营预测
4. 计算可用于债务偿还的现金流
5. 模型退出场景并计算IRR/MOIC

## 输出

- 完整的LBO模型，包括资金来源和使用、债务计划和回报
- 在各种退出倍数和年份的IRR和MOIC
- 入场/退出倍数和杠杆的敏感性表格

## 错误处理

| 错误 | 原因 | 解决方案 |
|-------|-------|----------|
| 负现金流 | 债务偿还超过EBITDA | 减少杠杆或重新结构化债务条款 |
| IRR #NUM! | 无有效解决方案 | 检查退出价值是否超过股权贡献 |
| 循环引用 | 与利息挂钩的现金回收 | 启用迭代计算 |

## 示例

**示例：中市场LBO**

请求： "为EBITDA为1亿美元的公司构建一个8倍入场LBO模型"
结果：60%高级/40%股权结构，5年模型，7倍-10倍退出IRR分析

**示例：附加收购**

请求： "模型具有协同效应的附加收购"
结果：包含协同效应逐步实施和增值分析的集成模型

## 资源

- [Macabacus LBO Modeling](https://macabacus.com/)
- [WSO PE Interview Prep](https://www.wallstreetoasis.com/)
- `{baseDir}/references/lbo-formulas.md` 用于债务计划模板