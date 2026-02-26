<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:10:27
翻译模型: glm-4-flash
原文大小: 2,495 字符
-->

---

# 发布文件

此目录包含用于轻松安装 PICT 测试设计器技能的预打包发布文件。

## 最小安装包

**文件：** `pict-test-designer-minimal.zip` (9.3 KB)

此 ZIP 文件仅包含技能正常运行所需的基本文件：

- `SKILL.md` - 核心技能定义
- `LICENSE` - MIT 许可证
- `references/pict_syntax.md` - PICT 语法参考
- `references/examples.md` - 常见模式和示例
- `README-INSTALL.txt` - 安装说明

### 快速安装

**个人使用（所有项目）：**
```bash
# 下载 ZIP 文件
wget https://github.com/omkamal/pypict-claude-skill/raw/main/releases/pict-test-designer-minimal.zip

# 解压并安装
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal ~/.claude/skills/pict-test-designer

# 重新启动 Claude Code
```

**项目特定使用：**
```bash
# 下载 ZIP 文件
wget https://github.com/omkamal/pypict-claude-skill/raw/main/releases/pict-test-designer-minimal.zip

# 解压并安装
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal .claude/skills/pict-test-designer

# 重新启动 Claude Code
```

**Windows：**
```powershell
# 手动下载或使用：
Invoke-WebRequest -Uri "https://github.com/omkamal/pypict-claude-skill/raw/main/releases/pict-test-designer-minimal.zip" -OutFile "pict-test-designer-minimal.zip"

# 解压到：
# 个人：%USERPROFILE%\.claude\skills\pict-test-designer\
# 项目：  .claude\skills\pict-test-designer\
```

## 不包含的内容

最小包不包括：

- 完整示例（ATM 测试计划）
- 辅助脚本（pict_helper.py）
- 扩展文档（README.md、QUICKSTART.md 等）

要获取包含示例和文档的完整包，请克隆完整仓库：
```bash
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer
```

## 验证

安装后，重新启动 Claude Code 并通过以下方式验证：
```
您是否有访问 pict-test-designer 技能的权限？
```

或者立即开始使用它：
```
为具有用户名、密码和“记住我”复选框的登录功能设计测试用例。
```

## 版本信息

- **当前版本：** 1.0.0
- **最后更新：** 2025 年 10 月 19 日
- **大小：** 9.3 KB（压缩）
- **文件：** 5 个文件

## 支持

有关问题、疑问或贡献：
- GitHub 问题：https://github.com/omkamal/pypict-claude-skill/issues
- 完整文档：https://github.com/omkamal/pypict-claude-skill