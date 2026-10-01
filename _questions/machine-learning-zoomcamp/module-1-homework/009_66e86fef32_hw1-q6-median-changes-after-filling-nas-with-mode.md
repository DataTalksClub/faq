---
id: 66e86fef32
question: 'Homework 1 Q6: Why does the median of horsepower change after filling NAs
  with the most frequent value?'
sort_order: 9
---

In pandas, filling missing values with the column mode can change the median because the median is sensitive to how many values fall below vs. above it.

In this case, `df.horsepower.mode()[0]` (the most frequent value) is `252.0`, while the original median is `254.0`. When you replace all `877` missing values with `252.0`, you add a large block of values below the original median, so the median shifts down to `252.0`.

A couple of implementation notes:
- `mode()` returns a Series (to handle ties). That’s why you use `[0]` to get the single most common value: `df.horsepower.mode()[0]`.
- `fillna()` does not modify the DataFrame in place unless you assign the result back (e.g., `df['horsepower'] = df['horsepower'].fillna(mode)`, or use the returned Series/column in your next calculation).