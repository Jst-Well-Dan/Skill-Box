# Interaction Guide

This guide defines how to interact with users during deep reading analysis - from questioning techniques to adapting based on user signals.

## Progressive Questioning Technique

Don't overwhelm users with all questions at once. Use a conversational, progressive approach.

### Initial Light Touch

**Start simple:**
```
"I'll help you analyze this article. What's your main goal?
(Understanding, problem-solving, research, decision-making, or just exploring?)"
```

**If user is vague or says "just help me understand it":**
→ Default to Level 2 (Standard), auto-select frameworks, start analyzing

**If user is specific:**
→ Adapt depth and frameworks to their stated need

### Progressive Depth Offering

**After delivering initial analysis:**
```
"Want to go deeper on any part? I can apply [framework X] to explore [specific aspect]."
```

**Examples:**
- "Should we do an inversion analysis to identify potential failure modes?"
- "Would you like me to apply mental models from economics and psychology to this?"
- "Want me to map out the system dynamics here?"

### Framework Suggestions

**Offer specific frameworks when relevant:**

```
"I notice this article makes several strong claims.
Want me to apply Critical Thinking framework to evaluate the argument quality?"
```

```
"This strategy has some risks not addressed in the article.
Should we use Inversion Thinking to identify what could go wrong?"
```

```
"Multiple perspectives would be valuable here.
Let's try Critical Thinking from different angles?"
```

---

## Reading User Signals

Adapt your approach based on what the user says and does:

### Signal: User wants conciseness

**Indicators:**
- "What's the main point?"
- "Give me the TL;DR"
- "I'm in a hurry"
- Short, fast responses from user

**Response:**
→ Use Level 1 (Quick mode)
→ Focus on SCQA breakdown
→ Provide top 3 insights only
→ Skip elaborate examples

---

### Signal: User challenges your analysis

**Indicators:**
- "I disagree because..."
- "What about [counterpoint]?"
- "That doesn't seem right"
- Critical questions

**Response:**
→ Lean into Critical Thinking
→ Apply Inversion to examine assumptions
→ Acknowledge alternative perspectives
→ Show your reasoning explicitly

---

### Signal: User wants practical application

**Indicators:**
- "How do I use this?"
- "What should I do with this information?"
- "How does this apply to my situation?"
- Mentions specific problem/context

**Response:**
→ Focus on practical application
→ Skip abstract frameworks, prioritize concrete steps
→ Generate specific action plan
→ Use Inversion to identify obstacles

---

### Signal: User wants multiple perspectives

**Indicators:**
- "What are different ways to look at this?"
- "Are there other viewpoints?"
- "How would [X person/field] see this?"
- Open-minded, exploratory tone

**Response:**
→ Apply Critical Thinking from multiple angles
→ Use Systems Thinking for different relationships
→ Present contrasting interpretations
→ Avoid premature conclusion

---

### Signal: User mentions risks

**Indicators:**
- "What could go wrong?"
- "What are the downsides?"
- "Is this safe/reliable?"
- Cautious language

**Response:**
→ Immediately apply Inversion Thinking
→ Use Critical Thinking on evidence quality
→ Identify unstated assumptions
→ Provide risk mitigation strategies

---

### Signal: User wants to understand connections

**Indicators:**
- "How does this relate to [X]?"
- "What's the big picture?"
- "How do these pieces fit together?"
- Systems-level questions

**Response:**
→ Use Systems Thinking
→ Map relationships and feedback loops
→ Show how concepts interconnect
→ Identify leverage points

---

### Signal: User is learning/studying

**Indicators:**
- "I'm trying to learn about..."
- "Can you explain [concept]?"
- "I don't understand [part]"
- Student-like questions

**Response:**
→ Use SCQA to build clear structure
→ Provide clear examples
→ Check understanding with questions
→ Connect to prior knowledge
→ Generate verification questions

---

### Signal: User is researching/writing

**Indicators:**
- "I'm writing about..."
- "I need to cite..."
- "What's the evidence for...?"
- Mentions sources, references

**Response:**
→ Apply Critical Thinking rigorously
→ Use 5W2H for completeness
→ Cite specific passages/paragraphs
→ Compare with other sources (Level 4)
→ Note strengths AND limitations

---

### Signal: User is deciding between options

**Indicators:**
- "Should I choose A or B?"
- "Which approach is better?"
- "Help me decide..."
- Evaluative questions

**Response:**
→ Use Critical Thinking for balanced evaluation
→ Apply Inversion for risk analysis
→ Use Systems Thinking for impact mapping
→ Provide scenario analysis
→ Give clear recommendation with reasoning

---

## Conversation Flow Patterns

### Pattern 1: Escalating Depth

```
User: "Analyze this article"
You: [Deliver Level 1 analysis]
User: [Engages, asks followup]
You: "Want to go deeper? I can apply [framework]..."
User: "Yes"
You: [Deliver Level 2/3 analysis]
```

**Principle:** Start light, escalate based on engagement

---

### Pattern 2: Framework Stacking

```
User: "Use SCQA to analyze this"
You: [Apply SCQA]
User: "What are the risks?"
You: "Let me add Inversion Thinking..." [Apply Inversion]
User: "How do these elements connect?"
You: "Adding Systems Thinking..." [Apply Systems Thinking]
```

**Principle:** Stack frameworks progressively as user requests

---

### Pattern 3: Iterative Refinement

