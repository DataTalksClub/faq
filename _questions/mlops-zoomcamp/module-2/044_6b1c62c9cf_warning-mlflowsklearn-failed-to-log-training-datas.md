---
id: 6b1c62c9cf
question: 'WARNING: mlflow.sklearn: Failed to log training dataset information to
  MLflow Tracking.'
sort_order: 44
---

When using MLflow's autolog function, you may encounter the following warning:

```
WARNING mlflow.sklearn: Failed to log training dataset information to MLflow Tracking. Reason: 'numpy.ndarray' object has no attribute 'toarray'
```

This occurs because the autolog function is attempting to log your dataset. MLflow expects the dataset to be in a `pd.DataFrame` format. If you're following course code that provides a `numpy.ndarray`, MLflow fails as the `numpy.ndarray` is already an array.

Since we are not processing datasets in this zoomcamp, use the following parameter in the autolog function to prevent logging datasets:

```python
log_datasets = False
```
