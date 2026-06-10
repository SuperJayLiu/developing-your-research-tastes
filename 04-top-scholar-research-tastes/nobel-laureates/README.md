# Nobel Laureates

This page is a bridge rather than a trophy case. Nobel recognition often makes a scholar's contribution easier to summarize, but research taste still has to be extracted from the papers themselves. The useful question is not why the scholar became famous. The useful question is what repeated research move became powerful enough to change how other scholars ask questions.

Read Nobel-linked work for the deep move: a new way to measure, a new way to model incentives, a new way to identify causal effects, a new way to interpret market prices, or a new way to connect institutions to outcomes. Then ask how that move can be practiced without pretending your project has the same scope.

```mermaid
flowchart LR
    A["Recognized contribution"] --> B["Underlying research move"]
    B --> C["Portable skill"]
    C --> D["Boundary against imitation"]
```

## Evidence Cache

The local evidence cache now starts with official NobelPrize.org PDFs rather than copyrighted journal files. The downloader stores PDFs under `00-start-here/_support/evidence/nobel-open-access/pdfs/`, which is ignored by Git, and records the auditable source list in `00-start-here/_support/evidence/nobel-open-access/download_manifest.json`.

This is the right first layer for Nobel-based skill work: prize lectures and official scientific background documents explain the recognized contribution and usually name the canonical papers. The next layer should be selective author-hosted or working-paper versions of those canonical papers, not bulk copies of paywalled PDFs.

## Taste Atlas

The completed first-pass taste synthesis is in [Nobel Research Taste Atlas](nobel-taste-atlas.md), with a compact index in [Nobel Skill Map](nobel-skill-map.md). The full reusable skills are written in [Nobel Detailed Skill Cards](nobel-detailed-skill-cards.md). The atlas summarizes each Economic Sciences laureate from the official Nobel motivation, the local Nobel PDF evidence where available, extracted text metadata, and a portable skill/boundary diagnosis.
