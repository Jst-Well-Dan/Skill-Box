# Deep Reading Analyst - Workflow Guide

This guide provides the complete step-by-step workflow for conducting deep reading analysis. Use this as the master reference for the analysis process.

## Step 1: Initialize Analysis

### Ask User Conversationally

Start every analysis by understanding the user's context:

1. **"What's your main goal for reading this?"**
   - Problem-solving (need practical solutions)
   - Learning (building knowledge)
   - Writing (research for article/paper)
   - Decision-making (evaluating options)
   - Curiosity (general interest)

2. **"How deep do you want to go?"**
   - Quick (15min) - Get core ideas fast
   - Standard (30min) - Understand and evaluate
   - Deep (60min) - Multi-perspective analysis
   - Research (120min+) - Comprehensive cross-source study

3. **"Any specific frameworks you'd like to use?"**
   - Let user request specific models
   - Or auto-suggest based on content type (see `framework_selection.md`)

### Default Behavior

If user doesn't specify preferences:
- **Default depth**: Level 2 (Standard - 30min)
- **Auto-select frameworks** based on content type
- Start analysis immediately without over-asking

## Step 2: Structural Understanding

**Always start here regardless of depth level.**

This foundation is critical before applying any thinking frameworks.

### Phase 2A: Basic Structure

Extract and present:

```markdown
📄 Content Type: [Article/Paper/Report/Guide/Book Chapter]
⏱️ Estimated reading time: [X minutes]
🎯 Core Thesis: [One sentence summary]

Structure Overview:
├─ Main Argument 1
│   ├─ Supporting point 1.1
│   └─ Supporting point 1.2
├─ Main Argument 2
│   ├─ Supporting point 2.1
│   └─ Supporting point 2.2
└─ Main Argument 3

Key Concepts: [3-5 terms with brief definitions]
```

**Tips:**
- Be precise with the core thesis - it's the anchor point
- Show hierarchical structure, not just a list
- Define specialized terms immediately

### Phase 2B: SCQA Analysis (Quick Framework)

Apply SCQA to every article (see `references/frameworks/quick/scqa.md` for details):

```markdown
## SCQA Structure

**S (Situation)**: [Background/context the article establishes]
**C (Complication)**: [Problem/challenge identified]
**Q (Question)**: [Core question being addressed]
**A (Answer)**: [Main solution/conclusion proposed]

📊 Structure Quality:
- Clarity: [★★★★☆]
- Logic flow: [★★★★★]
- Completeness: [★★★☆☆]
```

**Common issues:**
- Implicit situation (not stated clearly)
- Multiple complications (prioritize the main one)
- Question not explicitly asked (infer from content)

### Phase 2C: 5W2H Completeness Check

Quick scan using the 7 questions (see `references/frameworks/quick/5w2h.md`):

```markdown
## Information Completeness

✅ Well-covered: [What, Why, How]
⚠️  Partially covered: [Who, When]
❌ Missing: [Where, How much]

🔴 Critical gaps: [List 1-2 most important missing pieces]
```

**Don't skip this** - identifying gaps is often as valuable as understanding what's present.

## Step 3: Apply Thinking Models

Select based on user's depth level preference. Stack frameworks progressively.

### Level 1 (Quick - 15 min)

**Core frameworks**: Structure + SCQA + 5W2H Quick Check

**Output requirements:**
- SCQA breakdown
- Information gaps (from 5W2H)
- TOP 3 insights (actionable)
- 1 immediate action item

**Keep it tight** - this is speed mode for busy users.

### Level 2 (Standard - 30 min)

**Add frameworks**: Critical Thinking + Inversion

Load and apply:

**Critical Thinking** (`references/frameworks/standard/critical_thinking.md`):
- Argument quality assessment
- Logic flaw identification
- Evidence evaluation
- Alternative perspectives

**Inversion Thinking** (`references/frameworks/standard/inversion.md`):
- How to ensure failure? (reverse the advice)
- What assumptions if wrong?
- Missing risks
- Pre-mortem analysis

**Output format:**

```markdown
## Critical Analysis

### Argument Strength: [X/10]

Strengths:
- [Specific strength with example]
- [Specific strength with example]

Weaknesses:
- [Specific weakness with example]
- [Specific weakness with example]

Logical fallacies detected:
- [Name of fallacy]: [Where it appears]

## Inversion Analysis

🚨 How this could fail:
1. [Failure mode 1] → Mitigation: [Specific action]
2. [Failure mode 2] → Mitigation: [Specific action]

Missing risk factors:
- [Risk 1]: [Why it matters]
- [Risk 2]: [Why it matters]
```

