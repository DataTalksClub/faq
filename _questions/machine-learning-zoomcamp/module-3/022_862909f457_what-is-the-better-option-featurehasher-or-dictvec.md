---
id: 862909f457
question: What is the better option FeatureHasher or DictVectorizer?
sort_order: 22
---

These methods both receive a dictionary as input. While the `DictVectorizer` will store a large vocabulary and take up more memory, `FeatureHasher` creates vectors with a predefined length. They are both used for handling categorical features.

- If you have high cardinality in categorical features, it's better to use `FeatureHasher`.
- If you want to preserve feature names in transformed data and have a small number of unique values, use `DictVectorizer`.

Your choice will depend on your data. For more information, you can visit [scikit-learn.org](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)