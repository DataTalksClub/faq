---
course: machine-learning-zoomcamp
id: af50bd4d07
question: Meaning of mean in homework 2, question 3
section: 2. Machine Learning for Regression
sort_order: 780
---

In question 3 of HW02 it is mentioned: ‘For computing the mean, use the training only’. What does that mean?

It means that you should use only the training data set for computing the mean, not validation or  test data set. This is how you can calculate the mean

df_train['column_name'].mean( )

Another option:

df_train[‘column_name’].describe()

(Bhaskar Sarma)

