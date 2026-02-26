<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:12:52
翻译模型: glm-4-flash
原文大小: 9,408 字符
-->

---
name: notebooklm
description: 使用此技能直接从 Claude Code 查询您的 Google NotebookLM 笔记本，以获取 Gemini 的基于文档、有引用支持的答案。浏览器自动化、库管理、持久认证。通过仅使用文档响应，大幅减少幻觉。
---

# NotebookLM 研究助手技能

与 Google NotebookLM 交互，使用 Gemini 的基于文档的答案查询文档。每个问题都会打开一个新的浏览器会话，仅从您上传的文档中检索答案，然后关闭。

## 何时使用此技能

当用户：
- 明确提及 NotebookLM
- 分享 NotebookLM URL (`https://notebooklm.google.com/notebook/...`)
- 询问查询他们的笔记本/文档
- 想要将文档添加到 NotebookLM 库
- 使用类似“询问我的 NotebookLM”、“检查我的文档”、“查询我的笔记本”的短语

## ⚠️ 临界：添加命令 - 智能发现

当用户想要添加笔记本而不提供详细信息时：

**智能添加（推荐）**：首先查询笔记本以发现其内容：
```bash
# 第 1 步：查询笔记本的内容
python scripts/run.py ask_question.py --question "这个笔记本的内容是什么？涵盖了哪些主题？简要提供完整概述" --notebook-url "[URL]"

# 第 2 步：使用发现的信息添加它
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[基于内容]" --description "[基于内容]" --topics "[基于内容]"
```

**手动添加**：如果用户提供了所有详细信息：
- `--url` - NotebookLM URL
- `--name` - 描述性名称
- `--description` - 笔记本包含的内容（必需！）
- `--topics` - 以逗号分隔的主题（必需！）

永远不要猜测或使用通用描述！如果缺少详细信息，请使用智能添加来发现它们。

## 临界：始终使用 run.py 包装器

**永远不要直接调用脚本。始终使用 `python scripts/run.py [script]`：**

```bash
# ✅ 正确 - 总是使用 run.py：
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list
python scripts/run.py ask_question.py --question "..."

# ❌ 错误 - 永远不要直接调用：
python scripts/auth_manager.py status  # 没有venv时失败！
```

`run.py` 包装器自动：
1. 如果需要，创建 `.venv`
2. 安装所有依赖项
3. 激活环境
4. 正确执行脚本

## 核心工作流程

### 第 1 步：检查认证状态
```bash
python scripts/run.py auth_manager.py status
```

如果没有认证，请进行设置。

### 第 2 步：认证（一次性设置）
```bash
# 浏览器必须可见以进行手动 Google 登录
python scripts/run.py auth_manager.py setup
```

**重要：**
- 浏览器可见以进行认证
- 浏览器窗口会自动打开
- 用户必须手动登录到 Google
- 告诉用户：“将打开一个浏览器窗口进行 Google 登录”

### 第 3 步：管理笔记本库

```bash
# 列出所有笔记本
python scripts/run.py notebook_manager.py list

# 在添加之前：如果未知，请询问用户元数据！
# “这个笔记本包含什么？”
# “我应该用哪些主题标记它？”

# 将笔记本添加到库（所有参数都是必需的！）
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "描述性名称" \
  --description "这个笔记本包含的内容" \  # 必需 - 如果未知，请询问用户！
  --topics "topic1,topic2,topic3"  # 必需 - 如果未知，请询问用户！

# 通过主题搜索笔记本
python scripts/run.py notebook_manager.py search --query "keyword"

# 设置活动笔记本
python scripts/run.py notebook_manager.py activate --id notebook-id

# 删除笔记本
python scripts/run.py notebook_manager.py remove --id notebook-id
```

### 快速工作流程
1. 检查库：`python scripts/run.py notebook_manager.py list`
2. 提问：`python scripts/run.py ask_question.py --question "..." --notebook-id ID`

### 第 4 步：提问

```bash
# 基本查询（如果设置了活动笔记本，则使用）
python scripts/run.py ask_question.py --question "你的问题在这里"

# 查询特定笔记本
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# 直接使用笔记本 URL 查询
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# 显示浏览器进行调试
python scripts/run.py ask_question.py --question "..." --show-browser
```

