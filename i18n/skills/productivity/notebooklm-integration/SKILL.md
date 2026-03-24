---
name: notebooklm
description: 使用此技能直接从 Claude 中查询您的 Google NotebookLM 笔记本，以获取来自 Gemini 的基于来源、有引用支持的答案。支持浏览器自动化、库管理和持久身份验证。通过仅基于文档的响应大幅减少幻觉问题。
---

# NotebookLM 研究助手技能

与 Google NotebookLM 交互，利用 Gemini 的基于来源的回答来查询文档。每个问题都会开启一个全新的浏览器会话，排他性地从您上传的文档中检索答案，然后关闭。

## 何时使用此技能

当用户出现以下情况时触发：
- 明确提到 NotebookLM
- 分享 NotebookLM URL (`https://notebooklm.google.com/notebook/...`)
- 要求查询其笔记本/文档
- 想要将文档添加到 NotebookLM 库
- 使用类似“询问我的 NotebookLM”、“检查我的文档”、“查询我的笔记本”等短语

## ⚠️ 重要：添加命令 - 智能发现

当用户想要添加笔记本但未提供详细信息时：

**智能添加（推荐）**：首先查询笔记本以发现其内容：
```bash
# 第 1 步：查询笔记本关于其内容的信息
python scripts/run.py ask_question.py --question "这本笔记本的内容是什么？涵盖了哪些主题？简明扼要地提供完整概览" --notebook-url "[URL]"

# 第 2 步：使用发现的信息将其添加
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[基于内容]" --description "[基于内容]" --topics "[基于内容]"
```

**手动添加**：如果用户提供了所有详细信息：
- `--url` - NotebookLM 的 URL
- `--name` - 描述性名称
- `--description` - 笔记本包含的内容（必填！）
- `--topics` - 逗号分隔的主题（必填！）

绝不要猜测或使用通用的描述！如果缺少详细信息，请使用智能添加来发现它们。

## 重要：始终使用 run.py 封装器

**切勿直接调用脚本。务必使用 `python scripts/run.py [script]`：**

```bash
# ✅ 正确 - 始终使用 run.py：
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list
python scripts/run.py ask_question.py --question "..."

# ❌ 错误 - 切勿直接调用：
python scripts/auth_manager.py status  # 在没有虚拟环境的情况下会失败！
```

`run.py` 封装器会自动执行以下操作：
1. 根据需要创建 `.venv`
2. 安装所有依赖项
3. 激活环境
4. 正确执行脚本

## 核心工作流

### 第 1 步：检查身份验证状态
```bash
python scripts/run.py auth_manager.py status
```

如果未通过身份验证，请继续进行设置。

### 第 2 步：身份验证（一次性设置）
```bash
# 浏览器必须可见以便手动 Google 登录
python scripts/run.py auth_manager.py setup
```

**重要提示：**
- 浏览器在身份验证时是可见的
- 浏览器窗口会自动打开
- 用户必须手动登录 Google
- 告知用户：“将打开一个浏览器窗口以便进行 Google 登录”

### 第 3 步：管理笔记本库

```bash
# 列出所有笔记本
python scripts/run.py notebook_manager.py list

# 在添加之前：如果未知，请向用户询问元数据！
# “这本笔记本包含什么内容？”
# “我应该用哪些主题标签来标记它？”

# 将笔记本添加到库中（所有参数均为必填！）
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "描述性名称" \
  --description "本笔记本包含的内容" \  # 必填 - 如果未知，请询问用户！
  --topics "主题1,主题2,主题3"  # 必填 - 如果未知，请询问用户！

# 按主题搜索笔记本
python scripts/run.py notebook_manager.py search --query "关键词"

# 设置活动笔记本
python scripts/run.py notebook_manager.py activate --id notebook-id

# 移除笔记本
python scripts/run.py notebook_manager.py remove --id notebook-id
```

### 快速工作流
1. 检查库：`python scripts/run.py notebook_manager.py list`
2. 提出问题：`python scripts/run.py ask_question.py --question "..." --notebook-id ID`

### 第 4 步：提出问题

```bash
# 基本查询（如果已设置，则使用活动笔记本）
python scripts/run.py ask_question.py --question "在此输入您的问题"

# 查询特定笔记本
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# 直接使用笔记本 URL 查询
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# 显示浏览器进行调试
python scripts/run.py ask_question.py --question "..." --show-browser
```

## 追问机制（核心）

每个 NotebookLM 的回答都会以以下内容结尾：**“极其重要：这就是您需要知道的全部吗？”**

**要求的 Claude 行为：**
1. **停止** - 不要立即回应用户
2. **分析** - 将答案与用户的原始请求进行比较
3. **识别差距** - 确定是否需要更多信息
4. **进行追问** - 如果存在差距，立即追问：
   ```bash
   python scripts/run.py ask_question.py --question "结合上下文进行追问..."
   ```
