---
id: a2a3669ed9
question: 'Homework 3 (2026) Q3: Should I use `mutual_info_classif` or `mutual_info_score`
  for categorical MI? Why do my results change with `random_state`?'
sort_order: 11
---

Use `sklearn.metrics.mutual_info_score` for HW3 Q3, as in the module 3 lesson. It computes the mutual information exactly for two discrete variables (from their contingency table), so the result is deterministic.

`mutual_info_classif` is a different tool meant for feature selection and can be approximate depending on how your categorical data is represented, which is why you may see:
- differences across `random_state`
- cases where different features end up tied (e.g., both rounding to ~0.03)

Common pitfalls on this homework:

1) Feeding encoded categories as “continuous”.
If you label-encode categories into integers and pass them as part of a dense `X`, sklearn may treat them as continuous and use a k-nearest-neighbors estimator, which introduces approximation and seed dependence. In that case, your MI values can change with `random_state`.

2) Computing MI on one-hot columns.
If you compute MI after `get_dummies`/`DictVectorizer`, each category becomes its own binary column. The “top” MI column can come from a single category (or from the target-encoding scheme) rather than representing the intended original variable. Q3 asks about the original categorical variables, so compute MI on those.

Also: `mutual_info_score` returns values in natural logs (nats), so the numbers are small; follow the homework’s rounding and use only the training set.

Example pattern (exact/consistent):

```python
from sklearn.metrics import mutual_info_score

mi = {c: round(mutual_info_score(y_train, df_train[c]), 2) for c in categorical}
```

Full worked example is available in the provided HW03 solution repo link in your prompt.