---
id: 6739977244
question: Why are all my predicted probabilities negative when I use predict_log_proba?
sort_order: 30
---

`predict_log_proba` returns log-probabilities (always ≤ 0), not probabilities. For AUC and threshold-based metrics, use `predict_proba` and take the positive class column:

```python
y_pred = model.predict_proba(X_val)[:, 1]
```
