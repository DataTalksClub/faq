---
id: 91675fa206
question: uv keeps using the wrong virtual environment—how do I fix it?
sort_order: 33
---

This usually happens when you have multiple projects in different folders, each with its own `.venv`, and `uv` (or your shell) is still pointing to the previous environment.

Try this:

- Run `deactivate` to exit the currently active virtual environment (if one is active).
- `cd` into the folder for the project you want.
- Create/use the environment in that folder: `uv venv` (this creates a `.venv` inside the current project directory).
- Activate it: `source .venv/bin/activate`.
- Run `which python` (or `where python` on Windows) and confirm it points into that project's `.venv`.
