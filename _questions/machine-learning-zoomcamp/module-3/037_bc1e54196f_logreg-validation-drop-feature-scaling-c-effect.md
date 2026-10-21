---
id: bc1e54196f
question: Why does my logistic regression validation AUC drop vs the single feature
  AUC, and why does `C=0.001` beat `C=1`?
sort_order: 37
---

Your model isn’t broken—this behavior usually comes from feature scaling interacting with L2 regularization.

In the homework setup, one numeric column (e.g. `annual_income`) can have a much larger scale (tens of thousands) than the other features (often 0–10 or one-hot 0/1). Logistic regression with regularization (scikit-learn’s default L2 penalty) is not scale-invariant, so the optimizer will let the large-magnitude feature dominate when `C` is larger.

As a result:
- With larger `C` (weaker regularization, e.g. `C=1`), the model can over-rely on the unscaled `annual_income` column, making the score ranking on validation worse than ranking by `lead_score` alone.
- With smaller `C` (stronger regularization, e.g. `C=0.001`), the weights shrink, limiting how much the unscaled income feature can distort the fit—so validation AUC improves.

How to fix (recommended for your own modeling):
1. Scale numeric columns using `fit` on the training data only.
2. Apply the same scaler to validation/test.
3. Then proceed with `DictVectorizer` (fit on train, transform val) and train logistic regression.

Example:
```python
from sklearn.preprocessing import StandardScaler

numerical = ["number_of_courses_viewed", "annual_income", "interaction_count", "lead_score"]

scaler = StandardScaler().fit(df_train[numerical])
df_train[numerical] = scaler.transform(df_train[numerical])
df_val[numerical] = scaler.transform(df_val[numerical])

# then continue with DictVectorizer + LogisticRegression as usual
```

Important for the homework answers:
- If you’re submitting the specific values the questions ask for, use the required preprocessing (the unscaled setup). In that case, lower validation AUC (e.g. ~0.732) and `C=0.001` beating `C=1` are expected.

Takeaways:
- Always compare against the best single-feature baseline.
- For regularized linear models, scale numeric features.
- Hyperparameters like `C` may appear to “flip” depending on whether features are on comparable scales.