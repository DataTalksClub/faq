---
id: a3d5c94238
question: When using `DictVectorizer`, why can a Decision Tree split on an encoded feature like
  `origin=USA` instead of the original categorical column `origin`?
sort_order: 31
---

`DictVectorizer` turns each categorical value into its own binary feature. For example, the column `origin` can become `origin=USA`, `origin=Europe`, and `origin=Asia`.

For the binary feature `origin=USA`, a tree sends rows with value `0` to the left branch when its rule is `origin=USA <= 0.5`. It sends rows with value `1` to the right branch when its rule is `origin=USA > 0.5`. In `export_text`, the `<=` branch appears first and the `>` branch appears second. A value of `1` marks cars from the USA.

To map the encoded feature back to its original column, look at `dv.get_feature_names_out()`. It lists `origin=USA` as a feature derived from `origin`. Report `origin` when the homework asks for the original feature.

See the [scikit-learn DictVectorizer API](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html) and [tree.export_text API](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html).
