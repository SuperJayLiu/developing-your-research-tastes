#!/usr/bin/env python3
"""Lightweight repo checks for the simplified README-based structure."""
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
    if '	' in text:
        warnings.append(f'Tab character found: {md.relative_to(ROOT)}')
    if re.search(r'TBD', text):
        warnings.append(f'TBD marker found: {md.relative_to(ROOT)}')

# Scholar pages should now be folder/README.md pages, not individual per-skill files.
scholar_dir = ROOT / '04-top-scholar-research-tastes'
for kind in ['economists', 'finance-scholars']:
    base = scholar_dir / kind
    if not base.exists():
        errors.append(f'Missing scholar type folder: {base.relative_to(ROOT)}')
        continue
    for scholar_folder in sorted(p for p in base.iterdir() if p.is_dir()):
        page = scholar_folder / 'README.md'
        if not page.exists():
            errors.append(f'Scholar folder missing README: {page.relative_to(ROOT)}')
            continue
        text = page.read_text(encoding='utf-8')
        if not text.startswith('---'):
            errors.append(f'Scholar README missing front matter: {page.relative_to(ROOT)}')
        for key in ['title:', 'type:', 'open_access_status:', 'open_access_confidence:']:
            if key not in text[:700]:
                errors.append(f'Scholar README missing {key} {page.relative_to(ROOT)}')
        if '## Skill:' not in text and '## Skills Not Yet Filled' not in text:
            warnings.append(f'Scholar README has no skill sections: {page.relative_to(ROOT)}')
        extra_md = [p for p in scholar_folder.glob('*.md') if p.name != 'README.md']
        if extra_md:
            errors.append(f'Scholar folder has extra markdown files: {scholar_folder.relative_to(ROOT)}')

# The old detailed skills/by-scholar tree should not return.
by_scholar = ROOT / 'skills' / 'by-scholar'
if by_scholar.exists():
    nested_skill_files = [p for p in by_scholar.rglob('*.md') if p.name != 'README.md']
    if nested_skill_files:
        warnings.append('skills/by-scholar contains nested markdown files; scholar skills should live inside scholar READMEs')

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
