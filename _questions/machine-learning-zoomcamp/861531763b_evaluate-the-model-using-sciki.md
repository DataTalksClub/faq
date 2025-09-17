---
course: machine-learning-zoomcamp
id: 861531763b
question: Evaluate the Model using scikit learn metrics
section: 4. Evaluation Metrics for Classification
sort_order: 1630
---

Model evaluation metrics can be easily computed using off the shelf calculations available in scikit learn library. This saves a lot of time and more precise compared to our own calculations from the scratch using numpy and pandas libraries.

from sklearn.metrics import (accuracy_score,

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

(Harish Balasundaram)

