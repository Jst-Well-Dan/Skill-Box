---
name: baoyu-article-illustrator
description: Analyzes article structure, identifies positions requiring visual aids, generates illustrations with Type × Style two-dimension approach. Use when user asks to "illustrate article", "add images", "generate images for article", or "为文章配图".
---

# Article Illustrator

Analyze articles, identify illustration positions, generate images with Type × Style consistency.

## Usage

```bash
# Auto-select type and style based on content
/baoyu-article-illustrator path/to/article.md

# Specify type
/baoyu-article-illustrator path/to/article.md --type infographic

# Specify style
/baoyu-article-illustrator path/to/article.md --style blueprint

# Combine type and style
/baoyu-article-illustrator path/to/article.md --type flowchart --style notion

# Specify density
/baoyu-article-illustrator path/to/article.md --density rich

# Direct content input
/baoyu-article-illustrator
[paste content]
```

## Options

| Option | Description |
|--------|-------------|
| `--type <name>` | Illustration type (see Type Gallery) |
| `--style <name>` | Visual style (see Style Gallery) |
| `--density <level>` | Image count: minimal / balanced / rich |

## Two Dimensions

| Dimension | Controls | Examples |
|-----------|----------|----------|
| **Type** | Information structure, content layout | infographic, scene, flowchart, comparison, framework, timeline |
| **Style** | Visual aesthetics, colors, mood | notion, warm, minimal, blueprint, watercolor, elegant |

Type × Style can be freely combined. Example: `--type infographic --style blueprint` creates technical data visualization with schematic aesthetics.

## Type Gallery

| Type | Description | Best For |
|------|-------------|----------|
| `infographic` | Data visualization, charts, metrics | Technical articles, data analysis, comparisons |
| `scene` | Atmospheric illustration, mood rendering | Narrative articles, personal stories, emotional content |
| `flowchart` | Process diagrams, step visualization | Tutorials, workflows, decision trees |
| `comparison` | Side-by-side, before/after contrast | Product comparisons, option evaluations |
| `framework` | Concept maps, relationship diagrams | Methodologies, models, architecture design |
| `timeline` | Chronological progression | History, project progress, evolution |

## Density Options

| Density | Count | Description |
|---------|-------|-------------|
| `minimal` | 1-2 | Core concepts only |
| `balanced` (Default) | 3-5 | Major sections coverage |
| `rich` | 6+ | Rich visual support |

## Style Gallery

| Style | Description | Best For |
|-------|-------------|----------|
| `notion` (Default) | Minimalist hand-drawn line art | Knowledge sharing, SaaS, productivity |
| `elegant` | Refined, sophisticated | Business, thought leadership |
| `warm` | Friendly, approachable | Personal growth, lifestyle, education |
| `minimal` | Ultra-clean, zen-like | Philosophy, minimalism, core concepts |
| `blueprint` | Technical schematics | Architecture, system design, engineering |
| `watercolor` | Soft artistic with natural warmth | Lifestyle, travel, creative |
| `editorial` | Magazine-style infographic | Tech explainers, journalism |
| `scientific` | Academic precise diagrams | Biology, chemistry, technical research |

Full style specifications: `references/styles/<style>.md`

## Type × Style Compatibility

| | notion | warm | minimal | blueprint | watercolor | elegant | editorial | scientific |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| infographic | ✓✓ | ✓ | ✓✓ | ✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓ |
| scene | ✓ | ✓✓ | ✓ | ✗ | ✓✓ | ✓ | ✓ | ✗ |
| flowchart | ✓✓ | ✓ | ✓ | ✓✓ | ✗ | ✓ | ✓✓ | ✓ |
| comparison | ✓✓ | ✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✓✓ | ✓ |
| framework | ✓✓ | ✓ | ✓✓ | ✓✓ | ✗ | ✓✓ | ✓ | ✓✓ |
| timeline | ✓✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ | ✓✓ | ✓ |

✓✓ = highly recommended | ✓ = compatible | ✗ = not recommended

## Auto Selection

| Content Signals | Recommended Type | Recommended Style |
|-----------------|------------------|-------------------|
| API, metrics, data, comparison, numbers | infographic | blueprint, notion |
| Story, emotion, journey, experience, personal | scene | warm, watercolor |
| How-to, steps, workflow, process, tutorial | flowchart | notion, minimal |
| vs, pros/cons, before/after, alternatives | comparison | notion, elegant |
| Framework, model, architecture, principles | framework | blueprint, notion |
| History, timeline, progress, evolution | timeline | elegant, warm |

## Output Directory

