#!/usr/bin/env python3
"""Create a new scholar page from a minimal template.

Usage:
  python3 00-start-here/_support/scripts/new_scholar_page.py "Scholar Name" economics
  python3 00-start-here/_support/scripts/new_scholar_page.py "Scholar Name" finance
"""
from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[3]

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

if len(sys.argv) < 3:
    print('Usage: python3 00-start-here/_support/scripts/new_scholar_page.py "Scholar Name" economics|finance')
    sys.exit(1)

name = sys.argv[1]
field = sys.argv[2].lower()
folder = 'economists' if field.startswith('econ') else 'finance-scholars'
slug = slugify(name)
path = ROOT / '04-top-scholar-research-tastes' / folder / slug / 'README.md'
if path.exists():
    print(f'Already exists: {path.relative_to(ROOT)}')
    sys.exit(1)
path.parent.mkdir(parents=True, exist_ok=True)

content = (
    f'---\n'
    f'title: "{name}"\n'
    f'type: "scholar-profile"\n'
    f'field: ["{field}"]\n'
    f'status: "seed"\n'
    f'open_access_status: "unfinished-upload-needed"\n'
    f'open_access_confidence: "low"\n'
    f'primary_skill_clusters: []\n'
    f'representative_papers: []\n'
    f'related_skills: []\n'
    f'related_collections: ["top-scholar-skills"]\n'
    f'tags: []\n'
    f'---\n\n'
    f'# {name}\n\n'
    f'{name} is read here as a source of research judgment, not as a topic list. Replace this paragraph with a short account of the repeated research move visible across representative papers.\n\n'
    f'## Evidence Base\n\n'
    f'Add representative paper anchors, author pages, journal links, Nobel materials, or uploaded PDFs before marking the page reviewed. Each anchor should show something about question choice, mechanism, evidence, framing, or boundary.\n\n'
    f'| Evidence Anchor | What To Check |\n'
    f'|---|---|\n'
    f'| Representative paper or source | Explain what the source shows about the scholar\\'s research taste. |\n\n'
    f'## Reading The Taste\n\n'
    f'Read across the evidence anchors and identify what the scholar repeatedly refuses to leave vague. That refusal should become the center of the page.\n\n'
    f'## Skill: Name The Mature Skill\n\n'
    f'Use this skill when a live project faces the same class of research problem. State the trigger before applying the skill.\n\n'
    f'The research move should name the action, the evidence anchor, the feedback signal, and the boundary. The skill is mature only if it changes a decision in the reader\\'s project.\n\n'
    f'Practice the skill in one page by writing the trigger, mechanism or design, closest alternative explanation, evidence that would change a skeptical reader\\'s mind, and narrowest honest contribution claim.\n\n'
    f'## Open-Access Evidence\n\n'
    f'Add public evidence links before moving the page beyond seed status.\n\n'
    f'## Upload Needed\n\n'
    f'Upload canonical papers before expanding.\n'
)
path.write_text(content, encoding='utf-8')
print(f'Created: {path.relative_to(ROOT)}')
