#!/usr/bin/env python3
"""Create a new scholar page from a minimal template.

Usage:
  python3 scripts/new_scholar_page.py "Scholar Name" economics
  python3 scripts/new_scholar_page.py "Scholar Name" finance
"""
from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

if len(sys.argv) < 3:
    print('Usage: python3 scripts/new_scholar_page.py "Scholar Name" economics|finance')
    sys.exit(1)

name = sys.argv[1]
field = sys.argv[2].lower()
folder = 'economists' if field.startswith('econ') else 'finance-scholars'
slug = slugify(name)
path = ROOT / '04-top-scholar-research-tastes' / folder / f'{slug}.md'
if path.exists():
    print(f'Already exists: {path.relative_to(ROOT)}')
    sys.exit(1)

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
    f'## One-Sentence Research Taste\n\n'
    f'TODO.\n\n'
    f'## Signature Questions\n\n'
    f'TODO.\n\n'
    f'## Skill 1: TODO\n\n'
    f'### What the skill means\n\n'
    f'### Evidence\n\n'
    f'### How to practice it\n\n'
    f'## Open-Access Evidence\n\n'
    f'TODO.\n\n'
    f'## Upload Needed\n\n'
    f'Upload canonical papers before expanding.\n'
)
path.write_text(content, encoding='utf-8')
print(f'Created: {path.relative_to(ROOT)}')
