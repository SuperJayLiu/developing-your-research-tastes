# Developing Your Research Tastes

Local, offline-first tooling for extracting a scholar's repeated research and writing habits from a folder of PDFs and turning them into copy/pasteable research taste skill cards.

The repository is intentionally simple at the user-facing layer:

- `data/raw/<scholar-slug>/` contains source PDFs.
- `data/processed/<scholar-slug>/` contains machine-readable diagnostics.
- `scholars/<scholar-slug>/README.md` is the only public scholar-facing output.

## What This Produces

For each scholar, the extractor writes one Markdown page with:

- corpus summary and parser diagnostics
- a short explanation of the extraction method
- copy/paste research skill cards
- evidence anchors from the parsed papers
- critical boundaries for when not to imitate the habit
- exercises for practicing the habit

The goal is not topic modeling. The repo looks for repeated rhetorical and methodological behavior: how a scholar frames gaps, states aims, names evidence, foregrounds credibility checks, and limits claims.

## Install

Core mode is fully local and does not require transformers or paid APIs.

```bash
bash scripts/install.sh core
```

Enhanced mode installs optional local embedding dependencies. It still expects any models to be available locally.

```bash
bash scripts/install.sh enhanced
```

## Optional GROBID

GROBID is recommended for better scholarly PDF structure extraction. Run it locally:

```bash
docker run --rm --init -p 8070:8070 grobid/grobid:0.9.0-crf
```

The extractor automatically falls back to pure Python parsing if GROBID is unavailable or omitted.

## Usage

Place one scholar's PDFs under `data/raw/<scholar-slug>/`, then run:

```bash
python scripts/extract_scholar_taste.py \
  --scholar-name "Jane Doe" \
  --input-dir data/raw/jane-doe \
  --grobid-url http://localhost:8070
```

Without GROBID:

```bash
python scripts/extract_scholar_taste.py \
  --scholar-name "Jane Doe" \
  --input-dir data/raw/jane-doe
```

## Quality Checks

```bash
python scripts/check_repo.py
pytest -q
```

or:

```bash
bash scripts/run_tests.sh
```

## Design Principles

- Rule-first and auditable by default.
- No paid APIs.
- English-only first release.
- Deterministic outputs.
- One scholar folder, one README.
- Machine artifacts stay outside the public scholar folder.
- Skill cards require repeated support across papers unless marked low-support.

## Limitations

PDF extraction is imperfect because PDFs store layout more reliably than semantic paragraphs. Born-digital PDFs usually work better than scanned PDFs. Scanned PDFs need OCR, which is not included in the core profile.

Inferred taste is also provisional. Small corpora, coauthorship, journal conventions, and topic shifts can distort results. Treat generated cards as draft research aids until reviewed by a human.
