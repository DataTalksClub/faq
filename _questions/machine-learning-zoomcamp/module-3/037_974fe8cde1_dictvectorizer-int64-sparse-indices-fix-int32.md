---
id: 974fe8cde1
question: 'How do I fix `ValueError: Only sparse matrices with 32-bit integer indices
  are accepted. Got int64 indices` when using `DictVectorizer` with scikit-learn?'
sort_order: 37
---

This error means scikit-learn expects a sparse matrix whose internal index arrays use 32-bit integers, but `DictVectorizer` produced a CSR matrix with 64-bit index arrays (`int64`).

Fix it by converting the sparse matrix index arrays to `int32` right before calling `.fit()`:

```python
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

dv = DictVectorizer()
train_dict = df[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

# Force sparse matrix indices to 32-bit integers
X_train.indices = X_train.indices.astype(np.int32)
X_train.indptr = X_train.indptr.astype(np.int32)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)
```

Why this happens: with newer NumPy (2.x) and scikit-learn, `DictVectorizer` can emit a sparse feature matrix whose index pointer arrays are `int64`. Some scikit-learn estimators/solvers strictly require `int32` sparse indices, so training fails with the `ValueError`. Casting `indices` and `indptr` resolves the mismatch without changing your data or model setup.