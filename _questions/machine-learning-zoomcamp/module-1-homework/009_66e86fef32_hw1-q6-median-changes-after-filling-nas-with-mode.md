---
id: 66e86fef32
question: 'Homework 1 Q6: Why does the median of horsepower change after filling NAs
  with the most frequent value?'
sort_order: 9
---

The median is the middle value of the sorted column. Filling NAs adds many copies of one value. If that value (the mode) lies below the original median, the middle shifts down; if it lies above, the middle shifts up. With hundreds of NAs the shift is easy to see.

```python
median_before = df['horsepower'].median()
mode = df['horsepower'].mode()[0]
median_after = df['horsepower'].fillna(mode).median()
```

Compare `mode` with `median_before` to predict the direction. See also "Why the mode returns a Series instead of a single value?" and "Why are there still missing values after I use `fillna()` in Pandas?".
