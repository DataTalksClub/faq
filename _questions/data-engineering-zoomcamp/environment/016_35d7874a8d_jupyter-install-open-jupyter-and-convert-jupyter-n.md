---
id: 35d7874a8d
question: 'Jupyter: Install nbconvert, fix ''Failed to spawn'' nbconvert error, and
  convert notebook to Python script (including uv integration)'
sort_order: 16
---

### Install and upgrade nbconvert

First, ensure nbconvert is installed and upgraded:

```bash
pip install nbconvert --upgrade
```

### Resolve 'Failed to spawn: `nbconvert`' error (uv-based workflow)

If the issue persists, add nbconvert support to uv and then run nbconvert:

```bash
uv add jupyter nbconvert
uv run jupyter nbconvert --to=script notebook.ipynb
```

### Alternative: Convert Jupyter Notebook to Python Script (nbconvert)

You can also convert directly using nbconvert without uv:

```bash
python3 -m jupyter nbconvert --to=script <your_notebook.ipynb>
```

Replace <your_notebook.ipynb> with the actual notebook filename, e.g. notebook.ipynb.
