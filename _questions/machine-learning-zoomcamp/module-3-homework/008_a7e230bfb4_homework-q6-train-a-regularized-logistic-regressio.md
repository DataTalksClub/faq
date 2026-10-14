---
id: a7e230bfb4
question: 'Homework Q6: Train a regularized logistic regression
  with C=0.0'
sort_order: 8
---

This is not possible since the parameter `C` represents the inverse of the regularization strength. Setting `C` to 0 means infinite regularization. Attempting this with the scikit-learn module of Logistic Regression will result in a `ValueError`.

Smaller `C` means stronger regularization: coefficients are pushed toward zero, so predictions (and validation accuracy) change. Larger `C` means weaker regularization and a closer fit to the training data.
