<!--
本文件由智谱 AI 自动翻译生成
原文件: AUTHENTICATION.md
翻译时间: 2025-12-12 16:12:13
翻译模型: glm-4-flash
原文大小: 5,601 字符
-->

# 认证架构

## 概述

此技能使用一种**混合认证方法**，结合了两种方法的优点：

1. **持久浏览器配置文件** (`user_data_dir`) 用于一致的浏览器指纹识别
2. 从 `state.json` 进行**手动Cookie注入**，以实现可靠的会话Cookie持久性

## 为什么选择这种方法？

### 问题

Playwright/Patchright存在一个已知的bug ([#36139](https://github.com/microsoft/playwright/issues/36139))，即在使用 `launch_persistent_context()` 与 `user_data_dir` 结合时，**会话Cookie**（没有 `Expires` 属性的Cookie）无法正确持久化。

**发生的情况：**
- ✅ 持久Cookie（带有 `Expires` 日期）→ 正确保存到浏览器配置文件
- ❌ 会话Cookie（没有 `Expires`）→ **浏览器重启后丢失**

**影响：**
- 一些Google认证Cookie是会话Cookie
- 用户会经历随机的认证失败
- “在我的机器上可行”综合症（取决于Google使用的Cookie）

### TypeScript与Python

**MCP服务器**（TypeScript）可以通过传递 `storage_state` 作为参数来绕过这个问题：

```typescript
// TypeScript - 可行！
const context = await chromium.launchPersistentContext(userDataDir, {
  storageState: "state.json",  // ← 加载Cookie，包括会话Cookie
  channel: "chrome"
});
```

但是**Python的Playwright API不支持此功能** ([#14949](https://github.com/microsoft/playwright/issues/14949))：

```python
# Python - 不支持！
context = playwright.chromium.launch_persistent_context(
    user_data_dir=profile_dir,
    storage_state="state.json",  # ← 参数在Python中不可用！
    channel="chrome"
)
```

## 我们的解决方案：混合方法

我们使用一个**两阶段认证系统**：

### 阶段 1：设置 (`auth_manager.py setup`)

1. 使用 `user_data_dir` 启动持久上下文
2. 用户手动登录
3. **保存状态到两个地方：**
   - 浏览器配置文件目录（自动，用于指纹和持久Cookie）
   - `state.json` 文件（显式保存，用于会话Cookie）

```python
context = playwright.chromium.launch_persistent_context(
    user_data_dir="browser_profile/",
    channel="chrome"
)
# 用户登录...
context.storage_state(path="state.json")  # 保存所有Cookie
```

### 阶段 2：运行时 (`ask_question.py`)

1. 使用 `user_data_dir` 启动持久上下文（加载指纹和持久Cookie）
2. **从 `state.json` 手动注入Cookie**（添加会话Cookie）

```python
# 第 1 步：使用浏览器配置文件启动
context = playwright.chromium.launch_persistent_context(
    user_data_dir="browser_profile/",
    channel="chrome"
)

# 第 2 步：从 state.json 手动注入Cookie
with open("state.json", 'r') as f:
    state = json.load(f)
    context.add_cookies(state['cookies'])  # ← 会话Cookie的解决方案！
```

## 优点

| 特性 | 我们的方法 | 纯 `user_data_dir` | 纯 `storage_state` |
|---------|--------------|----------------------|----------------------|
| **浏览器指纹一致性** | ✅ 重启后相同 | ✅ 相同 | ❌ 每次都变化 |
| **会话Cookie持久性** | ✅ 手动注入 | ❌ （bug）丢失 | ✅ 原生支持 |
| **持久Cookie持久性** | ✅ 自动 | ✅ 自动 | ✅ 原生支持 |
| **Google信任度** | ✅ 高（相同浏览器） | ✅ 高 | ❌ 低（新浏览器） |
| **跨平台可靠性** | ✅ Chrome所需 | ⚠️ Chromium问题 | ✅ 可移植 |
| **缓存性能** | ✅ 保持缓存 | ✅ 保持缓存 | ❌ 无缓存 |

## 文件结构

```
~/.claude/skills/notebooklm/data/
├── auth_info.json              # 认证元数据
├── browser_state/
│   ├── state.json             # Cookie + localStorage（用于手动注入）
│   └── browser_profile/       # Chrome用户配置文件（用于指纹和缓存）
│       ├── Default/
│       │   ├── Cookies        # 持久Cookie仅（会话Cookie缺失！）
│       │   ├── Local Storage/
│       │   └── Cache/
│       └── ...
```

## 为什么 `state.json` 是关键的

尽管我们使用了 `user_data_dir`，但我们**仍然需要 `state.json`**，因为：

1. **会话Cookie** 没有保存到浏览器配置文件（Playwright bug）
2. **手动注入** 是加载会话Cookie的唯一可靠方式
3. **验证** - 我们可以在启动前检查Cookie是否已过期

## 代码引用

**设置：** `scripts/auth_manager.py:94-120`
- 行 100-113：使用 `channel="chrome"` 启动持久上下文
- 行 167：通过 `context.storage_state()` 保存到 `state.json`

**运行时：** `scripts/ask_question.py:77-118`
- 行 86-99：启动持久上下文
- 行 101-118：手动Cookie注入解决方案

**验证：** `scripts/auth_manager.py:236-298`
- 行 262-275：启动持久上下文
- 行 277-287：用于验证的手动Cookie注入

## 相关问题

- [microsoft/playwright#36139](https://github.com/microsoft/playwright/issues/36139) - 会话Cookie未持久化
- [microsoft/playwright#14949](https://github.com/microsoft/playwright/issues/14949) - 持久上下文的存储状态
- [StackOverflow 问题](https://stackoverflow.com/questions/79641481/) - 会话Cookie持久化问题

## 未来改进

如果Playwright在Python的 `launch_persistent_context()` 中添加对 `storage_state` 参数的支持，我们可以简化为：

```python
# 未来（当Python API支持时）：
context = playwright.chromium.launch_persistent_context(
    user_data_dir="browser_profile/",
    storage_state="state.json",  # ← 会自动处理所有事情！
    channel="chrome"
)
```

直到那时，我们的混合方法是最可靠的解决方案。