---
id: 59ad389756
question: 'PySpark on Windows: "Python was not found; run without arguments to install
  from the Microsoft Store"'
sort_order: 1
---

PySpark spawns Python workers via `python.exe`, and on Windows that often resolves to the Microsoft Store stub if a real Python isn't on `PATH` first. The error appears when running UDFs (or any operation that forks a worker).

`PYSPARK_PYTHON` tells Spark which interpreter to use; setting it explicitly fixes this.

## Fix

In the same shell where you launch PySpark, set `PYSPARK_PYTHON` to your project's Python:

```bash
# inside an activated venv:
export PYSPARK_PYTHON="$(which python)"
export PYSPARK_DRIVER_PYTHON="$(which python)"
```

Or set it in the script before creating the SparkSession:

```python
import os, sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
```

Running scripts via `uv run python script.py` also avoids the issue because `uv` invokes the venv's interpreter directly.
