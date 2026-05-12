---
id: 02cd286eb8
question: Compute Recall, Precision, and F1 Score using scikit-learn library
sort_order: 17
---

You can use the Scikit Learn library to calculate precision, recall, and F1 score without having to define true positive, true negative, false positive, and false negative manually.

```python
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_true, y_pred, average='binary')
recall = recall_score(y_true, y_pred, average='binary')
f1 = f1_score(y_true, y_pred, average='binary')
```

Replace `y_true` and `y_pred` with your actual data. The `average` parameter is set to `'binary'` by default for binary classification.