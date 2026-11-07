---
id: 5264f68ccf
question: 'Why does starting Uvicorn with `&` from a Jupyter notebook fail with `OSError: Background processes not supported`?'
sort_order: 78
---

Jupyter/IPython runs shell commands through a piped implementation that doesn't support commands ending in `&`.

Start Uvicorn in a separate terminal, or launch it from Python with `subprocess.Popen`:

```python
import shutil
import subprocess

uv_path = shutil.which("uv")
if uv_path is None:
    raise RuntimeError("Could not find uv on PATH; start Uvicorn in a separate terminal.")

server = subprocess.Popen([
    uv_path,
    "run",
    "uvicorn",
    "predict:app",
    "--host", "0.0.0.0",
    "--port", "9696",
])

# Send requests from other notebook cells while the server runs.

server.terminate()
server.wait()
```

Run the cell from the project directory so `uv run` can find the project. Stop the server when you finish.
