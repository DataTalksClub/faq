---
id: 4c3e29589e
question: Why do we use cross validation?
sort_order: 18
---

Cross-validation evaluates the performance of a model and chooses the best hyperparameters. It does this by splitting the dataset into multiple parts (folds), typically 5 or 10. It then trains and evaluates your model multiple times, each time using a different fold as the validation set and the remaining folds as the training set.

"C" is a hyperparameter typically associated with regularization in models like Support Vector Machines (SVM) and logistic regression.

- **Smaller "C" values**: They introduce more regularization, which means the model will try to find a simpler decision boundary, potentially underfitting the data. This is because it penalizes the misclassification of training examples more severely.

- **Larger "C" values**: They reduce the regularization effect, allowing the model to fit the training data more closely, potentially overfitting. This is because it penalizes misclassification less severely, allowing the model to prioritize getting training examples correct.