```
User: "Analyze this article"
You: [Deliver analysis]
User: "But what about [aspect you missed]?"
You: "Great point - let me apply [appropriate framework] to that..."
User: [Satisfied or asks another question]
You: [Refine further or wrap up]
```

**Principle:** Iterate based on gaps user identifies

---

### Pattern 4: Goal Pivot

```
User: "Help me understand this article"
You: [Start learning-oriented analysis]
User: "Actually, I need to decide whether to implement this"
You: "Switching to decision-making mode..." [Pivot to Inversion + Critical Thinking]
```

**Principle:** Adapt when user's goal becomes clearer

---

## Phrasing Best Practices

### ✅ DO: Use clear, conversational language

**Good:**
```
"The article makes 3 main arguments. The first one is strong because [evidence],
but the second has a logical gap - it assumes [X] without proving it."
```

**Bad:**
```
"Upon examination of the argumentative structure, one observes a
multiplicity of claims, among which certain evidentiary deficiencies are manifest..."
```

---

### ✅ DO: Signal framework usage

**Good:**
```
"Let me apply the SCQA framework to map the structure:
S (Situation): [...]
C (Complication): [...]
Q (Question): [...]
A (Answer): [...]"
```

**Bad:**
```
[Just presents SCQA analysis without naming it or explaining why]
```

---

### ✅ DO: Offer choices, don't assume

**Good:**
```
"I can either:
1. Go deeper with mental models (30 more mins)
2. Give you an action plan based on what we have
3. Find related sources to compare

What would be most valuable?"
```

**Bad:**
```
"Now I'll apply 5 more frameworks..." [without asking]
```

---

### ✅ DO: Connect insights to user's context

**Good:**
```
"This insight is relevant because you mentioned [user's situation].
You could apply this by [specific action]."
```

**Bad:**
```
"This is an important insight." [generic, no personalization]
```

---

### ✅ DO: Acknowledge uncertainty

**Good:**
```
"The article doesn't provide enough data to fully evaluate this claim.
I'd rate the evidence strength at 4/10. To strengthen this, you'd need [specific info]."
```

**Bad:**
```
"The claim is true/false." [absolute statement without nuance]
```

---

## Adaptive Response Templates

### When user seems overwhelmed

```
"Let me simplify this. The core idea is: [one sentence].
The one thing you should do: [one action].

Want me to explain any specific part?"
```

---

### When user seems bored/disengaged

```
"What specific part interests you most?
Or what would make this analysis more useful for you?"
```

---

### When user is skeptical

```
"You're right to question that. Let me apply Critical Thinking framework
to examine this claim more rigorously:

[Present evidence evaluation, identify assumptions, note limitations]

What's your take on this after seeing the evidence?"
```

---

### When user wants more depth

```
"Great question - let's go deeper. I'll apply [Framework X] to explore this:

[Detailed analysis using appropriate framework]

This reveals [key insight]. See any other angles we should examine?"
```

---

### When user wants to wrap up

```
"Let me give you the essential takeaways:

🎯 Top 3 insights:
1. [Insight] → Action: [Tiny, specific]
2. [Insight] → Action: [Tiny, specific]
3. [Insight] → Action: [Tiny, specific]

💡 Quick win for next 24 hours: [One small thing to try]

Good to go, or want to discuss any of these?"
```

---

## Meta-Questions to Check Understanding

Periodically verify the analysis is valuable:

### Understanding check
```
"Does this explanation make sense? Want me to clarify any part?"
```

### Value check
```
"Is this the level of detail you're looking for, or should I go deeper/stay lighter?"
```

### Direction check
```
"We've covered [aspects]. What would be most useful to explore next?"
```

### Framework check
```
"Which thinking framework has been most helpful so far? Why?"
```

---

## Handling Edge Cases

### User provides very long content (10k+ words)

```
"This is substantial content. I recommend we:
1. Start with Level 1 analysis of the full piece
2. Then deep-dive into sections you find most valuable

Sound good? Or prefer a different approach?"
```

---

### User provides multiple articles at once

```
"I see [N] articles here. Two options:
1. Level 1 analysis of each, then pick one for deep-dive
2. Immediate Level 4 cross-source comparison

Which serves your goal better?"
```

---

### Article is behind paywall / can't access

```
"I don't have access to this content. Could you:
1. Paste the key sections you want analyzed, or
2. Paste the full text if you have access, or
3. Share the main arguments and I'll help analyze those?

What works for you?"
```

---

### User disagrees with article's premise

```
"I hear you - you're skeptical of the core argument. Let me:
1. Apply Critical Thinking to evaluate its logical strength
2. Use Inversion to identify what assumptions might be wrong
3. Suggest alternative perspectives

This way you'll have a solid critique. Want to proceed?"
```

---

### Content is in non-English language

```
"I can analyze content in [language]. Shall I:
1. Analyze in [original language] and present findings in [preferred language]
2. Or would you like me to translate key sections first?

What's your preference?"
```

---

## Remember

- **Read the room**: Adapt tone and depth to user engagement
- **Offer, don't impose**: Suggest frameworks, let user choose
- **Progressive disclosure**: Start light, deepen as user shows interest
- **Clear signaling**: Always explain what framework you're using and why
- **Personal relevance**: Connect insights to user's stated goals
- **Action-oriented**: End with concrete next steps, not just insights

The best analysis is one the user actually uses. Make it accessible, relevant, and actionable.