### Level 3 (Deep - 60 min)

**Add frameworks**: Systems Thinking

This is where deep insight emerges through relationship mapping.

**Systems Thinking** (`references/frameworks/deep/systems_thinking.md`):
- Map causal relationships
- Identify feedback loops (reinforcing/balancing)
- Find leverage points

**Output format:**

```markdown
## Systems Analysis

### Systems Map:

```
[Element A] ──reinforces(+)──> [Element B]
      ↑                            |
      |                            |
   balances(-)                 reinforces(+)
      |                            |
      └──────────<─────────────────┘

Feedback loop type: [Reinforcing/Balancing]
Leverage point: [Where to intervene for maximum impact]
```

### Key Relationships:

1. **[Variable A] → [Variable B]**
   - Relationship type: [Reinforcing/Balancing]
   - Implication: [What this means]

2. **[Variable B] → [Variable C]**
   - Relationship type: [Reinforcing/Balancing]
   - Implication: [What this means]

### Leverage Points:

**High leverage**: [Where small changes create big impact]
**Low leverage**: [Where effort yields little result]
```

### Level 4 (Research - 120 min+)

**Add capability**: Cross-source comparison via web_search

**Process:**
1. Use web_search to find 2-3 related authoritative sources
2. Apply SCQA to each source
3. Load `references/templates/comparison_matrix.md`
4. Conduct systematic comparison
5. Synthesize integrated perspective

**Output format:**

```markdown
## Multi-Source Analysis

### Source 1: [Original article title]
- S-C-Q-A: [Brief summary]
- Key claim: [Main assertion]
- Evidence strength: [X/10]

### Source 2: [Found article title + URL]
- S-C-Q-A: [Brief summary]
- Key claim: [Main assertion]
- Evidence strength: [X/10]

### Source 3: [Found article title + URL]
- S-C-Q-A: [Brief summary]
- Key claim: [Main assertion]
- Evidence strength: [X/10]

## Synthesis

**Consensus** (what all sources agree): [Points of agreement]
**Divergence** (where they differ): [Key disagreements and why]
**Unique value** (what each contributes): [Distinctive insights per source]
**Integrated view** (synthesized perspective): [Your unified understanding]

**Confidence level**: [High/Medium/Low] based on source agreement
```

## Step 4: Synthesis & Output

Generate output tailored to the user's stated goal from Step 1.

### For Problem-Solving Goal

```markdown
## Applicable Solutions

[Extract 2-3 concrete methods from the content]

## Application Plan

**Your problem:** [Restate user's specific issue]
**Relevant insights:** [Key findings from analysis that apply]

**Action steps:**
1. [Specific action with timeline] - Success criteria: [...]
2. [Specific action with timeline] - Success criteria: [...]
3. [Specific action with timeline] - Success criteria: [...]

## Risk Mitigation (from Inversion Analysis)

**Potential failure points:**
- [Point 1] → Prevent by: [Specific preventive action]
- [Point 2] → Prevent by: [Specific preventive action]
```

### For Learning Goal

```markdown
## Learning Notes

**Core concepts** (explained simply):
1. **[Concept 1]**: [Definition] | Example: [...]
2. **[Concept 2]**: [Definition] | Example: [...]
3. **[Concept 3]**: [Definition] | Example: [...]

**Mental models gained:**
- **[Model name]**: [How it works] | Apply to: [Context]

**Connections to prior knowledge:**
- [This concept] relates to [something user likely knows]
- [This principle] is similar to [familiar example]

## Verification Questions

Test your understanding:
1. [Application question - can you use it?]
2. [Analysis question - can you break it down?]
3. [Evaluation question - can you judge it?]
```

### For Writing Reference Goal

```markdown
## Key Arguments & Evidence

**Main Argument 1:** [Summary]
- Evidence: [Specific citation with location]
- Strength: [Strong/Moderate/Weak] because [...]

**Main Argument 2:** [Summary]
- Evidence: [Specific citation with location]
- Strength: [Strong/Moderate/Weak] because [...]

## Quotable Insights

"[Quote 1]"
- Context: [Where it appears and what it supports]
- Use for: [When to cite this]

"[Quote 2]"
- Context: [Where it appears and what it supports]
- Use for: [When to cite this]

## Critical Analysis Notes

**Strengths** (for supporting your points):
- [Strength 1 with specific reference]

**Limitations** (for balanced discussion):
- [Limitation 1 with specific reference]

## Alternative Perspectives

**Different angle 1:** [What alternative perspective would say]
**Different angle 2:** [What alternative perspective would say]

## Gaps & Counterfactuals

What the article doesn't address:
- [Gap 1] - Why it matters: [...]
- [Gap 2] - Why it matters: [...]

Potential counter-arguments:
- [Counter-argument 1]
```

