---
id: '2488656439'
question: 'ValueError: multi_class must be in (''ovo'', ''ovr'')'
sort_order: 10
---

I'm getting "ValueError: multi_class must be in ('ovo', 'ovr')" when using `roc_auc_score` to evaluate feature importance of numerical variables in question 1.

This error occurs because the parameters were passed to `roc_auc_score` incorrectly. Here is the correct usage:

```python
roc_auc_score(y_train, df_train[col])
```