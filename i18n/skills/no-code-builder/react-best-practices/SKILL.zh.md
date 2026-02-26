---
name: vercel-react-best-practices
description: Vercel 工程师提供的 React 和 Next.js 性能优化指南。该技能应在编写、审查或重构 React/Next.js 代码时使用，以确保最佳的性能模式。触发涉及 React 组件、Next.js 页面、数据获取、包优化或性能改进的任务。
---

# Vercel React 最佳实践

Vercel 维护的 React 和 Next.js 应用程序的全面性能优化指南。包含 8 个类别下的 45 条规则，根据影响优先级排序，以指导自动化重构和代码生成。

## 应用场景

在以下情况下参考这些指南：

- 编写新的 React 组件或 Next.js 页面
- 实现数据获取（客户端或服务器端）
- 审查代码以发现性能问题
- 重构现有的 React/Next.js 代码
- 优化包大小或加载时间

## 按优先级排序的规则类别

| 优先级 | 类别 | 影响 | 前缀 |
|----------|----------|--------|--------|
| 1 | 消除瀑布效应 | CRITICAL | `async-` |
| 2 | 包大小优化 | CRITICAL | `bundle-` |
| 3 | 服务器端性能 | HIGH | `server-` |
| 4 | 客户端数据获取 | MEDIUM-HIGH | `client-` |
| 5 | 重新渲染优化 | MEDIUM | `rerender-` |
| 6 | 渲染性能 | MEDIUM | `rendering-` |
| 7 | JavaScript 性能 | LOW-MEDIUM | `js-` |
| 8 | 高级模式 | LOW | `advanced-` |

## 快速参考

### 1. 消除瀑布效应 (CRITICAL)

- `async-defer-await` - 将 await 移动到实际使用的分支中
- `async-parallel` - 使用 Promise.all() 进行独立操作
- `async-dependencies` - 使用 better-all 进行部分依赖
- `async-api-routes` - 在 API 路由中尽早开始 promises，延迟等待
- `async-suspense-boundaries` - 使用 Suspense 来流式传输内容

### 2. 包大小优化 (CRITICAL)

- `bundle-barrel-imports` - 直接导入，避免 barrel 文件
- `bundle-dynamic-imports` - 使用 next/dynamic 对重组件进行动态导入
- `bundle-defer-third-party` - 在 hydrate 后加载分析/日志
- `bundle-conditional` - 仅在功能激活时加载模块
- `bundle-preload` - 在悬停/聚焦时预加载以提高感知速度

### 3. 服务器端性能 (HIGH)

- `server-cache-react` - 使用 React.cache() 进行请求去重
- `server-cache-lru` - 使用 LRU 缓存进行跨请求缓存
- `server-serialization` - 最小化传递给客户端组件的数据
- `server-parallel-fetching` - 重新构建组件以并行化获取
- `server-after-nonblocking` - 使用 after() 进行非阻塞操作

### 4. 客户端数据获取 (MEDIUM-HIGH)

- `client-swr-dedup` - 使用 SWR 进行自动请求去重
- `client-event-listeners` - 去重全局事件监听器

### 5. 重新渲染优化 (MEDIUM)

- `rerender-defer-reads` - 不要订阅仅在回调中使用的状态
- `rerender-memo` - 将昂贵的操作提取到 memoized 组件中
- `rerender-dependencies` - 在 effects 中使用原始依赖
- `rerender-derived-state` - 订阅派生布尔值，而不是原始值
- `rerender-functional-setstate` - 使用功能 setState 以稳定回调
- `rerender-lazy-state-init` - 将函数传递给 useState 以处理昂贵的值
- `rerender-transitions` - 使用 startTransition 进行非紧急更新

### 6. 渲染性能 (MEDIUM)

- `rendering-animate-svg-wrapper` - 动画 div 包装器，而不是 SVG 元素
- `rendering-content-visibility` - 使用 content-visibility 进行长列表
- `rendering-hoist-jsx` - 将静态 JSX 提取到组件外部
- `rendering-svg-precision` - 减少 SVG 坐标精度
- `rendering-hydration-no-flicker` - 使用内联脚本进行客户端数据
- `rendering-activity` - 使用 Activity 组件进行显示/隐藏
- `rendering-conditional-render` - 使用三元运算符，而不是 && 进行条件判断

### 7. JavaScript 性能 (LOW-MEDIUM)

- `js-batch-dom-css` - 通过类或 cssText 分组 CSS 更改
- `js-index-maps` - 为重复查找构建 Map
- `js-cache-property-access` - 在循环中缓存对象属性
- `js-cache-function-results` - 在模块级 Map 中缓存函数结果
- `js-cache-storage` - 缓存 localStorage/sessionStorage 读取
- `js-combine-iterations` - 将多个 filter/map 合并到一个循环中
- `js-length-check-first` - 在昂贵的比较之前检查数组长度
- `js-early-exit` - 从函数中提前返回
- `js-hoist-regexp` - 在循环外创建 RegExp
- `js-min-max-loop` - 使用循环进行 min/max，而不是排序
- `js-set-map-lookups` - 使用 Set/Map 进行 O(1) 查找
- `js-tosorted-immutable` - 使用 toSorted() 进行不可变操作

### 8. 高级模式 (LOW)

- `advanced-event-handler-refs` - 在 refs 中存储事件处理器
- `advanced-use-latest` - 使用 useLatest 进行稳定的回调引用

## 如何使用

阅读单个规则文件以获取详细说明和代码示例：

```plaintext
rules/async-parallel.md
rules/bundle-barrel-imports.md
rules/_sections.md
```

每个规则文件包含：

- 有关为什么它很重要的简要说明
- 带有说明的错误代码示例
- 带有说明的正确代码示例
- 额外的上下文和参考资料

## 完整编译文档

对于包含所有规则展开的完整指南：`AGENTS.md`