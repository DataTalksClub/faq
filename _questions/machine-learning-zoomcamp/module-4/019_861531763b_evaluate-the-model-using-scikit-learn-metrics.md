---
id: 861531763b
question: Evaluate the Model using scikit learn metrics
sort_order: 19
---

Model evaluation metrics can be easily computed using the off-the-shelf calculations available in the scikit-learn library. This method is more precise compared to calculating from scratch using numpy and pandas libraries.

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

accuracy = accuracy_score(y_val, y_pred)
precision = precision_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)
roc_auc = roc_auc_score(y_val, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1-Score: {f1}')
print(f'ROC AUC: {roc_auc}')
```