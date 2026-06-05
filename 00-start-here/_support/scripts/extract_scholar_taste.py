#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import requests
import yaml
from bs4 import BeautifulSoup

try:
    from pdfminer.high_level import extract_text as pdfminer_extract_text
except Exception:  # pragma: no cover - import guard for partial installs
    pdfminer_extract_text = None

try:
    from pypdf import PdfReader
except Exception:  # pragma: no cover - import guard for partial installs
    PdfReader = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEXICONS = ROOT / "configs" / "lexicons.yml"

SECTION_ALIASES = {
    "abstract": "abstract",
    "introduction": "introduction",
    "background": "introduction",
    "literature": "introduction",
    "related work": "introduction",
    "method": "methods",
    "methods": "methods",
    "methodology": "methods",
    "data": "methods",
    "empirical strategy": "methods",
    "model": "methods",
    "results": "results",
    "findings": "results",
    "analysis": "results",
    "discussion": "discussion",
    "conclusion": "discussion",
    "conclusions": "discussion",
    "limitations": "discussion",
}


@dataclass
class PaperRecord:
    paper_id: str
    title: str
    source_pdf: str
    parser_mode: str
    sections: dict[str, str]
    references: list[str]


class SimpleSentence:
    def __init__(self, text: str) -> None:
        self.text = text


class SimpleDoc:
    def __init__(self, text: str) -> None:
        parts = re.split(r"(?<=[.!?])\s+", text)
        self.sents = [SimpleSentence(part.strip()) for part in parts if part.strip()]


class SimpleNLP:
    def __call__(self, text: str) -> SimpleDoc:
        return SimpleDoc(text)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "scholar"


def load_lexicons(path: Path = DEFAULT_LEXICONS) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): [str(item).lower() for item in v] for k, v in data.items()}


def load_nlp(model_name: str):
    try:
        import spacy
    except Exception:
        return SimpleNLP()

    try:
        nlp = spacy.load(model_name, disable=["ner", "tagger", "lemmatizer"])
    except Exception:
        nlp = spacy.blank("en")
    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")
    return nlp


def pdf_text_with_pypdf(pdf_path: Path) -> str:
    if PdfReader is None:
        return ""
    reader = PdfReader(str(pdf_path))
    parts: list[str] = []
    for page in reader.pages:
        try:
            parts.append(page.extract_text() or "")
        except Exception:
            continue
    return "\n".join(parts)


def extract_plain_text(pdf_path: Path) -> str:
    text = ""
    if pdfminer_extract_text is not None:
        try:
            text = pdfminer_extract_text(str(pdf_path)) or ""
        except Exception:
            text = ""
    if len(text.strip()) < 500:
        text = pdf_text_with_pypdf(pdf_path)
    return normalize_text(text)


def normalize_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def title_from_text(text: str, fallback: str) -> str:
    for line in text.splitlines():
        cleaned = line.strip()
        if 8 <= len(cleaned) <= 180 and not cleaned.lower().startswith(("abstract", "introduction")):
            return cleaned
    return fallback


def recover_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = defaultdict(list)
    current = "body"
    heading_pattern = re.compile(
        r"^\s*(?:\d+(?:\.\d+)*\s+)?(abstract|introduction|background|literature|related work|"
        r"method|methods|methodology|data|empirical strategy|model|results|findings|analysis|"
        r"discussion|conclusion|conclusions|limitations)\s*$",
        re.IGNORECASE,
    )
    for raw_line in text.splitlines():
        line = raw_line.strip()
        match = heading_pattern.match(line)
        if match:
            current = SECTION_ALIASES[match.group(1).lower()]
            continue
        if line:
            sections[current].append(line)

    result = {name: "\n".join(parts).strip() for name, parts in sections.items() if parts}
    if "abstract" not in result:
        abstract_match = re.search(r"\babstract\b(.{200,2500}?)(?:\n\s*\bintroduction\b|\n\s*1\s+)", text, re.I | re.S)
        if abstract_match:
            result["abstract"] = normalize_text(abstract_match.group(1))
    if not any(key in result for key in ("abstract", "introduction", "methods", "results", "discussion")):
        result["body"] = text
    return result


def extract_fallback(pdf_path: Path) -> PaperRecord:
    text = extract_plain_text(pdf_path)
    if not text:
        raise ValueError(f"No extractable text found in {pdf_path}")
    digest = hashlib.sha1(str(pdf_path).encode("utf-8")).hexdigest()[:12]
    return PaperRecord(
        paper_id=digest,
        title=title_from_text(text, pdf_path.stem),
        source_pdf=str(pdf_path),
        parser_mode="fallback",
        sections=recover_sections(text),
        references=[],
    )


