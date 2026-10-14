---
id: c267eb97a2
question: 'Homework 2 Q4: Why does validation RMSE get worse as I increase the regularization parameter r?'
sort_order: 6
---

That can be correct. Regularization doesn't always help, and the lecture's implementation makes it especially likely to hurt here.

`train_linear_regression_reg` adds `r * np.eye(...)` to the whole diagonal of `XᵀX`, including the position of the column of ones. So the **intercept (bias) is penalized too**. The homework features are not scaled (`model_year` is around 2000, `vehicle_weight` in the thousands), so the best model needs a large intercept to offset them. As `r` grows, ridge shrinks that intercept toward 0 and predictions drift away from the target.

You can see this by excluding the bias from the penalty:

```python
X1 = np.column_stack([np.ones(len(X_train)), X_train])
P = r * np.eye(X1.shape[1])
P[0, 0] = 0  # don't regularize the bias
w = np.linalg.solve(X1.T @ X1 + P, X1.T @ y_train)
```

With only four numeric features and thousands of rows, there's little overfitting or collinearity for ridge to fix. In the lecture's car-price example, regularization helped because duplicated and one-hot columns made `XᵀX` nearly singular.

For the homework, keep the lecture code as it is. In practice, standardize the features and don't penalize the intercept. Scikit-learn's `Ridge` already leaves the intercept unpenalized.
