---
course: machine-learning-zoomcamp
id: 139ae54c4f
question: Difference between predict(X) and predict_proba(X)[:, 1]
section: 4. Evaluation Metrics for Classification
sort_order: 1550
---

In case of using predict(X) for this task we are getting the binary classification predictions which are 0 and 1. This may lead to incorrect evaluation values.

The solution is to use predict_proba(X)[:,1], where we get the probability that the value belongs to one of the classes.

Vladimir Yesipov

Predict_proba shows probabilities per class.

Ani Mkrtumyan

