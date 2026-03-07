# 安全审查脚本使用说明

## 📋 概述

`security-audit.ps1` 是一个自动化安全审查工具，用于扫描外部技能中的潜在安全风险，并建议是否需要使用 `danger-` 前缀命名。

**版本**: v1.1  
**更新日期**: 2026-01-25

### 🆕 v1.1 改进

基于实际使用经验优化，显著降低误报率：

1. ✅ **排除XML命名空间** - 不再误判Office OOXML的schemas URLs
2. ✅ **识别安装说明** - 排除Dependencies/Installation章节
3. ✅ **可信来源白名单** - Anthropic/Vercel等官方技能风险评分减半
4. ✅ **精确模式匹配** - 改进sudo/root等关键词检测

**误报率改善**: 从 ~78% 降至预期 <20%

---

## 🚀 快速开始

### 基础用法

```powershell
# 扫描skills_incoming目录
.\scripts\security-audit.ps1 -TargetPath ".\skills_incoming"

# 详细模式（显示所有发现的文件）
.\scripts\security-audit.ps1 -TargetPath ".\skills_incoming" -DetailedOutput

# 生成Markdown报告
.\scripts\security-audit.ps1 -TargetPath ".\skills_incoming" -GenerateReport
```

**注意**: `-DetailedOutput` 替代了 `-Verbose`（避免PowerShell参数冲突）

---

## 🔍 检查项目

脚本会对每个技能进行**6大类安全检查**：

### 1️⃣ 可执行文件检测
**检查内容**: .py, .sh, .ps1, .bat, .exe, .cmd  
**风险级别**:
- 0-2个文件: 🟢 Low
- 3-5个文件: 🟠 Medium  
- 5+个文件: 🟡 High

### 2️⃣ 硬编码凭据扫描
**检查模式**:
- `api_key = "..."`
- `token = "..."`
- `password = "..."`
- `authorization = "..."`

**风险级别**: 🔴 Critical

### 3️⃣ 外部网络调用
**检查内容**:
- Python: `requests.*`, `urllib.*`
- JavaScript: `fetch()`, `axios.*`
- PowerShell: `Invoke-WebRequest`

**风险级别**:
- 1-3个文件: 🟠 Medium
- 3+个文件: 🟡 High

### 4️⃣ 危险系统操作
**检查模式**:
- 删除: `rm -rf`, `Remove-Item -Recurse`
- 格式化: `format`, `mkfs`
- 权限: `chmod 777`
- 执行: `os.system()`, `exec()`

**风险级别**: 🔴 Critical

### 5️⃣ 权限提升请求
**检查内容**: SKILL.md中提及
- `sudo`
- `administrator`
- `root`
- `elevated`

**风险级别**: 🟡 High

### 6️⃣ Python依赖包审查
**可疑包示例**:
- `pycrypto` (加密)
- `paramiko` (SSH)
- `scrapy` (爬虫)

**风险级别**: 🟠 Medium

---

## 📊 风险评分系统

每个检查项会贡献风险分数，累加后计算总风险：

| 风险级别 | 评分范围 | 说明 | 建议 |
|----------|----------|------|------|
| ✅ Safe | 0 | 完全安全 | 正常命名 |
| 🟢 Low | 1-4 | 轻微风险 | 正常命名，注意监控 |
| 🟠 Medium | 5-9 | 中等风险 | 考虑danger前缀 |
| 🟡 High | 10-14 | 高风险 | **建议danger前缀** |
| 🔴 Critical | 15+ | 严重风险 | **必须danger前缀** |

---

## 🏷️ Danger前缀命名规范

### 何时使用danger前缀？

**必须使用** (High/Critical):
- 技能涉及外部API调用
- 技能执行系统级操作
- 技能需要管理员权限
- 技能处理敏感数据

**示例**:
- `gemini-web` → `danger-gemini-web`
- `x-to-markdown` → `danger-x-to-markdown`
- `system-cleaner` → `danger-system-cleaner`

### Danger前缀的作用

1. **视觉警告**: 用户在安装时立即识别风险
2. **明确责任**: 告知用户需自行承担风险
3. **审查提示**: 提醒用户仔细阅读SKILL.md
4. **可视化网站**: 可添加风险徽章🔴

---

## 📝 输出示例

### 控制台输出

```
🔍 Skill Box 安全审查工具
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
扫描目录: .\skills_incoming

发现 3 个技能待审查...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 检查技能: baoyu-gemini-web
路径: E:\...\baoyu-gemini-web

  [1/6] 扫描可执行文件...
    ✅ 未发现可执行文件
  [2/6] 扫描硬编码凭据...
    ✅ 未发现硬编码凭据
  [3/6] 扫描外部网络调用...
    🟡 High: 在 2 个文件中发现网络调用
  [4/6] 扫描危险系统操作...
    ✅ 未发现危险系统操作
  [5/6] 扫描权限提升请求...
    ✅ 未要求权限提升
  [6/6] 扫描Python依赖包...
    ℹ️  无requirements.txt文件

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📊 风险评分: 7 分 | 风险级别: 🟡 High
  ⚠️  命名建议: danger-baoyu-gemini-web
  💡 说明: 建议在插件名称添加'danger-'前缀，告知用户此技能涉及外部调用或系统操作

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 审查总结
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
已扫描技能: 3
总风险评分: 14
需要danger前缀: 2
安全技能: 1

⚠️  需要添加danger前缀的技能:
  • baoyu-gemini-web → danger-baoyu-gemini-web (风险: High, 评分: 7)
  • baoyu-x-to-markdown → danger-baoyu-x-to-markdown (风险: High, 评分: 7)

✅ 审查完成！
```

