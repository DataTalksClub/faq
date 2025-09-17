---
course: mlops-zoomcamp
id: 78b515b003
question: ImportError when using ColumnQuantileMetric with Evidently
section: 'Module 5: Monitoring'
sort_order: 1910
---

[Problem description]
 While working on the monitoring module homework, the instructions mention using ColumnQuantileMetric. However, attempting to import it results in an error:
 ImportError: cannot import name 'ColumnQuantileMetric' from 'evidently.metrics'

[Solution description]
 The ColumnQuantileMetric class does not exist in current versions of Evidently (e.g., 0.7.8+). The correct class to use is QuantileValue, which serves the same purpose.

Additionally, the expected argument is not column_name, but column. This differs from other metrics like MissingValueCount that use column_name.

If you see a ValidationError: column field required, you are likely using the wrong parameter name.

You can use it as follows:

from evidently.metrics import QuantileValue

QuantileValue(column="fare_amount", quantile=0.5)

This mismatch likely results from outdated references or changes in the library’s API.

Added by Yann Pham-Van

