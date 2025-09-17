---
id: 862909f457
question: What is the better option FeatureHasher or DictVectorizer
section: 3. Machine Learning for Classification
course: machine-learning-zoomcamp
sort_order: 1280
---

These both methods receive the dictionary as an input. While the DictVectorizer will store the big vocabulary and takes more memory. FeatureHasher create a vectors with predefined length. They are both used for categorical features.

When you have a high cardinality for categorical features better to use FeatureHasher. If you want to preserve feature names in transformed data and have a small number of unique values is DictVectorizer. But your choice will dependence on your data.
You can read more by follow the link https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html

Olga Rudakova

