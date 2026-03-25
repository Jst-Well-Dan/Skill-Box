# Skillbox 分类映射表

## 文档说明

本文档记录了 Skillbox 技能分类的映射关系。分类的 **Key 值（文件夹名称）** 已更新为新的 kebab-case 名称。

> **重要提示**: `marketplace.json` 文件中的 `category` 和 `source` 字段已同步更新为新的分类名称。

---

## 完整映射表

| Category Key | 中文名称 | 英文名称 |
|--------------|---------|---------|
| `no-code-builder` | 零代码构建 | No-Code Builder |
| `office-automation` | 办公自动化 | Office Automation |
| `content-pipeline` | 内容流水线 | Content Pipeline |
| `immersive-reading` | 沉浸式研读 | Immersive Reading |
| `visual-creative` | 视觉与创意 | Visual & Creative |
| `brand-marketing` | 品牌与营销 | Brand & Marketing |
| `business-analyst` | 商业分析师 | Business Analyst |

---

## 分类说明

### 1. `no-code-builder` - 零代码构建 / No-Code Builder
**设计理念**: 告诉用户这里不是教你写代码，而是帮你不用写代码也能做东西。

**适用技能**:
- 前端开发工具
- 低代码/无代码构建工具
- 可视化开发辅助

---


### 2. `office-automation` - 办公自动化 / Office Automation
**设计理念**: 经典命名，对打工人最有效，强调自动化效率。

**适用技能**:
- Word/Excel/PowerPoint 处理
- PDF 文档操作
- 办公流程自动化

---

### 3. `content-pipeline` - 内容流水线 / Content Pipeline
**设计理念**: 强调"自动化"和"效率"，将内容创作比作工业化流水线。

**适用技能**:
- 文章写作
- 视频内容创作
- 自动化内容生成

---

### 4. `immersive-reading` - 沉浸式研读 / Immersive Reading
**设计理念**: 强调深度和效率，专注于学习和研究的沉浸体验。

**适用技能**:

- 深度阅读分析
- 学术研究辅助
- 知识管理工具

---

### 5. `visual-creative` - 视觉与创意 / Visual & Creative
**设计理念**: 更直观地表达视觉创意和媒体设计的核心。

**适用技能**:
- 图像设计
- 算法艺术
- 多媒体创作

---

### 6. `brand-marketing` - 品牌与营销 / Brand & Marketing
**设计理念**: 比"营销"更具体，直击商业痛点，强调品牌建设。

**适用技能**:
- 品牌策划
- 市场营销
- 商业分析

---

### 7. `business-analyst` - 商业分析师 / Business Analyst
**设计理念**: 拟人化表达，不仅处理数据，更提供分析洞察。

**适用技能**:
- 数据可视化
- 商业智能分析
- CSV/表格数据处理

---

## 技术实现

### 翻译文件位置
- 中文翻译: `src/i18n/locales/zh-CN.json`
- 英文翻译: `src/i18n/locales/en.json`

### 配置示例

**zh-CN.json:**
```json
"categories": {
  "explore": "技能分区",
  "all": "全部分类",
  "allSkills": "所有技能",
  "no-code-builder": "零代码构建",
  "office-automation": "办公自动化",
  "content-pipeline": "内容流水线",
  "immersive-reading": "沉浸式研读",
  "visual-creative": "视觉与创意",
  "brand-marketing": "品牌与营销",
  "business-analyst": "商业分析师"
}
```

**en.json:**
```json
"categories": {
  "explore": "Skill Zones",
  "all": "All Categories",
  "allSkills": "All Skills",
  "no-code-builder": "No-Code Builder",
  "office-automation": "Office Automation",
  "content-pipeline": "Content Pipeline",
  "immersive-reading": "Immersive Reading",
  "visual-creative": "Visual & Creative",
  "brand-marketing": "Brand & Marketing",
  "business-analyst": "Business Analyst"
}
```

---

## 使用指南

### 添加新技能时
在 `marketplace.json` 中添加技能时，使用以下 `category` 值之一：

```json
{
  "name": "your-skill-name",
  "description": "Your skill description",
  "source": "./no-code-builder/skill-folder",
  "category": "no-code-builder",  // 使用映射表中的 Category Key
  "author": {
    "name": "Your Name"
  }
}
```

### 可用的分类 Key
- `no-code-builder` - 零代码构建
- `office-automation` - 办公自动化
- `content-pipeline` - 内容流水线
- `immersive-reading` - 沉浸式研读
- `visual-creative` - 视觉与创意
- `brand-marketing` - 品牌与营销
- `business-analyst` - 商业分析师

---

## 版本历史

### v2.0.0 - 2025-12-14
- ✅ 重命名所有分类文件夹为新的 kebab-case 名称
- ✅ 更新 marketplace.json 中的 category 和 source 字段
- ✅ 更新 Python 脚本中的 SKILL_CATEGORIES 列表

### v1.0.0 - 2025-12-13
- ✅ 初始版本
- ✅ 完成所有分类的中英文名称优化
- ✅ 建立分类映射关系
- ✅ 实现 i18n 国际化支持

---

## 维护说明

1. **保持一致性**: 所有新增技能必须使用映射表中定义的 Category Key
2. **文件夹对应**: 确保物理文件夹名称与 Category Key 一致
3. **命名规范**: Category Key 使用小写字母和连字符（kebab-case）
4. **同步更新**: 添加新分类时需同时更新文件夹、marketplace.json 和 Python 脚本

---

## 联系方式

如有疑问或建议，请访问：
- GitHub: https://github.com/Jst-Well-Dan/claude-skills-vault
- 作者: Jst-Well-Dan

---

**最后更新**: 2025-12-14
