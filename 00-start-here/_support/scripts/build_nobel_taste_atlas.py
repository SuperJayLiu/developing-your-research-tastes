#!/usr/bin/env python3
"""Build a Nobel research taste atlas from official Nobel evidence PDFs."""
from __future__ import annotations

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import unicodedata

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_DIR = ROOT / "00-start-here" / "_support" / "evidence" / "nobel-open-access"
API_PATH = EVIDENCE_DIR / "nobel_api_eco.json"
MANIFEST_PATH = EVIDENCE_DIR / "download_manifest.json"
TEXT_INDEX_PATH = EVIDENCE_DIR / "nobel_pdf_read_index.json"
ATLAS_PATH = ROOT / "04-top-scholar-research-tastes" / "nobel-laureates" / "nobel-taste-atlas.md"
SKILL_MAP_PATH = ROOT / "04-top-scholar-research-tastes" / "nobel-laureates" / "nobel-skill-map.md"


KEYWORD_GROUPS = {
    "formal_theory_allocation": [
        "general equilibrium", "welfare theory", "optimum allocation", "economic theory",
        "analytical methods", "rigorous reformulation", "efficient utilization",
        "dynamic economic theory", "static economic theory",
    ],
    "growth_innovation": [
        "growth", "innovation", "technology", "technological", "creative destruction",
        "development", "productivity", "industrialization", "knowledge",
    ],
    "institutions_governance": [
        "institution", "institutions", "property rights", "transaction costs",
        "governance", "commons", "political", "regulation", "law",
    ],
    "causal_econometrics": [
        "causal", "identification", "natural experiment", "instrumental",
        "econometric", "selective samples", "discrete choice", "cointegration",
        "volatility", "time series", "ARCH",
    ],
    "incentives_information": [
        "incentive", "incentives", "asymmetric information", "information",
        "contract", "mechanism design", "auction", "game theory", "equilibrium",
        "strategic", "principal-agent",
    ],
    "finance_macro": [
        "asset", "prices", "financial", "finance", "derivatives", "banks",
        "banking", "crises", "monetary", "fiscal", "business cycles",
        "macroeconomic", "exchange rate", "portfolio",
    ],
    "welfare_behavior_development": [
        "welfare", "poverty", "consumption", "behavioral", "psychological",
        "decision-making", "developing countries", "labour", "labor",
        "human behaviour", "experiments",
    ],
    "markets_trade_design": [
        "market", "markets", "trade", "capital movements", "industrial",
        "search frictions", "stable allocations", "market design", "allocation",
        "input-output", "national accounts",
    ],
}


