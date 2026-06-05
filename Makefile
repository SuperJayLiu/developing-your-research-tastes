.PHONY: install install-enhanced extract check test

install:
	bash scripts/install.sh core

install-enhanced:
	bash scripts/install.sh enhanced

extract:
	python scripts/extract_scholar_taste.py --help

check:
	python scripts/check_repo.py

test:
	pytest -q
