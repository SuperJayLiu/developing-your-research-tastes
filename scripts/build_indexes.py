#!/usr/bin/env python3
"""Build simple Markdown indexes from existing pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def title_of(path):
    text = path.read_text(encoding='utf-8')
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else path.stem.replace('-', ' ').title()

def write_index(folder, heading):
    p = ROOT / folder
    lines = [f'# {heading}', '', 'Generated index. Run `python3 scripts/build_indexes.py` to refresh.', '']
    for md in sorted(p.glob('*.md')):
        if md.name == 'README.md':
            continue
        lines.append(f'- [{title_of(md)}]({md.name})')
    (p / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

write_index('04-top-scholar-research-tastes/economists', 'Economists')
write_index('04-top-scholar-research-tastes/finance-scholars', 'Finance Scholars')
write_index('skills/by-scholar', 'Skills by Scholar')
print('Indexes rebuilt.')
