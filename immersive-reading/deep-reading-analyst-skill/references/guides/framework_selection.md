# Framework Selection Guide

This guide helps you choose the most appropriate thinking frameworks based on content type, user goals, and analysis depth.

## Available Frameworks (5 Core)

| Framework | Purpose | Best For |
|-----------|---------|----------|
| **SCQA** | Structure extraction | Understanding article flow |
| **5W2H** | Completeness check | Finding information gaps |
| **Critical Thinking** | Argument evaluation | Assessing quality and logic |
| **Inversion** | Risk identification | Finding failure modes |
| **Systems Thinking** | Relationship mapping | Understanding connections |

---

## Auto-Selection by Content Type

When user doesn't specify frameworks, auto-suggest based on what you're analyzing:

### 📄 Strategy/Business Articles

**Best frameworks**: SCQA + Inversion + Systems Thinking

**Why:**
- SCQA maps business logic structure
- Inversion identifies strategic risks
- Systems Thinking reveals market dynamics

**Example triggers:**
- "How to grow your startup"
- "Product management strategies"
- "Market analysis of..."

---

### 📊 Research Papers

**Best frameworks**: 5W2H + Critical Thinking + Systems Thinking

**Why:**
- 5W2H checks methodological completeness
- Critical Thinking evaluates evidence quality
- Systems Thinking maps variable relationships

**Example triggers:**
- Academic papers with citations
- Scientific studies
- Technical reports

---

### 💡 How-to Guides / Tutorials

**Best frameworks**: SCQA + 5W2H

**Why:**
- SCQA checks if problem/solution is clear
- 5W2H ensures no steps are missing

**Example triggers:**
- "How to do X"
- "Step-by-step guide"
- "Tutorial on..."

---

### 🎯 Opinion Pieces / Essays

**Best frameworks**: Critical Thinking + Inversion

**Why:**
- Critical Thinking evaluates argument strength
- Inversion reveals unstated assumptions

**Example triggers:**
- Op-eds
- Personal essays
- Thought leadership posts

---

### 📈 Case Studies

**Best frameworks**: SCQA + Systems Thinking + Inversion

**Why:**
- SCQA extracts the narrative structure
- Systems Thinking reveals cause-effect chains
- Inversion identifies what could have gone wrong

**Example triggers:**
- Company success/failure stories
- Project post-mortems
- "How [Company] did [Thing]"

---

### 🗞️ News Articles

**Best frameworks**: 5W2H + Critical Thinking

**Why:**
- 5W2H checks journalistic completeness
- Critical Thinking identifies bias/missing context

**Example triggers:**
- Current events reporting
- Press releases
- News analysis

---

## Selection by User Goal

Override content-type defaults based on what user wants to achieve:

### Goal: Problem-Solving

**Prioritize**: Inversion + Critical Thinking + Systems Thinking

**Why:** Need risk awareness, quality evaluation, understanding relationships

### Goal: Learning / Understanding

**Prioritize**: SCQA + Systems Thinking + 5W2H

**Why:** Need clear structure, conceptual connections, complete picture

### Goal: Writing / Research

**Prioritize**: Critical Thinking + 5W2H + Comparison Matrix

**Why:** Need evidence evaluation, completeness check, source synthesis

### Goal: Decision-Making

**Prioritize**: Inversion + Critical Thinking + Systems Thinking

**Why:** Need risk analysis, quality assessment, understanding impact

### Goal: Curiosity / Exploration

**Prioritize**: Systems Thinking + Critical Thinking + SCQA

**Why:** Need connections, critical perspective, organized understanding

---

## Selection by Depth Level

Each level builds on previous ones (cumulative):

### Level 1: Quick (15 min)

**Included frameworks:**
- ✅ SCQA - Structure
- ✅ 5W2H - Completeness

**Output:** Fast understanding, identify gaps

---

### Level 2: Standard (30 min)

**Added frameworks:**
- ✅ Critical Thinking - Evaluate arguments
- ✅ Inversion - Identify risks

**Output:** Critical analysis, risk awareness

---

### Level 3: Deep (60 min)

**Added frameworks:**
- ✅ Systems Thinking - Relationship mapping

**Output:** Deep insights, integrated understanding

---

### Level 4: Research (120 min+)

