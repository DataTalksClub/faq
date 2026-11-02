---
id: a3d5c94238
question: When using `DictVectorizer`, why can a Decision Tree split on an encoded
  feature like `origin=USA` instead of the original categorical column `origin`?
sort_order: 31
---

`DictVectorizer` turns each categorical value into its own binary feature before the Decision Tree is trained. So the tree doesn’t see the original column `origin`; it sees the transformed feature space such as:
- `origin=USA`
- `origin=Europe`
- `origin=Asia`

That’s why a split like `origin=USA <= 0.5` actually means: “send rows where the encoded binary feature for category `USA` is 1 (i.e., `origin` is `USA`) to one side; everything else to the other side.” The `<= 0.5` threshold is just how sklearn expresses a split on a binary {0,1} feature.

If you need to map what the tree is using back to the original dataset feature, you can inspect the encoded feature names with `dv.get_feature_names_out()` and relate `origin=USA` back to the original categorical column `origin`.