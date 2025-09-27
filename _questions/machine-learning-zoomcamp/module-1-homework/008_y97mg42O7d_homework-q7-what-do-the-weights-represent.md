---
id: y97mg42O7d
question: 'Homework Q7: What do the weights represent?'
sort_order: 8
---

The weight vector, `w`, contains the coefficients for a linear model fit between the target variable, `y`, and the input features in `X`, with the model estimate of `y`, `y_est` defined as follows:
$$ y_{est} = w[0]*X[0] + w[1]*X[1] $$
where the values in brackets refer to each column of the feature matrix, `X`, and the corresponding row of the weight vector, `w`. Each value in `w` describes the slope of the trend line that fits `y` the best for each feature. As we'll learn in Module 2, least squares yields a "best" fit that minimizes the squared difference between `y` and `y_est`. The weights, `w`, can be checked to see if they're reasonable by multiplying `X` by the weight vector, `w`:
$$ y_{est} = X.dot(w) $$
This should produce a vector, `y_est` that is similar, plus or minus some error, to the original target variable, `y`.
