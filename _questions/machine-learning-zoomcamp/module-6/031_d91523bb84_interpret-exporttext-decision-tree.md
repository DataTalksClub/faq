---
id: d91523bb84
question: How do I read the output of `export_text` for a decision tree (what do `<=
  0.50` and `> 0.50` mean, and which block is the left or right branch)?
sort_order: 31
---

`export_text` prints the tree as text, so the branches are stacked vertically:

- Top block = left branch: the condition shown in the top block evaluates to `0`.
- Bottom block = right branch: the condition shown in the bottom block evaluates to `1`.

When you use `DictVectorizer` for one-hot encoding, each category becomes a `0/1` column (for example, `records=yes` is either `0` or `1`). Scikit-learn then represents the split on that binary feature using a threshold around `0.5`, so:

- `<= 0.50` corresponds to the feature being `0`
- `> 0.50` corresponds to the feature being `1`

In other words, for a split like `records=yes <= 0.50` (top block), the rule means `records=yes` is `0` (so the original category was not `yes`). For `records=yes > 0.50` (bottom block), it means `records=yes` is `1` (the category is `yes`).

The `class: ...` lines under each leaf are the model’s predicted class label for that branch. What numeric label (e.g., `0` vs `1`) means in real terms depends on how you encoded the target `y`.

Watch for double negatives: if the feature name itself includes `no` (e.g., `records=no`), then `records=no <= 0.50` means `records=no` is `0`, which implies the original category is actually `yes`. Always translate each condition back into plain words before interpreting the leaf predictions.