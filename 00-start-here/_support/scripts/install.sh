#!/usr/bin/env bash
set -euo pipefail

PROFILE="${1:-core}"

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r requirements-core.txt

if [[ "$PROFILE" == "enhanced" ]]; then
  pip install -r requirements-enhanced.txt
  python -m spacy download en_core_web_sm || true
fi

echo "Install complete for profile: ${PROFILE}"
