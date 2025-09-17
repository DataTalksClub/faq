---
course: machine-learning-zoomcamp
id: e41007991b
question: Warning about modifying Dataframes inside functions
section: 2. Machine Learning for Regression
sort_order: 850
---

When applying a function to a DataFrame, it is important to consider that if you do not want to alter the original DataFrame, you should create a copy of it first. Failing to do so may result in unintended modifications to the original dataset. To preserve the integrity of your data, always use df.copy() before making any changes.

(added by Karina)

