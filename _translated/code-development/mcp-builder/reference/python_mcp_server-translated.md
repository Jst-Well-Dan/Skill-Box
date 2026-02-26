<!--
本文件由智谱 AI 自动翻译生成
原文件: python_mcp_server.md
翻译时间: 2025-12-12 16:11:25
翻译模型: glm-4-flash
原文大小: 26,182 字符
-->

---
# Python MCP 服务器实现指南

## 概述

本文档提供了使用 MCP Python SDK 实现 MCP 服务器时的 Python 特定最佳实践和示例。它涵盖了服务器设置、工具注册模式、使用 Pydantic 的输入验证、错误处理以及完整的示例。

---

## 快速参考

### 关键导入
```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List, Dict, Any
from enum import Enum
import httpx
```

### 服务器初始化
```python
mcp = FastMCP("service_mcp")
```

### 工具注册模式
```python
@mcp.tool(name="tool_name", annotations={...})
async def tool_function(params: InputModel) -> str:
    # 实现部分
    pass
```

---

## MCP Python SDK 和 FastMCP

官方 MCP Python SDK 提供了 FastMCP，这是一个用于构建 MCP 服务器的高级框架。它提供：
- 从函数签名和文档字符串自动生成描述和 inputSchema
- Pydantic 模型集成用于输入验证
- 基于装饰器的工具注册 `@mcp.tool`

**对于完整的 SDK 文档，请使用 WebFetch 加载：**
`https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`

## 服务器命名约定

Python MCP 服务器必须遵循以下命名模式：
- **格式**：`{service}_mcp`（小写，下划线分隔）
- **示例**：`github_mcp`、`jira_mcp`、`stripe_mcp`

名称应该是：
- 通用的（不特定于特定功能）
- 描述性的，描述要集成的服务/API
- 从任务描述中容易推断出来
- 不包含版本号或日期

## 工具实现

### 工具命名

使用 snake_case 为工具命名（例如，"search_users"、"create_project"、"get_channel_info"），名称清晰、以动作为导向。

**避免命名冲突**：包含服务上下文以防止重叠：
- 使用 "slack_send_message" 而不是 "send_message"
- 使用 "github_create_issue" 而不是 "create_issue"
- 使用 "asana_list_tasks" 而不是 "list_tasks"

### 使用 FastMCP 的工具结构

工具使用 `@mcp.tool` 装饰器和 Pydantic 模型进行输入验证来定义：

```python
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("example_mcp")

# 定义 Pydantic 模型进行输入验证
class ServiceToolInput(BaseModel):
    '''服务工具操作的输入模型。'''

    model_config = ConfigDict(
        str_strip_whitespace=True,  # 自动从字符串中删除空白字符
        validate_assignment=True,    # 验证赋值
        extra='forbid'              # 禁止额外字段
    )

    param1: str = Field(..., description="第一个参数描述（例如，'user123'，'project-abc'）", min_length=1, max_length=100)
    param2: Optional[int] = Field(default=None, description="具有约束条件的可选整数参数", ge=0, le=1000)
    tags: Optional[List[str]] = Field(default_factory=list, description="要应用的标签列表", max_items=10)

@mcp.tool(
    name="service_tool_name",
    annotations={
        "title": "人类可读的工具标题",
        "readOnlyHint": True,     # 工具不修改环境
        "destructiveHint": False,  # 工具不执行破坏性操作
        "idempotentHint": True,    # 重复调用没有额外效果
        "openWorldHint": False     # 工具不与外部实体交互
    }
)
async def service_tool_name(params: ServiceToolInput) -> str:
    '''工具描述自动成为 'description' 字段。

    此工具在服务上执行特定操作。在处理之前，使用 ServiceToolInput Pydantic 模型验证所有输入。

    Args:
        params (ServiceToolInput): 验证后的输入参数，包含：
            - param1 (str)：第一个参数描述
            - param2 (Optional[int])：具有默认值的可选参数
            - tags (Optional[List[str]])：标签列表

    Returns:
        str：包含操作结果的 JSON 格式响应
    '''
    # 实现部分
    pass
```

## Pydantic v2 关键功能

- 使用 `model_config` 而不是嵌套 `Config` 类
- 使用 `field_validator` 而不是已弃用的 `validator`
- 使用 `model_dump()` 而不是已弃用的 `dict()`
- 验证器需要 `@classmethod` 装饰器
- 验证器方法需要类型提示

