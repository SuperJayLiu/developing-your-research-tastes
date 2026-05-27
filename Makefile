.PHONY: check index zip

check:
	python3 scripts/check_repo.py

index:
	python3 scripts/build_indexes.py

zip:
	cd .. && zip -r developing-your-research-tastes.zip developing-your-research-tastes -x "*/.git/*" "*.DS_Store" "*__pycache__*"
