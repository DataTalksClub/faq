---
id: b4c8ac5a0c
question: How to compute the quantile or percentile of Pandas DataFrame column (or
  Pandas Series)?
sort_order: 5
---

To compute the 75% percentile or 0.75 quantile:

```python
quantile = df["col"].quantile(q=0.75)
```