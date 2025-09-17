---
id: c2f713127c
question: How to get feature importance for XGboost model
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 3870
---

Using model.feature_importances_ can gives you an error:

AttributeError: 'Booster' object has no attribute 'feature_importances_'

Answer: if you train the model like this: model = xgb.train you should use get_score() instead

Ekaterina Kutovaia

