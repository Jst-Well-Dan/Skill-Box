<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:12:04
翻译模型: glm-4-flash
原文大小: 7,306 字符
-->

---

<div align="center">

[![加入 AI 社区](https://img.shields.io/badge/🚀_Join-AI_Community_(FREE)-4F46E5?style=for-the-badge)](https://www.skool.com/ai-for-your-business)
[![GitHub 个人资料](https://img.shields.io/badge/GitHub-@coffeefuelbump-181717?style=for-the-badge&logo=github)](https://github.com/coffeefuelbump)

[![Link Tree](https://img.shields.io/badge/Linktree-Everything-green?style=for-the-badge&logo=linktree&logoColor=white)](https://linktr.ee/corbin_brown)
[![YouTube 会员](https://img.shields.io/badge/YouTube-Become%20a%20Builder-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCJFMlSxcvlZg5yZUYJT0Pug/join)

</div>

---

# 📊 CSV 数据汇总器 - Claude 技能

一个强大的 Claude 技能，可以自动分析 CSV 文件并生成带有可视化的全面洞察。上传任何 CSV 文件，即可获得即时、智能的分析，无需询问您想要什么！

<div align="center">

[![版本](https://img.shields.io/badge/version-2.1.0-blue.svg)](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![许可证](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

</div>

## 🚀 功能

- **🤖 智能且自适应** - 自动检测数据类型（销售、客户、财务、调查等）并应用相关分析
- **📈 全面分析** - 生成统计数据、相关性、分布和趋势
- **🎨 自动可视化** - 根据您的数据创建多个图表：
  - 基于日期的数据的时间序列图
  - 数字关系的相关性热图
  - 分布直方图
  - 类别分解
- **⚡ 主动式** - 无需提问！只需上传 CSV 即可立即获得完整分析
- **🔍 数据质量检查** - 自动检测并报告缺失值
- **📊 多行业支持** - 适应电子商务、医疗保健、金融、运营、调查等更多行业

## 📥 快速下载

<div align="center">

### 2 步开始

**1️⃣ 下载技能**  
[![下载技能](https://img.shields.io/badge/Download-CSV%20Data%20Summarizer%20Skill-blue?style=for-the-badge&logo=download)](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill/raw/main/csv-data-summarizer.zip)

**2️⃣ 尝试演示数据**  
[![下载演示 CSV](https://img.shields.io/badge/Download-Sample%20P%26L%20Financial%20Data-green?style=for-the-badge&logo=data)](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill/raw/main/examples/showcase_financial_pl_data.csv)

</div>

---

## 📦 包含内容

```
csv-data-summarizer-claude-skill/
├── SKILL.md              # Claude 技能定义
├── analyze.py            # 全面分析引擎
├── requirements.txt      # Python 依赖项
├── examples/
│   └── showcase_financial_pl_data.csv  # 演示 P&L 财务数据集（15 个月，25 个指标）
└── resources/
    ├── sample.csv        # 示例数据集
    └── README.md         # 使用文档
```

## 🎯 工作原理

1. **上传**任何 CSV 文件到 Claude.ai
2. **技能自动激活**当检测到 CSV 时
3. **分析立即运行** - 检查数据结构并适应
4. **交付结果** - 带有多个可视化的完整分析

无需提示。无需选择选项。只需即时、全面的洞察！

## 📥 安装

### 对于 Claude.ai 用户

1. 下载最新版本：[`csv-data-summarizer.zip`](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill/releases)
2. 前往 [Claude.ai](https://claude.ai) → 设置 → 能力 → 技能
3. 上传 zip 文件
4. 启用技能
5. 完成！上传任何 CSV 并观看它工作 ✨

### 对于开发者

```bash
git clone git@github.com:coffeefuelbump/csv-data-summarizer-claude-skill.git
cd csv-data-summarizer-claude-skill
pip install -r requirements.txt
```

## 📊 示例数据集亮点

包含的演示 CSV 包含 **15 个月的 P&L 数据**，包括：
- 3 个产品线（SaaS、企业、服务）
- 25 个财务指标，包括收入、支出、利润率、CAC、LTV
- 季度趋势显示业务增长
- 完美用于展示时间序列分析、相关性分析和财务洞察

## 🎨 示例用例

- **📊 销售数据** → 收入趋势、产品性能、区域分析
- **👥 客户数据** → 人口统计、细分、地理模式
- **💰 财务数据** → 交易分析、趋势检测、相关性
- **⚙️ 运营数据** → 性能指标、时间序列分析
- **📋 调查数据** → 响应分布、交叉表

## 🛠️ 技术细节

**依赖项：**
- Python 3.8+
- pandas 2.0+
- matplotlib 3.7+
- seaborn 0.12+

**生成的可视化：**
- 时间序列趋势图
- 相关性热图
- 分布直方图
- 类别条形图

## 📝 示例输出

```
============================================================
📊 数据概览
============================================================
行数：100 | 列数：15

📋 数据类型：
  • order_date: object
  • total_revenue: float64
  • customer_segment: object
  ...

🔍 数据质量：
✓ 没有缺失值 - 数据集完整！

📈 数值分析：
[所有数值列的摘要统计信息]

🔗 相关性：
[显示关系的相关性矩阵]

📅 时间序列分析：
日期范围：2024-01-05 到 2024-04-11
跨度：97 天

📊 创建的可视化：
  ✓ correlation_heatmap.png
  ✓ time_series_analysis.png
  ✓ distributions.png
  ✓ categorical_distributions.png
```

## 🌟 连接并了解更多

<div align="center">

[![加入 AI 社区](https://img.shields.io/badge/Join-AI%20Community%20(FREE)-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTAgM2MxLjY2IDAgMyAxLjM0IDMgM3MtMS4zNCAzLTMgMy0zLTEuMzQtMy0zIDEuMzQtMyAzLTN6bTAgMTQuMmMtMi41IDAtNC43MS0xLjI4LTYtMy4yMi4wMy0xLjk5IDQtMy4wOCA2LTMuMDggMS45OSAwIDUuOTcgMS4wOSA2IDMuMDgtMS4yOSAxLjk0LTMuNSAzLjIyLTYgMy4yMnoiLz48L3N2Zz4=)](https://www.skool.com/ai-for-your-business/about)

[![Link Tree](https://img.shields.io/badge/Linktree-Everything-green?style=for-the-badge&logo=linktree&logoColor=white)](https://linktr.ee/corbin_brown)

[![YouTube 会员](https://img.shields.io/badge/YouTube-Become%20a%20Builder-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCJFMlSxcvlZg5yZUYJT0Pug/join)

[![Twitter 关注](https://img.shields.io/badge/Twitter-Follow%20@corbin__braun-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/corbin_braun)

</div>

## 🤝 贡献

欢迎贡献！请随意：
- 报告错误
- 提出新功能
- 提交拉取请求
- 分享您的用例

## 📄 许可证

MIT 许可证 - 欢迎用于个人或商业项目！

## 🙏 致谢

由 [Anthropic](https://www.anthropic.com/news/skills) 为 Claude 技能平台构建。

---

<div align="center">

**用 ❤️ 为 AI 社区制作**

⭐ 如果您觉得这个仓库有用，请给它加星！

</div>