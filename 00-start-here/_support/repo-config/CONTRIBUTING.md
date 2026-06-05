# Contributing

Contributions should strengthen the book rather than add more visible folders. If you add a new reader-facing page, place it inside one of the numbered chapters from `00` to `05`. If you add scripts, templates, generated data, or archival support material, place it under `00-start-here/_support/` so the public reading path remains clean.

A good contribution reads like a chapter paragraph, not a loose note. Prefer prose that explains the judgment behind a research move. Tables and diagrams are welcome when they clarify structure, but a page should not become a collection of unexplained bullet points.

Before pushing, run:

```bash
python3 00-start-here/_support/scripts/check_repo.py
pytest -q 00-start-here/_support/tests
```

When improving scholar pages, check the skill against representative papers. A skill should be transferable, supported by repeated patterns, and bounded by a clear warning about when imitation would become bad taste.
