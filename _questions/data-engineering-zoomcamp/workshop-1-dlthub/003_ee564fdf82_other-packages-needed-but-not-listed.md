---
id: ee564fdf82
question: Other packages needed but not listed
sort_order: 3
---

If you are running Jupyter Notebook on a fresh new Codespace or in a local machine with a new virtual environment, you will need these packages to run the starter Jupyter Notebook offered by the teacher. Execute this command to install all the necessary dependencies:

```bash
pip install duckdb pandas numpy pyarrow
```

Or save it into a `requirements.txt` file:

```
dlt[duckdb]
duckdb
pandas
numpy
pyarrow  # Optional, needed for Parquet support
```

Then run:

```bash
pip install -r requirements.txt
```