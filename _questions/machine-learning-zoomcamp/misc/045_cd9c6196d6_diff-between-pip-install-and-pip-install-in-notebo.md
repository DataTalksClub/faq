---
id: cd9c6196d6
question: What’s the difference between `!pip install` and `pip install`?
sort_order: 45
---

In a notebook (Jupyter), `!pip install ...` uses the `!` prefix to run a shell command from a notebook cell. So `!pip install x` installs `x` using `pip`.

If you’re in Jupyter, you can also use `%pip install x`—the `%pip` magic installs into the same Python environment that the notebook kernel is using.

In a terminal like Git Bash, don’t use `!`. Bash treats `!` as history expansion and can rerun an earlier command you didn’t intend.

If you hit permission issues in Git Bash, run pip via Python instead (avoids common pip/path confusion):

```bash
python -m pip install x
```