---
course: machine-learning-zoomcamp
id: a7e230bfb4
question: Question 6 of HW 3 asks to train a regularized logistic regression with
  c = 0.
section: 3. Machine Learning for Classification
sort_order: 1380
---

This is not possible since the parameter C represents the inverse of the regularization strength, and setting C to 0 means infinite regularization and hence trying this through the scikit learn module of Logistic Regression will give ValueError

