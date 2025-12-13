# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Claude Skills Vault, a curated collection of 47+ practical Claude Skills organized across 8 categories. The repository serves as both a marketplace of skills and a framework for managing and distributing them. Skills are modular packages that extend Claude's capabilities with specialized knowledge, workflows, and tool integrations.

## Repository Structure

```
awesome-claude-skills/
├── .claude-plugin/
│   └── marketplace.json          # Central registry of all 47+ skills
│
├── Category Directories/          # Skills organized by category
│   ├── business-marketing/
│   ├── collaboration-project-management/
│   ├── communication-writing/
│   ├── creative-media/
│   ├── data-analysis/
│   ├── development/
│   ├── document-processing/
│   ├── document-skills/          # Legacy Office document skills
│   └── productivity-organization/
│
├── scripts/                       # Python automation for skill management
│   ├── fetch_external_skills.py  # Main orchestrator for fetching external skills
│   ├── github_fetcher.py         # GitHub API interactions
│   ├── marketplace_updater.py    # Updates marketplace.json
│   ├── skill_processor.py        # Validates and processes skills
│   └── utils.py                  # Common utilities
│
├── config/
│   └── external_skills_config.json  # Configuration for external skill sources
│
├── awesome-skills-showcase/      # React/Vite web showcase application
│   ├── src/                      # TypeScript/React source code
│   └── package.json              # Node.js dependencies and scripts
│
└── requirements.txt              # Python dependencies
```

## Skill Structure

Every skill follows a standardized structure:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter with name and description
│   └── Markdown instructions
└── Optional directories:
    ├── scripts/      # Executable code (Python/Bash)
    ├── references/   # Documentation loaded on demand
    └── assets/       # Templates, images, etc.
```

The `name` and `description` in YAML frontmatter are critical - they determine when Claude activates the skill.

## Python Environment and Scripts

### Dependencies

Install Python dependencies before running scripts:
```bash
pip install -r requirements.txt
```

Required packages:
- `requests>=2.31.0` - HTTP requests for GitHub API
- `python-frontmatter>=1.1.0` - Parse YAML frontmatter in SKILL.md files
- `PyYAML>=6.0.1` - YAML parsing
- `jsonschema>=4.20.0` - Validate JSON schemas

### Fetching External Skills

The primary automation tool is `fetch_external_skills.py`, which fetches skills from external GitHub repositories and integrates them into the marketplace.

**Basic usage:**
```bash
# Fetch all configured skills
python scripts/fetch_external_skills.py --all

# Fetch specific skill by ID
python scripts/fetch_external_skills.py --skill markdown-to-epub-converter

# Dry run (simulate without writing)
python scripts/fetch_external_skills.py --dry-run --all

# Force re-fetch existing skills
python scripts/fetch_external_skills.py --force --all

# Use custom config file
python scripts/fetch_external_skills.py --config path/to/config.json
```

**Configuration:**
External skills are defined in `config/external_skills_config.json`. Each skill entry includes:
- `id` - Unique identifier
- `github_url` - Source repository URL
- `repo_type` - Type: `standalone`, `multi_skill`
- `target_folder` - Destination directory
- `category` - Marketplace category
- `extraction_config` - How to extract from repo:
  - `full_repo` - Clone entire repository
  - `subfolder` - Extract specific subfolder
  - `deep_nested` - Extract deeply nested subfolder

### Script Architecture

The fetching system is modular:

1. **fetch_external_skills.py** - Main orchestrator
   - Loads configuration
   - Validates environment
   - Coordinates fetching workflow
   - Generates execution reports

2. **github_fetcher.py** - GitHub interactions
   - Handles GitHub API authentication (uses `GITHUB_TOKEN` env var)
   - Downloads repositories via API or git clone
   - Extracts specific subfolders based on config

3. **skill_processor.py** - Skill validation
   - Validates SKILL.md structure and frontmatter
   - Checks for required metadata (name, description)
   - Normalizes skill metadata

4. **marketplace_updater.py** - Registry management
   - Updates `.claude-plugin/marketplace.json`
   - Merges new skills with existing ones
   - Maintains marketplace schema

## Web Showcase Application

The `awesome-skills-showcase/` directory contains a React/Vite web application for browsing skills.

### Development Commands

```bash
# Navigate to showcase directory
cd awesome-skills-showcase

