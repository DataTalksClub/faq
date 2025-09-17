---
id: a55ee615db
question: Reading parquet files with Pandas (pyarrow dependency)
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 770
---

Error

A module that was compiled using NumPy 1.x cannot be run in NumPy 2.2.4 as it may crash.
OR

AttributeError: module 'pyarrow' has no attribute '__version__'

Solution: Down grade the version of your numpy

pip uninstall numpy -y

conda remove numpy --force

conda clean --all -y

conda install numpy=1.26 -y

Added by Uchechukwu Fortune Njoku

