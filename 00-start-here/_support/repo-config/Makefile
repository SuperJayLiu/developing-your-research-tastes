.PHONY: check index zip install install-enhanced extract test

check:
	python3 00-start-here/_support/scripts/check_repo.py

index:
	python3 00-start-here/_support/scripts/build_indexes.py

zip:
	cd .. && zip -r developing-your-research-tastes.zip developing-your-research-tastes -x "*/.git/*" "*.DS_Store" "*__pycache__*"

install:
	bash 00-start-here/_support/scripts/install.sh core

install-enhanced:
	bash 00-start-here/_support/scripts/install.sh enhanced

extract:
	python 00-start-here/_support/scripts/extract_scholar_taste.py --help

test:
	pytest -q 00-start-here/_support/tests
