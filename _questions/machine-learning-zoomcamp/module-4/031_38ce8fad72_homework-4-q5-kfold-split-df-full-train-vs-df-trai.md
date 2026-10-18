---
id: 38ce8fad72
question: 'Homework 4 Q5: For 5-fold cross-validation, should `KFold` split `df_train`
  or `df_full_train`?'
sort_order: 31
---

Use `df_full_train` when calling `kfold.split(...)`.

Reason: cross-validation is standing in for the usual train/validation split. `df_full_train` (the 80% part) is what you normally split into train/val, so in CV you re-split that same 80% into train/val 5 different ways. That keeps the CV scores comparable to the single `df_val` score from Q2.

Common traps:
- Don’t reuse `df_full_train` with the target still attached. In these questions `df_full_train` still contains `converted`. When you build the fold subsets, split the target from the features (e.g., `df_tr['converted']` / `df_va['converted']`) and drop `converted` from the feature dicts before vectorizing/training.
- Fit a fresh `DictVectorizer` inside each fold. Don’t reuse one vectorizer fitted outside the CV loop, or you risk information leakage across folds.

Also, for Q6: re-initialize `KFold` for each value of `C` (same `shuffle`/`random_state`) so every `C` sees identical folds.