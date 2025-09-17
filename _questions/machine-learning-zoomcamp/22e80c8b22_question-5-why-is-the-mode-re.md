---
course: machine-learning-zoomcamp
id: 22e80c8b22
question: 'Question 5: Why is the mode returned as a Series instead of a single value
  in my DataFrame?'
section: 1. Introduction to Machine Learning
sort_order: 470
---

When you calculate the mode using the mode() function in pandas, the function always returns a Series. This design choice allows mode() to handle cases where there may be multiple modes (i.e., multiple values with the same highest frequency). Even when there is only one mode, the function will still return a Series with that single value.

If you are certain that your column has only one mode and you want to extract it as a single value, you can access the first element of the Series returned by mode():

(added by Karina)

