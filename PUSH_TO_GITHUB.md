# Push This Repo to GitHub from Mac

This repo is ready for you to push manually.

## 1. Unzip

If the ZIP is in Downloads:

```bash
cd ~/Downloads
unzip developing-your-research-tastes-revised.zip
cd developing-your-research-tastes
```

## 2. Optional: check the repo before pushing

```bash
python3 scripts/check_repo.py
```

## 3. Create a new GitHub repo

Go to:

```text
https://github.com/new
```

Suggested repo name:

```text
developing-your-research-tastes
```

Do **not** initialize with README, license, or .gitignore, because this folder already has them.

## 4. Push from Terminal

```bash
git init
git add .
git commit -m "Initial research taste curriculum structure"
git branch -M main
git remote add origin https://github.com/SuperJayLiu/developing-your-research-tastes.git
git push -u origin main
```

## 5. Enable GitHub Pages

In GitHub:

```text
Settings → Pages → Build and deployment → Source: Deploy from a branch
```

Then choose:

```text
Branch: main
Folder: /docs
```

Your site should become available at:

```text
https://superjayliu.github.io/developing-your-research-tastes/
```

## 6. Future updates

```bash
git add .
git commit -m "Update research taste notes"
git push
```
