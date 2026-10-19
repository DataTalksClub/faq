---
id: 8e58068607
question: Why should we use the same KFold splits when comparing different hyperparameter
  values (e.g., different Logistic Regression `C` values)?
sort_order: 31
---

When comparing different hyperparameter values (like Logistic Regression’s `C`), you want the score differences to reflect the hyperparameter effect—not randomness from changing train/validation splits.

If you use the same `KFold` configuration (for example, `KFold(n_splits=5, shuffle=True, random_state=1)`), then each hyperparameter value is evaluated on the same fold assignments. That makes the comparison fairer because every value of `C` sees the same subsets as validation across the cross-validation runs.

If you instead generate different random splits for each hyperparameter value, the mean AUC (or accuracy) can shift partly due to the particular split rather than due to the hyperparameter itself. Reusing the same folds also improves reproducibility, since rerunning the experiment gives the same fold partitions.