```
illustrations/{topic-slug}/
├── source-{slug}.{ext}
├── outline.md
├── prompts/
│   └── illustration-{slug}.md
└── NN-{type}-{slug}.png
```

**Slug**: Extract 2-4 word topic in kebab-case.
**Conflict**: Append `-YYYYMMDD-HHMMSS` if exists.

## Workflow

### Progress

```
- [ ] Step 1: Setup & Analyze
- [ ] Step 2: Confirm Settings ⚠️ REQUIRED
- [ ] Step 3: Generate Outline
- [ ] Step 4: Generate Images
- [ ] Step 5: Finalize
```

### Step 1: Setup & Analyze

**1.1 Load Preferences (EXTEND.md)**

Use Bash to check EXTEND.md existence (priority order):

```bash
# Check project-level first
test -f .baoyu-skills/baoyu-article-illustrator/EXTEND.md && echo "project"

# Then user-level (cross-platform: $HOME works on macOS/Linux/WSL)
test -f "$HOME/.baoyu-skills/baoyu-article-illustrator/EXTEND.md" && echo "user"
```

┌──────────────────────────────────────────────────────────┬───────────────────┐
│                           Path                           │     Location      │
├──────────────────────────────────────────────────────────┼───────────────────┤
│ .baoyu-skills/baoyu-article-illustrator/EXTEND.md        │ Project directory │
├──────────────────────────────────────────────────────────┼───────────────────┤
│ $HOME/.baoyu-skills/baoyu-article-illustrator/EXTEND.md  │ User home         │
└──────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐
│  Result   │                                  Action                                   │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Found     │ Read, parse, display summary                                              │
├───────────┼───────────────────────────────────────────────────────────────────────────┤
│ Not found │ Ask user with AskUserQuestion (see references/config/first-time-setup.md) │
└───────────┴───────────────────────────────────────────────────────────────────────────┘

**EXTEND.md Supports**: Watermark | Preferred type/style | Custom style definitions | Language preference

Schema: `references/config/preferences-schema.md`

**1.2 Analyze Content**

Read article, detect language, classify content.

| Analysis | Description |
|----------|-------------|
| Content type | Technical / Tutorial / Methodology / Narrative |
| Core arguments | 2-5 main points that MUST be visualized |
| Visual opportunities | Positions where illustrations add value |
| Recommended type | Based on content signals |
| Recommended density | Based on article length and complexity |

**1.3 Extract Core Arguments**

Extract 2-5 core arguments that MUST be visualized:
- Main thesis
- Key concepts reader needs
- Comparisons/contrasts being made
- Framework/model proposed

**CRITICAL**: If article uses metaphors (e.g., "电锯切西瓜"), do NOT illustrate literally. Visualize the **underlying concept** instead.

**1.4 Identify Positions**

**What to Illustrate**:
- Core arguments (REQUIRED)
- Abstract concepts needing visualization
- Data comparisons, metrics
- Processes, workflows

**What NOT to Illustrate**:
- Metaphors literally
- Decorative scenes without information
- Generic illustrations

### Step 2: Confirm Settings ⚠️

**Do NOT skip.** Use AskUserQuestion with 3-4 questions in ONE call.

**Question 1: Illustration Type**

Based on content analysis, recommend type:
- [Recommended type based on signals] (Recommended)
- infographic - Data visualization, charts
- scene - Atmospheric, mood rendering
- flowchart - Process, steps
- comparison - Side-by-side contrast
- framework - Concept relationships
- timeline - Chronological progression
- mixed - Combine multiple types

**Question 2: Density**

- minimal (1-2 images) - Core concepts only
- balanced (3-5 images) (Recommended) - Major sections
- rich (6+ images) - Comprehensive visual support

**Question 3: Style**

Based on recommended Type, suggest compatible styles (see Type × Style Compatibility matrix):
- [Best compatible style for recommended type] (Recommended)
- [Other highly compatible styles: ✓✓ from matrix]
- [Compatible styles: ✓ from matrix]

**Question 4** (only if source ≠ user language):
- Language: Source language / User language

### Step 3: Generate Outline

Based on confirmed Type + Density + Style, generate illustration outline.

**Outline Format** (`outline.md`):

```yaml
---
type: infographic
density: balanced
style: blueprint
image_count: 4
---

## Illustration 1

**Position**: [section] / [paragraph]
**Purpose**: [why this illustration helps]
**Visual Content**: [what to show]
**Type Application**: [how type applies here]
**Filename**: 01-infographic-concept-name.png

## Illustration 2
...
```

