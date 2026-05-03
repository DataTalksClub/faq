---
id: 122d2b0aed
question: How do I install the necessary dependencies to run the code?
sort_order: 2
---

To run the provided code, ensure that the `dlt[duckdb]` package is installed. You can do this by executing the following installation command in a Jupyter notebook:

```bash
!pip install dlt[duckdb]
```

If you’re installing it locally, make sure to also have `duckdb` installed before the `duckdb` package is loaded:

```zsh
pip install "dlt[duckdb]"
```