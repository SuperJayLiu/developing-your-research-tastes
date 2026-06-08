# Nobel Open-Access Evidence Cache

This folder records legal source material for Nobel-linked research taste extraction. The PDFs themselves are downloaded locally into `pdfs/` and ignored by Git so the public repository does not become a binary archive.

The first download target is official Nobel material: prize lectures, lecture slides, popular information, and advanced scientific background PDFs from NobelPrize.org. These sources are safe evidence anchors for understanding a laureate's recognized contribution. They are not a substitute for reading canonical journal papers, but they provide a clean starting point before collecting author-hosted or working-paper versions of specific articles.

Run the downloader from the repository root:

```bash
python3 00-start-here/_support/scripts/download_nobel_open_access.py
```

The script writes a machine-readable manifest to `download_manifest.json`. Each entry records the year, laureate, source type, URL, local file path, byte count, and SHA-256 hash.

Do not add paywalled journal PDFs here. If a paper is not openly hosted by the author, NobelPrize.org, a university, NBER/SSRN/RePEc/arXiv, or another legitimate open source, record a citation and DOI rather than storing the PDF.
