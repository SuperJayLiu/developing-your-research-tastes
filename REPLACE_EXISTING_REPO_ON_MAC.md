# Replace the Existing GitHub Repo with This Revised Version

This guide replaces all existing files in your local clone of `SuperJayLiu/developing-your-research-tastes` with the revised repo files, then pushes the replacement commit to GitHub.

## What this does

- Keeps your `.git/` history locally.
- Deletes old working-tree files.
- Copies in the revised repo files.
- Commits the replacement.
- Pushes to `main`.

## 0. Recommended: make a backup branch

```bash
git checkout main
git pull origin main
git checkout -b backup-before-replacement
git push -u origin backup-before-replacement
git checkout main
```

## 1. Unzip the revised repo package

Assuming the ZIP is in `~/Downloads`:

```bash
cd ~/Downloads
unzip developing-your-research-tastes-full-replacement.zip
```

You should now have:

```bash
~/Downloads/developing-your-research-tastes/
```

This folder is the revised version.

## 2. Go to your existing local repo clone

Example:

```bash
cd ~/Documents/GitHub/developing-your-research-tastes
```

If your repo is somewhere else, `cd` into that folder instead.

Check that you are in the right repo:

```bash
git remote -v
```

You should see:

```text
https://github.com/SuperJayLiu/developing-your-research-tastes.git
```

## 3. Replace all existing files locally

Run this from inside your existing local clone:

```bash
rsync -av --delete \
  --exclude='.git' \
  ~/Downloads/developing-your-research-tastes/ ./
```

This deletes files that are no longer in the revised repo and copies in the new version.

## 4. Check and commit

```bash
python3 scripts/check_repo.py
git status
git add -A
git commit -m "Replace repo with revised research taste curriculum"
git push origin main
```

## If GitHub rejects the push

First pull and re-run the replacement:

```bash
git pull origin main --rebase
rsync -av --delete --exclude='.git' ~/Downloads/developing-your-research-tastes/ ./
git add -A
git commit -m "Replace repo with revised research taste curriculum"
git push origin main
```

If you intentionally want to overwrite remote `main`, use force-with-lease:

```bash
git push --force-with-lease origin main
```

Use force-with-lease only if you are sure nobody else pushed important changes.
