---
id: 873bb2b4f6
question: Why do LogisticRegression and LinearRegression+sigmoid produce different
  accuracy?
sort_order: 35
---

They are different models, so different accuracy is expected:

- `LogisticRegression` learns its weights by minimizing log loss, with L2 regularization by default (`C=1.0`).
- `LinearRegression` minimizes squared error without regularization. A sigmoid applied afterward only rescales the predictions; it doesn't change the learned weights.
- Neither model optimizes accuracy directly, so logistic regression isn't guaranteed to have higher accuracy.

Also check your threshold. `sigmoid(z) >= 0.5` is the same as `z >= 0`. Linear regression on a 0/1 target already outputs values around 0–1, so "sigmoid, then threshold at 0.5" predicts 1 for almost every row. Threshold the raw linear prediction at 0.5 instead.
