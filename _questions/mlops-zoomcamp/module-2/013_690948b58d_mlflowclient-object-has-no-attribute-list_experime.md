---
id: 690948b58d
question: MlflowClient object has no attribute 'list_experiments'
sort_order: 13
---

Since version 1.29, the `list_experiments` method was deprecated and then removed in later versions.

Use `search_experiments` instead:

```python
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
experiments = client.search_experiments()
```