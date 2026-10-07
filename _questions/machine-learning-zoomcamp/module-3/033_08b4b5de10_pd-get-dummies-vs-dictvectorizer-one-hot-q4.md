---
id: 08b4b5de10
question: Can I use `pd.get_dummies` instead of `DictVectorizer` for one-hot encoding
  (Homework 3 Q4)?
sort_order: 33
---

Yes, you can use `pd.get_dummies`, but `DictVectorizer` is safer and is what the lectures use.

The main risk with `pd.get_dummies` is that it is applied separately to each split. If a category appears in training but not in validation (or vice versa), the encoded feature matrices can end up with a different set of columns. That can either crash your pipeline or, worse, silently misalign features.

With `DictVectorizer`, you fit on training only and then transform validation/test with the same learned mapping, so the column layout is locked. Unseen categories at transform time become all-zero columns, which is the intended behavior.

If you still use `get_dummies`, make sure you explicitly align the columns between splits, for example by reindexing validation to match training’s columns and filling missing values with 0.

Also, when using `DictVectorizer`, note that `get_feature_names_out()` lets you inspect the resulting feature/column names.