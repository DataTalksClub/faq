---
id: 9cfe589a2e
question: 'Video 3.2.8: ValueError: not enough values to unpack (expected 3, got 1)'
sort_order: 29
---

Ensure the upstream connections for the xgboost training are in the right order:

- `data` → `training_set`
- `data_2` → `hyperparameter_tuning/xgboost`

If your tree doesn't look like this:

1. Remove the connections for the `xgboost` block.
2. Reconnect starting with the training set, then `hyperparameter_tuning/xgboost`.
