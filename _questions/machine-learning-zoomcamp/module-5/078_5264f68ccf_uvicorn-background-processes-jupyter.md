---
id: 5264f68ccf
question: 'Why does starting Uvicorn with `&` from a Jupyter notebook fail with `OSError:
  Background processes not supported`?'
sort_order: 78
---

This happens because Jupyter/IPython runs shell commands through a piped implementation that doesn’t support backgrounding commands that end with `&`, so `uv run uvicorn ... &` fails with `OSError: Background processes not supported`.

If you need the API to keep running while other notebook cells make requests, start the server from Python using `subprocess.Popen`:

```python
import subprocess
import shutil

uv_path = shutil.which("uv")

server = subprocess.Popen([
    uv_path,
    "run",
    "uvicorn",
    "predict:app",
    "--host", "0.0.0.0",
    "--port", "9696"
])

# ...send requests from other cells...

server.terminate()
server.wait()
```

Alternatively, start Uvicorn in a separate terminal (not inside the notebook) and leave it running while you call the API from the notebook.