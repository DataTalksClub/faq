---
id: 3cc0ce528e
question: Is it best to train your model only on the most important features?
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4200
---

I’m just looking back at the lessons in week 3 (churn prediction project), and lesson 3.6 talks about Feature Importance for categorical values. At , the mutual info scores show that the some features are more important than others, but then in lesson 3.10 the Logistic Regression model is trained on all of the categorical variables (see ). Once we have done feature importance, is it best to train your model only on the most important features?

Not necessarily - rather, any feature that can offer additional predictive value should be included (so, e.g. predict with & without including that feature; if excluding it drops performance, keep it, else drop it). A few individually important features might in fact be highly correlated with others, & dropping some might be fine. There are many feature selection algorithms, it might be interesting to read up on them (among the methods we've learned so far in this course, L1 regularization (Lasso) implicitly does feature selection by shrinking some weights all the way to zero).

By Rileen Sinha