ARCHETYPES = {
    "formal_theory_allocation": {
        "label": "formal theory, equilibrium, and allocation",
        "question": "The question taste is to make a broad economic problem mathematically disciplined: what is the benchmark allocation, what constraints define it, and what changes when the assumptions are relaxed?",
        "method": "The method taste is to build a clear formal structure that turns intuition into propositions, comparative statics, or welfare statements that other scholars can inspect and reuse.",
        "evidence": "The evidence standard is analytical transparency: the contribution should make assumptions, constraints, equilibrium logic, and welfare implications visible rather than hiding judgment inside notation.",
        "boundary": "The boundary is that formal theory becomes bad taste when rigor floats away from the economic object or when the model proves a result whose relevance is never disciplined.",
        "skills": [
            "Build the benchmark model before adding institutional or empirical complications.",
            "Use assumptions to clarify what must be true for the result to matter.",
            "Translate the formal result back into an economic decision, constraint, or welfare tradeoff.",
        ],
    },
    "growth_innovation": {
        "label": "growth, innovation, and historical change",
        "question": "The question taste is to make long-run progress explainable rather than merely descriptive: what conditions allow knowledge, technology, institutions, or investment to change the path of an economy?",
        "method": "The method taste is to combine a compact mechanism with evidence that spans time, sectors, or countries, so that a growth story has a moving part rather than a label.",
        "evidence": "The evidence standard is comparative and cumulative: a persuasive claim must show why the proposed channel matters beyond one episode and why rival channels are not doing all the work.",
        "boundary": "The boundary is that long-run narratives become weak when persistence is asserted without a transmission mechanism or when historical texture substitutes for a testable claim.",
        "skills": [
            "Turn a long-run fact into a mechanism with a state variable, incentive, or institutional condition.",
            "Use historical comparison to separate persistence, shock, and adaptation.",
            "State why the mechanism travels beyond the original episode without claiming universality.",
        ],
    },
    "institutions_governance": {
        "label": "institutions, governance, and political economy",
        "question": "The question taste is to treat rules, rights, organizations, and political constraints as causes of economic outcomes, not background context.",
        "method": "The method taste is to identify how a rule changes incentives or feasible actions, then ask what evidence would distinguish that channel from geography, technology, selection, or demand.",
        "evidence": "The evidence standard is mechanism-level institutional comparison: the reader should see which rule matters, who responds to it, and what observable implication follows.",
        "boundary": "The boundary is that institutional explanation becomes loose when every difference is called an institution or when the institutional channel is not separated from other historical forces.",
        "skills": [
            "Translate an institutional detail into a causal mechanism.",
            "Compare governance arrangements by the incentives and constraints they create.",
            "Keep the claim bounded to what the institutional evidence can actually identify.",
        ],
    },
    "causal_econometrics": {
        "label": "causal design, econometrics, and measurement discipline",
        "question": "The question taste is to ask what can be learned credibly from imperfect data once selection, simultaneity, dynamics, or measurement limits are made explicit.",
        "method": "The method taste is to define the estimand, model the source of variation, and make assumptions visible enough that a skeptical reader can locate the identifying force.",
        "evidence": "The evidence standard is design transparency: the empirical object, counterfactual, assumptions, and failure modes must be clearer than the final coefficient.",
        "boundary": "The boundary is that technical sophistication becomes bad taste when it hides the identifying assumption or lets method replace substance.",
        "skills": [
            "Name the object of learning before estimating it.",
            "Turn a data limitation into an explicit design or model assumption.",
            "Write the failure mode of the empirical strategy in plain language.",
        ],
    },
    "incentives_information": {
        "label": "incentives, information, contracts, and strategic design",
        "question": "The question taste is to ask how hidden information, hidden action, strategic interaction, or design constraints change the outcome that a simple market benchmark would predict.",
        "method": "The method taste is to build a minimal model where the friction is doing real work and the prediction changes when the friction is removed.",
        "evidence": "The evidence standard is internal discipline: assumptions, incentive constraints, equilibrium logic, and comparative statics must point in the same direction.",
        "boundary": "The boundary is that theory becomes decorative when the model is elegant but does not sharpen a prediction, welfare tradeoff, or institutional implication.",
        "skills": [
            "Isolate the information or incentive friction before adding complexity.",
            "Use the model to generate a prediction that could be wrong.",
            "Explain the real institution through the constraint that binds in the model.",
        ],
    },
    "finance_macro": {
        "label": "finance, macroeconomics, and market signals",
        "question": "The question taste is to use prices, balance sheets, monetary regimes, or financial institutions to learn about risk, beliefs, constraints, and aggregate outcomes.",
        "method": "The method taste is to connect a market or macro fact to a disciplined benchmark, then ask which interpretation survives when risk, information, frictions, and policy are considered.",
        "evidence": "The evidence standard is interpretive separation: a price pattern, crisis fact, or macro series must be linked to a mechanism rather than treated as self-explanatory.",
        "boundary": "The boundary is that market evidence becomes weak when a pattern is named as a mechanism before alternative interpretations are ruled out.",
        "skills": [
            "Use prices or balance sheets as evidence without confusing them with explanation.",
            "Separate risk, beliefs, frictions, and policy channels before claiming a mechanism.",
            "Build a benchmark case first, then show which friction makes the observed fact informative.",
        ],
    },
    "welfare_behavior_development": {
        "label": "welfare, behavior, poverty, and human decision-making",
        "question": "The question taste is to connect individual behavior, welfare, poverty, or development outcomes to constraints and choices that can be observed and improved.",
        "method": "The method taste is to make the human decision problem concrete, then use theory, experiments, data, or welfare accounting to learn what changes the outcome.",
        "evidence": "The evidence standard is practical mechanism evidence: a good result should say not only what happens, but why it happens and what intervention or welfare interpretation follows.",
        "boundary": "The boundary is that human-centered economics becomes vague when it reports outcomes without clarifying the constraint, behavior, or welfare criterion.",
        "skills": [
            "Turn a human outcome into a decision problem with constraints.",
            "Use experiments, surveys, or welfare formulas to distinguish mechanism from description.",
            "Keep policy claims tied to the behavioral or welfare evidence actually observed.",
        ],
    },
    "markets_trade_design": {
        "label": "markets, trade, allocation, and design",
        "question": "The question taste is to ask how markets allocate resources once frictions, rules, information, location, or matching constraints are made explicit.",
        "method": "The method taste is to build a clear benchmark of allocation and then show which market feature changes prices, quantities, welfare, or participation.",
        "evidence": "The evidence standard is allocative clarity: the paper should show who gains, who loses, what constraint binds, and why the market arrangement matters.",
        "boundary": "The boundary is that market-design language becomes empty when it celebrates a mechanism without showing the allocation problem it solves.",
        "skills": [
            "Start from the allocation problem before proposing a market mechanism.",
            "Use a benchmark to identify which friction changes the outcome.",
            "Explain the welfare or distributional consequence of the market design choice.",
        ],
    },
}


