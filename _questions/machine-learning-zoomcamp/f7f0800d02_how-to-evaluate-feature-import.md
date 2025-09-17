---
course: machine-learning-zoomcamp
id: f7f0800d02
question: How to evaluate feature importance for numerical variables with AUC?
section: 4. Evaluation Metrics for Classification
sort_order: 1660
---

You can use roc_auc_score function from sklearn.metrics module and pass the vector of the target variable (‘above_average’) as the first argument and the vector of feature values as the second one. This function will return AUC score for the feature that was passed as a second argument.

(Denys Soloviov)

