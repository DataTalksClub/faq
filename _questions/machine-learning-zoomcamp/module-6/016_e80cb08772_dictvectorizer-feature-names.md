---
id: e80cb08772
question: How can I preserve the feature names created by `DictVectorizer` when converting
  the data to an XGBoost `DMatrix`?
sort_order: 16
---

After `DictVectorizer` transforms your dataframe, `X_train` contains the encoded values, but the feature names are not automatically attached to the NumPy/scipy matrix you pass into `xgb.DMatrix`. You can preserve meaningful names by pulling them from the fitted vectorizer and passing them as `feature_names`.

First, get the names from the fitted vectorizer:

`feature_names = list(dv.get_feature_names_out())`

Then create your `DMatrix` and pass `feature_names` explicitly:

```python
feature_names = list(dv.get_feature_names_out())

dtrain = xgb.DMatrix(
    X_train,
    label=y_train,
    feature_names=feature_names,
)

dval = xgb.DMatrix(
    X_val,
    label=y_val,
    feature_names=feature_names,
)
```

This doesn’t change training or predictions—it just attaches the metadata so later inspection (e.g., feature-related outputs) is easier to interpret. 

If you hit a type error, note that `xgb.DMatrix` expects a list of strings; converting `dv.get_feature_names_out()` to a Python list (or using `.tolist()`) avoids the `numpy.ndarray` issue.