def extract_with_grobid(pdf_path: Path, grobid_url: str) -> PaperRecord:
    endpoint = grobid_url.rstrip("/") + "/api/processFulltextDocument"
    with pdf_path.open("rb") as handle:
        response = requests.post(
            endpoint,
            files={"input": (pdf_path.name, handle, "application/pdf")},
            data={"consolidateHeader": "0", "consolidateCitations": "0", "includeRawCitations": "1"},
            timeout=60,
        )
    response.raise_for_status()
    tei = response.text
    return parse_grobid_tei(tei, pdf_path)


def parse_grobid_tei(tei: str, pdf_path: Path) -> PaperRecord:
    soup = BeautifulSoup(tei, "xml")
    title_node = soup.find("title", {"type": "main"}) or soup.find("title")
    title = title_node.get_text(" ", strip=True) if title_node else pdf_path.stem
    sections: dict[str, list[str]] = defaultdict(list)

    abstract = soup.find("abstract")
    if abstract:
        sections["abstract"].append(abstract.get_text(" ", strip=True))

    for div in soup.find_all("div"):
        head = div.find("head")
        heading = head.get_text(" ", strip=True).lower() if head else ""
        section = "body"
        for alias, normalized in SECTION_ALIASES.items():
            if alias in heading:
                section = normalized
                break
        text = div.get_text(" ", strip=True)
        if text:
            sections[section].append(text)

    references = [bibl.get_text(" ", strip=True) for bibl in soup.find_all("biblStruct")]
    digest = hashlib.sha1(str(pdf_path).encode("utf-8")).hexdigest()[:12]
    return PaperRecord(
        paper_id=digest,
        title=title,
        source_pdf=str(pdf_path),
        parser_mode="grobid",
        sections={name: normalize_text("\n".join(parts)) for name, parts in sections.items()},
        references=references,
    )


def sentences_by_section(paper: PaperRecord, nlp) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for section, text in paper.sections.items():
        doc = nlp(text[:900_000])
        result[section] = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 20]
    return result


def sentence_has_cue(sentence: str, cues: list[str]) -> bool:
    lower = sentence.lower()
    return any(cue in lower for cue in cues)


def analyze_paper(
    paper: PaperRecord,
    nlp,
    lexicons: dict[str, list[str]] | None = None,
    max_evidence: int = 2,
) -> dict[str, Any]:
    lexicons = lexicons or load_lexicons()
    by_section = sentences_by_section(paper, nlp)
    signals: dict[str, list[dict[str, str]]] = defaultdict(list)

    section_to_signal = {
        "abstract": ["aim", "method", "boundary"],
        "introduction": ["gap", "aim"],
        "methods": ["method"],
        "results": ["credibility"],
        "discussion": ["boundary"],
        "body": ["gap", "aim", "method", "credibility", "boundary"],
    }

    for section, sentences in by_section.items():
        candidate_signals = section_to_signal.get(section, ["gap", "aim", "method", "credibility", "boundary"])
        for sentence in sentences:
            for signal in candidate_signals:
                if len(signals[signal]) >= max_evidence:
                    continue
                if sentence_has_cue(sentence, lexicons.get(signal, [])):
                    signals[signal].append({"section": section, "snippet": sentence})

    return {
        "paper_id": paper.paper_id,
        "title": paper.title,
        "source_pdf": paper.source_pdf,
        "parser_mode": paper.parser_mode,
        "section_names": sorted(paper.sections),
        "signals": dict(signals),
    }


def support_label(ratio: float, paper_count: int) -> str:
    if paper_count < 4:
        return "draft-low-support"
    if ratio >= 0.6:
        return "high"
    if ratio >= 0.35:
        return "medium"
    return "low"


