---
id: 1913393ea4
question: 'PicklingError: Could not serialize object: IndexError: tuple index out
  of range'
sort_order: 54
---

This version combination worked for resolving the issue:

- **PySpark**: 3.3.2
- **Pandas**: 1.5.3

If you continue to encounter the error:

```
Py4JJavaError: An error occurred while calling o180.showString. : org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 6.0 failed 1 times, most recent failure: Lost task 0.0 in stage 6.0 (TID 6) (host.docker.internal executor driver): org.apache.spark.SparkException: Python worker failed to connect back.
```

Try running the following before initializing `SparkSession`:

```python
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
```