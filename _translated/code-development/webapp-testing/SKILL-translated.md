<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:10:30
翻译模型: glm-4-flash
原文大小: 3,861 字符
-->

---
name: webapp-testing
description: 使用 Playwright 与本地 Web 应用进行交互和测试的工具套件。支持验证前端功能、调试 UI 行为、捕获浏览器截图和查看浏览器日志。
license: 详细条款请参阅 LICENSE.txt
---

# Web 应用测试

要测试本地 Web 应用，编写原生的 Python Playwright 脚本。

**可用的辅助脚本**：
- `scripts/with_server.py` - 管理服务器生命周期（支持多个服务器）

**始终先运行 `--help` 来查看用法**。 在尝试运行脚本并发现需要绝对必要的定制解决方案之前，不要阅读源代码。这些脚本可能非常大，因此会污染你的上下文窗口。它们存在是为了直接作为黑盒脚本调用，而不是被摄入到你的上下文窗口中。

## 决策树：选择你的方法

```
用户任务 → 是否是静态 HTML？
    ├─ 是 → 直接读取 HTML 文件以识别选择器
    │         ├─ 成功 → 使用选择器编写 Playwright 脚本
    │         └─ 失败/不完整 → 作为动态处理（以下）
    │
    └─ 否（动态 Web 应用）→ 服务器是否已经运行？
        ├─ 否 → 运行：python scripts/with_server.py --help
        │        然后使用辅助工具并编写简化的 Playwright 脚本
        │
        └─ 是 → 探索-然后行动：
            1. 导航并等待网络空闲
            2. 捕获截图或检查 DOM
            3. 从渲染状态中识别选择器
            4. 使用发现的选择器执行操作
```

## 示例：使用 with_server.py

要启动服务器，首先运行 `--help`，然后使用辅助工具：

**单个服务器：**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**多个服务器（例如，后端 + 前端）：**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

要创建自动化脚本，仅包含 Playwright 逻辑（服务器会自动管理）：
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # 总是在无头模式下启动 chromium
    page = browser.new_page()
    page.goto('http://localhost:5173') # 服务器已运行并准备就绪
    page.wait_for_load_state('networkidle') # CRITICAL：等待 JS 执行
    # ... 你的自动化逻辑
    browser.close()
```

## 探索-然后行动模式

1. **检查渲染的 DOM**：
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **从检查结果中识别选择器**

3. **使用发现的选择器执行操作**

## 常见陷阱

❌ **不要** 在动态应用中等待 `networkidle` 之前检查 DOM
✅ **要** 在检查之前等待 `page.wait_for_load_state('networkidle')`

## 最佳实践

- **将捆绑的脚本作为黑盒使用** - 要完成一项任务，考虑是否可以使用 `scripts/` 中提供的脚本之一。这些脚本可以可靠地处理常见的复杂工作流程，而不会污染上下文窗口。使用 `--help` 查看用法，然后直接调用。
- 使用 `sync_playwright()` 对于同步脚本
- 完成后始终关闭浏览器
- 使用描述性的选择器：`text=`, `role=`, CSS 选择器或 IDs
- 添加适当的等待：`page.wait_for_selector()` 或 `page.wait_for_timeout()`

## 参考文件

- **examples/** - 显示常见模式的示例：
  - `element_discovery.py` - 在页面上发现按钮、链接和输入
  - `static_html_automation.py` - 使用 file:// URLs 进行本地 HTML
  - `console_logging.py` - 在自动化过程中捕获控制台日志