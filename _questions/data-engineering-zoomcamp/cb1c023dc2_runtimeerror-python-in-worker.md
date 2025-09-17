---
course: data-engineering-zoomcamp
id: cb1c023dc2
question: 'RuntimeError: Python in worker has different version 3.11 than that in
  driver 3.10, PySpark cannot run with different minor versions. Please check environment
  variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.'
section: 'Module 5: pyspark'
sort_order: 3820
---

import os

import sys

os.environ['PYSPARK_PYTHON'] = sys.executable

os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

Dataproc Pricing:

