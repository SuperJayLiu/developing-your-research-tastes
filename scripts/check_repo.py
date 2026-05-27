#!/usr/bin/env python3
"""Lightweight repo checks for Markdown/front matter consistency."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

required = [
    'README.md',
    'PUSH_TO_GITHUB.md',
    'STRUCTURE.md',
    '00-start-here/README.md',
    '01-train-your-taste-model/README.md',
    '02-general-features-of-good-research-taste/README.md',
    '03-journal-research-tastes/README.md',
    '04-top-scholar-research-tastes/README.md',
    '05-tastes-by-research-step/README.md',
    'templates/skill-card-template.md',
    'templates/scholar-page-template.md',
]

for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f'Missing required file: {rel}')

for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    if not text.strip():
        errors.append(f'Empty markdown file: {md.relative_to(ROOT)}')
    if '\t' in text:
        warnings.append(f'Tab character found: {md.relative_to(ROOT)}')
    if re.search(r'\bTBD\b', text):
        warnings.append(f'TBD marker found: {md.relative_to(ROOT)}')

scholar_dir = ROOT / '04-top-scholar-research-tastes'
for md in list((scholar_dir/'economists').glob('*.md')) + list((scholar_dir/'finance-scholars').glob('*.md')):
    if md.name == 'README.md':
        continue
    text = md.read_text(encoding='utf-8')
    if not text.startswith('---'):
        errors.append(f'Scholar page missing front matter: {md.relative_to(ROOT)}')
    for key in ['title:', 'type:', 'open_access_status:', 'open_access_confidence:']:
        if key not in text[:600]:
            errors.append(f'Scholar page missing {key} {md.relative_to(ROOT)}')
    if '## Skill ' not in text:
        warnings.append(f'Scholar page has no skill sections: {md.relative_to(ROOT)}')

print('Repo check complete.')
print(f'Errors: {len(errors)}')
for e in errors:
    print(f'ERROR: {e}')
print(f'Warnings: {len(warnings)}')
for w in warnings[:50]:
    print(f'WARN: {w}')
if len(warnings) > 50:
    print(f'... {len(warnings)-50} more warnings')

sys.exit(1 if errors else 0)
