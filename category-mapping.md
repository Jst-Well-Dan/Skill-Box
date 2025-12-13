# Skillbox 分类映射表

## 文档说明

本文档记录了 Skillbox 网站中技能分类的映射关系。分类的 **Key 值保持不变**，仅修改了在用户界面上显示的**中英文名称**。

> **重要提示**: `marketplace.json` 文件中的 `category` 字段不需要修改。系统会通过 `i18n` 翻译文件自动映射显示新的分类名称。

---

## 完整映射表

| Category Key | 原中文名称 | 新中文名称 | 原英文名称 | 新英文名称 |
|--------------|----------|----------|----------|----------|
| `code-development` | 代码开发 | **零代码构建** | Code Development | **No-Code Builder** |
| `office-documents` | Office文档 | **办公自动化** | Office Documents | **Office Automation** |
| `content-creation` | 内容创作 | **内容流水线** | Content Creation | **Content Pipeline** |
| `learning-research` | 学习研究 | **沉浸式研读** | Learning & Research | **Immersive Reading** |
| `creative-media` | 创意媒体 | **视觉与创意** | Creative Media | **Visual & Creative** |
| `business-marketing` | 商务营销 | **品牌与营销** | Business Marketing | **Brand & Marketing** |
| `data-analysis` | 数据分析 | **商业分析师** | Data Analysis | **Business Analyst** |

---

## 分类说明

### 1. `code-development` - 零代码构建 / No-Code Builder
**设计理念**: 告诉用户这里不是教你写代码，而是帮你不用写代码也能做东西。

**适用技能**:
- 前端开发工具
- 低代码/无代码构建工具
- 可视化开发辅助

---


### 2. `office-documents` - 办公自动化 / Office Automation
**设计理念**: 经典命名，对打工人最有效，强调自动化效率。

**适用技能**:
- Word/Excel/PowerPoint 处理
- PDF 文档操作
- 办公流程自动化

---

### 3. `content-creation` - 内容流水线 / Content Pipeline
**设计理念**: 强调"自动化"和"效率"，将内容创作比作工业化流水线。

**适用技能**:
- 文章写作
- 视频内容创作
- 自动化内容生成

---

### 4. `learning-research` - 沉浸式研读 / Immersive Reading
**设计理念**: 强调深度和效率，专注于学习和研究的沉浸体验。

**适用技能**:
- 深度阅读分析
- 学术研究辅助
- 知识管理工具

---

### 5. `creative-media` - 视觉与创意 / Visual & Creative
**设计理念**: 更直观地表达视觉创意和媒体设计的核心。

**适用技能**:
- 图像设计
- 算法艺术
- 多媒体创作

---

### 6. `business-marketing` - 品牌与营销 / Brand & Marketing
**设计理念**: 比"营销"更具体，直击商业痛点，强调品牌建设。

**适用技能**:
- 品牌策划
- 市场营销
- 商业分析

---

### 7. `data-analysis` - 商业分析师 / Business Analyst
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
  "code-development": "零代码构建",
  "office-documents": "办公自动化",
  "content-creation": "内容流水线",
  "learning-research": "沉浸式研读",
  "creative-media": "视觉与创意",
  "business-marketing": "品牌与营销",
  "data-analysis": "商业分析师"
}
```

**en.json:**
```json
"categories": {
  "explore": "Skill Zones",
  "all": "All Categories",
  "allSkills": "All Skills",
  "code-development": "No-Code Builder",
  "office-documents": "Office Automation",
  "content-creation": "Content Pipeline",
  "learning-research": "Immersive Reading",
  "creative-media": "Visual & Creative",
  "business-marketing": "Brand & Marketing",
  "data-analysis": "Business Analyst"
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
  "source": "./category-folder/skill-folder",
  "category": "code-development",  // 使用映射表中的 Category Key
  "author": {
    "name": "Your Name"
  }
}
```

### 修改分类显示名称
如需修改分类的显示名称，请编辑：
1. `src/i18n/locales/zh-CN.json` - 修改中文显示名称
2. `src/i18n/locales/en.json` - 修改英文显示名称

**不要修改** `marketplace.json` 中的 `category` 字段值！

---

## 版本历史

### v1.0.0 - 2025-12-13
- ✅ 初始版本
- ✅ 完成所有分类的中英文名称优化
- ✅ 建立分类映射关系
- ✅ 实现 i18n 国际化支持

---

## 维护说明

1. **保持一致性**: 所有新增技能必须使用映射表中定义的 Category Key
2. **同步更新**: 修改分类显示名称时，需同步更新中英文翻译文件
3. **避免冲突**: 不要直接修改 marketplace.json 中的 category 值
4. **命名规范**: Category Key 使用小写字母和连字符（kebab-case）

---

## 联系方式

如有疑问或建议，请访问：
- GitHub: https://github.com/Jst-Well-Dan/claude-skills-vault
- 作者: Jst-Well-Dan

---

**最后更新**: 2025-12-13
