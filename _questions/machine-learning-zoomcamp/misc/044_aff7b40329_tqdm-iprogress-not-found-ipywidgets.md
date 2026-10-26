---
id: aff7b40329
question: 'How to fix the tqdm warning: "IProgress not found" in Jupyter (missing
  ipywidgets)?'
sort_order: 44
---

`tqdm` shows this warning when it tries to draw an interactive progress bar in Jupyter but can't find `ipywidgets`. Either it isn't installed, or it's installed in a different environment from the notebook kernel.

Install `ipywidgets` in the environment that runs the notebook.

With `uv`:

```bash
uv add ipywidgets
```

Otherwise, use pip or conda:

```bash
pip install ipywidgets
conda install -c conda-forge ipywidgets
```

Then restart the Jupyter kernel (or the VS Code notebook session) so it picks up the new package.

In VS Code with the Jupyter extension, you may then see "widgets require us to download supporting files from a 3rd party website (Error loading @jupyter-widgets/controls)".

To allow these downloads only for this project, create `.vscode/settings.json` at the project root with this setting:

```json
{
    "jupyter.widgetScriptSources": [
        "jsdelivr.com",
        "unpkg.com"
    ]
}
```
