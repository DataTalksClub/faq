---
id: 866f5d58d2
question: 'What does ''use the numerical variable as a score'' mean for AUC?'
sort_order: 29
---

You're treating each numerical feature as if it were the model's predicted score, and computing how well it discriminates the two classes:

```python
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_train, df_train['balance'])
```

If `auc < 0.5`, invert the score by passing `-df_train['column']` (or take `1 - auc`). The numerical values don't need to be in [0, 1] — AUC only cares about ranking, not magnitudes.