def base_cards() -> dict[str, dict[str, str]]:
    return {
        "gap": {
            "title": "Frame the contribution by locating the gap before the claim",
            "skill": "Before stating your main claim, name the specific gap, contrast, or unresolved tension that makes the claim necessary.",
            "prompt": "Review my introduction. Have I made the gap precise before presenting the contribution, or am I asking the reader to care too early?",
            "boundary": "Do not manufacture a gap by flattening prior work; the contrast must be specific and fair.",
            "exercise": "Rewrite one introduction paragraph so the gap appears before the main contribution sentence.",
        },
        "aim": {
            "title": "State the research aim in direct action language",
            "skill": "Use explicit aim language so readers can quickly see what the paper asks, studies, examines, or shows.",
            "prompt": "Review my abstract and introduction. Can a reader identify the research question and main action of the paper in one pass?",
            "boundary": "Do not overstate the aim as a solved result when the design only supports a narrower claim.",
            "exercise": "Write three one-sentence versions of the paper aim, then choose the most precise one.",
        },
        "method": {
            "title": "Expose the evidence logic early",
            "skill": "Make the design, measurement, data construction, or source of identifying variation visible before the reader reaches technical detail.",
            "prompt": "Review my abstract and methods overview. Is the evidence logic visible enough for a skeptical reader to know what makes the claim credible?",
            "boundary": "Do not imitate strong design rhetoric when assumptions, measurement, or data quality cannot support it.",
            "exercise": "Rewrite the design paragraph so the reader sees the source of variation, measurement choice, and main comparison.",
        },
        "credibility": {
            "title": "Sell credibility with prioritized checks",
            "skill": "After the headline result, foreground the robustness, heterogeneity, placebo, or mechanism checks that most change whether the result is believable.",
            "prompt": "Review my results section. Have I prioritized the checks that actually matter, or listed tests without explaining their credibility value?",
            "boundary": "Do not bury the reader in unranked robustness exercises; foreground checks that alter interpretation.",
            "exercise": "Choose one headline result and list the three checks that most strengthen or weaken it.",
        },
        "boundary": {
            "title": "State where the argument should and should not travel",
            "skill": "Use the discussion to specify where the result, mechanism, or implication is likely to hold, where it may fail, and what remains out of scope.",
            "prompt": "Review my discussion. Have I stated the boundary conditions that matter for interpretation?",
            "boundary": "Do not tack on generic limitations; name actual conditions under which the claim weakens.",
            "exercise": "Write one sentence beginning 'This should travel when...' and one beginning 'This may fail when...'.",
        },
    }


def build_cards(analyses: list[dict[str, Any]], min_support: int = 2, total_papers: int | None = None) -> list[dict[str, Any]]:
    total_papers = total_papers if total_papers is not None else len(analyses)
    signal_support: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for analysis in analyses:
        for signal, evidence in analysis.get("signals", {}).items():
            if evidence:
                signal_support[signal].append(
                    {
                        "paper": analysis["title"],
                        "source_pdf": analysis["source_pdf"],
                        "snippets": evidence,
                    }
                )

    cards: list[dict[str, Any]] = []
    templates = base_cards()
    for signal, template in templates.items():
        support = signal_support.get(signal, [])
        if len(support) < min_support:
            continue
        ratio = len(support) / max(total_papers, 1)
        snippets = []
        for item in support[:3]:
            snippets.append(
                {
                    "paper": item["paper"],
                    "snippets": [
                        f"{snippet['section']}: {snippet['snippet']}" for snippet in item["snippets"][:2]
                    ],
                }
            )
        cards.append(
            {
                "title": template["title"],
                "support_count": len(support),
                "support_ratio": ratio,
                "confidence": support_label(ratio, total_papers),
                "skill": template["skill"],
                "prompt": template["prompt"],
                "why": "This habit appears repeatedly in the parsed corpus and is expressed as a transferable research action rather than a topic-specific imitation.",
                "evidence": snippets,
                "critical_boundary": template["boundary"],
                "exercise": template["exercise"],
            }
        )

    cards.sort(key=lambda card: (card["support_ratio"], card["support_count"], card["title"]), reverse=True)
    cards.append(
        {
            "title": "Meta-skill: extract taste by triangulating framing, method, evidence, and limits",
            "support_count": total_papers,
            "support_ratio": 1.0 if total_papers else 0.0,
            "confidence": "methodology",
            "skill": "Infer taste from repeated rhetorical behavior across papers: gap framing, aim language, evidence logic, credibility checks, and claim boundaries. Do not infer taste from topic words alone.",
            "prompt": "Given a set of papers, identify repeated habits in framing, design, evidence, and limits. Turn only repeated habits into transferable action statements with boundaries.",
            "why": "This card documents the repo's extraction logic so the output can be audited manually.",
            "evidence": [],
            "critical_boundary": "Do not infer a stable taste from one paper, one topic cluster, or one method label.",
            "exercise": "Pick three papers and manually label one sentence each for gap, aim, method, credibility, and boundary.",
        }
    )
    return cards


