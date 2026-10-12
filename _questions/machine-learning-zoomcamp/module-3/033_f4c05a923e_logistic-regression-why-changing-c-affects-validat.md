---
id: f4c05a923e
question: Why does changing `C` in Logistic Regression change validation accuracy?
sort_order: 33
---

In scikit-learn Logistic Regression, `C` is the inverse of the regularization strength.

- Smaller `C` ⇒ stronger regularization ⇒ more penalty on large coefficients. This can lead to simpler decision boundaries and potentially underfitting.
- Larger `C` ⇒ weaker regularization ⇒ less penalty on coefficients. This can allow the model to fit the training data more closely and potentially overfit.

Because regularization directly affects the learned coefficients, changing `C` changes the model’s predictions on the validation set, so the validation accuracy can change as well.

A common approach is to try several candidate `C` values, evaluate each one on the validation set (or via cross-validation), and pick the `C` that gives the best validation performance.