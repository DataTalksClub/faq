---
course: machine-learning-zoomcamp
id: 9e300560ca
question: When should we transform the target variable to logarithm distribution?
section: 2. Machine Learning for Regression
sort_order: 790
---

When the target variable has a long tail distribution, like in prices, with a wide range, you can transform the target variable with np.log1p() method, but be aware if your target variable has negative values, this method will not work

