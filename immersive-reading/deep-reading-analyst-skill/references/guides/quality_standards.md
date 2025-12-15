# Quality Standards

This document defines the quality standards for deep reading analysis. Use this as a checklist before delivering any analysis.

## Core Quality Principles

### 1. Faithfulness to Original Content

**Standard:** Never misrepresent the source material.

**Checklist:**
- [ ] Quotes are accurate and properly attributed
- [ ] Author's arguments are represented fairly, even if flawed
- [ ] Context is preserved (no cherry-picking)
- [ ] Paraphrases maintain original meaning
- [ ] Clear distinction between author's views and your analysis

**Common violations:**
- ❌ Exaggerating claims for effect
- ❌ Removing qualifying language ("might" → "will")
- ❌ Attributing your inferences to the author
- ❌ Presenting speculation as stated fact

**Example - Bad:**
```
"The author claims that remote work destroys productivity."
```
[When article actually said: "Some studies suggest remote work may reduce productivity in certain contexts"]

**Example - Good:**
```
"The author argues that remote work 'may reduce productivity in certain contexts,'
citing [specific studies]. However, they acknowledge this isn't universal."
```

---

### 2. Fact vs. Opinion Distinction

**Standard:** Always distinguish factual claims from opinions/interpretations.

**Checklist:**
- [ ] Factual claims are labeled as "data," "evidence," "research shows"
- [ ] Opinions are labeled as "argument," "claims," "suggests," "believes"
- [ ] Your analysis is clearly marked as interpretation
- [ ] Speculative elements are explicitly flagged

**Signal words:**

**Facts/Evidence:**
- "The data shows..."
- "According to [source]..."
- "Measured results indicate..."

**Opinions/Arguments:**
- "The author argues..."
- "They claim..."
- "The article suggests..."

**Your Analysis:**
- "My interpretation..."
- "From a [framework] perspective..."
- "This could be understood as..."

---

### 3. Concrete Examples Required

**Standard:** Every abstract insight must be grounded in specific examples.

**Checklist:**
- [ ] Key insights include specific examples from the text
- [ ] Action items are concrete and measurable
- [ ] Frameworks applied show specific application, not just theory
- [ ] Paragraph/section numbers cited for important points

**Example - Bad:**
```
"The article has some good ideas about productivity."
```

**Example - Good:**
```
"The article presents a specific productivity technique: 'time-blocking in 90-minute
intervals' (paragraph 12), based on ultradian rhythm research. Example given:
Author blocks 9:00-10:30 AM for deep work, takes 15-min break, repeats."
```

---

### 4. Appropriate Framework Application

**Standard:** Use frameworks to reveal insights, not to check boxes.

**Checklist:**
- [ ] Frameworks chosen are genuinely useful for this content
- [ ] Application goes deep, not just surface-level
- [ ] Insights emerge from framework, not forced into it
- [ ] Multiple frameworks reveal different angles (not redundant)
- [ ] User can see why each framework was valuable

**Red flags:**
- ❌ Using all frameworks on every article (overkill)
- ❌ Superficial application ("White hat: facts exist")
- ❌ Frameworks contradict or repeat each other
- ❌ User doesn't understand why framework was used

**Example - Bad (forced):**
```
"Applying Systems Thinking: This how-to article about baking bread forms a system."
```
[Systems Thinking adds no value to a simple linear process]

**Example - Good (appropriate):**
```
"Applying Systems Thinking: The article describes urban planning where
traffic patterns (Variable A) influence business locations (Variable B),
which influences housing demand (Variable C), which reinforces traffic patterns.
This creates a reinforcing feedback loop. Leverage point: Public transit
investment could break the cycle."
```

---

### 5. User Context Connection

**Standard:** Connect insights to the user's situation when possible.

**Checklist:**
- [ ] Recalled user's stated goal (problem-solving, learning, etc.)
- [ ] Action items relate to their context
- [ ] Examples relevant to their domain (if mentioned)
- [ ] Language level matches their expertise
- [ ] Output format fits their stated need

