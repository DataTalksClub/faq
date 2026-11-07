---
id: cd9c6196d6
question: What’s the difference between `!pip install` and `pip install`?
sort_order: 45
---

In a Jupyter notebook, `!pip install x` runs the shell command `pip install x`. Prefer `%pip install x`: IPython runs it against the environment used by the current notebook kernel.

In a terminal such as Git Bash, omit `!`. Bash treats it as history expansion, so it can run a previous command instead of the command you intended.

If you run `python -m pip install x`, Python uses the `pip` module installed for that interpreter. This targets the intended interpreter. You may still need to use an environment where you have write access to resolve a permission error. Use an environment where you have write access, such as the course project's virtual environment.
