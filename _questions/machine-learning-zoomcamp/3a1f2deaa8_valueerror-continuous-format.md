---
course: machine-learning-zoomcamp
id: 3a1f2deaa8
question: 'ValueError: continuous format is not supported'
section: 6. Decision Trees and Ensemble Learning
sort_order: 2510
---

Calling roc_auc_score() to get auc is throwing the above error.

Solution to this issue is to make sure that you pass y_actuals as 1st argument and y_pred as 2nd argument.

roc_auc_score(y_train, y_pred)

Hareesh Tummala

