---
id: af50bd4d07
question: 'Homework: Q3: Meaning of mean'
sort_order: 3
---

In question 3 of HW02 it is mentioned: ‘For computing the mean, use the training only’. What does that mean?

It means you compute the mean from the training set only, not from the validation or test set (and not from the full dataset before splitting). Then you use that same value to fill missing values in all three splits:

```python
mean_hp = df_train['horsepower'].mean()

df_train_filled = df_train.fillna(mean_hp)
df_val_filled = df_val.fillna(mean_hp)
df_test_filled = df_test.fillna(mean_hp)
```

Why: validation and test data stand in for data the model has never seen. If the mean is computed on the full dataset, information from those rows leaks into training (data leakage), and your validation score becomes slightly optimistic. Don't recompute the mean separately for each split either. In production you'd only have the training statistics.
