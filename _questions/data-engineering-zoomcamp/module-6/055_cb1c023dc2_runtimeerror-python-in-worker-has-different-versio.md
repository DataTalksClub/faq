---
id: cb1c023dc2
question: 'RuntimeError: Python in worker has different version 3.11 than that in
  driver 3.10, PySpark cannot run with different minor versions. Please check environment
  variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.'
sort_order: 55
---

To resolve the version mismatch error between the worker and driver Python versions in PySpark, set the environment variables `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` to the same executable.

```python
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
```

For further information on Dataproc Pricing, visit: [Dataproc Pricing](https://cloud.google.com/dataproc/pricing#on_gke_pricing)