```python
from pydantic import BaseModel, Field, field_validator, ConfigDict

class CreateUserInput(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True
    )

    name: str = Field(..., description="用户的全名", min_length=1, max_length=100)
    email: str = Field(..., description="用户的电子邮件地址", pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: int = Field(..., description="用户的年龄", ge=0, le=150)

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("电子邮件不能为空")
        return v.lower()
```

## 响应格式选项

支持多种输出格式以提高灵活性：

```python
from enum import Enum

class ResponseFormat(str, Enum):
    '''工具响应的输出格式。'''

    MARKDOWN = "markdown"
    JSON = "json"

class UserSearchInput(BaseModel):
    query: str = Field(..., description="搜索查询")
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="输出格式：'markdown' 用于人类可读或 'json' 用于机器可读"
    )
```

**Markdown 格式**：
- 使用标题、列表和格式化以提高清晰度
- 将时间戳转换为人类可读格式（例如，"2024-01-15 10:30:00 UTC" 而不是纪元）
- 显示带有 ID 的显示名称（例如，"@john.doe (U123456)"）
- 省略冗余元数据（例如，只显示一个配置文件图像 URL，而不是所有大小）
- 合理地组织相关信息

**JSON 格式**：
- 返回适合程序处理的结构化完整数据
- 包含所有可用字段和元数据
- 使用一致的字段名称和类型

## 分页实现

对于列出资源的工具：

```python
class ListInput(BaseModel):
    limit: Optional[int] = Field(default=20, description="返回的最大结果数", ge=1, le=100)
    offset: Optional[int] = Field(default=0, description="跳过的结果数以进行分页", ge=0)

async def list_items(params: ListInput) -> str:
    # 使用分页进行 API 请求
    data = await api_request(limit=params.limit, offset=params.offset)

    # 返回分页信息
    response = {
        "total": data["total"],
        "count": len(data["items"]),
        "offset": params.offset,
        "items": data["items"],
        "has_more": data["total"] > params.offset + len(data["items"]),
        "next_offset": params.offset + len(data["items"]) if data["total"] > params.offset + len(data["items"]) else None
    }
    return json.dumps(response, indent=2)
```

## 字符限制和截断

添加 CHARACTER_LIMIT 常量以防止响应过大：

```python
# 模块级别
CHARACTER_LIMIT = 25000  # 最大响应字符大小

async def search_tool(params: SearchInput) -> str:
    result = generate_response(data)

    # 检查字符限制并在需要时截断
    if len(result) > CHARACTER_LIMIT:
        # 截断数据并添加通知
        truncated_data = data[:max(1, len(data) // 2)]
        response["data"] = truncated_data
        response["truncated"] = True
        response["truncation_message"] = (
            f"响应从 {len(data)} 截断到 {len(truncated_data)} 项。 "
            f"使用 'offset' 参数或添加过滤器以查看更多结果。"
        )
        result = json.dumps(response, indent=2)

    return result
```

## 错误处理

提供清晰、可操作的错误消息：

```python
def _handle_api_error(e: Exception) -> str:
    '''所有工具跨工具的一致错误格式。'''

    if isinstance(e, httpx.HTTPStatusError):
        if e.response.status_code == 404:
            return "错误：资源未找到。请检查 ID 是否正确。"
        elif e.response.status_code == 403:
            return "错误：拒绝访问。您没有访问此资源的权限。"
        elif e.response.status_code == 429:
            return "错误：超出配额。请稍后再进行请求。"
        return f"错误：API 请求失败，状态码 {e.response.status_code}"
    elif isinstance(e, httpx.TimeoutException):
        return "错误：请求超时。请重试。"
    return f"错误：发生了意外的错误：{type(e).__name__}"
```

## 共享实用工具

将常用功能提取到可重用的函数中：

```python
# 共享 API 请求函数
async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
    '''所有 API 调用的可重用函数。'''

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method,
            f"{API_BASE_URL}/{endpoint}",
            timeout=30.0,
            **kwargs
        )
        response.raise_for_status()
        return response.json()
```

## Async/Await 最佳实践

始终使用 async/await 进行网络请求和 I/O 操作：

```python
# 良好：异步网络请求
async def fetch_data(resource_id: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/resource/{resource_id