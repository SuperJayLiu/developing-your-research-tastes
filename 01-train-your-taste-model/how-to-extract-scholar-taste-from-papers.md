# How to Extract Research Taste from Scholar Papers

This repo treats research taste as an observable pattern, not a personality trait.

A scholar's taste should be extracted from repeated choices in papers:

```text
question choice
    → model or empirical design
    → test or falsification logic
    → writing/framing move
    → transferable skill
    → critical boundary
```

## The Four-Part Extraction Lens

### 1. Question taste

Ask:

- What kinds of questions does this scholar repeatedly choose?
- Are the questions about anomalies, mechanisms, institutions, measurement, theory, policy, or markets?
- What makes the question important rather than merely clever?

Bad extraction:

> This scholar studies labor markets.

Better extraction:

> This scholar repeatedly chooses labor-market settings where a transparent institutional shock can test a controversial causal claim.

### 2. Design or theory taste

Ask:

- What kind of empirical design, model, or measurement move makes the question answerable?
- Does the paper rely on institutional variation, a benchmark model, a field experiment, a historical comparison, portfolio sorts, structural restrictions, or a new dataset?
- Why is this design/model a judgment choice rather than just a technique?

Bad extraction:

> This paper uses IV.

Better extraction:

> The paper uses an institutionally interpretable instrument and clearly states the complier group, so the method disciplines the causal claim.

### 3. Testing taste

Ask:

- What does the paper need to show for the claim to be believable?
- What alternative mechanisms are ruled out?
- What result would make the theory weaker?
- Does the paper test mechanisms, boundary conditions, heterogeneity, or only the main effect?

Good taste usually includes a clear failure condition.

### 4. Writing taste

Read the abstract and introduction carefully.

Ask:

- How does the paper make the reader care?
- How quickly does it move from broad motivation to exact contribution?
- Does the introduction state the puzzle, mechanism, design, and contribution?
- Does it overclaim relative to the evidence?

A good introduction often has this structure:

```text
Important phenomenon
    → unresolved puzzle
    → mechanism or design opportunity
    → evidence/model
    → contribution
    → scope and limits
```

## The Skill Extraction Formula

Use this sentence:

```text
This scholar teaches the skill of [research move] by using [design/model/test] to show [mechanism], while limiting the claim to [scope condition].
```

Example:

```text
This scholar teaches the skill of turning historical institutions into causal systems by using historically grounded variation to test whether institutional differences persistently affect economic outcomes, while limiting the claim to settings where rival geographic and selection channels can be addressed.
```

## Critical Standards

A skill is only useful if it is:

### Generalisable

It can be applied outside the original paper's topic.

### Justifiable

It is grounded in observable patterns across papers, not vague admiration.

### Critical

It includes boundaries, failure modes, and common overextensions.

## What Not to Do

Do not extract taste like this:

- "Use RCTs."
- "Study finance."
- "Write clearly."
- "Use big data."
- "Be like Fama."
- "Be like Acemoglu."

Extract taste like this:

- "Use field experiments as learning systems, not only evaluation devices."
- "Treat prices as model-dependent tests of information, risk, and mispricing."
- "Turn institutional details into causal variation."
- "Make measurement infrastructure part of the contribution."
- "Separate the factor construction from the factor interpretation."

## Paper-Level Worksheet

For every paper, fill this in:

```markdown
# Paper Taste Extraction

## Paper

## Scholar

## Broad question

## Exact research question

## Mechanism

## Design or model

## What is tested?

## What would weaken the claim?

## Abstract/introduction move

## Skill extracted

## Why the skill generalises

## Critical boundary

## Practice exercise
```

## Scholar-Level Worksheet

After reading 3 to 5 papers by one scholar, fill this in:

```markdown
# Scholar Taste Extraction

## Repeated question pattern

## Repeated design/model pattern

## Repeated testing pattern

## Repeated writing/framing pattern

## Skill 1

## Skill 2

## Skill 3

## Skill 4

## What not to copy

## What needs uploaded evidence before further extraction
```
