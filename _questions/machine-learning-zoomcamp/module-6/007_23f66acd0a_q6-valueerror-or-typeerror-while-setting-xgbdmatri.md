---
id: 23f66acd0a
question: 'Q6: ValueError: feature_names must not contain [, ], or < when creating
  `xgb.DMatrix` with DictVectorizer'
sort_order: 7
---

When creating `xgb.DMatrix`, `feature_names` has strict formatting rules. If your `DictVectorizer` produces names with characters like `[` `]` `<` `>` or `=`, XGBoost will raise:

`ValueError: feature_names must not contain [, ], or <`

To fix it, clean/rename the feature names before passing them to `DMatrix` (keep the same cleaned names for train/val/test).

Example using regex:

```python
import re
import xgboost as xgb

# feature names from DictVectorizer
feature_names = dv.get_feature_names_out().tolist()

# replace invalid characters with underscore
clean_feature_names = [re.sub(r'[\[\]<> =]', '_', f).replace(' ', '_') for f in feature_names]

dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=clean_feature_names)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=clean_feature_names)
```

If you don’t need to set `feature_names` explicitly, another option is to omit `feature_names=` entirely; XGBoost will still train, but feature names won’t be preserved for interpretability.