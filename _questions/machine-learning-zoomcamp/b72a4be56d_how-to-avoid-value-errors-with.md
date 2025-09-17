---
id: b72a4be56d
question: How to avoid Value errors with array shapes in homework?
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 450
---

First of all use np.dot for matrix multiplication. When you compute matrix-matrix multiplication you should understand that order of multiplying is crucial and affects the result of the multiplication!

Dimension Mismatch

To perform matrix multiplication, the number of columns in the 1st matrix should match the number of rows in the 2nd matrix. You can rearrange the order to make sure that this satisfies the condition.

Added by Leah Gotladera

