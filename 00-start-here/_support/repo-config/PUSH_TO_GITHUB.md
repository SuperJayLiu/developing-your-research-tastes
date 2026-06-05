# Push To GitHub

The repository is designed to publish as a book-like GitHub project. The visible top-level folders should remain the numbered chapters `00` through `05`; support material belongs under `00-start-here/_support/`.

Before pushing, run the local checks:

```bash
python3 00-start-here/_support/scripts/check_repo.py
pytest -q 00-start-here/_support/tests
```

Then commit and push normally:

```bash
git status --short
git add .
git commit -m "Improve book-style research taste chapters"
git push origin main
```

If GitHub rejects the push because the remote moved, fetch first and merge carefully. Do not force-push over remote work unless the repository owner explicitly asks for that.