**Added capability:**
- ✅ Cross-source Comparison - Multi-article synthesis

**Output:** Scholarly-level analysis, synthesized perspective

---

## Custom Framework Combinations

Users can explicitly request specific combinations:

### "SCQA + Inversion"
**Use case:** Understand structure while checking for risks
**Good for:** Business plans, strategy documents

### "Critical Thinking + Systems Thinking"
**Use case:** Quality evaluation with relationship mapping
**Good for:** Research papers, complex analysis

### "5W2H + Critical Thinking"
**Use case:** Completeness check + quality evaluation
**Good for:** Research papers, reports

### "Inversion + Systems Thinking"
**Use case:** Risk analysis with impact mapping
**Good for:** Decision-making, strategic planning

---

## Framework Loading Strategy

To manage context efficiently:

### Always Load (Baseline - Level 1)
- SCQA
- 5W2H

These are quick frameworks used in nearly every analysis.

### Load on Demand (Level 2)
- Critical Thinking
- Inversion

Only load when user reaches Standard depth or explicitly requests.

### Load Selectively (Level 3)
- Systems Thinking - Use for complex relationships

### Load for Research (Level 4)
- Comparison Matrix - Only for multi-source analysis

---

## Suggesting Frameworks Mid-Analysis

During conversation, proactively offer relevant frameworks:

### Trigger Patterns

**User challenges an argument:**
> "I notice some logical issues here. Should we apply **Critical Thinking** framework?"

**User asks about risks:**
> "Want me to use **Inversion Thinking** to identify failure modes?"

**User wants to understand connections:**
> "This has several moving parts - should we map it with **Systems Thinking**?"

**User wants completeness check:**
> "Should we run a **5W2H** analysis to see what's missing?"

**User wants structure:**
> "Let me apply **SCQA** to map out the article's structure."

---

## Framework Selection Decision Tree

```
User provides content
    ↓
Has user specified frameworks?
    ├─ YES → Use requested frameworks
    └─ NO → Continue
         ↓
What's the depth level?
    ├─ Level 1 → SCQA + 5W2H
    ├─ Level 2 → Add Critical Thinking + Inversion
    ├─ Level 3 → Add Systems Thinking
    └─ Level 4 → Add Cross-source Comparison
         ↓
What's the content type?
    ├─ Business → Emphasize SCQA + Inversion + Systems
    ├─ Research → Emphasize 5W2H + Critical + Systems
    ├─ How-to → Emphasize SCQA + 5W2H
    ├─ Opinion → Emphasize Critical + Inversion
    └─ Case Study → Emphasize SCQA + Systems + Inversion
         ↓
What's the user goal?
    ├─ Problem-solving → Prioritize Inversion + Critical
    ├─ Learning → Prioritize SCQA + Systems
    ├─ Writing → Prioritize Critical + 5W2H
    ├─ Decision → Prioritize Inversion + Systems
    └─ Curiosity → Prioritize Systems + Critical
         ↓
Apply selected frameworks
```

---

## Quick Reference Table

| Content Type | Primary Frameworks | Secondary Frameworks |
|--------------|-------------------|---------------------|
| Strategy/Business | SCQA, Inversion | Systems Thinking |
| Research Papers | 5W2H, Critical | Systems Thinking |
| How-to Guides | SCQA, 5W2H | Critical Thinking |
| Opinion Pieces | Critical, Inversion | SCQA |
| Case Studies | SCQA, Systems | Inversion |
| News | 5W2H, Critical | SCQA |

| User Goal | Primary Frameworks | Secondary Frameworks |
|-----------|-------------------|---------------------|
| Problem-solving | Inversion, Critical | Systems |
| Learning | SCQA, Systems | 5W2H |
| Writing | Critical, 5W2H | Comparison Matrix |
| Decision-making | Inversion, Systems | Critical |
| Curiosity | Systems, Critical | SCQA |

---

## Remember

- **Fewer, deeper > more, shallower**: Better to apply 2-3 frameworks thoroughly than all 5 superficially
- **User preference overrides all**: If user requests specific frameworks, honor that
- **Adapt mid-flight**: Start with auto-selection, offer alternatives based on what you discover
- **Signal clearly**: Always tell user which frameworks you're applying and why
