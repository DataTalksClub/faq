---
id: a9dddac58b
question: Random Forest gives the same RMSE for all n_estimators values
sort_order: 30
---

Common bugs:

1. Forgetting to call `.fit(X_train, y_train)` inside the loop — you score the same untrained model each iteration.
2. Using `predict_proba` instead of `predict` for a regression task.
3. `max_depth=1` (or another fixed shallow setting) implicitly forcing every model to be a stump.

Make sure each iteration creates a fresh `RandomForestRegressor`, fits it on the training data, predicts on `X_val`, and computes RMSE.
