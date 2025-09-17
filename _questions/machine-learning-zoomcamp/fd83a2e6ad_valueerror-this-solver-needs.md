---
course: machine-learning-zoomcamp
id: fd83a2e6ad
question: 'ValueError: This solver needs samples of at least 2 classes in the data,
  but the data contains only one class: 0'
section: 4. Evaluation Metrics for Classification
sort_order: 1450
---

Solution description: duplicating the

df.churn = (df.churn == 'yes').astype(int)

This is causing you to have only 0's in your churn column. In fact, match with the error you are getting:  ValueError: This solver needs samples of at least 2 classes in the data, but the data contains only one class: 0.

It is telling us that it only contains 0's.

Delete one of the below cells and you will get the accuracy

Humberto Rodriguez

