---
id: 3cc0ce528e
question: Is it best to train your model only on the most important features?
sort_order: 27
---

Not necessarily. While some features may show higher importance, it's essential to consider the predictive value of all features. Here are a few guidelines:

- **Evaluate Predictive Value**: Include features that offer additional predictive value. Test your model with and without certain features. If excluding a feature decreases performance, it should be retained.
- **Correlation Consideration**: Some important features might be highly correlated with others. It may be fine to drop some correlated features if they do not improve model performance.
- **Feature Selection Algorithms**: Consider using feature selection methods like L1 regularization (Lasso), which implicitly selects features by shrinking some weights to zero.

Refer to the lessons in week 3 of the churn prediction project for more insights, especially around feature importance for categorical values. Specifically, lesson 3.6 discusses mutual info scores, and lesson 3.10 demonstrates training a Logistic Regression model on all categorical variables.