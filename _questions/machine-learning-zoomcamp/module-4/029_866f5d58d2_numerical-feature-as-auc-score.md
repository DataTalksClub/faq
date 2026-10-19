---
id: 866f5d58d2
question: Why can a numerical feature have a ROC AUC below 0.5, and why can we invert
  the feature when using AUC for feature importance?
sort_order: 29
---

A ROC AUC below 0.5 doesn’t mean the feature is useless—it often means the feature is predictive but in the opposite direction.

AUC measures how well your feature values rank positive examples above negative ones. If your feature tends to give higher scores to the negative class (instead of the positive class), then the ranking is “reversed,” and the AUC can drop below 0.5.

When you compute AUC using a single numerical feature as the `y_score`, you can flip the ranking by negating that feature:

```python
from sklearn.metrics import roc_auc_score

auc = roc_auc_score(y_train, df_train[feature])
if auc < 0.5:
    auc = roc_auc_score(y_train, -df_train[feature])
```

Negating the feature reverses the order of the scores, turning a reversed relationship into a correctly oriented one. This is why, for feature importance based on AUC, an AUC < 0.5 can indicate meaningful predictive information—just with the opposite sign.