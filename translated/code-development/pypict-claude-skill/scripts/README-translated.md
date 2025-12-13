<!--
本文件由智谱 AI 自动翻译生成
原文件: README.md
翻译时间: 2025-12-12 16:10:18
翻译模型: glm-4-flash
原文大小: 1,680 字符
-->

---

# 脚本

此目录包含用于处理 PICT 模型和测试用例的辅助脚本。

## 可用脚本

### pict_helper.py

一个 Python 工具，用于：
- 从 JSON 配置生成 PICT 模型
- 将 PICT 输出格式化为 Markdown 表格
- 将 PICT 输出解析为 JSON

**安装：**
```bash
pip install pypict --break-system-packages
```

**使用方法：**

1. **从配置生成 PICT 模型：**
   ```bash
   python pict_helper.py generate config.json > model.txt
   ```

2. **将 PICT 输出格式化为 Markdown：**
   ```bash
   python pict_helper.py format output.txt
   ```

3. **将 PICT 输出解析为 JSON：**
   ```bash
   python pict_helper.py parse output.txt
   ```

**示例 config.json：**
```json
{
    "parameters": {
        "Browser": ["Chrome", "Firefox", "Safari"],
        "OS": ["Windows", "MacOS", "Linux"],
        "Memory": ["4GB", "8GB", "16GB"]
    },
    "constraints": [
        "IF [OS] = \"MacOS\" THEN [Browser] <> \"IE\"",
        "IF [Memory] = \"4GB\" THEN [OS] <> \"MacOS\""
    ]
}
```

## 未来脚本

我们欢迎以下贡献：
- 测试自动化生成器
- 导出至测试管理工具（JIRA，TestRail）
- 与 CI/CD 管道集成
- 覆盖率分析工具
- 约束验证实用工具

## 贡献

有有用的脚本要分享吗？

1. 将您的脚本添加到此目录
2. 更新此 README 以包含使用说明
3. 在您的脚本中添加注释和示例
4. 提交一个 pull request

有关指南，请参阅 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 依赖项

当前脚本使用：
- Python 3.7+
- pypict（可选，用于直接 PICT 集成）

每个脚本中应清楚地记录所有依赖项。