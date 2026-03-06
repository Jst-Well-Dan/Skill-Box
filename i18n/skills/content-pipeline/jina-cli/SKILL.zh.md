---
name: jina-cli
description: 使用 Jina AI Reader API 读取网页内容并搜索网络。适用于从 URL 提取内容、阅读社交媒体帖子 (X/Twitter) 或搜索当前信息的网络搜索。
---

# jina - 网页内容读取与搜索

用于读取网页内容并执行 AI 驱动的网络搜索的 CLI 工具。

## 快速开始

**macOS/Linux**:
```bash
curl -fsSL https://raw.githubusercontent.com/geekjourneyx/jina-cli/main/scripts/install.sh | bash
```

**Windows (需要安装 Go)**:
```powershell
# 1. 通过 Go 安装
go install github.com/geekjourneyx/jina-cli/cli@latest

# 2. 重命名并添加到 PATH (一次性设置)
cd "$HOME/go/bin"; mv cli.exe jina.exe
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$HOME\go\bin", "User")
```

**基本用法**:
```bash
# 读取 URL
jina read --url "https://example.com"

# 搜索网络
jina search --query "golang latest news"
```

## 命令

| 命令 | 用途 |
|---------|---------|
| `read` | 提取并转换 URL 内容为 LLM 友好格式 |
| `search` | 执行 AI 驱动的结果处理和网络搜索 |
| `config` | 管理设置 (set/get/list/path) |

## Read 命令

从任何 URL 提取内容：

```bash
# 基本读取
jina read --url "https://example.com"

# 带有图像描述的读取 (需要 API Key)
jina read -u "https://x.com/user/status/123" --with-alt

# 从文件批量处理
jina read --file urls.txt

# 输出为 Markdown
jina read -u "https://example.com" --output markdown

# 保存到文件
jina read -u "https://example.com" --output-file result.md
```

### 响应格式

API 可以通过 `--format` 返回不同格式的内容：
- `markdown` - 默认，LLM 友好的 Markdown
- `html` - 原始 HTML
- `text` - 纯文本
- `screenshot` - 截图的 URL

### 高级选项

```bash
# 绕过缓存
jina read -u "https://example.com" --no-cache

# 使用代理
jina read -u "https://example.com" --proxy "http://proxy.com:8080"

# CSS 选择器提取
jina read -u "https://example.com" --target-selector "article.main"

# 等待元素加载
jina read -u "https://example.com" --wait-for-selector "#content"

# 转发 Cookie
jina read -u "https://example.com" --cookie "session=abc123"

# 针对带有哈希路由的 SPA 使用 POST 方法
jina read -u "https://example.com/#/route" --post
```

## Search 命令

搜索网络并自动获取前几个结果的内容：

```bash
# 基本搜索
jina search --query "golang latest news"

# 限制在特定网站
jina search -q "AI developments" --site techcrunch.com --site theverge.com

# 限制结果数量
jina search -q "climate change" --limit 10

# 输出格式
jina search -q "news" --output markdown
```

### 站点过滤

使用多个 `--site` 标志将搜索限制在特定域名：
```bash
jina search -q "startup funding" --site techcrunch.com --site theverge.com --site wired.com
```

## 配置

配置文件：`~/.jina-reader/config.yaml`

**优先级**: 命令行参数 > 环境变量 > 配置文件 > 默认值

**环境变量**:
- `JINA_API_BASE_URL` - Read API URL (默认: `https://r.jina.ai/`)
- `JINA_SEARCH_API_URL` - Search API URL (默认: `https://s.jina.ai/`)
- `JINA_TIMEOUT` - 请求超时时间，单位秒 (默认: `30`)
- `JINA_WITH_GENERATED_ALT` - 启用图像描述 (默认: `false`)
- `JINA_OUTPUT_FORMAT` - 输出格式: json/markdown (默认: `json`)
- `JINA_PROXY_URL` - 代理服务器 URL

**配置命令**:
```bash
# 设置 API Key (使用 --with-alt 时需要)
jina config set key your_jina_api_key

# 设置配置
jina config set timeout 60
jina config set with-generated-alt true

# 查看配置
jina config list
jina config get timeout
jina config path
```

## 故障排除

### 401 需要身份验证
如果您在使用 `--with-alt` 时收到 `401 Unauthorized` 错误，请确保已配置有效的 API 密钥：
`jina config set key YOUR_API_KEY`

### 找不到命令 (Windows)
如果 `go install` 后无法识别 `jina`，请确保 `$HOME\go\bin` 在系统 PATH 中，并且二进制文件已命名为 `jina.exe`（默认为 `cli.exe`）。

## 输出格式

**JSON 格式**（默认，机器可读）：
```json
{
  "success": true,
  "data": {
    "url": "https://example.com",
    "content": "# Extracted Content\n\n...",
    "title": "Page Title"
  }
}
```

**Markdown 格式**（人类可读）：
```bash
jina read -u "https://example.com" --output markdown
```

## 常见用例

### 阅读社交媒体帖子

```bash
# X (Twitter) 帖子
jina read -u "https://x.com/elonmusk/status/123456" --with-alt

# --with-alt 标志为嵌入图像启用 VLM 图像描述
```

### 阅读文章/博客

```bash
# 标准文章
jina read -u "https://blog.example.com/article"

# 使用特定格式
jina read -u "https://example.com" --format text --output markdown
```

### 研究工作流

```bash
# 1. 搜索话题
jina search -q "quantum computing 2025" --limit 10

# 2. 阅读特定结果
jina read --file search_results.txt
```

### 批量处理

创建一个每行一个 URL 的文件：
```bash
cat > urls.txt << EOF
https://example.com/page1
https://example.com/page2
https://x.com/user/status/123
EOF

jina read --file urls.txt --output markdown
```

## 项目结构

```
cli/
├── main.go              # 根命令
├── read.go              # read 命令
├── search.go            # search 命令
├── config.go            # config 命令
└── pkg/
    ├── api/client.go    # Jina API HTTP 客户端
    ├── config/          # 配置文件管理
    └── output/          # JSON/Markdown 格式化程序
```

## 实现说明

- 需要 **Go 1.24+**
- 除了 Cobra 外 **零依赖**
- **单二进制文件** 分发
- 配置存储为简单的 `key=value` 格式（不依赖 YAML 库）

有关 API 详细信息：请参阅 `cli/pkg/api/client.go`
