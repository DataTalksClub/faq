---
id: 74486f4c87
question: Using GitHub Codespaces and added a Python package, but imports fail in
  my Jupyter notebook—what should I do?
sort_order: 35
---

The notebook is probably using a different Python environment from the one
where you installed the package.

Run this in a notebook cell to see the kernel's interpreter:

```python
import sys

print(sys.executable)
```

Then run `uv pip list` in the Codespaces terminal. If the package is listed
there but `sys.executable` does not point into the same project environment,
use the kernel picker near the top of the notebook to select the repository's
`.venv`.

Restart the kernel after switching, then try the import again.
