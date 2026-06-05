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

## Local Scholar Taste Extractor

This repo also includes a local, offline-first extractor that turns one scholar's PDFs into copy/paste research skill cards.

Core output contract:

- `data/raw/<scholar-slug>/` contains source PDFs and is ignored by git.
- `data/processed/<scholar-slug>/` contains machine-readable diagnostics and is ignored by git.
- `scholars/<scholar-slug>/README.md` is the generated public scholar page for local experiments.

Install the core profile:

```bash
bash scripts/install.sh core
```

Run extraction without external services:

```bash
python scripts/extract_scholar_taste.py \
  --scholar-name "Jane Doe" \
  --input-dir data/raw/jane-doe
```

Optional local GROBID parsing:

```bash
docker run --rm --init -p 8070:8070 grobid/grobid:0.9.0-crf

python scripts/extract_scholar_taste.py \
  --scholar-name "Jane Doe" \
  --input-dir data/raw/jane-doe \
  --grobid-url http://localhost:8070
```

The extractor is rule-first and auditable: it looks for repeated gap framing, aim language, method and evidence logic, credibility checks, and critical boundaries. It does not infer research taste from topic words alone.

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

## Copy/Paste Scholar Skills

The repo now includes a generated scholar-skill layer:

```text
skills/by-scholar/
├── economists/
└── finance-scholars/
```

Each generated skill is designed to be copied directly into a research memo, AI prompt, self-review checklist, or project design note. The skill cards are extracted from scholars' observable paper patterns: question choice, empirical/theoretical tests, mechanism discipline, and abstract/introduction framing.

Current generated layer:

- 41 ready-to-draft scholars
- 124 copy/paste scholar-derived skill cards
- progress README files at the top of each scholar type folder
- upload-needed scholars kept unfinished until papers are provided

## Simplified Page Rule

To keep the repo easy to browse:

- one scholar = one folder with one `README.md`;
- all scholar-derived skills live as sections inside that scholar README;
- one journal/perspective/research-step = one folder with one `README.md`;
- separate per-skill files are used only for general skill categories, not for scholar-specific skills.
