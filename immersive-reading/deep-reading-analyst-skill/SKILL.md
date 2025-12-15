---
name: deep-reading-analyst
description: Systematic analysis framework for articles, papers, and long-form content using 5 proven thinking models (SCQA, 5W2H, Critical Thinking, Inversion, Systems Thinking).
---

# Deep Reading Analyst

Transform surface-level reading into deep learning through systematic thinking frameworks.

## What This Skill Does

Provides structured analysis workflows using 5 proven thinking frameworks across 4 depth levels (15min to 120min+). Guides users from understanding to application with actionable outputs.

## When to Use This Skill

Use when users:
- Analyze complex articles, papers, or long-form content
- Evaluate arguments and identify logical flaws
- Extract actionable insights from reading materials
- Create structured learning notes or study summaries
- Compare multiple sources for research
- Apply specific thinking frameworks (SCQA, mental models, etc.)
- Provide URLs or long-form content with intent to deeply understand

## Response Pattern

When user provides content for analysis:

### 1. Quick Assessment (15 seconds)
- Identify content type (article/paper/guide/opinion/case study)
- Check if user specified depth level or frameworks
- Note user's stated goal (problem-solving/learning/writing/decision/curiosity)

### 2. Initialize Analysis (conversationally)

Ask brief orientation questions if unclear:
- "What's your main goal?" (problem-solving/learning/writing/decision/curiosity)
- "How deep?" (quick 15min / standard 30min / deep 60min / research 120min+)
- "Any specific frameworks?" (or auto-suggest based on content type)

**Default if user doesn't specify**: Level 2 (Standard, 30min), auto-select frameworks

See `references/guides/framework_selection.md` for auto-selection rules by content type.

### 3. Conduct Analysis

**Always start with structural understanding:**
- Extract core thesis (1 sentence)
- Apply SCQA framework (`references/frameworks/quick/scqa.md`)
- Run 5W2H completeness check (`references/frameworks/quick/5w2h.md`)

**Then apply frameworks based on depth level:**

- **Level 1** (15min): SCQA + 5W2H → Top 3 insights + 1 action
- **Level 2** (30min): Add Critical Thinking + Inversion
- **Level 3** (60min): Add Systems Thinking
- **Level 4** (120min+): Add cross-source comparison via web_search

Load framework reference files as needed. See detailed workflow in `references/guides/workflow_guide.md`.

### 4. Generate Tailored Output

Format output based on user's stated goal:
- **Problem-solving**: Solutions + action plan + risk mitigation
- **Learning**: Concept notes + verification questions
- **Writing**: Arguments + evidence + quotes + critical analysis
- **Decision-making**: Scenario analysis + recommendation
- **Curiosity**: Key insights + interesting patterns + rabbit holes

See `references/templates/output_formats.md` for templates.

### 5. Knowledge Activation

Always end with:
- 🎯 Top 3 takeaways (insight + why it matters + one action each)
- 💡 Quick win (one thing to try in next 24 hours)
- 🔗 Next steps (to deepen or apply)
- 🧭 Frameworks used (checklist of what was applied)

### 6. Adapt to User Signals

Throughout conversation, read signals and adjust:
- User wants conciseness → Switch to Level 1 mode
- User challenges analysis → Lean into Critical Thinking + Inversion
- User asks "how to use" → Focus on action plan
- User wants multiple views → Apply Critical Thinking from different angles
- User mentions risks → Apply Inversion immediately
- User asks about connections → Use Systems Thinking

See `references/guides/interaction_guide.md` for detailed interaction patterns.

## Analysis Depth Levels

| Level | Time | Frameworks | Output |
|-------|------|-----------|---------|
| **Level 1 (Quick)** | 15min | SCQA + 5W2H | Structure + gaps + top 3 insights + 1 action |
| **Level 2 (Standard)** | 30min | + Critical Thinking + Inversion | Argument evaluation + risk analysis |
| **Level 3 (Deep)** | 60min | + Systems Thinking | Relationship mapping + leverage points |
| **Level 4 (Research)** | 120min+ | + Cross-source comparison | Multi-article synthesis + integrated view |

## Framework Arsenal

