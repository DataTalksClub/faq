---
id: 78b515b003
question: ImportError when using ColumnQuantileMetric with Evidently
sort_order: 2
---

While working on the monitoring module homework, the instructions mention using `ColumnQuantileMetric`. However, attempting to import it results in an error:

```python
ImportError: cannot import name 'ColumnQuantileMetric' from 'evidently.metrics'
```

The `ColumnQuantileMetric` class does not exist in current versions of Evidently (e.g., 0.7.8+). The correct class to use is `QuantileValue`, which serves the same purpose.

Additionally, the expected argument is not `column_name`, but `column`. This differs from other metrics like `MissingValueCount` that use `column_name`.

If you see a `ValidationError: column field required`, you are likely using the wrong parameter name.

You can use it as follows:

```python
from evidently.metrics import QuantileValue

QuantileValue(column="fare_amount", quantile=0.5)
```

This mismatch likely results from outdated references or changes in the library’s API.