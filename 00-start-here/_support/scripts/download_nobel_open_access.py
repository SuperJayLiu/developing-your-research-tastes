#!/usr/bin/env python3
"""Download legal/open-access Nobel evidence PDFs.

The downloader intentionally targets official NobelPrize.org PDFs first:
lecture PDFs, lecture slide PDFs, popular information, and advanced
scientific background documents. It writes binaries to a local ignored cache
and writes a tracked manifest for auditability.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_DIR = ROOT / "00-start-here" / "_support" / "evidence" / "nobel-open-access"
DEFAULT_PDF_DIR = EVIDENCE_DIR / "pdfs"
DEFAULT_MANIFEST = EVIDENCE_DIR / "download_manifest.json"
NOBEL_API = "https://api.nobelprize.org/2.1/nobelPrizes?nobelPrizeCategory=eco&limit=100&sort=asc"
USER_AGENT = "research-taste-evidence-downloader/1.0"


def request(url: str, method: str = "GET", timeout: int = 20):
    return Request(url, method=method, headers={"User-Agent": USER_AGENT})


def fetch_json(url: str) -> dict:
    with urlopen(request(url), timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def ascii_slug(text: str) -> str:
    text = text.replace("ø", "o").replace("Ø", "O").replace("ł", "l").replace("Ł", "L")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"\b(jr|sr|sir|dr|prof)\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    parts = [p for p in text.split() if p not in {"von", "van", "de", "da", "of"}]
    return parts[-1] if parts else "unknown"


def laureate_name(laureate: dict) -> str:
    for key in ("knownName", "fullName"):
        value = laureate.get(key, {}).get("en")
        if value:
            return value
    return "Unknown Laureate"


def candidate_urls(year: int, slug: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []

    if year <= 2017:
        bases = [(2018, 6)]
    else:
        bases = [(year, 10), (year, 11), (year, 12), (year + 1, 1), (year + 1, 2)]

    for upload_year, month in bases:
        mm = f"{month:02d}"
        candidates.append((
            "lecture",
            f"https://www.nobelprize.org/uploads/{upload_year}/{mm}/{slug}-lecture.pdf",
        ))
        candidates.append((
            "lecture-slides",
            f"https://www.nobelprize.org/uploads/{upload_year}/{mm}/{slug}-lecture-slides.pdf",
        ))

    for month in (10, 11, 12):
        mm = f"{month:02d}"
        candidates.append((
            "advanced-background",
            f"https://www.nobelprize.org/uploads/{year}/{mm}/advanced-economicsciencesprize{year}.pdf",
        ))
        candidates.append((
            "popular-background",
            f"https://www.nobelprize.org/uploads/{year}/{mm}/popular-economicsciencesprize{year}.pdf",
        ))

    return candidates


def is_pdf_url(url: str) -> tuple[bool, int | None]:
    try:
        with urlopen(request(url, "HEAD"), timeout=15) as response:
            content_type = response.headers.get("content-type", "").lower()
            length = response.headers.get("content-length")
            return "pdf" in content_type, int(length) if length else None
    except HTTPError as error:
        if error.code == 405:
            return False, None
        return False, None
    except (TimeoutError, URLError):
        return False, None


def download_pdf(url: str, destination: Path) -> tuple[int, str]:
    with urlopen(request(url), timeout=45) as response:
        content_type = response.headers.get("content-type", "").lower()
        data = response.read()

    if "pdf" not in content_type and not data.startswith(b"%PDF"):
        raise ValueError(f"Not a PDF response: {url}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    return len(data), digest


def hash_existing_pdf(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Existing file does not look like a PDF: {path}")
    return len(data), hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--sleep", type=float, default=0.05, help="Delay between URL checks.")
    args = parser.parse_args()

    payload = fetch_json(NOBEL_API)
    prizes = payload.get("nobelPrizes", [])
    downloads: dict[str, dict] = {}
    missed: list[dict] = []
    checked_urls: set[str] = set()

    for prize in prizes:
        year = int(prize["awardYear"])
        laureates = prize.get("laureates", [])
        for laureate in laureates:
            name = laureate_name(laureate)
            slug = ascii_slug(name)
            found_for_laureate = False

            for source_type, url in candidate_urls(year, slug):
                if url in checked_urls:
                    continue
                checked_urls.add(url)
                time.sleep(args.sleep)

                ok, expected_bytes = is_pdf_url(url)
                if not ok:
                    continue

                filename = Path(url).name
                destination = args.pdf_dir / str(year) / slug / filename

                if destination.exists():
                    try:
                        size, digest = hash_existing_pdf(destination)
                    except ValueError as error:
                        missed.append({
                            "year": year,
                            "laureate": name,
                            "source_type": source_type,
                            "url": url,
                            "reason": str(error),
                        })
                        continue
                    downloads[url] = {
                        "year": year,
                        "laureate": name,
                        "slug": slug,
                        "source_type": source_type,
                        "url": url,
                        "local_path": str(destination.relative_to(ROOT)),
                        "bytes": size,
                        "expected_bytes": expected_bytes,
                        "sha256": digest,
                    }
                    found_for_laureate = True
                    continue

                try:
                    size, digest = download_pdf(url, destination)
                except (HTTPError, URLError, TimeoutError, ValueError) as error:
                    missed.append({
                        "year": year,
                        "laureate": name,
                        "source_type": source_type,
                        "url": url,
                        "reason": str(error),
                    })
                    continue

                downloads[url] = {
                    "year": year,
                    "laureate": name,
                    "slug": slug,
                    "source_type": source_type,
                    "url": url,
                    "local_path": str(destination.relative_to(ROOT)),
                    "bytes": size,
                    "expected_bytes": expected_bytes,
                    "sha256": digest,
                }
                found_for_laureate = True

            if not found_for_laureate:
                missed.append({
                    "year": year,
                    "laureate": name,
                    "source_type": "lecture-or-slides",
                    "url": f"https://www.nobelprize.org/prizes/economic-sciences/{year}/{slug}/lecture/",
                    "reason": "No direct official PDF found from candidate URL patterns.",
                })

    manifest = {
        "source": "NobelPrize.org official PDFs discovered from the Nobel API and public upload URL patterns.",
        "api_url": NOBEL_API,
        "pdf_dir": str(args.pdf_dir.relative_to(ROOT)),
        "download_count": len(downloads),
        "missed_count": len(missed),
        "downloads": sorted(downloads.values(), key=lambda x: (x["year"], x["slug"], x["source_type"], x["url"])),
        "missed": missed,
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Downloaded/recorded PDFs: {manifest['download_count']}")
    print(f"Missed candidate records: {manifest['missed_count']}")
    print(f"Manifest: {args.manifest.relative_to(ROOT)}")
    print(f"PDF cache: {args.pdf_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
