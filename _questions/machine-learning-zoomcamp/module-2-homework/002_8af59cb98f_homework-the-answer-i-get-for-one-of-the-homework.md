---
id: 8af59cb98f
question: 'Homework: The answer I get for one of the homework questions doesn''t match
  any of the options. What should I do?'
sort_order: 2
---

Select the option closest to your answer. If your value falls between two options, choose the larger one.

Check these parts of the assignment first:

- the named dataset and columns
- the exact train, validation, and test split
- the preprocessing, metric, and rounding

If you need a fill value, such as a mean, calculate it from the training split only. For 2026 car data, download `car_fuel_efficiency_2026.csv` from `cohorts/2026/data/` rather than reusing an older dataset.

In Homework 6, fill missing values with zeros before making the split.

Use the exact calls in the [2026 Homework 6 instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md#preparing-the-dataset):

```python
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(
    df_full_train, test_size=0.25, random_state=1
)
```

For Question 2, use `DictVectorizer(sparse=True)`. Fit the vectorizer on the feature dictionaries from `df_train`. Then use the fitted vectorizer to transform feature dictionaries from `df_val`, so validation rows don't influence its vocabulary. Train the random forest with the assignment's parameters and calculate RMSE on validation data.

For questions about standard deviation, `np.std` uses `ddof=0`, while pandas `.std()` uses `ddof=1` by default. Follow the rounding precision stated in each question. Round Q3 to 3 decimals and Q4 to 4 decimals for these 2026 questions.

Use the specified seed, and recreate `idx = np.arange(n)` before each required shuffle.