### Markdown报告 (使用-GenerateReport)

自动生成 `security-audit-report-YYYYMMDD-HHMMSS.md`：

```markdown
# Skill Box 安全审查报告

**生成时间**: 2026-01-25 02:04:00  
**扫描目录**: .\skills_incoming

---

## 📊 总览
- **已扫描技能**: 3
- **总风险评分**: 14
- **需要danger前缀**: 2
- **安全技能**: 1

## ⚠️ 高风险技能

### baoyu-gemini-web
- **建议命名**: `danger-baoyu-gemini-web`
- **风险级别**: High
- **风险评分**: 7
- **发现问题**:
  - [High] 外部网络调用: 在 2 个文件中发现网络调用
...
```

---

## 🔧 集成到添加技能流程

### Phase 0.5: 安全检验

在导入外部技能后、移动文件前执行：

```powershell
# 1. 克隆外部仓库
cd skills_incoming
git clone https://github.com/author/repo.git

# 2. 运行安全审查
cd ..
.\scripts\security-audit.ps1 -TargetPath ".\skills_incoming" -Verbose -GenerateReport

# 3. 审查报告，决定是否使用danger前缀

# 4. 根据建议重命名技能文件夹
cd skills_incoming\repo\skills
Rename-Item "skill-name" "danger-skill-name"

# 5. 继续正常的添加流程
```

---

## 📋 常见问题

### Q1: 是否所有High/Critical技能都必须加danger前缀？

**A**: 建议但不强制。关键判断标准：
- ✅ 涉及外部API → 必须
- ✅ 系统级操作 → 必须  
- ⚠️ 仅有可执行脚本 → 可选（如果是工具类）
- ℹ️ 误报（如github.com访问）→ 不需要

### Q2: danger前缀会影响技能使用吗？

**A**: 不影响Claude调用技能，仅作为：
- 用户安装时的风险提示
- 可视化网站的标识
- 文档中的明确说明

### Q3: 如何处理误报？

**A v1.1 已显著改善**: 

**自动优化**:
- ✅ XML命名空间自动排除（`http://schemas.*`）
- ✅ 安装说明章节自动跳过
- ✅ 可信来源风险评分减半

**仍需人工判断的情况**:
- 文档中的示例代码（非实际执行）
- 用户确认后的操作（有`read -r`提示）

**查看详情**: 使用`-DetailedOutput`查看具体文件

### Q4: 可信来源白名单包括哪些？

**A**: 当前白名单（风险评分自动减半50%）：
- **Anthropic** - Claude官方技能
- **Vercel Labs** - Next.js/Vercel官方
- **ComposioHQ** - 知名技能贡献者
- **Jeremy Longshore** - 商业分析工具作者

脚本会自动从`marketplace.json`读取author信息。

### Q5: 已添加的技能需要复查吗？

**A**: 建议对以下技能复查：
```powershell
# 扫描整个仓库（耗时较长）
.\scripts\security-audit.ps1 -TargetPath "." -GenerateReport
```

---

## 🆕 v1.1 改进详情

### 改进1: 排除XML命名空间

**问题**: Office OOXML脚本中的`http://schemas.openxmlformats.org/...`被误判为网络调用

**解决**: 自动排除包含以下模式的URLs：
```
http://schemas.*
http://www.w3.org/
https://github.com
https://localhost
```

**效果**: document-suite等Anthropic官方技能不再误报

---

### 改进2: 识别安装说明章节

**问题**: 文档中的`sudo apt-get install pandoc`被误判为权限提升

**解决**: 自动排除以下章节的内容：
- `## Dependencies`
- `## Installation`
- `## Prerequisites`
- `## Setup`
- `## Requirements`

**效果**: 安装说明vs实际代码区分清晰

---

### 改进3: 可信来源白名单

**问题**: Anthropic官方的20个Python脚本触发High风险

**解决**: 
- 从`marketplace.json`读取author信息
- 可信来源的可执行文件风险评分减半
- 输出显示`(可信来源: Anthropic)`标签

**效果**: 
- slack-gif-creator: 评分从11降至约6
- document-skills-*: 评分显著下降

---

### 改进4: 精确模式匹配

**优化的检测规则**:
```powershell
# Before
"sudo"

# After  
"sudo\s+(?!apt|yum|brew)"  # 排除包管理器相关
```

```powershell
# Before
"root\s+"

# After
"root\s+(?!cause|directory)"  # 排除其他含义的root
```

---

## 🛡️ 安全最佳实践

1. **新技能必审**: 所有外部技能导入前必须运行此脚本
2. **保存报告**: 使用`-GenerateReport`保存审查记录
3. **定期复查**: 每季度对高风险技能复查一次
4. **用户告知**: 在README中列出需要外部账号授权的技能
5. **文档完善**: 在涉及账号访问的SKILL.md开头添加说明

---

## 📞 技术支持

**脚本位置**: `scripts/security-audit.ps1`  
**问题反馈**: GitHub Issues  
**误报分析**: `security-audit-false-positive-analysis.md`

---

**最后更新**: 2026-01-25  
**脚本版本**: v1.1

