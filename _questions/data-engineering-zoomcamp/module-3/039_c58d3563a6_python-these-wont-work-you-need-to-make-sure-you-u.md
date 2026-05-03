---
id: c58d3563a6
question: 'Python: These won''t work. You need to make sure you use Int64.'
sort_order: 39
---

Incorrect:

```python
df['DOlocationID'] = pd.to_numeric(df['DOlocationID'], downcast=integer)
```

or

```python
df['DOlocationID'] = df['DOlocationID'].astype(int)
```

Correct:

```python
df['DOlocationID'] = df['DOlocationID'].astype('Int64')
```