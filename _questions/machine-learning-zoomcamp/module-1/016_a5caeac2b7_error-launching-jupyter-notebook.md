---
id: a5caeac2b7
question: 'Jupyter: ImportError "cannot import name ''contextfilter'' from ''jinja2''"'
sort_order: 16
---

`contextfilter` was removed in Jinja 3.1, but old `nbconvert` versions still try to import it. Upgrade nbconvert:

```bash
uv add --upgrade nbconvert
# or
pip install --upgrade nbconvert
```

Then restart the kernel / Jupyter server.
