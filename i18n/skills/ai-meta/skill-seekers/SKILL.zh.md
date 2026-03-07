---
name: skill-seekers
description: 使用 Skill Seekers CLI 从文档网站、GitHub 仓库、PDF 文件或本地代码库生成 AI 技能（SKILL.md）。当用户希望从外部文档创建新技能、将 GitHub 仓库分析为技能、将 PDF 转换为结构化 AI 知识，或为 Claude、Gemini、OpenAI 打包技能时使用。
---

# Skill Seekers

一个通用的预处理工具，可将任何文档、GitHub 仓库、PDF 或视频转化为结构化的 AI 知识资产。

## 快速入门

1. **创建技能**: `skill-seekers create https://docs.django.com/`
2. **AI 增强**: `skill-seekers enhance output/django/`
3. **打包**: `skill-seekers package output/django --target claude`

## 来源类型

- **URL**: `skill-seekers create <url>`
- **GitHub**: `skill-seekers create <owner/repo>`
- **本地路径**: `skill-seekers create ./path`
- **PDF**: `skill-seekers create file.pdf`

## 导出目标

支持 `claude`, `gemini`, `openai`, `langchain`, `cursor`, `markdown` 等。
