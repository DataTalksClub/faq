---
id: c6c716b9e7
question: How to copy a dataframe without changing the original dataframe?
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 810
---

Copy of a dataframe is made with X_copy = X.copy().

This is called creating a deep copy.  Otherwise it will keep changing the original dataframe if used like this: X_copy = X.

Any changes to X_copy will reflect back to X. This is not a real copy, instead it is a “view”.

(Memoona Tahira)

