---
id: 481e174dd4
question: Found array with 0 sample(s)
sort_order: 9
---

```python
ValueError: Found array with 0 sample(s) (shape=(0, 6)) while a minimum of 1 is required by LinearRegression.
```

This error occurs because the generated data is based on an early date, resulting in an empty training dataset.

Adjust the following:

```python
begin = datetime.datetime(202X, X, X, 0, 0)
```