---
course: machine-learning-zoomcamp
id: a0b5f19b14
question: Null column is appearing even if I applied .fillna()
section: 2. Machine Learning for Regression
sort_order: 680
---

When creating a duplicate of your dataframe by doing the following:

X_train = df_train

X_val = df_val

You’re still referencing the original variable, this is called a shallow copy. You can make sure that no references are attaching both variables and still keep the copy of the data do the following to create a deep copy:

X_train = df_train.copy()

X_val = df_val.copy()

Added by Ixchel García

