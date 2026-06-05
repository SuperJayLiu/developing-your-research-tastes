.PHONY: check index zip install install-enhanced extract test

check:
	python3 scripts/check_repo.py

index:
	python3 scripts/build_indexes.py

zip:
	cd .. && zip -r developing-your-research-tastes.zip developing-your-research-tastes -x "*/.git/*" "*.DS_Store" "*__pycache__*"

install:
	bash scripts/install.sh core

install-enhanced:
	bash scripts/install.sh enhanced

extract:
	python scripts/extract_scholar_taste.py --help

test:
	pytest -q
