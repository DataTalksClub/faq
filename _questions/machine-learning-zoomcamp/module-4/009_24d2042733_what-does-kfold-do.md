---
id: 24d2042733
question: What does KFold do?
sort_order: 9
---

KFold is a cross-validation technique that splits your dataset into k equal parts (folds). It trains the model k times, each time using a different fold as the validation set while training on the remaining folds. This process helps provide a more reliable estimate of a model's performance by ensuring every data point gets to be in both the training and validation sets. The average score across all folds offers a robust evaluation, minimizing the risk of overfitting to a specific train-test split.

**What does this line do?**

```python
KFold(n_splits=n_splits, shuffle=True, random_state=1)
```

- **Positioning in Code:** Whether you instantiate KFold inside the loop over different regularization values like `[0.01, 0.1, 1, 10]` or outside, it typically does not affect your answer. This is because `KFold` is essentially a generator object containing the information `n_splits`, `shuffle`, and `random_state`.

- **Impact of Random State:** Changing the `random_state` can yield different results because it affects how the data is shuffled. However, the creation of the `KFold` object, either inside or outside a loop, doesn't make a difference as long as the configuration (`n_splits`, `shuffle`, `random_state`) remains constant.

- **Best Practice:** It is recommended to create the `KFold` object before the loop to avoid unnecessary repetition:

  ```python
  kFold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
  for C in [0.01, 0.1, 1, 10]:
      for train_idx, val_idx in kFold.split(df_full_train):
          # train and evaluate model
  ```

For more details, you can refer to the official [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html).