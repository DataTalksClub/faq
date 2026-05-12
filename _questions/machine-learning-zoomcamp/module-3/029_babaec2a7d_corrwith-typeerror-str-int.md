---
id: babaec2a7d
question: 'TypeError: unsupported operand type(s) for /: ''str'' and ''int'' when running corrwith'
sort_order: 29
---

One of the columns you think is numeric is actually stored as object/string. In the churn dataset, `totalcharges` has spaces (`' '`) for missing values, which causes pandas to store it as object. Convert it explicitly first:

```python
df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce').fillna(0)
```

Make sure `churn` is also numeric (e.g., `(df.churn == 'yes').astype(int)`).
