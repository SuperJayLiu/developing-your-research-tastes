#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="${1:-$HOME/Downloads/developing-your-research-tastes}"
TARGET_DIR="${2:-$(pwd)}"

if [ ! -d "$TARGET_DIR/.git" ]; then
  echo "Error: target directory is not a git repo: $TARGET_DIR" >&2
  echo "Run this script from inside your existing local clone, or pass target dir as second arg." >&2
  exit 1
fi

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: revised source folder not found: $SOURCE_DIR" >&2
  echo "Unzip the replacement ZIP first, or pass source dir as first arg." >&2
  exit 1
fi

if [ ! -f "$SOURCE_DIR/README.md" ]; then
  echo "Error: source folder does not look like the repo root: $SOURCE_DIR" >&2
  exit 1
fi

echo "Replacing contents of: $TARGET_DIR"
echo "Using revised source: $SOURCE_DIR"

rsync -av --delete --exclude='.git' "$SOURCE_DIR/" "$TARGET_DIR/"

echo "Done. Next run:"
echo "  python3 scripts/check_repo.py"
echo "  git status"
echo "  git add -A"
echo "  git commit -m 'Replace repo with revised research taste curriculum'"
echo "  git push origin main"
