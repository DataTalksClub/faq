---
id: 23f66acd0a
question: 'Q6: XGBoost DMatrix feature-name TypeError and invalid-name ValueError'
sort_order: 7
---

If `dv.get_feature_names_out()` returns a NumPy array, call `.tolist()` to convert it to a Python list before passing it to `xgb.DMatrix`. This fixes a `TypeError` that says XGBoost expected a sequence of strings but received a NumPy array.

A separate `ValueError` can occur when a feature name contains `[`, `]`, or `<`. XGBoost doesn't allow those characters in `feature_names`. Names such as `ocean_proximity=<1H OCEAN` contain a less-than sign. The equals sign and greater-than sign are allowed by this specific check.

Replace the unsupported characters before creating each `DMatrix`, using the same renamed features for training and validation:

```python
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb

train_records = [
    {"ocean_proximity": "<1H OCEAN", "median_income": 8.3},
    {"ocean_proximity": "INLAND", "median_income": 4.0},
]
y_train = [500000.0, 100000.0]
valid_records = [{"ocean_proximity": "INLAND", "median_income": 5.2}]

dv = DictVectorizer(sparse=True)
X_train = dv.fit_transform(train_records)
X_val = dv.transform(valid_records)

feature_names = dv.get_feature_names_out().tolist()
translation = str.maketrans({
    "[": "_LBRACKET_",
    "]": "_RBRACKET_",
    "<": "_LT_",
})
safe_feature_names = [name.translate(translation) for name in feature_names]

dtrain = xgb.DMatrix(
    X_train,
    label=y_train,
    feature_names=safe_feature_names,
)
dval = xgb.DMatrix(
    X_val,
    feature_names=safe_feature_names,
)
```

Check that the renamed feature names stay unique. For this `ValueError`, you can also omit `feature_names` when creating `DMatrix`, but the model output will no longer show those labels.

See XGBoost's [feature-name validation code for v1.7.6](https://github.com/dmlc/xgboost/blob/v1.7.6/python-package/xgboost/core.py#L1048-L1075), the [DMatrix API](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.DMatrix), and [scikit-learn DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html).
