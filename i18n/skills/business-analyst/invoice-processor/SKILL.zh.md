---
name: invoice-processor
description: 自动处理 PDFs/images 中的发票到 Excel 电子表格，使用 AI 视觉识别技术。当用户提及 "发票", "invoice", "处理发票", "识别发票", "提取发票", 或需要将发票文件转换为 Excel 格式时，使用此技能。
---

# 发票处理器

使用 AI 视觉模型提取结构化信息并生成格式化 Excel 报告的发票文件处理的全自动工作流程。

## 何时使用

**当用户提及以下内容时自动触发：**
- "处理发票" / "识别发票" / "提取发票信息" / "发票转Excel"
- 处理发票文件（PDF, JPG, PNG）
- 将发票转换为 Excel 格式

## 执行环境说明

**⚠️ 关键：非 ASCII 目录名的路径处理**

当项目目录包含中文或其他非 ASCII 字符（例如，“发票助手agent”）时，您必须从项目根目录使用完整相对路径：

```bash
# ❌ 错误 - 将因编码错误而失败
python scripts/check_env.py

# ✅ 正确 - 使用从 .claude/skills/ 的完整路径
python .claude/skills/invoice-processor/scripts/check_env.py
```

**跨平台兼容性：**
- 使用 Unix 风格的命令（Git Bash, Linux, macOS）
- ❌ `dir /b` → ✅ `ls`

## 设置

在 `invoice-processor` 目录中创建一个 `.env` 文件：

```bash
# 从模板复制
cp .env.example .env

# 使用您的 API 密钥编辑
# .env 内容：
GLM_API_KEY=your_actual_api_key_here
```

从：https://open.bigmodel.cn/ 获取您的 API 密钥。

## 工作流程

### 步骤 1：环境检查（推荐）

```bash
python .claude/skills/invoice-processor/scripts/check_env.py
```

验证：GLM_API_KEY 已设置，已安装所需软件包（aiohttp, PyMuPDF, openpyxl）

### 步骤 2：识别发票

```bash
# 默认：处理 'invoices' 目录 → 'invoice_results.json'
python .claude/skills/invoice-processor/scripts/invoice_ocr.py

# 自定义路径
python .claude/skills/invoice-processor/scripts/invoice_ocr.py -i <input_path> -o <output.json>
```

**作用：**
- 扫描发票文件（JPG, JPEG, PNG, PDF）
- 将 PDF 转换为图像（200 DPI）
- 同时处理最多 5 个文件
- 提取 9 个字段：类型、编号、日期、买方/卖方名称、金额（不含/含税）、税、项目
- 保存到 JSON，包含成功/错误状态

**参数：**
- `-i, --input`: 输入路径（默认：`invoices`）
- `-o, --output`: 输出 JSON（默认：`invoice_results.json`）

**先决条件：**
- `.env` 文件中的 `GLM_API_KEY`（见设置部分）
- `pip install aiohttp PyMuPDF`

### 步骤 3：生成 Excel 报告

```bash
# 默认：'invoice_results.json' → 'invoice_results.xlsx'
python .claude/skills/invoice-processor/scripts/convert_to_excel.py

# 自定义路径
python .claude/skills/invoice-processor/scripts/convert_to_excel.py -i <input.json> -o <output.xlsx>
```

**作用：**
- 读取步骤 2 的 JSON
- 创建具有 12 列的格式化 Excel
- 成功转换后自动删除输入 JSON

**参数：**
- `-i, --input`: 输入 JSON（默认：`invoice_results.json`）
- `-o, --output`: 输出 Excel（默认：`invoice_results.xlsx`）

**先决条件：**
- `pip install openpyxl`

## 使用示例

### 基本使用（非 ASCII 目录名）

```bash
# 3 步完整工作流程
python .claude/skills/invoice-processor/scripts/check_env.py
python .claude/skills/invoice-processor/scripts/invoice_ocr.py -i invoices -o invoice_results.json
python .claude/skills/invoice-processor/scripts/convert_to_excel.py -i invoice_results.json -o invoice_results.xlsx
```

### 自定义路径

```bash
python .claude/skills/invoice-processor/scripts/invoice_ocr.py -i invoices_2024 -o results_2024.json
python .claude/skills/invoice-processor/scripts/convert_to_excel.py -i results_2024.json -o report_2024.xlsx
```

## 故障排除

### 脚本未找到 / 编码错误
**错误：** `can't open file '...\��Ʊ����agent\scripts\...'`
**原因：** 短路径（`scripts/`）在非 ASCII 目录中失败
**解决方案：** 使用完整路径：`.claude/skills/invoice-processor/scripts/...`

### 命令未找到
**错误：** `dir: cannot access '/b'`
**原因：** Windows CMD 命令在 Unix shell 中
**解决方案：** 使用 `ls` 代替 `dir`

### API 密钥未设置
**错误：** `错误: 请在 .env 文件中设置 GLM_API_KEY`
**解决方案：** 在 `invoice-processor` 目录中创建 `.env` 文件，内容为 `GLM_API_KEY=your_key`

### PDF 支持已禁用
**警告：** `未安装 PyMuPDF，PDF 支持已禁用`
**解决方案：** `pip install PyMuPDF`

## 注意事项

- GLM API 限制：5 个并发请求，每个请求 60 秒超时
- 图像限制：最大 5MB，最大 6000x6000 像素
- PDF 自动转换为图像（临时文件清理）
- **路径最佳实践：** 当项目目录包含非 ASCII 字符时，始终使用完整相对路径（`.claude/skills/invoice-processor/scripts/`）

--- 

有关详细设计原则、自定义选项和架构指南，请参阅 [README.md](README.md)。