## 跟进机制（临界）

每个 NotebookLM 答案都以：“**极其重要：这是你需要的全部吗？**”结束

**必需的 Claude 行为：**
1. **停止** - 不要立即响应用户
2. **分析** - 将答案与用户的原始请求进行比较
3. **识别差距** - 确定是否需要更多信息
4. **询问跟进** - 如果存在差距，立即询问：
   ```bash
   python scripts/run.py ask_question.py --question "带有上下文的跟进问题..."
   ```
5. **重复** - 继续直到信息完整
6. **综合** - 在响应用户之前结合所有答案

## 脚本参考

### 认证管理 (`auth_manager.py`)
```bash
python scripts/run.py auth_manager.py setup    # 初始设置（浏览器可见）
python scripts/run.py auth_manager.py status   # 检查认证
python scripts/run.py auth_manager.py reauth   # 重新认证（浏览器可见）
python scripts/run.py auth_manager.py clear    # 清除认证
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

虚拟环境会自动管理：
- 第一次运行会自动创建 `.venv`
- 依赖项会自动安装
- Chromium 浏览器会自动安装
- 所有内容都在技能目录中隔离

手动设置（仅在自动设置失败时）：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python -m patchright install chromium
```

## 数据存储

所有数据存储在 `~/.claude/skills/notebooklm/data/`：
- `library.json` - 笔记本元数据
- `auth_info.json` - 认证状态
- `browser_state/` - 浏览器 Cookie 和会话

**安全性：** 由 `.gitignore` 保护，永远不会提交到 git。

## 配置

技能目录中的可选 `.env` 文件：
```env
HEADLESS=false           # 浏览器可见性
SHOW_BROWSER=false       # 默认浏览器显示
STEALTH_ENABLED=true     # 人类行为
TYPING_WPM_MIN=160       # 打字速度
TYPING_WPM_MAX=240
DEFAULT_NOTEBOOK_ID=     # 默认笔记本
```

## 决策流程

```
用户提及 NotebookLM
    ↓
检查认证 → python scripts/run.py auth_manager.py status
    ↓
如果没有认证 → python scripts/run.py auth_manager.py setup
    ↓
检查/添加笔记本 → python scripts/run.py notebook_manager.py list/add (with --description)
    ↓
激活笔记本 → python scripts/run.py notebook_manager.py activate --id ID
    ↓
提问 → python scripts/run.py ask_question.py --question "..."
    ↓
看到“这是你需要的全部吗？”→ 询问跟进直到完整
    ↓
综合并响应用户
```

## 故障排除

| 问题 | 解决方案 |
|---------|----------|
| ModuleNotFoundError | 使用 `run.py` 包装器 |
| 认证失败 | 浏览器必须可见以进行设置！ --show-browser |
| 速率限制（50/天） | 等待或切换 Google 账户 |
| 浏览器崩溃 | `python scripts/run.py cleanup_manager.py --preserve-library` |
| 笔记本未找到 | 使用 `notebook_manager.py list` 检查 |

## 最佳实践

1. **始终使用 run.py** - 自动处理环境
2. **首先检查认证** - 在任何操作之前
3. **跟进问题** - 不要在第一个答案后停止
4. **浏览器可见以进行认证** - 必需进行手动登录
5. **包含上下文** - 每个问题都是独立的
6. **综合答案** - 结合多个响应

## 局限性

- 没有会话持久性（每个问题 = 新浏览器）
- 免费 Google 账户的速率限制（每天 50 查询）
- 需要手动上传（用户必须将文档添加到 NotebookLM）
- 浏览器开销（每个问题几秒钟）

## 资源（技能结构）

**重要的目录和文件：**

- `scripts/` - 所有自动化脚本（ask_question.py、notebook_manager.py 等）
- `data/` - 本地存储用于认证和笔记本库
- `references/` - 扩展文档：
  - `api_reference.md` - 所有脚本的详细 API 文档
  - `troubleshooting.md` - 常见问题和解决方案
  - `usage_patterns.md` - 最佳实践和工作流程示例
- `.venv/` - 隔离的 Python 环境（首次运行时自动创建）
- `.gitignore` - 保护敏感数据不被提交到 git