**Outline Requirements**:
- Each illustration position justified by content needs
- Type applied consistently across all illustrations
- Style characteristics reflected in visual descriptions
- Count matches density selection

### Step 4: Generate Images

**4.1 Create Prompts**

Follow Prompt Construction principles below. Save each to `prompts/illustration-{slug}.md`.

**4.2 Select Generation Skill**

Check available image generation skills. If multiple, ask user to choose.

**4.3 Apply Watermark** (if enabled in preferences)

Add to prompt: `Include a subtle watermark "[content]" positioned at [position] with approximately [opacity*100]% visibility.`

**4.4 Generate**

1. Generate sequentially
2. After each: "Generated X/N"
3. On failure: auto-retry once, then log and continue

### Step 5: Finalize

**5.1 Update Article**

Insert after corresponding paragraph:
```markdown
![description](illustrations/{slug}/NN-{type}-{slug}.png)
```

Alt text: concise description in article's language.

**5.2 Output Summary**

```
Article Illustration Complete!

Article: [path]
Type: [type name]
Density: [minimal/balanced/rich]
Style: [style name]
Location: [directory path]
Images: X/N generated

Positions:
- 01-infographic-xxx.png → After "[Section]"
- 02-infographic-yyy.png → After "[Section]"

[If failures]
Failed:
- NN-type-zzz.png: [reason]
```

## Prompt Construction

### Principles

Good prompts must include:

1. **Layout Structure First**: Describe composition, zones, flow direction
2. **Specific Data/Labels**: Use actual numbers, terms from article
3. **Visual Relationships**: How elements connect
4. **Semantic Colors**: Meaning-based color choices (red=warning, green=efficient)
5. **Style Characteristics**: Line treatment, texture, mood
6. **Aspect Ratio**: End with ratio and complexity level

### Type-Specific Prompts

**Infographic**:
```
[Title] - Data Visualization

Layout: [grid/radial/hierarchical]

ZONES:
- Zone 1: [data point with specific values]
- Zone 2: [comparison with metrics]
- Zone 3: [summary/conclusion]

LABELS: [specific numbers, percentages, terms from article]
COLORS: [semantic color mapping]
STYLE: [style characteristics]
ASPECT: 16:9
```

**Scene**:
```
[Title] - Atmospheric Scene

FOCAL POINT: [main subject]
ATMOSPHERE: [lighting, mood, environment]
MOOD: [emotion to convey]
COLOR TEMPERATURE: [warm/cool/neutral]
STYLE: [style characteristics]
ASPECT: 16:9
```

**Flowchart**:
```
[Title] - Process Flow

Layout: [left-right/top-down/circular]

STEPS:
1. [Step name] - [brief description]
2. [Step name] - [brief description]
...

CONNECTIONS: [arrow types, decision points]
STYLE: [style characteristics]
ASPECT: 16:9
```

**Comparison**:
```
[Title] - Comparison View

LEFT SIDE - [Option A]:
- [Point 1]
- [Point 2]

RIGHT SIDE - [Option B]:
- [Point 1]
- [Point 2]

DIVIDER: [visual separator]
STYLE: [style characteristics]
ASPECT: 16:9
```

**Framework**:
```
[Title] - Conceptual Framework

STRUCTURE: [hierarchical/network/matrix]

NODES:
- [Concept 1] - [role]
- [Concept 2] - [role]

RELATIONSHIPS: [how nodes connect]
STYLE: [style characteristics]
ASPECT: 16:9
```

**Timeline**:
```
[Title] - Chronological View

DIRECTION: [horizontal/vertical]

EVENTS:
- [Date/Period 1]: [milestone]
- [Date/Period 2]: [milestone]

MARKERS: [visual indicators]
STYLE: [style characteristics]
ASPECT: 16:9
```

### What to Avoid

- Vague descriptions ("a nice image")
- Literal metaphor illustrations
- Missing concrete labels/annotations
- Generic decorative elements

## Modification

| Action | Steps |
|--------|-------|
| **Edit** | Update prompt → Regenerate → Update reference |
| **Add** | Identify position → Create prompt → Generate → Update outline → Insert reference |
| **Delete** | Delete files → Remove reference → Update outline |

## References

| File | Content |
|------|---------|
| [references/styles.md](references/styles.md) | Style gallery & compatibility matrix |
| `references/styles/<style>.md` | Full style specifications |
| `references/config/preferences-schema.md` | EXTEND.md schema |
| `references/config/first-time-setup.md` | First-time setup flow |

## Extension Support

Custom configurations via EXTEND.md. See **Step 1.1** for paths and supported options.
