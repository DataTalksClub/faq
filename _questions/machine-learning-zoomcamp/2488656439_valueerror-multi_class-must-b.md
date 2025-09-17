---
id: 2488656439
question: ValueError: multi_class must be in ('ovo', 'ovr')
section: 4. Evaluation Metrics for Classification
course: machine-learning-zoomcamp
sort_order: 1520
---

I’m getting “ValueError: multi_class must be in ('ovo', 'ovr')” when using roc_auc_score to evaluate feature importance of numerical variables in question 1.

I was getting this error because I was passing the parameters to roc_auc_score incorrectly (df_train[col] , y_train) . The correct way is to pass the parameters in this way: roc_auc_score(y_train, df_train[col])

Asia Saeed

