---
id: 1e3f5f4a5d
question: Why is my Q5 std 0.013 instead of 0.007?
sort_order: 7
---

Copy the model constructor exactly as the homework specifies:

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

The bare constructor `LogisticRegression(max_iter=1000)` silently uses the default solver `lbfgs`. On the 2026 lead-scoring data it throws `ConvergenceWarning: lbfgs failed to converge` and produces fold AUCs around [0.776, 0.787, 0.799, 0.811, 0.780] with std **0.013** — a different multiple-choice option. With `solver='liblinear'` the folds are around [0.731, 0.730, 0.736, 0.741, 0.721] with std **0.007**, the correct answer. Same data, same seed, wrong solver, wrong answer.

The warning in your output is the tell: if you see `ConvergenceWarning` in Q5, your solver is wrong. Also fit a fresh `DictVectorizer` inside each fold — fitting it once outside the loop leaks validation data into training.