### Level 1: Quick Analysis (15 min)
- 📋 **SCQA** - Structure thinking → `references/frameworks/quick/scqa.md`
- 🔍 **5W2H** - Completeness check → `references/frameworks/quick/5w2h.md`

### Level 2: Standard Analysis (30 min)
- 🎯 **Critical Thinking** - Argument evaluation → `references/frameworks/standard/critical_thinking.md`
- 🔄 **Inversion** - Risk identification → `references/frameworks/standard/inversion.md`

### Level 3: Deep Analysis (60 min)
- 🔗 **Systems Thinking** - Relationship mapping → `references/frameworks/deep/systems_thinking.md`

### Level 4: Research Analysis (120 min+)
- 📊 **Cross-Source Comparison** - Multi-article synthesis → `references/templates/comparison_matrix.md`

## Quality Standards

Every analysis must:
- ✅ Stay faithful to original content (no misrepresentation)
- ✅ Distinguish facts from opinions
- ✅ Provide concrete examples from the text
- ✅ Apply frameworks appropriately (not force-fit)
- ✅ Connect to user's stated goal and context
- ✅ End with specific, actionable steps
- ✅ Cite specific sections (paragraph numbers, quotes)

Avoid:
- ❌ Overwhelming with all frameworks (respect depth level)
- ❌ Academic jargon without explanation
- ❌ Analysis without application
- ❌ Verbatim copying (synthesize instead)
- ❌ Superficial framework application

See full quality checklist in `references/guides/quality_standards.md`.

## Reference Files

### Guides (How to use this skill)
- **Workflow**: `references/guides/workflow_guide.md` - Complete Step 1-5 process
- **Framework selection**: `references/guides/framework_selection.md` - When to use which framework
- **Interaction**: `references/guides/interaction_guide.md` - How to adapt to user signals
- **Quality**: `references/guides/quality_standards.md` - Standards and checklist

### Frameworks (Thinking models)
- **Quick**: `references/frameworks/quick/` - SCQA, 5W2H (Level 1, 15min)
- **Standard**: `references/frameworks/standard/` - Critical Thinking, Inversion (Level 2, 30min)
- **Deep**: `references/frameworks/deep/` - Systems Thinking (Level 3, 60min)

### Templates (Output formats)
- **Formats**: `references/templates/output_formats.md` - 8 output format templates
- **Comparison**: `references/templates/comparison_matrix.md` - Cross-source analysis template

## Progressive Disclosure Design

This skill uses three-level loading:
1. **Metadata** (always loaded): Name + description (~100 words)
2. **SKILL.md** (loaded when triggered): Usage guide (~150 lines)
3. **References** (loaded as needed): Detailed frameworks and guides

Load reference files only when:
- User chooses deeper analysis level
- Specific framework is requested or needed
- Detailed guidance required for complex situations

This keeps context efficient while providing comprehensive capabilities.

## Advanced Usage

### Custom Framework Combinations
Users can request specific combinations:
- "Use SCQA + Inversion" - Structure with risk analysis
- "Apply Critical Thinking + Systems Thinking" - Quality check with relationship mapping
- "5W2H + Critical Thinking" - Completeness + quality check

### Iterative Deepening
Start light, offer to go deeper:
- After Level 1: "Want to go deeper on any part?"
- Mid-analysis: "Should we apply [X framework] to explore this?"
- Based on engagement: Progressively add frameworks

### Domain-Specific Optimization
Auto-optimize for content type (see `framework_selection.md`):
- **Business/Strategy**: SCQA + Inversion + Systems Thinking
- **Technical/Research**: 5W2H + Critical Thinking + Systems Thinking
- **Personal Development**: SCQA + Inversion + Critical Thinking
- **Decision-Making**: Inversion + SCQA + Systems Thinking
- **Creative**: SCQA + Critical Thinking + Systems Thinking

---

**Remember**: The goal is insight and action, not framework completion. Use frameworks as tools to reveal understanding, not as checklists to complete. Quality of thinking > quantity of frameworks applied.

**Progressive approach**: Start with what user needs, offer more depth as they engage. Read signals, adapt accordingly.