# Install dependencies (if not already installed)
pnpm install

# Start development server (default: http://localhost:5173)
pnpm dev

# Build for production
pnpm build

# Type check TypeScript
pnpm build  # Includes tsc -b

# Lint code
pnpm lint

# Preview production build
pnpm preview
```

### Tech Stack

- **React 19.2** - UI framework
- **TypeScript** - Type safety
- **Vite 7** - Build tool and dev server
- **Tailwind CSS 3.4** - Styling
- **Radix UI** - Headless UI components
- **shadcn/ui patterns** - UI component patterns
- **Lucide React** - Icons

## Marketplace Registry

The `.claude-plugin/marketplace.json` file is the central registry. It follows this schema:

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "awesome-claude-skills",
  "version": "1.0.0",
  "description": "...",
  "owner": { "name": "...", "email": "..." },
  "plugins": [
    {
      "name": "skill-name",
      "description": "When to use this skill...",
      "source": "./category/skill-folder",
      "category": "category-name"
    }
  ]
}
```

When adding new skills manually, ensure:
1. The skill directory contains a valid `SKILL.md` with frontmatter
2. The `source` path is relative to repository root
3. The `description` clearly states when Claude should use the skill
4. The skill is placed in the appropriate category directory

## Creating New Skills

Use the `skill-creator` skill (in `development/skill-creator/`) for guidance. Key principles:

1. **Required: SKILL.md** with YAML frontmatter containing `name` and `description`
2. **Description Quality**: Be specific about when Claude should use the skill (use third-person)
3. **Progressive Disclosure**: Keep SKILL.md lean (~5k words max), use `references/` for detailed docs
4. **Scripts for Deterministic Tasks**: Place executable code in `scripts/` when the same code is repeatedly rewritten
5. **Assets for Output**: Use `assets/` for templates, images, or files used in output (not loaded into context)

Template structure available at `development/template-skill/`.

## Git Workflow

**Current branch:** master
**Main branch:** master (use for PRs)

When committing changes:
- Follow conventional commit style by examining recent commits with `git log`
- Include co-author attribution as shown in recent commits
- Do not commit to skip tests or hooks unless explicitly requested

## Common Development Patterns

### Adding a New Skill Manually

1. Create skill directory in appropriate category folder
2. Write `SKILL.md` with proper frontmatter
3. Add optional `scripts/`, `references/`, or `assets/` as needed
4. Update `.claude-plugin/marketplace.json` with new entry
5. Test skill activation by using it in Claude Code

### Fetching Skills from External Sources

1. Add skill configuration to `config/external_skills_config.json`
2. Run: `python scripts/fetch_external_skills.py --skill <skill-id>`
3. Verify skill was fetched to correct category directory
4. Confirm `marketplace.json` was updated

### Modifying the Showcase Web App

1. Navigate to `awesome-skills-showcase/`
2. Run `pnpm dev` for hot-reload development
3. Edit TypeScript/React files in `src/`
4. Build with `pnpm build` before committing

## Important Files

- **marketplace.json** - Central registry, do not corrupt JSON structure
- **external_skills_config.json** - Configuration for automated skill fetching
- **requirements.txt** - Python dependencies for automation scripts
- **SKILL.md files** - Each skill's definition, must have valid YAML frontmatter
- **README.md** - Public documentation, keep in sync with actual skill count

## Categories

1. **development** - Software development, testing, code quality (14 skills)
2. **productivity-organization** - Task management, document processing (10 skills)
3. **communication-writing** - Content creation, research (6 skills)
4. **creative-media** - Visual content, video, creative work (6 skills)
5. **business-marketing** - Business operations, marketing (5 skills)
6. **collaboration-project-management** - Team collaboration, version control (3 skills)
7. **data-analysis** - Data analysis and debugging (2 skills)
8. **document-processing** - Document conversion (1 skill)

When adding new skills, place them in the most appropriate category or create a new category if needed.
