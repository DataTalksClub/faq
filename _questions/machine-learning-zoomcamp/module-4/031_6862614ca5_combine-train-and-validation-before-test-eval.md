---
id: 6862614ca5
question: Why do we combine the training and validation datasets before evaluating
  the final model on the test dataset?
sort_order: 31
---

The validation set is used during model selection and hyperparameter tuning (i.e., to estimate performance and decide which model configuration to keep).

Once you’ve selected the final model, you no longer need the validation set for tuning—so it’s common to retrain the final model on the combined data (train + validation) to let it learn from as much labeled data as possible.

You should still keep the test set untouched until the very end, because the test set is reserved for the final, unbiased evaluation on unseen data.

Example:
- `df_train_full = pd.concat([df_train, df_val])`
- Train the final model using `df_train_full`
- Report performance only once on the held-out test dataset