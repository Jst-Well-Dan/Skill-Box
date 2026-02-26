<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:11:08
翻译模型: glm-4-flash
原文大小: 2,836 字符
-->

---

# CSV 数据汇总器 - 资源

---

## 🌟 连接并了解更多

<div align="center">

### 🚀 **加入我们的社区**
[![加入 AI 社区](https://img.shields.io/badge/Join-AI%20Community%20(FREE)-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTAgM2MxLjY2IDAgMyAxLjM0IDMgM3MtMS4zNCAzLTMgMy0zLTEuMzQtMy0zIDEuMzQtMyAzLTN6bTAgMTQuMmMtMi41IDAtNC43MS0xLjI4LTYtMy4yMi4wMy0xLjk5IDQtMy4wOCA2LTMuMDggMS45OSAwIDUuOTcgMS4wOSA2IDMuMDgtMS4yOSAxLjk0LTMuNSAzLjIyLTYgMy4yMnoiLz48L3N2Zz4=)](https://www.skool.com/ai-for-your-business/about)

### 🔗 **所有链接**
[![Link Tree](https://img.shields.io/badge/Linktree-Everything-green?style=for-the-badge&logo=linktree&logoColor=white)](https://linktr.ee/corbin_brown)

### 🛠️ **成为构建者**
[![YouTube Membership](https://img.shields.io/badge/YouTube-Become%20a%20Builder-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCJFMlSxcvlZg5yZUYJT0Pug/join)

### 🐦 **关注 Twitter**
[![Twitter Follow](https://img.shields.io/badge/Twitter-Follow%20@corbin__braun-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/corbin_braun)

</div>

---

## 样本数据

`sample.csv` 文件包含以下列的示例销售数据：

- **date**: 交易日期
- **product**: 产品名称（Widget A、B 或 C）
- **quantity**: 销售的商品数量
- **revenue**: 交易的总收入
- **customer_id**: 唯一客户标识符
- **region**: 地理区域（北、南、东、西）

## 使用示例

### 基本汇总
```
分析 sample.csv
```

### 使用自定义 CSV
```
这是我的 sales_data.csv 文件。你能汇总它吗？
```

### 专注于特定见解
```
这个数据集中的收入趋势是什么？
```

## 测试技能

在将技能上传到 Claude 之前，您可以在本地测试技能：

```bash
# 安装依赖项
pip install -r ../requirements.txt

# 运行分析
python ../analyze.py sample.csv
```

## 预期输出

分析将提供：

1. **数据集维度** - 行和列计数
2. **列信息** - 名称和数据类型
3. **汇总统计** - 数值列的均值、中位数、标准差、最小/最大值
4. **数据质量** - 缺失值检测和计数
5. **可视化** - 存在日期列时的时间序列图

## 自定义化

为了适应您的特定用例，请执行以下操作：

1. 修改 `analyze.py` 以包含特定领域的计算
2. 在绘图部分添加自定义可视化类型
3. 包含针对您的数据特定的验证规则
4. 添加更多样本数据集以测试不同场景

---