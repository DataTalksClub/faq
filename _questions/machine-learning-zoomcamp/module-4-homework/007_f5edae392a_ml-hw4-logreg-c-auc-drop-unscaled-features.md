---
id: f5edae392a
question: 'Homework Q4: Logistic regression validation AUC is worse than the single
  feature `lead_score`—is the model broken?'
sort_order: 7
---

No—your model isn’t broken. In this homework, the drop comes from feature scaling, not from the evaluation code.

`annual_income` is on the order of ~50,000, while most other features are between 0 and 10 (and one-hot columns are 0/1). Logistic regression with L2 regularization (e.g., sklearn’s default) is not scale-invariant, so the large unscaled `annual_income` column can dominate the fit when you use a larger `C`.

That’s why:
- `lead_score` alone can achieve a higher ROC AUC in Q1.
- The full model with `C=1` can underperform because the learned weights end up being shaped mainly by the unscaled income scale.
- With stronger regularization (smaller `C`, e.g. `C=0.001`), the weights are shrunk, which reduces the distortion from the unscaled income column—so it can look better.

The fix is to scale numeric columns using only the training split, then reuse the same scaler for validation.

Example:

```python
from sklearn.preprocessing import StandardScaler

numerical = [
    "number_of_courses_viewed",
    "annual_income",
    "interaction_count",
    "lead_score",
]

scaler = StandardScaler().fit(df_train[numerical])

df_train[numerical] = scaler.transform(df_train[numerical])
df_val[numerical] = scaler.transform(df_val[numerical])

# then continue with DictVectorizer + LogisticRegression as usual
```

After scaling, `C` should have little effect on AUC, because the feature scales are comparable. Also remember for the homework: if the instructions ask you to submit the unscaled values for the reported answers, submit those (e.g., ~0.732 for Q2 and the `C=0.001` result), even if scaling would improve performance.