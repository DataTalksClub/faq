---
id: 091cf6f73e
question: '`TypeError: Expecting a sequence of strings for feature names, got: <class
  ''numpy.ndarray''> ` when training xgboost model.'
sort_order: 2440
---

If you’re getting this error, It is likely because the feature names in dv.get_feature_names_out() are a np.ndarray instead of a list so you have to convert them into a list by using the to_list() method.

Ali Osman

