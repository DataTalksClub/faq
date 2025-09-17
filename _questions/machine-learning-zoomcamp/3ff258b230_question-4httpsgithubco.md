---
course: machine-learning-zoomcamp
id: 3ff258b230
question: '[Question 4](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2023/02-regression/homework.md#question-4):
  what is `r`, is it the same as `alpha` in [sklearn.Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)[()](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)?'
section: 2. Machine Learning for Regression
sort_order: 720
---

In the context of regression, particularly with regularization:

r typically represents the regularization parameter in some algorithms. It controls the strength of the penalty applied to the coefficients of the regression model to prevent overfitting.

In sklearn.Ridge(), the parameter alpha serves the same purpose as r. It specifies the amount of regularization applied to the model. A higher value of alpha increases the amount of regularization, which can reduce model complexity and improve generalization.

`r` is a regularization parameter.

It’s similar to `alpha` in [sklearn.Ridge()](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html), as both control the "strength" of regularization (increasing both will lead to stronger regularization), but mathematically not quite, here's how both are used:

[sklearn.Ridge()](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)

||y - Xw||^2_2 + alpha * ||w||^2_2

[lesson’s notebook](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/02-regression/notebook.ipynb) (`train_linear_regression_reg` function)

XTX = XTX + r * np.eye(XTX.shape[0])

`r` adds “noise” to the main diagonal to prevent multicollinearity, which “breaks” finding inverse matrix.

