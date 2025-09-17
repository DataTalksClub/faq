---
course: machine-learning-zoomcamp
id: 28f7297895
question: What is the difference between .decision_function() and .predict_proba()?
section: 3. Machine Learning for Classification
sort_order: 1360
---

In Scikit-Learn’s LogisticRegression, a model that is trained will have raw values and the predicted probabilities.

.decision_function() returns raw values which are a linear combination of the features and weights, similar to the output of Linear Regression.

.predict_proba() goes one step further by inputting these raw values into the sigmoid function, to convert them into probabilities (between 0 and 1).

![Image](images/machine-learning-zoomcamp/image_d2a8633d.png)

Kemal Dahha

