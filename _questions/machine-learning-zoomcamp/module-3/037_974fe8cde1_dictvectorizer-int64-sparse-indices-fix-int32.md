---
id: 974fe8cde1
question: 'How do I fix `ValueError: Only sparse matrices with 32-bit integer indices
  are accepted. Got int64 indices` when using `DictVectorizer` with scikit-learn?'
sort_order: 37
---

The `liblinear` solver accepts only sparse matrices with 32-bit (`int32`) index arrays. Depending on your SciPy and scikit-learn versions, `DictVectorizer` can return a sparse matrix with `int64` index arrays, so `.fit()` fails.

The simplest way is to use a dense matrix, as in the course notebooks:

```python
dv = DictVectorizer(sparse=False)
```

If you want to keep the sparse matrix, cast its index arrays to `int32` before training:

```python
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

train_dicts = [
    {'lead_source': 'paid_ads', 'number_of_courses_viewed': 1},
    {'lead_source': 'organic_search', 'number_of_courses_viewed': 4},
]
y_train = [0, 1]

dv = DictVectorizer()
X_train = dv.fit_transform(train_dicts)

X_train.indices = X_train.indices.astype(np.int32)
X_train.indptr = X_train.indptr.astype(np.int32)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)
```

Apply the same cast to `X_val` and `X_test` after `dv.transform(...)`.
