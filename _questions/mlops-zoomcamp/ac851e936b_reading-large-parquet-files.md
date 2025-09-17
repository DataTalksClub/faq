---
id: ac851e936b
question: Reading large parquet files
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 510
---

I have faced a problem while reading the large parquet file. I tried some workarounds but they were NOT successful with Jupyter.

The error message is:

IndexError: index 311297 is out of bounds for axis 0 with size 131743

I solved it by performing the homework directly as a python script.

Added by Ibraheem Taha ()

You can try using the Pyspark library

Answered by kamaldeen ()

Parquet format can be read in chunks: . (IK)

