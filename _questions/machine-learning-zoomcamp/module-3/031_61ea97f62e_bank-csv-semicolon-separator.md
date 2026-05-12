---
id: 61ea97f62e
question: 'How do I read bank-full.csv? Pandas isn''t separating the columns'
sort_order: 31
---

The bank dataset uses semicolons, not commas, as separators. Read it with:

```python
df = pd.read_csv('bank-full.csv', sep=';')
```
