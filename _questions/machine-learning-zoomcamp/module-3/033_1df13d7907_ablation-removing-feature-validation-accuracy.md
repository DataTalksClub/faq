---
id: 1df13d7907
question: Why can removing one feature at a time lead to almost no change in validation
  accuracy?
sort_order: 33
---

Removing a feature may result in almost no change in validation accuracy when that feature doesn’t add much new information beyond what the other features already provide.

Common reasons:
- Redundancy: the feature’s signal is largely captured by other correlated features, so the model performance stays similar.
- Weak contribution: the feature has low predictive value for the target, so dropping it doesn’t meaningfully affect predictions.

A simple check is to perform ablation:
1. Get the original validation accuracy using all features.
2. Remove one feature (e.g., `number_of_courses_viewed`) from both `df_train` and `df_val`.
3. Retrain the model and compute the new validation accuracy.
4. Compare accuracies; if the difference is very small, the removed feature had little impact.