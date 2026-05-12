---
id: c5b67c62c1
question: How do I convert a Jupyter notebook to a .py script?
sort_order: 36
---

From the command line:

```bash
jupyter nbconvert --to script notebook.ipynb
# or
uv run jupyter nbconvert --to script notebook.ipynb
```

In JupyterLab: File → Save and Export Notebook As → Executable Script.
