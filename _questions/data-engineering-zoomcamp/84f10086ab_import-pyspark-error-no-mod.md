---
id: 84f10086ab
question: Import pyspark - Error: No Module named ‘pyspark’
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3340
---

Ensure that your `PYTHONPATH` is set correctly to include the PySpark library. You can check if PySpark is pointing to the correct location by running:

import pyspark

print(pyspark.__file__)

It should point to the location where PySpark is installed (e.g., `/home/<your username>/spark/spark-3.x.x-bin-hadoop3.x/python/pyspark/__init__.py`)

