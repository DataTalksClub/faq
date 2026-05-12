---
id: a55ee615db
question: Reading parquet files with Pandas (pyarrow dependency)
sort_order: 52
---

A module that was compiled using NumPy 1.x cannot be run in NumPy 2.2.4 as it may crash.

```
AttributeError: module 'pyarrow' has no attribute '__version__'
```

Downgrade the version of your numpy:

```bash
pip uninstall numpy -y

conda remove numpy --force

conda clean --all -y

conda install numpy=1.26 -y
```