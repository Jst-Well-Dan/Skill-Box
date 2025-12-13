<!--
本文件由智谱 AI 自动翻译生成
原文件: forms.md
翻译时间: 2025-12-12 16:13:16
翻译模型: glm-4-flash
原文大小: 9,324 字符
-->

**CRITICAL: 您必须按顺序完成以下步骤。不要跳过编写代码。**

如果您需要填写 PDF 表单，首先检查 PDF 是否有可填写的表单字段。从该文件的目录中运行此脚本：
`python scripts/check_fillable_fields <file.pdf>`，根据结果转到“可填写字段”或“不可填写字段”，并遵循那些说明。

# 可填写字段
如果 PDF 有可填写表单字段：
- 从该文件的目录中运行此脚本：`python scripts/extract_form_field_info.py <input.pdf> <field_info.json>`。它将创建一个包含以下格式的 JSON 文件，其中列出字段：
```
[
  {
    "field_id": (字段的唯一 ID),
    "page": (页面编号，从 1 开始),
    "rect": ([左，下，右，上] PDF 坐标中的边界框，y=0 是页面的底部),
    "type": ("text"，"checkbox"，"radio_group" 或 "choice"),
  },
  // 复选框有 "checked_value" 和 "unchecked_value" 属性：
  {
    "field_id": (字段的唯一 ID),
    "page": (页面编号，从 1 开始),
    "type": "checkbox",
    "checked_value": (将字段设置为此值以选中复选框),
    "unchecked_value": (将字段设置为此值以取消选中复选框),
  },
  // 单选按钮组有一个 "radio_options" 列表，包含可能的选项。
  {
    "field_id": (字段的唯一 ID),
    "page": (页面编号，从 1 开始),
    "type": "radio_group",
    "radio_options": [
      {
        "value": (将字段设置为此值以选择此单选按钮选项),
        "rect": (此选项的单选按钮的边界框)
      },
      // 其他单选按钮选项
    ]
  },
  // 多选题字段有一个包含可能选项的 "choice_options" 列表：
  {
    "field_id": (字段的唯一 ID),
    "page": (页面编号，从 1 开始),
    "type": "choice",
    "choice_options": [
      {
        "value": (将字段设置为此值以选择此选项),
        "text": (选项的显示文本)
      },
      // 其他选项
    ],
  }
]
```
- 使用此脚本将 PDF 转换为 PNG（每页一个图像）（从该文件的目录中运行）：
`python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>`
然后分析图像以确定每个表单字段的用途（确保将边界框 PDF 坐标转换为图像坐标）。
- 创建一个 `field_values.json` 文件，其中包含每个字段要输入的值，格式如下：
```
[
  {
    "field_id": "last_name", // 必须与 `extract_form_field_info.py` 中的 field_id 匹配
    "description": "用户的姓氏",
    "page": 1, // 必须与 field_info.json 中的 "page" 值匹配
    "value": "Simpson"
  },
  {
    "field_id": "Checkbox12",
    "description": "如果用户 18 岁以上，则应选中的复选框",
    "page": 1,
    "value": "/On" // 如果这是一个复选框，则使用其 "checked_value" 值来选中它。如果是单选按钮组，则使用 "radio_options" 中的 "value" 值之一。
  },
  // 更多字段
]
```
- 从该文件的目录中运行 `fill_fillable_fields.py` 脚本以创建一个填写好的 PDF：
`python scripts/fill_fillable_fields.py <input pdf> <field_values.json> <output pdf>`
此脚本将验证您提供的字段 ID 和值是否有效；如果它打印错误消息，则更正适当的字段并再次尝试。

# 不可填写字段
如果 PDF 没有可填写表单字段，您需要通过视觉方式确定数据应添加的位置，并创建文本注释。按照以下步骤 *严格* 执行。您必须执行所有这些步骤以确保表单准确填写。每个步骤的详细信息如下。
- 将 PDF 转换为 PNG 图像并确定字段边界框。
- 创建一个包含字段信息和显示边界框的验证图像的 JSON 文件。
- 验证边界框。
- 使用边界框填写表单。

## 第 1 步：视觉分析（必需）
- 将 PDF 转换为 PNG 图像。从该文件的目录中运行此脚本：
`python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>`
脚本将为 PDF 的每一页创建一个 PNG 图像。
- 仔细检查每个 PNG 图像并识别所有表单字段和用户应输入数据的位置。对于每个用户应输入文本的表单字段，确定表单字段标签和用户应输入文本的区域边界框。标签和输入边界框 *必须不重叠*；文本输入框应仅包括应输入数据区域。通常，此区域将位于其标签的旁边、上方或下方。输入边界框必须足够高和宽，以容纳其文本。