**Example - Bad (generic):**
```
"This insight is important. You should think about it."
```

**Example - Good (personalized):**
```
"Since you're a product manager trying to improve team collaboration (your stated goal),
this insight about 'asynchronous decision-making' directly applies. You could:

Action: In next sprint planning, try the '5-whys async' technique the article describes
(paragraph 18) where team members document reasoning before the meeting.

Why it fits your context: Your team is distributed across timezones, making
real-time collaboration difficult."
```

---

### 6. Actionable Steps Required

**Standard:** Every analysis must end with concrete next steps.

**Checklist:**
- [ ] At least 1-3 immediate actions provided
- [ ] Actions are specific (not "think about this")
- [ ] Actions have clear success criteria when possible
- [ ] "Quick win" action doable in 24 hours
- [ ] Actions scaled to user's depth level (don't overwhelm)

**Specificity test:**

**Bad (vague):**
- "Apply this framework"
- "Think about these ideas"
- "Consider using this approach"

**Good (specific):**
- "In tomorrow's standup, ask each team member the SCQA questions about their blockers"
- "This week, spend 15 minutes mapping the feedback loops in your sales process using the template I provided"
- "Before your next decision meeting, use Inversion to list the top 3 ways this could fail"

---

### 7. Proper Citations

**Standard:** Reference specific parts of the source material.

**Checklist:**
- [ ] Important quotes include location (paragraph, section)
- [ ] Key arguments cite where they appear
- [ ] Data points reference source explicitly
- [ ] Multiple sources distinguished clearly (if Level 4)

**Example - Bad:**
```
"The article says productivity improves with breaks."
```

**Example - Good:**
```
"Section 3, paragraph 12: The article cites a Microsoft study showing
'productivity increased 23%' when workers took structured breaks every 90 minutes."
```

---

## Quality Checklist by Analysis Type

### Level 1 (Quick) - Minimum Standards

- [ ] SCQA framework properly applied
- [ ] 5W2H gaps identified (at least 2-3 key gaps)
- [ ] Top 3 insights are genuinely insights (not just summaries)
- [ ] 1 immediate action is specific and doable in 24 hours
- [ ] Core thesis accurately captured

**Time check:** Should deliver value in 15 minutes

---

### Level 2 (Standard) - Enhanced Standards

All Level 1 standards, plus:

- [ ] Critical thinking reveals at least 1-2 strengths AND weaknesses
- [ ] Logical fallacies identified by name and location (if any)
- [ ] Inversion analysis reveals risks not mentioned in article
- [ ] Failure modes include mitigation strategies
- [ ] Argument strength rated numerically (X/10) with justification

**Time check:** Should complete in 30 minutes

---

### Level 3 (Deep) - Rigorous Standards

All Level 2 standards, plus:

- [ ] Systems Thinking map shows relationships and feedback loops (if applicable)
- [ ] Leverage points identified for intervention
- [ ] Cross-framework insights identified (not just individual framework application)
- [ ] Each framework adds unique value (no redundancy)

**Time check:** Should complete in 60 minutes

---

### Level 4 (Research) - Scholarly Standards

All Level 3 standards, plus:

- [ ] 2-3 additional authoritative sources found and analyzed
- [ ] SCQA applied to each source
- [ ] Consensus vs. divergence clearly identified
- [ ] Source quality evaluated (authority, recency, bias)
- [ ] Integrated synthesis provided (not just comparison)
- [ ] Confidence level stated based on source agreement

**Time check:** Should complete in 120+ minutes

---

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Framework Overload

**Problem:** Using all frameworks on every article regardless of relevance.

**Fix:** Choose 2-3 frameworks that genuinely add value. Quality > quantity.

---

### ❌ Anti-Pattern 2: Academic Jargon

**Problem:** Using specialized terms without explanation.

**Bad:**
```
"The author commits the post hoc ergo propter hoc fallacy and exhibits
significant confirmation bias in their epistemological framework."
```

