#!/usr/bin/env bash
set -euo pipefail

PROFILE="${1:-core}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUPPORT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ROOT_DIR="$(cd "${SUPPORT_DIR}/../.." && pwd)"

cd "${ROOT_DIR}"

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -r "${SUPPORT_DIR}/repo-config/requirements-core.txt"

if [[ "$PROFILE" == "enhanced" ]]; then
  pip install -r "${SUPPORT_DIR}/repo-config/requirements-enhanced.txt"
  python -m spacy download en_core_web_sm || true
fi

echo "Install complete for profile: ${PROFILE}"