def clean_ascii(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def ascii_slug(text: str) -> str:
    text = text.replace("ø", "o").replace("Ø", "O").replace("ł", "l").replace("Ł", "L")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"\b(jr|sr|sir|dr|prof|iii)\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    parts = [p for p in text.split() if p not in {"von", "van", "de", "da", "of"}]
    return parts[-1] if parts else "unknown"


def name_of(laureate: dict) -> str:
    return laureate.get("knownName", {}).get("en") or laureate.get("fullName", {}).get("en") or "Unknown Laureate"


def read_pdf_text(path: Path, max_chars: int = 120_000) -> dict:
    try:
        reader = PdfReader(str(path))
        chunks: list[str] = []
        for page in reader.pages:
            if sum(len(c) for c in chunks) >= max_chars:
                break
            try:
                chunks.append(page.extract_text() or "")
            except Exception:
                continue
        text = clean_ascii("\n".join(chunks))
        return {"path": str(path.relative_to(ROOT)), "pages": len(reader.pages), "chars": len(text), "text": text[:max_chars]}
    except Exception as error:
        return {"path": str(path.relative_to(ROOT)), "pages": 0, "chars": 0, "text": "", "error": str(error)}


def build_text_index(downloads: list[dict]) -> dict:
    index: dict[str, dict] = {}
    for item in downloads:
        path = ROOT / item["local_path"]
        if path.exists():
            index[item["local_path"]] = read_pdf_text(path)
    metadata_index = {
        key: {field: value for field, value in item.items() if field != "text"}
        for key, item in index.items()
    }
    TEXT_INDEX_PATH.write_text(json.dumps(metadata_index, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return index


def score_archetypes(text: str) -> Counter:
    lowered = text.lower()
    scores: Counter = Counter()
    for group, terms in KEYWORD_GROUPS.items():
        for term in terms:
            scores[group] += lowered.count(term)
    return scores


def choose_archetype(motivation: str, text: str) -> str:
    m = motivation.lower()
    priority_rules = [
        (
            "growth_innovation",
            [
                "economic growth", "technological", "innovation", "creative destruction",
                "climate change into long-run", "technological progress",
            ],
        ),
        (
            "institutions_governance",
            [
                "institutions", "institutional", "property rights", "transaction costs",
                "economic governance", "public regulation", "constitutional",
            ],
        ),
        (
            "causal_econometrics",
            [
                "econometric", "selective samples", "discrete choice", "time series",
                "time-varying volatility", "cointegration", "causal relationships",
                "cause and effect", "empirical contributions to labour economics",
                "dynamic models for the analysis",
                "national accounts", "input-output", "probability theory foundations",
            ],
        ),
        (
            "formal_theory_allocation",
            [
                "static and dynamic economic theory", "general economic equilibrium",
                "general equilibrium", "welfare theory", "optimum allocation",
                "rigorous reformulation", "efficient utilization of resources",
            ],
        ),
        (
            "finance_macro",
            [
                "financial markets", "asset prices", "derivatives", "banks and financial crises",
                "monetary", "fiscal", "business cycles", "exchange rate", "macroeconomic policy",
                "stabilization policy", "economic fluctuations", "intertemporal tradeoffs",
            ],
        ),
        (
            "incentives_information",
            [
                "asymmetric information", "incentives", "contract theory", "mechanism design",
                "auction", "game-theory", "non-cooperative games", "conflict and cooperation",
            ],
        ),
        (
            "markets_trade_design",
            [
                "international trade", "capital movements", "location of economic activity",
                "search frictions", "stable allocations", "market design", "market power",
                "laboratory experiments as a tool", "alternative market mechanisms",
            ],
        ),
        (
            "welfare_behavior_development",
            [
                "welfare economics", "poverty", "consumption", "behavioural economics",
                "behavioral economics", "psychological research", "judgment and decision-making",
                "developing countries", "global poverty", "labour market outcomes",
                "labor economics", "human behaviour", "decision-making process within economic organizations",
            ],
        ),
    ]
    for group, phrases in priority_rules:
        if any(phrase in m for phrase in phrases):
            return group

    combined = f"{motivation} {motivation} {motivation} {text[:80_000]}"
    scores = score_archetypes(combined)
    if not scores:
        return "markets_trade_design"
    return scores.most_common(1)[0][0]


def top_signals(text: str, limit: int = 5) -> list[str]:
    scores = score_archetypes(text)
    readable = {
        "formal_theory_allocation": "formal theory/allocation",
        "growth_innovation": "growth/innovation",
        "institutions_governance": "institutions/governance",
        "causal_econometrics": "causal/econometric design",
        "incentives_information": "incentives/information",
        "finance_macro": "finance/macro",
        "welfare_behavior_development": "welfare/behavior/development",
        "markets_trade_design": "markets/allocation/design",
    }
    return [readable[k] for k, _ in scores.most_common(limit) if scores[k] > 0]


def group_manifest(downloads: list[dict]) -> tuple[dict, dict]:
    by_slug_year: dict[tuple[int, str], list[dict]] = defaultdict(list)
    by_year_background: dict[int, list[dict]] = defaultdict(list)
    for item in downloads:
        key = (int(item["year"]), item["slug"])
        by_slug_year[key].append(item)
        if item["source_type"] in {"advanced-background", "popular-background"}:
            by_year_background[int(item["year"])].append(item)
    return by_slug_year, by_year_background


def evidence_for(year: int, slug: str, by_slug_year: dict, by_year_background: dict) -> list[dict]:
    items = list(by_slug_year.get((year, slug), []))
    seen = {item["url"] for item in items}
    for item in by_year_background.get(year, []):
        if item["url"] not in seen:
            items.append(item)
            seen.add(item["url"])
    return sorted(items, key=lambda x: (x["source_type"], x["url"]))


def evidence_line(items: list[dict], text_index: dict) -> tuple[str, str, int]:
    if not items:
        return "No direct official PDF in local cache", "none", 0
    counts = Counter(item["source_type"] for item in items)
    parts = [f"{count} {kind.replace('-', ' ')}" for kind, count in sorted(counts.items())]
    chars = sum(text_index.get(item["local_path"], {}).get("chars", 0) for item in items)
    signals = top_signals(" ".join(text_index.get(item["local_path"], {}).get("text", "") for item in items))
    return ", ".join(parts), ", ".join(signals) if signals else "no strong keyword signal", chars


def evidence_status(items: list[dict], chars: int) -> str:
    if not items:
        return "API-only, PDF needed"
    if chars < 1_000:
        return "PDF present, text extraction weak"
    return "PDF-backed"


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {clean_ascii(item)}" for item in items)


def render_atlas(api: dict, manifest: dict, text_index: dict) -> str:
    by_slug_year, by_year_background = group_manifest(manifest["downloads"])
    total_docs = manifest["download_count"]
    lines: list[str] = []
    lines.append("# Nobel Research Taste Atlas")
    lines.append("")
    lines.append("This atlas summarizes Nobel-linked research taste from official Nobel evidence. It uses the Nobel API snapshot for laureate names and motivations, the local NobelPrize.org PDF manifest for evidence files, and extracted text from the local PDF cache for keyword signals. It is not a complete literature review and it does not store copyrighted journal PDFs.")
    lines.append("")
    lines.append("The goal is practical: convert each recognized contribution into a portable research skill while preserving the boundary that prevents shallow imitation.")
    lines.append("")
    lines.append("```mermaid")
    lines.append("flowchart LR")
    lines.append('    A["Nobel motivation"] --> B["Official PDF evidence"]')
    lines.append('    B --> C["Taste diagnosis"]')
    lines.append('    C --> D["Copyable skill"]')
    lines.append('    D --> E["Boundary condition"]')
    lines.append("```")
    lines.append("")
    lines.append("## Evidence Read")
    lines.append("")
    lines.append(f"The local cache currently records {total_docs} official Nobel PDFs. The generated PDF text index is `00-start-here/_support/evidence/nobel-open-access/nobel_pdf_read_index.json`; it records page counts, extracted character counts, and extraction errors where relevant. PDF binaries remain ignored by Git.")
    lines.append("")
    lines.append("## How To Use This Atlas")
    lines.append("")
    lines.append("Read the laureate entry as a first-pass taste diagnosis. The entry should tell you what question the laureate made important, what method or model carried the argument, what evidence standard disciplines the contribution, and what mistake a reader should avoid when copying the move.")
    lines.append("")
    for prize in api.get("nobelPrizes", []):
        year = int(prize["awardYear"])
        laureates = prize.get("laureates", [])
        names = [clean_ascii(name_of(l)) for l in laureates]
        lines.append(f"## {year} - {', '.join(names)}")
        lines.append("")
        for laureate in laureates:
            name = clean_ascii(name_of(laureate))
            slug = ascii_slug(name)
            motivation = clean_ascii(laureate.get("motivation", {}).get("en") or prize.get("topMotivation", {}).get("en", ""))
            docs = evidence_for(year, slug, by_slug_year, by_year_background)
            doc_text = " ".join(text_index.get(item["local_path"], {}).get("text", "") for item in docs)
            archetype_key = choose_archetype(motivation, doc_text)
            archetype = ARCHETYPES[archetype_key]
            evidence, signals, chars = evidence_line(docs, text_index)
            status = evidence_status(docs, chars)

            lines.append(f"### {name}")
            lines.append("")
            lines.append(f"Official motivation: {motivation}.")
            lines.append("")
            lines.append(f"Evidence read: {evidence}; extracted text: {chars:,} characters; status: {status}; PDF signals: {signals}.")
            lines.append("")
            lines.append(f"Taste diagnosis: {archetype['label']}.")
            lines.append("")
            lines.append(f"Question taste: {archetype['question']} In this case, the motivating contribution is: {motivation}.")
            lines.append("")
            lines.append(f"Method or model taste: {archetype['method']}")
            lines.append("")
            lines.append(f"Evidence standard: {archetype['evidence']}")
            lines.append("")
            lines.append(f"Contribution style: the useful contribution is not the topic label; it is the move that made the recognized problem tractable enough for other scholars to reuse.")
            lines.append("")
            lines.append(f"Boundary: {archetype['boundary']}")
            lines.append("")
            lines.append("Copyable skills:")
            lines.append("")
            lines.append(bullet_list(archetype["skills"]))
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_skill_map(api: dict, manifest: dict, text_index: dict) -> str:
    by_slug_year, by_year_background = group_manifest(manifest["downloads"])
    rows: list[str] = []
    for prize in api.get("nobelPrizes", []):
        year = int(prize["awardYear"])
        for laureate in prize.get("laureates", []):
            name = clean_ascii(name_of(laureate))
            slug = ascii_slug(name)
            motivation = clean_ascii(laureate.get("motivation", {}).get("en") or "")
            docs = evidence_for(year, slug, by_slug_year, by_year_background)
            doc_text = " ".join(text_index.get(item["local_path"], {}).get("text", "") for item in docs)
            archetype_key = choose_archetype(motivation, doc_text)
            archetype = ARCHETYPES[archetype_key]
            evidence, signals, chars = evidence_line(docs, text_index)
            status = evidence_status(docs, chars)
            skill = archetype["skills"][0]
            rows.append(
                f"| {year} | {name} | {clean_ascii(archetype['label'])} | {clean_ascii(skill)} | {evidence}; {chars:,} chars | {status} |"
            )

    header = """# Nobel Skill Map

This map is the compact index for the Nobel Research Taste Atlas. The atlas itself is in [nobel-taste-atlas.md](nobel-taste-atlas.md). The purpose is to keep the scholar-skill pipeline honest: first collect legal evidence, then infer recurring research moves, then write mature skill cards.

The current local cache contains official NobelPrize.org PDFs covering 1969 through 2025. The PDFs are stored locally and ignored by Git; the tracked manifest is `00-start-here/_support/evidence/nobel-open-access/download_manifest.json`.

```mermaid
flowchart LR
    A["Nobel API laureate list"] --> B["Official Nobel PDFs"]
    B --> C["Manifest and text index"]
    C --> D["Taste atlas"]
    D --> E["Mature skill cards"]
```

| Year | Scholar | Taste Cluster | First Portable Skill | Evidence | Status |
|---|---|---|---|---|---|
"""
    return header + "\n".join(rows) + "\n\n## Boundary\n\nDo not treat the Nobel cache as a complete literature archive. It is an evidence foundation for taste extraction. The next pass should use the advanced background bibliographies to choose a small set of canonical papers per laureate, then download only legal open-access versions.\n"


def main() -> int:
    api = json.loads(API_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    text_index = build_text_index(manifest["downloads"])
    ATLAS_PATH.write_text(render_atlas(api, manifest, text_index), encoding="utf-8")
    SKILL_MAP_PATH.write_text(render_skill_map(api, manifest, text_index), encoding="utf-8")
    print(f"Wrote {ATLAS_PATH.relative_to(ROOT)}")
    print(f"Wrote {SKILL_MAP_PATH.relative_to(ROOT)}")
    print(f"Wrote {TEXT_INDEX_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
