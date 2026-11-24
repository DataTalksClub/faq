---
id: 24aa4483c6
question: Why does the first cell of the lesson notebook (local) hang in VS Code on
  Windows?
sort_order: 46
---

If the notebook cell keeps spinning and no execution number appears, VS Code is usually waiting for a Jupyter kernel that fails to start (often because it’s using the wrong local Python).

To fix it on Windows:

1. Use the course’s environment with `uv` (don’t rely on VS Code’s default “Python 3” kernel).
2. From the repository root, create the environment with the notebooks extras:

```powershell
uv sync --extra notebooks
```

3. In VS Code, select the notebook kernel via the kernel picker (top-right of the notebook) → **Select Another Kernel** → **Python Environments**, then choose the repository environment Python (typically `.venv\Scripts\python.exe`).
4. Restart the kernel and run the notebook from the top.

Important: the course repository requires Python `>=3.12,<3.14` (check `pyproject.toml`). If you only have Python 3.14 installed, installing `ipykernel` into it won’t be the fix; use the version provided/managed by `uv`.

If it still spins, open **View → Output** and select **Jupyter** in the dropdown to see why the kernel failed to start.