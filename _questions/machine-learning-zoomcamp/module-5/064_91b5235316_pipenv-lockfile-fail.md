---
id: 91b5235316
question: 'pipenv install fails with ''Failed to lock Pipfile.lock'' or ''Python X.Y was not found'''
sort_order: 64
---

The Pipfile pins a Python version that isn't on your machine. Either:

- Install that Python version (`uv python install 3.11`, or your OS package manager) and try again.
- Or edit the `[requires]` section of your Pipfile to match the Python version you have, delete `Pipfile.lock`, and run `pipenv install` again.

Other tips for slow / hanging locks:

- `pipenv --rm` to wipe the existing environment, then start over.
- Run from an empty / clean folder.
- Use GitHub Codespaces if local resolution is too slow.
