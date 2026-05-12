---
id: 28f7297895
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_d2a8633d.png
question: What is the difference between .decision_function() and .predict_proba()?
sort_order: 26
---

In Scikit-Learn’s LogisticRegression, a model that is trained will have raw values and the predicted probabilities.

- **.decision_function()** returns raw values that are a linear combination of the features and weights, similar to the output of Linear Regression.

- **.predict_proba()** goes one step further by inputting these raw values into the sigmoid function to convert them into probabilities (between 0 and 1).

<{IMAGE:image_1}>