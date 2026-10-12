---
id: 88d1c0efae
question: What will happen if I don’t delete the target variable from the feature
  data?
sort_order: 33
---

If you accidentally keep the target column inside your feature matrix when training, you get target leakage.

What you’ll typically see:
- Training and validation metrics look almost perfect (e.g., accuracy or ROC AUC close to 1.0). This is a red flag because real-world data usually isn’t that predictable.
- The model assigns the target column an enormous weight, effectively learning the answer from the target itself.
- Performance drops sharply on new/unseen data, where the target value is not available at prediction time (or you would have to “cheat” during inference).

Why it’s a problem:
- The model isn’t learning patterns from the input features; it’s learning to read the target value you provided.
- In production, the target is exactly what you’re trying to predict, so it will not exist in the input features during inference—meaning the model fails or needs to be retrained.

How to avoid it:
- Separate the target (`y`) from the features (`X`) before training, and ensure the target column is not included in `X`.