def render_readme(
    scholar_name: str,
    slug: str,
    papers: list[PaperRecord],
    cards: list[dict[str, Any]],
    manifest: dict[str, Any],
) -> str:
    parser_mix = Counter(p.parser_mode for p in papers)
    status = "draft-low-support" if len(papers) < 4 else "draft-supported"
    lines: list[str] = [
        f"# {scholar_name}",
        "",
        f"**Slug:** `{slug}`  ",
        f"**Status:** `{status}`  ",
        "**Language:** `English`  ",
        f"**Parsed papers:** `{len(papers)}`  ",
        f"**Parser mix:** `{dict(parser_mix)}`",
        "",
        "## Corpus Summary",
        "",
        "This README was generated locally from a folder of PDFs. Cards are based on repeated rhetorical and methodological patterns, not on topic words alone.",
        "",
        "### Parsed Papers",
        "",
    ]
    for paper in papers:
        lines.append(f"- **{paper.title}** - `{Path(paper.source_pdf).name}` via `{paper.parser_mode}`")
    lines.extend(
        [
            "",
            "## How The Taste Was Extracted",
            "",
            "The extractor looks for repeated patterns in title/abstract framing, introduction gap-claim logic, method and design language, results-side credibility checks, and discussion-side scope conditions.",
            "",
            "## Copy/Paste Skill Cards",
            "",
        ]
    )
    if not cards:
        lines.extend(["No stable cards cleared the support threshold. Add papers or lower `--min-support`.", ""])

    for card in cards:
        lines.extend(
            [
                f"### {card['title']}",
                "",
                "**Copy/Paste Research Skill**",
                "",
                f"> {card['skill']}",
                "",
                "**Copy/Paste AI / Self-Review Prompt**",
                "",
                f"> {card['prompt']}",
                "",
                f"**Why this looks like {scholar_name}'s taste**",
                "",
                card["why"],
                "",
                f"**Support:** `{card['support_count']}/{len(papers)}` papers  ",
                f"**Confidence:** `{card['confidence']}`",
                "",
            ]
        )
        if card.get("evidence"):
            lines.extend(["**Evidence Anchors**", ""])
            for item in card["evidence"]:
                for snippet in item["snippets"][:2]:
                    lines.append(f"- **{item['paper']}**: {snippet}")
            lines.append("")
        lines.extend(
            [
                "**Critical Boundary**",
                "",
                card["critical_boundary"],
                "",
                "**Exercise**",
                "",
                card["exercise"],
                "",
            ]
        )

    lines.extend(["## Extraction Settings", "", "```json", json.dumps(manifest, indent=2), "```", ""])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract research taste skill cards from a local scholar PDF folder.")
    parser.add_argument("--scholar-name", required=True)
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--scholar-root", default="scholars")
    parser.add_argument("--processed-root", default="data/processed")
    parser.add_argument("--grobid-url", default="")
    parser.add_argument("--spacy-model", default="en_core_web_sm")
    parser.add_argument("--language", default="en")
    parser.add_argument("--min-support", type=int, default=2)
    parser.add_argument("--max-evidence", type=int, default=2)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.language != "en":
        raise SystemExit("This reference implementation currently supports English only.")

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        raise SystemExit(f"Input folder does not exist: {input_dir}")
    pdfs = sorted(input_dir.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in {input_dir}")

    slug = slugify(args.scholar_name)
    scholar_dir = Path(args.scholar_root) / slug
    processed_dir = Path(args.processed_root) / slug
    scholar_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    nlp = load_nlp(args.spacy_model)
    lexicons = load_lexicons()
    papers: list[PaperRecord] = []
    analyses: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for pdf in pdfs:
        try:
            if args.grobid_url:
                try:
                    paper = extract_with_grobid(pdf, args.grobid_url)
                except Exception:
                    paper = extract_fallback(pdf)
            else:
                paper = extract_fallback(pdf)
            papers.append(paper)
            analyses.append(analyze_paper(paper, nlp, lexicons=lexicons, max_evidence=args.max_evidence))
        except Exception as exc:
            errors.append({"pdf": str(pdf), "error": str(exc)})

    manifest = {
        "scholar_name": args.scholar_name,
        "slug": slug,
        "run_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_dir": str(input_dir),
        "paper_count": len(papers),
        "min_support": args.min_support,
        "max_evidence": args.max_evidence,
        "spacy_model": args.spacy_model,
        "grobid_url": args.grobid_url or None,
        "language": args.language,
        "errors": errors,
    }
    cards = build_cards(analyses, min_support=args.min_support, total_papers=len(papers))
    readme = render_readme(args.scholar_name, slug, papers, cards, manifest)

    (scholar_dir / "README.md").write_text(readme, encoding="utf-8")
    (processed_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (processed_dir / "papers.json").write_text(json.dumps([asdict(p) for p in papers], indent=2), encoding="utf-8")
    (processed_dir / "analysis.json").write_text(json.dumps(analyses, indent=2), encoding="utf-8")

    print(f"Wrote {scholar_dir / 'README.md'}")
    print(f"Wrote {processed_dir / 'manifest.json'}")
    print(f"Wrote {processed_dir / 'analysis.json'}")
    if errors:
        print(f"Completed with {len(errors)} extraction errors.", file=sys.stderr)
    return 0 if papers else 1


if __name__ == "__main__":
    raise SystemExit(main())
