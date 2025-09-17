---
id: eecebb4f2f
question: How to select column by dtype
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 430
---

What if there were hundreds of columns? How do you get the columns only with numeric or object data in a more concise way?

df.select_dtypes(include=np.number).columns.tolist()

df.select_dtypes(include='object').columns.tolist()

Added by Gregory Morris

