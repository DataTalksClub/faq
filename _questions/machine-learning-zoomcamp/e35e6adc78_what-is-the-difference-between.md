---
course: machine-learning-zoomcamp
id: e35e6adc78
question: What is the difference between OneHotEncoder and DictVectorizer?
section: 3. Machine Learning for Classification
sort_order: 1200
---

Both work in similar ways. That is, to convert categorical features to numerical variables for use in training the model. But the difference lies in the input. OneHotEncoder uses an array as input while DictVectorizer uses a dictionary.

Both will produce the same result. But when we use OneHotEncoder, features are sorted alphabetically. When you use DictVectorizer you stack features that you want.

Tanya Mard

