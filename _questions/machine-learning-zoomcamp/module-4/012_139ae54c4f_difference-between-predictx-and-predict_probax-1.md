---
id: 139ae54c4f
question: Difference between `predict(X)` and `predict_proba(X)[:, 1]`
sort_order: 12
---

Using `predict(X)` provides binary classification predictions, which are either 0 or 1. This could result in inaccurate evaluation values.

The alternative is to use `predict_proba(X)[:, 1]`, which gives the probability that the value belongs to a specific class.

`predict_proba` displays probabilities for each class.