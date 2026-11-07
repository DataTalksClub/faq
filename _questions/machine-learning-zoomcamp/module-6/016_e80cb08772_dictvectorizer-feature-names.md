---
id: e80cb08772
question: How can I preserve the feature names created by `DictVectorizer` when converting
  the data to an XGBoost `DMatrix`?
sort_order: 16
---

`DictVectorizer` stores the names of its output columns. Call `get_feature_names_out()` after fitting the vectorizer to retrieve those names. It returns a NumPy array, so convert that array to a list when you pass the names to XGBoost.

Assuming you've already fit `dv` and created `X_train` and `y_train`, create the matrix this way:

```python
import xgboost as xgb

feature_names = dv.get_feature_names_out().tolist()
dtrain = xgb.DMatrix(
    X_train,
    label=y_train,
    feature_names=feature_names,
)
```

Use the same ordered feature names for validation data. The names help you read feature-related model output, and the matrix values stay the same.

If XGBoost raises a `ValueError` about `[`, `]`, or `<` in feature names, see [the FAQ about invalid XGBoost feature names](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix).
