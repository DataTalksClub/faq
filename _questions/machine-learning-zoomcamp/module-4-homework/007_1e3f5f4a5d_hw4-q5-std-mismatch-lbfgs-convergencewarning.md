---
id: 1e3f5f4a5d
question: 'Homework 4 Q5: Why does my std not match the expected option, and why do I
  see `ConvergenceWarning: lbfgs failed to converge`?'
sort_order: 7
---

You're probably not using the model constructor from the homework.

Copy it exactly, including `solver='liblinear'`:

```python
from sklearn.model_selection import KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

kfold = KFold(n_splits=5, shuffle=True, random_state=1)

scores = []
for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train['converted'].values
    y_val = df_val['converted'].values

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(df_train.drop(columns=['converted']).to_dict(orient='records'))
    X_val = dv.transform(df_val.drop(columns=['converted']).to_dict(orient='records'))

    model = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000)
    model.fit(X_train, y_train)
    scores.append(roc_auc_score(y_val, model.predict_proba(X_val)[:, 1]))
```

`LogisticRegression(max_iter=1000)` without a `solver` uses the default `lbfgs` solver. On the homework data it doesn't converge, gives different fold AUCs, and produces a std that matches a different option.

If you see `ConvergenceWarning` in Q5, check the solver first. Also fit a fresh `DictVectorizer` inside each fold. Fitting it once outside the loop leaks validation data into training.
