<!--
本文件由智谱 AI 自动翻译生成
原文件: troubleshooting.md
翻译时间: 2025-12-12 16:13:00
翻译模型: glm-4-flash
原文大小: 8,990 字符
-->

# NotebookLM 技能故障排除指南

## 快速修复表格

| 错误 | 解决方案 |
|-------|----------|
| ModuleNotFoundError | 使用 `python scripts/run.py [script].py` |
| 认证失败 | 浏览器必须可见才能设置 |
| 浏览器崩溃 | `python scripts/run.py cleanup_manager.py --preserve-library` |
| 达到速率限制 | 等待 1 小时或切换账户 |
| 找不到笔记本 | `python scripts/run.py notebook_manager.py list` |
| 脚本不工作 | 总是使用 run.py 包装器 |

## 严重：始终使用 run.py

大多数问题都可以通过使用 run.py 包装器来解决：

```bash
# ✅ 正确 - 总是：
python scripts/run.py auth_manager.py status
python scripts/run.py ask_question.py --question "..."

# ❌ 错误 - 从不：
python scripts/auth_manager.py status  # ModuleNotFoundError!
```

## 常见问题和解决方案

### 认证问题

#### 未认证错误
```
错误：未认证。请先运行认证设置。
```

**解决方案：**
```bash
# 检查状态
python scripts/run.py auth_manager.py status

# 设置认证（浏览器必须可见！）
python scripts/run.py auth_manager.py setup
# 用户必须手动登录到 Google

# 如果设置失败，尝试重新认证
python scripts/run.py auth_manager.py reauth
```

#### 认证频繁过期
**解决方案：**
```bash
# 清除旧认证
python scripts/run.py cleanup_manager.py --preserve-library

# 新的认证设置
python scripts/run.py auth_manager.py setup --timeout 15

# 使用持久浏览器配置文件
export PERSIST_AUTH=true
```

#### Google 阻止自动化登录
**解决方案：**
1. 使用专门的 Google 账户进行自动化
2. 如果可用，启用“较不安全的应用程序访问”
3. 总是使用可见的浏览器：
```bash
python scripts/run.py auth_manager.py setup
# 浏览器必须可见 - 用户手动登录
# 没有存在无头参数 - 使用 --show-browser 进行调试
```

### 浏览器问题

#### 浏览器崩溃或挂起
```
TimeoutError: Waiting for selector failed
```

**解决方案：**
```bash
# 杀死挂起的进程
pkill -f chromium
pkill -f chrome

# 清理浏览器状态
python scripts/run.py cleanup_manager.py --confirm --preserve-library

# 重新认证
python scripts/run.py auth_manager.py reauth
```

#### 浏览器未找到错误
**解决方案：**
```bash
# 通过 run.py 安装 Chromium（自动）
python scripts/run.py auth_manager.py status
# run.py 将自动安装 Chromium

# 或手动安装（如果需要）
cd ~/.claude/skills/notebooklm
source .venv/bin/activate
python -m patchright install chromium
```

### 速率限制

#### 达到速率限制（每天 50 查询）
**解决方案：**

**选项 1：等待**
```bash
# 检查何时重置限制（通常是太平洋标准时间午夜）
date -d "明天 00:00 PST"
```

**选项 2：切换账户**
```bash
# 清除当前认证
python scripts/run.py auth_manager.py clear

# 使用不同账户登录
python scripts/run.py auth_manager.py setup
```

**选项 3：轮换账户**
```python
# 使用多个账户
accounts = ["account1", "account2"]
for account in accounts:
    # 在速率限制时切换账户
    subprocess.run(["python", "scripts/run.py", "auth_manager.py", "reauth"])
```

### 笔记本访问问题

#### 找不到笔记本
**解决方案：**
```bash
# 列出所有笔记本
python scripts/run.py notebook_manager.py list

# 搜索笔记本
python scripts/run.py notebook_manager.py search --query "keyword"

# 如果缺失，添加笔记本
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/..." \
  --name "Name" \
  --topics "topics"
```

#### 访问笔记本被拒绝
**解决方案：**
1. 检查笔记本是否仍然公开共享
2. 使用更新后的 URL 重新添加笔记本
3. 验证是否使用了正确的 Google 账户

#### 正在使用错误的笔记本
**解决方案：**
```bash
# 检查活动笔记本
python scripts/run.py notebook_manager.py list | grep "active"

# 激活正确的笔记本
python scripts/run.py notebook_manager.py activate --id correct-id
```

### 虚拟环境问题

#### ModuleNotFoundError
```
ModuleNotFoundError: No module named 'patchright'
```

**解决方案：**
```bash
# 总是使用 run.py - 它会自动处理 venv！
python scripts/run.py [any_script].py

# run.py 将：
# 1. 如果缺失，创建 .venv
# 2. 安装依赖项
# 3. 运行脚本
```

#### 错误的 Python 版本
**解决方案：**
```bash
# 检查 Python 版本（需要 3.8+）
python --version

# 如果版本错误，指定正确的 Python
python3.8 scripts/run.py auth_manager.py status
```

