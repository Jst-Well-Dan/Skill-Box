<!--
本文件由智谱 AI 自动翻译生成
原文件: api_reference.md
翻译时间: 2025-12-12 16:12:32
翻译模型: glm-4-flash
原文大小: 7,602 字符
-->

---
# NotebookLM 技能 API 参考文档

所有 NotebookLM 技能模块的完整 API 文档。

## 重要：始终使用 run.py 包装器

**所有命令都必须使用 `run.py` 包装器以确保正确环境：**

```bash
# ✅ 正确：
python scripts/run.py [script_name].py [arguments]

# ❌ 错误：
python scripts/[script_name].py [arguments]  # 将失败，因为没有 venv！
```

## 核心脚本

### ask_question.py
使用自动化浏览器交互查询 NotebookLM。

```bash
# 基本用法
python scripts/run.py ask_question.py --question "你的问题"

# 使用特定笔记本
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# 使用直接 URL
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# 显示浏览器（调试）
python scripts/run.py ask_question.py --question "..." --show-browser
```

**参数：**
- `--question` (必需)：要问的问题
- `--notebook-id`：使用库中的笔记本
- `--notebook-url`：直接使用 URL
- `--show-browser`：使浏览器可见

**返回：** 带有后续提示的答案文本

### notebook_manager.py
使用 CRUD 操作管理笔记本库。

```bash
# 智能添加（首先发现内容）
python scripts/run.py ask_question.py --question "这个笔记本的内容是什么？涵盖了哪些主题？简要提供完整概述" --notebook-url "[URL]"
# 然后使用发现的信息添加
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "名称" \
  --description "描述" \
  --topics "topic1,topic2"

# 直接添加（当你知道内容时）
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "名称" \
  --description "它包含的内容" \
  --topics "topic1,topic2"

# 列出笔记本
python scripts/run.py notebook_manager.py list

# 搜索笔记本
python scripts/run.py notebook_manager.py search --query "关键字"

# 激活笔记本
python scripts/run.py notebook_manager.py activate --id notebook-id

# 删除笔记本
python scripts/run.py notebook_manager.py remove --id notebook-id

# 显示统计信息
python scripts/run.py notebook_manager.py stats
```

**命令：**
- `add`：添加笔记本（需要 --url, --name, --topics）
- `list`：显示所有笔记本
- `search`：通过关键字查找笔记本
- `activate`：设置默认笔记本
- `remove`：从库中删除
- `stats`：显示库统计信息

### auth_manager.py
处理 Google 认证和浏览器状态。

```bash
# 设置（浏览器可见用于登录）
python scripts/run.py auth_manager.py setup

# 检查状态
python scripts/run.py auth_manager.py status

# 重新认证
python scripts/run.py auth_manager.py reauth

# 清除认证
python scripts/run.py auth_manager.py clear
```

**命令：**
- `setup`：初始认证（浏览器必须可见）
- `status`：检查是否已认证
- `reauth`：清除并重新设置
- `clear`：删除所有认证数据

### cleanup_manager.py
使用保留选项清理技能数据。

```bash
# 预览清理
python scripts/run.py cleanup_manager.py

# 执行清理
python scripts/run.py cleanup_manager.py --confirm

# 保留库
python scripts/run.py cleanup_manager.py --confirm --preserve-library

# 强制不提示
python scripts/run.py cleanup_manager.py --confirm --force
```

**选项：**
- `--confirm`：实际执行清理
- `--preserve-library`：保留笔记本库
- `--force`：跳过确认提示

### run.py
处理环境设置的脚本包装器。

```bash
# 用法
python scripts/run.py [script_name].py [arguments]

# 示例
python scripts/run.py auth_manager.py status
python scripts/run.py ask_question.py --question "..."
```

**自动操作：**
1. 如果缺失，则创建 `.venv`
2. 安装依赖项
3. 激活环境
4. 执行目标脚本

## Python API 使用

### 使用 run.py 中的 subprocess

```python
import subprocess
import json

# 总是使用 run.py 包装器
result = subprocess.run([
    "python", "scripts/run.py", "ask_question.py",
    "--question", "你的问题",
    "--notebook-id", "notebook-id"
], capture_output=True, text=True)

answer = result.stdout
```

### 直接导入（venv 存在后）

```python
# 仅当 venv 已创建并激活时才有效
from notebook_manager import NotebookLibrary
from auth_manager import AuthManager

library = NotebookLibrary()
notebooks = library.list_notebooks()

auth = AuthManager()
is_auth = auth.is_authenticated()
```

## 数据存储

位置：`~/.claude/skills/notebooklm/data/`

```
data/
├── library.json       # 笔记本元数据
├── auth_info.json     # 认证状态
└── browser_state/     # 浏览器cookies
    └── state.json
```

**安全性：** 由 `.gitignore` 保护，切勿提交。

## 环境变量

可选的 `.env` 文件配置：

```env
HEADLESS=false           # 浏览器可见性
SHOW_BROWSER=false       # 默认显示
STEALTH_ENABLED=true     # 人类行为
TYPING_WPM_MIN=160       # 打字速度
TYPING_WPM_MAX=240
DEFAULT_NOTEBOOK_ID=     # 默认笔记本
```

## 错误处理

常见模式：

```python
# 使用 run.py 防止大多数错误
result = subprocess.run([
    "python", "scripts/run.py", "ask_question.py",
    "--question", "问题"
], capture_output=True, text=True)

if result.returncode != 0:
    error = result.stderr
    if "rate limit" in error.lower():
        # 等待或切换账户
        pass
    elif "not authenticated" in error.lower():
        # 运行 auth setup
        subprocess.run(["python", "scripts/run.py", "auth_manager.py", "setup"])
```

## 速率限制

免费 Google 账户：每天 50 次查询

解决方案：
1. 等待重置（太平洋标准时间午夜）
2. 使用 `reauth` 切换账户
3. 使用多个 Google 账户

## 高级模式

### 并行查询

```python
import concurrent.futures
import subprocess

def query(question, notebook_id):
    result = subprocess.run([
        "python", "scripts/run.py", "ask_question.py",
        "--question", question,
        "--notebook-id", notebook_id
    ], capture_output=True, text=True)
    return result.stdout

# 同时运行多个查询
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(query, q, nb)
        for q, nb in zip(questions, notebooks)
    ]
    results = [f.result() for f in futures]
```

### 批量处理

```python
def batch_research(questions, notebook_id):
    results = []
    for question in questions:
        result = subprocess.run([
            "python", "scripts/run.py", "ask_question.py",
            "--question", question,
            "--notebook-id", notebook_id
        ], capture_output=True, text=True)
        results.append(result.stdout)
        time.sleep(2)  # 避免速率限制
    return results
```

## 模块类

### NotebookLibrary
- `add_notebook(url, name, topics)`
- `list_notebooks()`
- `search_notebooks(query)`
- `get_notebook(notebook_id)`
- `activate_notebook(notebook_id)`
- `remove_notebook(notebook_id)`

### AuthManager
- `is_authenticated()`
- `setup_auth(headless=False)`
- `get_auth_info()`
- `clear_auth()`
- `validate_auth()`

### BrowserSession (内部)
- 处理浏览器自动化
- 管理隐身行为
- 不建议直接使用

## 最佳实践

1. **始终使用 run.py** - 确保环境
2. **首先检查认证** - 在操作之前
3. **处理速率限制** - 实现重试
4. **包含上下文** - 问题相互独立
5. **清理会话** - 使用 cleanup_manager