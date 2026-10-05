---
id: 359acb3362
question: Is there a faster alternative to manually encoding categorical columns that
  triggers a pandas performance warning when repeatedly adding many columns?
sort_order: 33
---

That warning usually appears when you build the encoded DataFrame by repeatedly writing new columns into an existing `DataFrame` inside loops, e.g. `df[col] = ...` for many unique categories. Each assignment can force pandas to re-handle a larger frame, which is slow and memory-heavy.

Better options:
1) Use `DictVectorizer` (recommended in this course for classification feature engineering). Instead of manually creating one column per category, convert each row to a dictionary of categorical features and let scikit-learn do the one-hot expansion efficiently.

2) Use `pandas.get_dummies` (one-hot encoding) on the categorical columns in a single operation, then concatenate once with your numeric columns.

Key idea: avoid per-category/per-loop assignments like `df["%s" % j] = ...`. Build the encoded representation first (with `DictVectorizer` or `get_dummies`), then concatenate to `df_num` one time.

(Your approach idea—splitting object vs numeric columns, encoding the object part, and `pd.concat` once—matches this key idea. The main performance bottleneck is the repeated column assignment inside the nested loops, not the final merge.)