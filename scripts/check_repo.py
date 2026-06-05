#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(".")


def main() -> int:
    errors: list[str] = []
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / ".gitignore",
        ROOT / "requirements-core.txt",
        ROOT / "configs" / "thresholds.yml",
        ROOT / "configs" / "lexicons.yml",
        ROOT / "scripts" / "__init__.py",
        ROOT / "scripts" / "extract_scholar_taste.py",
        ROOT / "scripts" / "install.sh",
        ROOT / "scripts" / "check_repo.py",
        ROOT / "scripts" / "run_tests.sh",
        ROOT / "tests" / "test_extract.py",
        ROOT / ".github" / "workflows" / "ci.yml",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required file: {path}")

    scholars_root = ROOT / "scholars"
    if scholars_root.exists():
        for scholar_dir in sorted(scholars_root.iterdir()):
            if not scholar_dir.is_dir():
                continue
            files = [path.name for path in scholar_dir.iterdir() if path.is_file() and not path.name.startswith(".")]
            if "README.md" not in files:
                errors.append(f"{scholar_dir} is missing README.md")
            extras = sorted(name for name in files if name != "README.md")
            if extras:
                errors.append(f"{scholar_dir} contains extra files; expected only README.md: {extras}")

    if errors:
        print("\n".join(errors))
        return 1
    print("Repo check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
