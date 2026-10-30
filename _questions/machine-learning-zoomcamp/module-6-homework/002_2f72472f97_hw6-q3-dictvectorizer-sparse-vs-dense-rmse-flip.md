---
id: 2f72472f97
question: 'Homework 6 Q3: Why does sweeping `n_estimators` give different RMSE ranking
  when I use `DictVectorizer(sparse=False)` vs `sparse=True`?'
sort_order: 2
---

In Homework 6 Q3, you should use `DictVectorizer(sparse=True)` exactly as the homework specifies. If you accidentally use the default `DictVectorizer(sparse=False)`, you can get a different best `n_estimators` (for example, 150 instead of 100), even with the same `random_state` and the same train/validation split.

Why the numbers change: scikit-learn’s tree/ensemble code can take a different internal path for CSR sparse matrices vs dense arrays. The model is conceptually the same, but floating-point summation order and tie-breaking during split search differ slightly. That small change can move a few samples across leaves, and with a very tight RMSE margin, the “lowest RMSE” ranking can flip.

What to do:
- Create the vectorizer with `sparse=True`.
- Fit on the training dicts and transform validation dicts as usual.

Example:
```python
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=True)  # required by the homework
X_train = dv.fit_transform(df_train.to_dict(orient='records'))
X_val = dv.transform(df_val.to_dict(orient='records'))
```

If you used `sparse=False`, redo Q3 with `sparse=True`—the Q3 answer will match the homework’s expected selection (e.g., submit `100` in the scenario described).