以下是一些您可能会看到的表单结构示例：

*标签在框内*
```
┌────────────────────────┐
│ 名称：                  │
└────────────────────────┘
```
输入区域应位于“名称”标签的右侧并延伸到框的边缘。

*标签在行前*
```
电子邮件： _______________________
```
输入区域应位于行上方并包括其整个宽度。

*标签在行下*
```
_________________________
名称
```
输入区域应位于行上方并包括行的整个宽度。这对于签名和日期字段很常见。

*标签在行上*
```
请输入任何特殊要求：
________________________________________________
```
输入区域应从标签的底部延伸到行，并包括行的整个宽度。

*复选框*
```
您是美国公民吗？ 是 □  否 □
```
对于复选框：
- 寻找小方形框（□）- 这些是实际要针对的复选框。它们可能位于其标签的左侧或右侧。
- 区分标签文本（“是”，“否”）和可点击的复选框方块。
- 输入边界框应仅覆盖小方形，而不是文本标签。

### 第 2 步：创建 fields.json 和验证图像（必需）
- 创建一个名为 `fields.json` 的文件，其中包含表单字段和边界框的信息，格式如下：
```
{
  "pages": [
    {
      "page_number": 1,
      "image_width": (第一页图像宽度（像素）),
      "image_height": (第一页图像高度（像素）),
    },
    {
      "page_number": 2,
      "image_width": (第二页图像宽度（像素）),
      "image_height": (第二页图像高度（像素）),
    }
    // 更多页面
  ],
  "form_fields": [
    // 文本字段的示例。
    {
      "page_number": 1,
      "description": "用户姓氏应在此处输入",
      // 边界框是 [左，上，右，下]。标签和文本输入的边界框不应重叠。
      "field_label": "姓氏",
      "label_bounding_box": [30, 125, 95, 142],
      "entry_bounding_box": [100, 125, 280, 142],
      "entry_text": {
        "text": "Johnson", // 此文本将作为注释添加到 entry_bounding_box 位置
        "font_size": 14, // 可选，默认为 14
        "font_color": "000000", // 可选，RRGGBB 格式，默认为 000000（黑色）
      }
    },
    // 复选框的示例。针对复选框方块的目标边界框，而不是文本
    {
      "page_number": 2,
      "description": "如果用户 18 岁以上，则应选中的复选框",
      "entry_bounding_box": [140, 525, 155, 540],  // 覆盖复选框方块的较小边界框
      "field_label": "是",
      "label_bounding_box": [100, 525, 132, 540],  // 包含“是”文本的框
      // 使用“X”来选中复选框。
      "entry_text": {
        "text": "X",
      }
    }
    // 更多表单字段条目
  ]
}
```

通过从该文件的目录中运行此脚本为每个页面创建验证图像：
`python scripts/create_validation_image.py <page_number> <path_to_fields.json> <input_image_path> <output_image_path>

验证图像将在文本应输入的位置有红色矩形，并覆盖标签文本的蓝色矩形。

### 第 3 步：验证边界框（必需）
#### 自动交集检查
- 使用 `check_bounding_boxes.py` 脚本（从该文件的目录中运行）检查 fields.json 文件以验证边界框是否没有交集并且输入边界框足够高：
`python scripts/check_bounding_boxes.py <JSON 文件>`

如果有错误，重新分析相关字段，调整边界框，并迭代，直到没有剩余错误。请记住：标签（蓝色）边界框应包含文本标签，输入（红色）框不应包含任何文本。

#### 手动图像检查
**CRITICAL：在视觉检查验证图像之前不要继续**
- 红色矩形必须仅覆盖输入区域
- 红色矩形 *不得* 包含任何文本
- 蓝色矩形应包含标签文本
- 对于复选框：
  - 红色矩形必须位于复选框方块的中心
  - 蓝色矩形应覆盖复选框的文本标签

- 如果任何矩形看起来不正确，请修复 fields.json，重新生成验证图像，并再次验证。重复此过程，直到边界框完全准确。

### 第 4 步：向 PDF 添加注释
从该文件的目录中运行此脚本以使用 fields.json 中的信息创建一个填写好的 PDF：
`python scripts/fill_pdf_form_with_annotations.py <input_pdf_path> <path_to_fields.json> <output_pdf_path>