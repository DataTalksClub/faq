---
id: c213e31ea0
question: 'How to use AUC for numerical features?'
sort_order: 8
---

When calculating the ROC AUC score using [`sklearn.metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html), the function expects two parameters: `y_true` and `y_score`. For each numerical value in the dataframe, it will be passed as the `y_score` to the function, and the target variable will be passed as `y_true` each time.