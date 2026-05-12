---
id: c04cf606ed
question: 'Reading the homework CSV converts the string ''None'' to NaN'
sort_order: 29
---

Pandas treats `'None'` as a missing value by default. For columns where 'None' is a real category, use:

```python
df = pd.read_csv("path.csv", keep_default_na=False, na_values=['', 'NaN', 'null'])
```

This preserves the literal string 'None' in categorical columns like `Parent_Education_Level`.