### 网络问题

#### 连接超时
**解决方案：**
```bash
# 增加超时
export TIMEOUT_SECONDS=60

# 检查连接性
ping notebooklm.google.com

# 如果需要，使用代理
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

### 数据问题

#### 笔记本库损坏
```
列出笔记本时 JSON 解码错误
```

**解决方案：**
```bash
# 备份当前库
cp ~/.claude/skills/notebooklm/data/library.json library.backup.json

# 重置库
rm ~/.claude/skills/notebooklm/data/library.json

# 重新添加笔记本
python scripts/run.py notebook_manager.py add --url ... --name ...
```

#### 磁盘空间不足
**解决方案：**
```bash
# 检查磁盘使用情况
df -h ~/.claude/skills/notebooklm/data/

# 清理
python scripts/run.py cleanup_manager.py --confirm --preserve-library
```

## 调试技巧

### 启用详细日志记录
```bash
export DEBUG=true
export LOG_LEVEL=DEBUG
python scripts/run.py ask_question.py --question "Test" --show-browser
```

### 测试单个组件
```bash
# 测试认证
python scripts/run.py auth_manager.py status

# 测试笔记本访问
python scripts/run.py notebook_manager.py list

# 测试浏览器启动
python scripts/run.py ask_question.py --question "test" --show-browser
```

### 在错误时保存屏幕截图
将以下代码添加到脚本中进行调试：
```python
try:
    # 你的代码
except Exception as e:
    page.screenshot(path=f"error_{timestamp}.png")
    raise e
```

## 恢复程序

### 完全重置
```bash
#!/bin/bash
# 杀死进程
pkill -f chromium

# 如果存在，备份库
if [ -f ~/.claude/skills/notebooklm/data/library.json ]; then
    cp ~/.claude/skills/notebooklm/data/library.json ~/library.backup.json
fi

# 清理一切
cd ~/.claude/skills/notebooklm
python scripts/run.py cleanup_manager.py --confirm --force

# 删除 venv
rm -rf .venv

# 重新安装（run.py 将处理此操作）
python scripts/run.py auth_manager.py setup

# 如果存在备份，恢复库
if [ -f ~/library.backup.json ]; then
    mkdir -p ~/.claude/skills/notebooklm/data/
    cp ~/library.backup.json ~/.claude/skills/notebooklm/data/library.json
fi
```

### 部分恢复（保留数据）
```bash
# 保留认证和库，修复执行
cd ~/.claude/skills/notebooklm
rm -rf .venv

# run.py 将自动创建 venv
python scripts/run.py auth_manager.py status
```

## 错误信息参考

### 认证错误
| 错误 | 原因 | 解决方案 |
|-------|-------|----------|
| 未认证 | 无有效认证 | `run.py auth_manager.py setup` |
| 认证过期 | 会话过旧 | `run.py auth_manager.py reauth` |
| 无效凭证 | 错误账户 | 检查 Google 账户 |
| 2FA 需要 | 安全挑战 | 在可见浏览器中完成 |

### 浏览器错误
| 错误 | 原因 | 解决方案 |
|-------|-------|----------|
| 浏览器未找到 | Chromium 缺失 | 使用 run.py（自动安装） |
| 连接被拒绝 | 浏览器崩溃 | 杀死进程，重启 |
| 等待超时 | 页面缓慢 | 增加超时 |
| 上下文已关闭 | 浏览器终止 | 检查日志中的崩溃 |

### 笔记本错误
| 错误 | 原因 | 解决方案 |
|-------|-------|----------|
| 找不到笔记本 | 无效 ID | `run.py notebook_manager.py list` |
| 访问被拒绝 | 未共享 | 在 NotebookLM 中重新共享 |
| 无效 URL | 格式错误 | 使用完整的 NotebookLM URL |
| 无活动笔记本 | 未选择 | `run.py notebook_manager.py activate` |

## 预防提示

1. **始终使用 run.py** - 防止 90% 的问题
2. **定期维护** - 每周清理浏览器状态
3. **监控查询** - 跟踪每日计数以避免限制
4. **备份库** - 定期导出笔记本列表
5. **使用专用账户** - 为自动化使用单独的 Google 账户

## 获取帮助

### 要收集的诊断信息
```bash
# 系统信息
python --version
cd ~/.claude/skills/notebooklm
ls -la

# 技能状态
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list | head -5

# 检查数据目录
ls -la ~/.claude/skills/notebooklm/data/
```

### 常见问题

**Q：为什么在 Claude 网页 UI 中不起作用？**
A：网页 UI 没有网络访问。使用本地 Claude Code。

**Q：我可以使用多个 Google 账户吗？**
A：是的，使用 `run.py auth_manager.py reauth` 来切换。

**Q：如何增加速率限制？**
A：使用多个账户或升级到 Google Workspace。

**Q：这对我的 Google 账户安全吗？**
A：使用专用账户进行自动化。仅访问 NotebookLM。