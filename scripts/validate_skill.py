"""Check skill packaging and local Markdown targets; no network or mutation."""
from pathlib import Path
import re


def validate(root):
    skill = root / '.agents/skills/travel-guide/SKILL.md'
    text = skill.read_text()
    errors = []
    header = text.split('---', 2)
    if len(header) != 3 or not text.startswith('---\n'):
        errors.append('Missing frontmatter')
    else:
        for field in ('name', 'description'):
            if not re.search(rf'^{field}:\s*\S', header[1], re.M):
                errors.append(f'Missing {field}')
    count = 0
    for file in root.rglob('*.md'):
        if '.git' in file.parts:
            continue
        for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
            if ':' in link or link.startswith('#'):
                continue
            target = link.split('#')[0]
            if not target:
                continue
            count += 1
            if not (file.parent / target).exists():
                errors.append(f'{file.relative_to(root)}: missing {target}')
    return count, errors


if __name__ == '__main__':
    count, errors = validate(Path(__file__).resolve().parents[1])
    print(f'Checked {count} local Markdown targets')
    for error in errors:
        print(error)
    raise SystemExit(bool(errors))
