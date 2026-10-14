---
id: 19a42e2005
question: How to combine train and validation datasets, and why do we do it?
sort_order: 27
---

After you've used the validation set to choose the model and its parameters, you don't need it for tuning anymore. Retrain the final model on train + validation so it learns from more data. Keep the test set untouched and evaluate on it only once at the end.

Use `pandas.concat` function ([pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)) to combine two dataframes. To combine two numpy arrays, use `numpy.concatenate` ([numpy documentation](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)).

The code would be as follows:

```python
df_train_combined = pd.concat([df_train, df_val])
df_train_combined = df_train_combined.reset_index(drop=True)
y_train = np.concatenate((y_train, y_val), axis=0)
```