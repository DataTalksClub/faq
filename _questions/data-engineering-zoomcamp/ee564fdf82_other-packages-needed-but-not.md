---
course: data-engineering-zoomcamp
id: ee564fdf82
question: Other packages needed but not listed
section: Workshop 1 - dlthub
sort_order: 4380
---

If you are running Jupyter Notebook on a fresh new Codespace or in local machine with a new Virtual Environment, you will need this package to run the starter Jupyter Notebook offered by the teacher. Execute this:

Install all the necessary dependencies

pip install duckdb pandas numpy pyarrow

Or save it into a requirements.txt file:

dlt[duckdb]

duckdb

pandas

numpy

pyarrow  # Optional, needed for Parquet support

Then run pip install -r requirements.txt

