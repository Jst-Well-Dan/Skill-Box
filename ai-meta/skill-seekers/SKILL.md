---
name: skill-seekers
description: Generate AI skills (SKILL.md) from documentation websites, GitHub repositories, PDF files, or local codebases using the Skill Seekers CLI. Use when the user wants to create a new AI skill from external documentation, analyze a GitHub repo into a skill, convert a PDF into structured AI knowledge, or package skills for Claude, Gemini, or OpenAI.
---

# Skill Seekers

A universal preprocessing tool that turns any documentation, GitHub repo, PDF, or video into structured AI knowledge assets.

## Prerequisites

```bash
pip install skill-seekers
# Or with all features:
pip install skill-seekers[all]
```

## Quick Start (3 Commands)

```bash
# 1. Create skill from any source
skill-seekers create https://docs.django.com/

# 2. (Optional) Enhance with AI
skill-seekers enhance output/django/

# 3. Package for your AI platform
skill-seekers package output/django --target claude
```

## Source Types

| Source | Command | Example |
|--------|---------|---------|
| Documentation URL | `create <url>` | `skill-seekers create https://docs.react.dev/` |
| GitHub repo | `create <owner/repo>` | `skill-seekers create facebook/react` |
| Local codebase | `create <path>` | `skill-seekers create ./my-project` |
| PDF file | `create <file.pdf>` | `skill-seekers create manual.pdf` |
| YouTube video | `video --url <url>` | `skill-seekers video --url https://youtube.com/...` |

## Export Targets

```bash
skill-seekers package output/react --target claude      # Claude AI Skill (ZIP)
skill-seekers package output/react --target gemini      # Google Gemini (tar.gz)
skill-seekers package output/react --target openai      # OpenAI (ZIP)
skill-seekers package output/react --target langchain   # LangChain Documents (JSON)
skill-seekers package output/react --target cursor      # .cursorrules for Cursor IDE
skill-seekers package output/react --target markdown    # Universal Markdown (ZIP)
```

## Key Commands

```bash
# All-in-one: scrape + enhance + package + upload
skill-seekers install --config react

# GitHub repo with issues and changelog
skill-seekers github --repo owner/repo --include-issues --include-changelog

# Codebase analysis (local path or GitHub URL)
skill-seekers analyze --directory ./my-project --output output/my-skill/

# PDF with tables and parallel processing
skill-seekers pdf --pdf docs/manual.pdf --name myskill --extract-tables --parallel

# Multi-source unified skill (docs + GitHub + PDF combined)
skill-seekers unified --config configs/myframework_unified.json

# List and manage enhancement workflow presets
skill-seekers workflows list
skill-seekers create ./my-project --enhance-workflow security-focus
```

## Configuration

Skill Seekers uses JSON config files for repeatable scraping:

```json
{
  "name": "react",
  "base_url": "https://react.dev/",
  "max_pages": 200
}
```

Run with: `skill-seekers scrape --config configs/react.json`

Browse 24+ preset configs at [skillseekersweb.com](https://skillseekersweb.com/).

## AI Enhancement (Optional)

```bash
# Use Claude API for enhancement
export ANTHROPIC_API_KEY=sk-ant-...
skill-seekers enhance output/react/

# Use local Claude Code (free, no API cost)
skill-seekers create ./my-project --ai-mode local

# Apply security-focused enhancement workflow
skill-seekers enhance output/react/ --workflow security-focus
```

## Output Structure

```
output/react/
├── SKILL.md            # Main skill file (300-500+ lines)
└── references/         # Detailed reference files
    ├── api/            # API documentation
    ├── guides/         # How-to guides
    └── examples/       # Code examples
```

## Tips

- Use `--async --workers 8` for 3x faster scraping on large docs
- Use `skill-seekers resume --list` to continue interrupted jobs
- Set up multiple GitHub tokens via `skill-seekers config --github` to avoid rate limits
- 24+ ready-to-use presets for popular frameworks (React, Django, Godot, FastAPI, etc.)

## References

- [Skill Seekers GitHub](https://github.com/yusufkaraaslan/Skill_Seekers)
- [Full Documentation](https://github.com/yusufkaraaslan/Skill_Seekers/tree/main/docs)
- [CLI Reference](https://github.com/yusufkaraaslan/Skill_Seekers/blob/main/docs/reference/CLI_REFERENCE.md)
- [Preset Configs](https://skillseekersweb.com/)
