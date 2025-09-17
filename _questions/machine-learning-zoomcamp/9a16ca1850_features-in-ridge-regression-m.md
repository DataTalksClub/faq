---
course: machine-learning-zoomcamp
id: 9a16ca1850
question: Features in Ridge Regression Model
section: 3. Machine Learning for Classification
sort_order: 1240
---

Make sure that the features used in ridge regression model are only NUMERICAL ones not categorical.

Drop all categorical features first before proceeding.

(Aileah Gotladera)

While it is True that ridge regression accepts only numerical values, the categorical ones can be useful for your model. You have to transform them using one-hot encoding before training the model. To avoid the error of non convergence, put sparse=True when doing so.

(Erjon)

