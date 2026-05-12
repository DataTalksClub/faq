---
id: cda76de4e9
question: How to identify the shape of dataset in Pandas
sort_order: 15
---

To identify the shape of a dataset in Pandas, you can use the `.shape` attribute:

- `df.shape`: Returns a tuple representing the dimensionality of the DataFrame.
- `df.shape[0]`: Returns the number of rows.
- `df.shape[1]`: Returns the number of columns.

You can also use the built-in `len` function to find the total number of rows:

```python
len(df)
```