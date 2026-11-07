---
id: cd9c6196d6
question: What’s the difference between `!pip install` and `pip install`?
sort_order: 45
---

In a Jupyter notebook, `!pip install x` runs the shell command `pip install x`. Prefer `%pip install x`: IPython runs it against the environment used by the current notebook kernel.

In a terminal such as Git Bash, omit `!`. Bash treats it as history expansion, so it can run a previous command instead of the command you intended.

Run `python -m pip install x` to use the `pip` module for the selected Python interpreter. If it fails with a permission error, use an environment where you have write access, such as the course project's virtual environment.