**Good:**
```
"The author makes a logical error: assuming that because B happened after A,
A caused B (like saying 'I wore my lucky shirt and won the game, so the
shirt caused the win'). They also cherry-pick evidence that supports their
conclusion while ignoring contradicting studies."
```

**Fix:** Explain before using specialized terms, or use plain language.

---

### ❌ Anti-Pattern 3: Analysis Without Application

**Problem:** Providing insights without connecting to user's life.

**Bad:**
```
"The article presents 5 frameworks for decision-making. They are:
1. [Framework 1 description]
2. [Framework 2 description]
..."
```

**Good:**
```
"The article presents 5 decision-making frameworks. For your specific
situation (choosing between two job offers), the most relevant is
[Framework 3]. Here's how to apply it:

Step 1: [Concrete action]
Step 2: [Concrete action]

This helps you because [specific benefit for user's context]."
```

**Fix:** Always ask "So what? How does this help the user?"

---

### ❌ Anti-Pattern 4: Verbatim Copying

**Problem:** Quoting large sections instead of synthesizing.

**Bad:**
```
"The article says: [500-word quote pasted]

This is important."
```

**Good:**
```
"The article's core argument (Section 2) is that [synthesis in your words].
The author supports this with three key pieces of evidence:

1. [Evidence 1 summarized] - Strength: Strong because [...]
2. [Evidence 2 summarized] - Strength: Moderate because [...]
3. [Evidence 3 summarized] - Strength: Weak because [...]

Key quote: '[1-2 sentence essential quote]' (paragraph 12)

This matters because [implication for user]."
```

**Fix:** Synthesize and explain. Use short quotes for key phrases only.

---

### ❌ Anti-Pattern 5: Superficial Framework Application

**Problem:** Mentioning frameworks without actually applying them deeply.

**Bad:**
```
"Applying Critical Thinking:
- There are some arguments in the article
- I think they're okay
- Maybe there are some issues
[etc.]"
```

**Good:**
```
"Applying Critical Thinking to the main argument:

**Claim**: "Remote work increases productivity by 30%"

**Evidence evaluation**:
- Study cited has n=50 (small sample)
- Only measures self-reported productivity (subjective)
- Timeframe is 2 weeks (too short for lasting conclusions)
- Strength: 3/10

**Logical issues**:
- Hasty generalization: Extrapolates from tech workers to all professions
- Cherry-picking: Ignores 3 contradicting studies mentioned in footnotes
- Confounding variables: Doesn't control for novelty effect

**Verdict**: Weak argument. Needs larger, objective study over longer period."
```

**Fix:** Go deep with concrete details specific to the content and user's situation.

---

## Final Quality Check

Before delivering analysis, ask yourself:

1. **Accuracy:** Did I represent the source fairly?
2. **Clarity:** Will the user understand this without confusion?
3. **Relevance:** Does this connect to their stated goal?
4. **Actionability:** Can they do something with this?
5. **Value:** Did I add insight beyond summarizing?
6. **Efficiency:** Did I respect their time and attention?

If any answer is "no," revise before delivering.

---

## Quality Escalation Ladder

### Minimum (Never go below this):
- Accurate summary of main points
- At least 1 actionable insight
- No misrepresentation of source

### Good (Level 1-2):
- Structured analysis with frameworks
- Multiple insights with examples
- Concrete action steps
- Critical evaluation

### Excellent (Level 3):
- Multi-perspective analysis
- Cross-framework insights
- Deep connection to user context
- Anticipates follow-up questions

### Outstanding (Level 4):
- Synthesizes multiple sources
- Reveals non-obvious patterns
- Generates novel applications
- Transforms understanding

---

## Remember

Quality isn't about using more frameworks or writing longer analysis.

**Quality is:**
- Accuracy in representation
- Clarity in communication
- Relevance to user's needs
- Actionability of insights
- Efficiency of delivery

**The best analysis is one that:**
1. The user trusts (faithful to source)
2. The user understands (clear)
3. The user can use (actionable)
4. The user is glad they read (valuable)

When in doubt, optimize for these four attributes.