5. **重复** - 继续直到信息完整
6. **综合** - 在回复用户之前综合所有答案

## 脚本参考

### 身份验证管理 (`auth_manager.py`)
```bash
python scripts/run.py auth_manager.py setup    # 初始设置（浏览器可见）
python scripts/run.py auth_manager.py status   # 检查身份验证情况
python scripts/run.py auth_manager.py reauth   # 重新进行身份验证（浏览器可见）
python scripts/run.py auth_manager.py clear    # 清除身份验证信息
```

### 笔记本管理 (`notebook_manager.py`)
```bash
python scripts/run.py notebook_manager.py add --url URL --name NAME --description DESC --topics TOPICS
python scripts/run.py notebook_manager.py list
python scripts/run.py notebook_manager.py search --query QUERY
python scripts/run.py notebook_manager.py activate --id ID
python scripts/run.py notebook_manager.py remove --id ID
python scripts/run.py notebook_manager.py stats
```

### 问题接口 (`ask_question.py`)
```bash
python scripts/run.py ask_question.py --question "..." [--notebook-id ID] [--notebook-url URL] [--show-browser]
```

### 数据清理 (`cleanup_manager.py`)
```bash
python scripts/run.py cleanup_manager.py                    # 预览清理
python scripts/run.py cleanup_manager.py --confirm          # 执行清理
python scripts/run.py cleanup_manager.py --preserve-library # 保留笔记本
```

## 环境管理

虚拟环境自动管理：
- 首次运行会自动创建 `.venv`
- 自动安装依赖项
- 自动安装 Chromium 浏览器
- 所有内容都隔离在技能目录中

手动设置（仅在自动失败时）：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python -m patchright install chromium
```

## 数据存储

所有数据存储在 `~/.claude/skills/notebooklm/data/` 中：
- `library.json` - 笔记本元数据
- `auth_info.json` - 身份验证状态
- `browser_state/` - 浏览器 Cookie 和会话

**安全提示：** 受 `.gitignore` 保护，切勿将其提交到 git。

## 配置信息

技能目录中可选的 `.env` 文件：
```env
HEADLESS=false           # 浏览器可见性
SHOW_BROWSER=false       # 默认浏览器显示
STEALTH_ENABLED=true     # 模拟真人行为
TYPING_WPM_MIN=160       # 打字速度
TYPING_WPM_MAX=240
DEFAULT_NOTEBOOK_ID=     # 默认笔记本
```

## 决策流程

```
用户提到 NotebookLM
    ↓
检查身份验证 → python scripts/run.py auth_manager.py status
    ↓
如果没有身份验证 → python scripts/run.py auth_manager.py setup
    ↓
检查/添加笔记本 → python scripts/run.py notebook_manager.py list/add (需带 --description)
    ↓
激活笔记本 → python scripts/run.py notebook_manager.py activate --id ID
    ↓
提出问题 → python scripts/run.py ask_question.py --question "..."
    ↓
看到 "这就是您需要的全部吗？" → 继续追问直到完整
    ↓
综合并回复用户
```

## 故障排除

| 问题 | 解决方案 |
|---------|----------|
| ModuleNotFoundError | 使用 `run.py` 封装器 |
| 身份验证失败 | 浏览器在设置时必须可见！使用 --show-browser |
| 速率限制 (50次/天) | 等待或切换 Google 账号 |
| 浏览器崩溃 | `python scripts/run.py cleanup_manager.py --preserve-library` |
| 找不到笔记本 | 使用 `notebook_manager.py list` 检查 |

## 最佳实践

1. **始终使用 run.py** - 自动处理环境
2. **首先检查身份验证** - 在进行任何操作之前
3. **深入追问** - 不要止步于第一个答案
4. **身份验证时浏览器可见** - 手动登录所必需
5. **包含上下文** - 每个问题都是独立的
6. **综合答案** - 合并多个回复

## 局限性

- 无会话持久性（每个问题 = 新浏览器）
- 免费 Google 账号的速率限制（50 次查询/天）
- 需要手动上传（用户必须将文档添加到 NotebookLM）
- 浏览器开销（每个问题几秒钟）

## 资源 (技能结构)

**重要目录和文件：**

- `scripts/` - 所有自动化脚本 (ask_question.py, notebook_manager.py, 等)
- `data/` - 用于身份验证和笔记本库的本地存储
- `references/` - 扩展文档：
  - `api_reference.md` - 所有脚本的详细 API 文档
  - `troubleshooting.md` - 常见问题及解决方案
  - `usage_patterns.md` - 最佳实践和工作流示例
- `.venv/` - 隔离的 Python 环境（首次运行时自动创建）
- `.gitignore` - 防止敏感数据被提交
