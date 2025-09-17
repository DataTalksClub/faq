---
id: 146d28247c
question: What is the difference between pandas get_dummies and sklearn OnehotEncoder?
section: 3. Machine Learning for Classification
course: machine-learning-zoomcamp
sort_order: 1210
---

They are basically the same. There are some key differences with regards to their input/output types, handling of missing values, etc, but they are both techniques to one-hot-encode categorical variables with identical results. The biggest difference is get_dummies are a convenient choice when you are working with Pandas Dataframes, while if you are building a scikit-learn-based machine learning pipeline and need to handle categorical data as part of that pipeline, OneHotEncoder is a more suitable choice. [Abhirup Ghosh]

