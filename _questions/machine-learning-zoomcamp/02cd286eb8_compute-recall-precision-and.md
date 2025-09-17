---
course: machine-learning-zoomcamp
id: 02cd286eb8
question: Compute Recall, Precision, and F1 Score using scikit-learn library
section: 4. Evaluation Metrics for Classification
sort_order: 1610
---

In the demonstration video, we are shown how to calculate the precision and recall manually. You can use the Scikit Learn library to calculate the confusion matrix. precision, recall, f1_score without having to first define true positive, true negative, false positive, and false negative.

from sklearn.metrics import precision_score, recall_score, f1_score

precision_score(y_true, y_pred, average='binary')

recall_score(y_true, y_pred, average='binary')

f1_score(y_true, y_pred, average='binary')

Radikal Lukafiardi

