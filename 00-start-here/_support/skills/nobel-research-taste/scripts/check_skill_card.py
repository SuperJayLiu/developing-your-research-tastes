#!/usr/bin/env python3
"""Check whether a research-taste skill card has the minimum mature structure."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CHECKS = {
    "name": re.compile(r"(^|\n)name\s*:", re.IGNORECASE),
    "description": re.compile(r"(^|\n)description\s*:", re.IGNORECASE),
    "trigger_or_scope": re.compile(r"\b(use this skill|use when|trigger)\b", re.IGNORECASE),
    "research_move": re.compile(r"\b(core move|central move|research move|move 1)\b", re.IGNORECASE),
    "evidence_anchor": re.compile(r"\b(evidence anchor|evidence|source|paper|nobel)\b", re.IGNORECASE),
    "diagnostics": re.compile(r"\bdiagnostics?\b", re.IGNORECASE),
    "gotchas": re.compile(r"\b(gotchas?|anti-patterns?|failure mode|bad imitation|bad taste)\b", re.IGNORECASE),
    "practice": re.compile(r"\bpractice prompt\b|\bapply this skill\b", re.IGNORECASE),
    "boundary": re.compile(r"\b(boundary|too strong|cannot support|should not)\b", re.IGNORECASE),
    "transfer": re.compile(r"\b(transfer|different project|what changed)\b", re.IGNORECASE),
}


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown skill card or skill-card collection to check")
    parser.add_argument("--min-words", type=int, default=350, help="Minimum word count for a mature card")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    missing = [name for name, pattern in CHECKS.items() if not pattern.search(text)]
    words = word_count(text)

    print(f"Checked: {args.path}")
    print(f"Words: {words}")

    if words < args.min_words:
        missing.append(f"min_words_{args.min_words}")

    if missing:
        print("Missing structure:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Mature skill structure: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
