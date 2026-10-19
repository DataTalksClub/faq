---
id: aff7b40329
question: 'How to fix the tqdm warning: "IProgress not found" in Jupyter (missing
  ipywidgets)?'
sort_order: 42
---

This warning happens when `tqdm` tries to display an interactive progress bar in Jupyter, but the Jupyter widget backend (`ipywidgets`) isn’t installed (or isn’t visible in your currently active environment).

To fix it:
- Install `ipywidgets` in your active environment (the one where you run the notebook).
- If you use `uv`, run:

```bash
uv add ipywidgets
```

- Otherwise use one of:
  - `pip install ipywidgets`
  - `conda install -c conda-forge ipywidgets`
- Restart the Jupyter kernel / reload the notebook (or restart the VS Code notebook session) so the newly installed package is detected.