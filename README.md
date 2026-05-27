# Developing Your Research Tastes

A skill-based research taste curriculum for economics and finance.

This repository helps researchers train their personal **taste model**: the internal judgment system used to decide which questions are worth asking, which theories are promising, which evidence is convincing, and what makes a paper publishable.

The project is not a paper-summary archive. It is a structured system for turning great papers, scholars, journals, empirical designs, and research stories into reusable research skills.

## Core Idea

```text
Paper / Scholar / Journal / Research Step
        ↓
Research Move
        ↓
Transferable Skill
        ↓
Taste Principle
        ↓
Theory Development
        ↓
Theory Test
        ↓
Personal Taste Model Update
```

The goal is not only to read better papers.

The goal is to become the kind of researcher who can recognize, build, test, and communicate better ideas.

---

## The Five Pillars

### 1. Train Your Taste Model

Learn how to convert papers, scholars, journal examples, and research stories into reusable skills. Then use those skills to develop theories, derive predictions, test mechanisms, and update your own judgment.

Start here: [`01-train-your-taste-model/`](01-train-your-taste-model/)

### 2. General Features of Good Research Taste

Study what good research taste looks like across economics and finance: important questions, clean mechanisms, credible evidence, strong measurement, meaningful contribution, and clear writing.

Start here: [`02-general-features-of-good-research-taste/`](02-general-features-of-good-research-taste/)

### 3. Research Tastes of Top Economics and Finance Journals

Compare what different top journals tend to value in questions, evidence, theory, identification, contribution, and writing.

Start here: [`03-journal-research-tastes/`](03-journal-research-tastes/)

### 4. Research Tastes of Top Scholars

Extract transferable skills from leading economists, finance scholars, and Nobel laureates. Each scholar gets one page.

Start here: [`04-top-scholar-research-tastes/`](04-top-scholar-research-tastes/)

### 5. Research Taste by Research Step

Apply taste to each stage of a research project: idea generation, theory building, literature positioning, measurement, identification, empirical testing, mechanism testing, writing, and revision.

Start here: [`05-tastes-by-research-step/`](05-tastes-by-research-step/)

---

## Supporting Databases

The five pillars form the curriculum. These folders form the reusable database.

```text
skills/      reusable research moves
evidence/    papers, empirics, datasets, stories
practice/    drills and exercises
maps/        conceptual maps and navigation pages
templates/   standardized page formats
scripts/     repo helpers and checks
```

## Status Labels

Use these labels in front matter:

```yaml
status: seed | draft | reviewed | polished | canonical
open_access_status: ready-to-draft | partial | unfinished-upload-needed
confidence: low | medium | high
difficulty: beginner | intermediate | advanced
```

`ready-to-draft` means there appears to be enough public/open material to create a responsible first draft. `unfinished-upload-needed` means the scholar or topic is important, but the canonical material should be uploaded before expanding the page.

## How to Use This Repo

For learning:

1. Start with [`00-start-here/how-to-use-this-repo.md`](00-start-here/how-to-use-this-repo.md).
2. Read the taste model section.
3. Pick one research step or one scholar.
4. Extract one skill.
5. Use the skill to generate or test one theory.
6. Record the update in your personal taste log.

For building:

1. Add or improve a skill card in [`skills/`](skills/).
2. Add evidence in [`evidence/`](evidence/).
3. Add scholar pages in [`04-top-scholar-research-tastes/`](04-top-scholar-research-tastes/).
4. Use templates from [`templates/`](templates/).
5. Run `python3 scripts/check_repo.py` before pushing.

## Project Principle

Skills are the center.

Papers are evidence.  
Scholars are patterns.  
Journals are taste environments.  
Research steps are application contexts.  
Practice is how taste improves.


## Current Filled Scholar-Skill Batch

This version includes a first filled batch of scholar-derived research taste skills.

- **Filled scholar pages**: 33
- **Scholar-derived skill cards**: 132
- **Extraction standard**: generalisable, justifiable, and critical

The filled scholar pages live in:

```text
04-top-scholar-research-tastes/
```

The individual skill cards live in:

```text
skills/by-scholar/
```

The extraction method is documented here:

```text
01-train-your-taste-model/how-to-extract-scholar-taste-from-papers.md
```

A skill is not treated as valid just because a famous scholar used it. Each skill must be extracted from observable paper-level evidence:

1. the research question,
2. the empirical design or theory,
3. the test or falsification logic,
4. the abstract/introduction framing,
5. the scope condition or critical boundary.
