---
name: nano-pdf
description: 使用自然语言指令通过 nano-pdf CLI 编辑 PDF。支持修改标题、修复拼写错误等快速 PDF 编辑操作。
homepage: https://pypi.org/project/nano-pdf/
metadata:
  {
    "openclaw":
      {
        "emoji": "📄",
        "requires": { "bins": ["nano-pdf"] },
        "install":
          [
            {
              "id": "uv",
              "kind": "uv",
              "package": "nano-pdf",
              "bins": ["nano-pdf"],
              "label": "安装 nano-pdf (uv)",
            },
          ],
      },
  }
---

# nano-pdf

使用 `nano-pdf` 通过自然语言指令对 PDF 的特定页面应用编辑。

## 快速开始

```bash
nano-pdf edit deck.pdf 1 "将标题更改为 'Q3 业绩' 并修复副标题中的拼写错误"
```

注意事项：

- 页码可能是从 0 开始或从 1 开始，具体取决于工具的版本/配置。如果结果看起来偏移了一页，请尝试另一种方式。
- 在发出输出 PDF 之前，务必对其进行最终检查。
