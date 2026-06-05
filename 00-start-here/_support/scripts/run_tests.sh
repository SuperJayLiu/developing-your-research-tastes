#!/usr/bin/env bash
set -euo pipefail

if [[ -d ".venv" ]]; then
  source .venv/bin/activate
fi

python 00-start-here/_support/scripts/check_repo.py
pytest -q 00-start-here/_support/tests
