---
id: f580e98fdc
question: 'Waitress on Windows / Git Bash: "waitress-serve: command not found"'
sort_order: 35
---

`pip install waitress` does install `waitress-serve.exe`, but Python's `Scripts/` directory may not be on Git Bash's `PATH`. The pip output usually warns about this:

```
WARNING: The script waitress-serve.exe is installed in 'C:\Users\<you>\...\Scripts'
which is not on PATH.
```

To fix, add that `Scripts` directory to Git Bash's `PATH` permanently:

```bash
nano ~/.bashrc
# add this line, with the path from the warning:
export PATH="/c/Users/<you>/.../Scripts:$PATH"
```

Close Git Bash and reopen it. `waitress-serve --help` should now work.

If you're using `uv`, this isn't an issue because `uv run waitress-serve ...` runs the binary directly from the venv without needing it on `PATH`.
