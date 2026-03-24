---
name: weather
description: "通过 wttr.in 或 Open-Meteo 获取当前天气和预报。适用于：用户询问天气、温度或任何地点的预报。不适用于：历史天气数据、极端天气警报或详细的气象分析。无需 API 密钥。"
homepage: https://wttr.in/:help
metadata: { "openclaw": { "emoji": "🌤️", "requires": { "bins": ["curl"] } } }
---

# 天气查询技能

获取当前天气状况和预报。

## 何时使用

✅ **在以下情况下使用此技能：**

- “天气怎么样？”
- “今天/明天会下雨吗？”
- “[城市] 的温度是多少？”
- “本周天气预报”
- 旅行计划时的天气检查

## 何时不要使用

❌ **在以下情况下不要使用此技能：**

- 历史天气数据 → 使用天气档案/API
- 气候分析或趋势 → 使用专业数据源
- 超本地微气候数据 → 使用本地传感器
- 极端天气警报 → 检查官方气象源
- 航空/航海天气 → 使用专业服务（METAR 等）

## 地点

在天气查询中始终包含城市、地区或机场代码。

## 命令示例

### 当前天气

```bash
# 单行摘要
curl "wttr.in/Beijing?format=3"

# 详细的当前状况
curl "wttr.in/Shanghai?0"

# 特定城市
curl "wttr.in/New+York?format=3"
```

### 天气预报

```bash
# 3 天预报
curl "wttr.in/Guangzhou"

# 周预报
curl "wttr.in/Shenzhen?format=v2"

# 特定日期（0=今天, 1=明天, 2=后天）
curl "wttr.in/Beijing?1"
```

### 格式化选项

```bash
# 单行格式
curl "wttr.in/Beijing?format=%l:+%c+%t+%w"

# JSON 输出
curl "wttr.in/Beijing?format=j1"

# PNG 图像
curl "wttr.in/Beijing.png"
```

### 格式代码

- `%c` — 天气状况表情符号
- `%t` — 温度
- `%f` — “体感温度”
- `%w` — 风力
- `%h` — 湿度
- `%p` — 降水量
- `%l` — 地点

## 快速响应示例

**“天气如何？”**

```bash
curl -s "wttr.in/Beijing?format=%l:+%c+%t+(体感+%f),+%w+风,+%h+湿度"
```

**“会下雨吗？”**

```bash
curl -s "wttr.in/Beijing?format=%l:+%c+%p"
```

**“周末预报”**

```bash
curl "wttr.in/Beijing?format=v2"
```

## 注意事项

- 无需 API 密钥（使用 wttr.in）。
- 有速率限制；请勿高频请求。
- 适用于全球大多数城市。
- 支持机场代码：`curl wttr.in/PEK`
