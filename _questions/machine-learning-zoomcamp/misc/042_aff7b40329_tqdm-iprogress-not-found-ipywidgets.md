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

If you are using **VS Code with the Jupyter extension**, fixing the `ipywidgets` installation might trigger a follow-up prompt:
> *"widgets require us to download supporting files from a 3rd party website (Error loading @jupyter-widgets/controls)"*

To resolve this securely without opening third-party downloads globally across your entire computer, you can restrict the CDN download permissions strictly to this specific repository workspace:

1. Create a `.vscode/` directory at the absolute root of your project repository.
2. Create a `settings.json` file inside it.
3. Paste the following configuration override:

```json
{
    "jupyter.widgetScriptSources": [
        "jsdelivr.com",
        "unpkg.com"
    ]
}
```