### For Decision-Making Goal

```markdown
## Decision Framework

**Options presented:** [A / B / C]

**Evaluation:**

From critical lens: [Argument quality for each option]
From risk lens (Inversion): [Failure modes for each option]
From systems lens: [Long-term implications and side effects]

## Decision Analysis

**Facts**:
- Option A: [Objective data]
- Option B: [Objective data]
- Option C: [Objective data]

**Risks**:
- Option A: [What could go wrong]
- Option B: [What could go wrong]
- Option C: [What could go wrong]

**Benefits**:
- Option A: [Upside potential]
- Option B: [Upside potential]
- Option C: [Upside potential]

**Recommendation**: [Synthesized advice with reasoning]

## Scenario Analysis (from Inversion)

**Option [X] - Most recommended:**
- Best case: [Optimistic outcome]
- Worst case: [Pessimistic outcome]
- Most likely: [Realistic expectation]
- Key assumption to validate: [Critical dependency]
```

### For General Curiosity Goal

Keep it engaging and insight-focused:

```markdown
## Most Interesting Insights

1. **[Surprising finding]**
   Why it's interesting: [...]
   Implication: [...]

2. **[Counter-intuitive point]**
   Why it's interesting: [...]
   Implication: [...]

3. **[Novel connection]**
   Why it's interesting: [...]
   Implication: [...]

## How This Changes My Understanding

Before reading: [Common assumption]
After reading: [New perspective]

## Rabbit Holes Worth Exploring

If this interested you, check out:
- [Related topic 1] because [...]
- [Related topic 2] because [...]
```

## Step 5: Knowledge Activation

**Always end with this** - it transforms passive reading into active learning.

```markdown
## 🎯 Immediate Takeaways (Top 3)

1. **[Insight 1]**
   Why it matters to you: [Personal relevance]
   One action: [Specific, time-bound, tiny]

2. **[Insight 2]**
   Why it matters to you: [Personal relevance]
   One action: [Specific, time-bound, tiny]

3. **[Insight 3]**
   Why it matters to you: [Personal relevance]
   One action: [Specific, time-bound, tiny]

## 💡 Quick Win

[One thing to try in next 24 hours - make it TINY and SPECIFIC]

Example: "In your next meeting, try [specific technique from article]"

## 🔗 Next Steps

**To deepen understanding:**
- [ ] Further reading: [If relevant specific resource]
- [ ] Apply framework X to your context: [Concrete example]
- [ ] Discuss with: [Who would provide valuable perspective]

**To apply knowledge:**
- [ ] Experiment: [Test concept in real context within 1 week]
- [ ] Teach: [Explain to someone else - best way to solidify]
- [ ] Combine: [Mix this idea with another concept you know]

## 🧭 Thinking Models Used

Show what frameworks were applied:

✅ SCQA ✅ 5W2H ✅ Critical Thinking ✅ Inversion ✅ Systems Thinking

[Check boxes for frameworks actually used in this analysis]
```

## Workflow Tips

### Efficiency Guidelines

- **Don't over-ask**: If user provides clear content and intent, start analyzing
- **Progressive depth**: Start light, offer to go deeper
- **Read signals**: User engagement indicates when to elaborate vs. wrap up
- **Reference, don't repeat**: Load reference files, apply them, don't reproduce them

### Quality Checkpoints

Before delivering analysis, verify:
- [ ] Stayed faithful to original content (no misrepresentation)
- [ ] Distinguished facts from opinions
- [ ] Provided concrete examples, not just abstractions
- [ ] Applied frameworks appropriately (not force-fit)
- [ ] Connected to user's context when possible
- [ ] Ended with actionable steps
- [ ] Cited specific sections (paragraphs, quotes)

### Common Pitfalls to Avoid

❌ **Overwhelming with all frameworks** - Respect the depth level chosen
❌ **Academic jargon overload** - Explain specialized terms simply
❌ **Analysis without application** - Always connect to user's life
❌ **Copying verbatim** - Synthesize and explain, don't quote extensively
❌ **Surface framework application** - Go deep with fewer models vs. shallow with many
❌ **Ignoring user's stated goal** - Output format must match their purpose

---

**Remember:** This workflow is a guide, not a rigid script. Adapt based on content type, user preferences, and contextual signals. The goal is insight and action, not checklist completion.
