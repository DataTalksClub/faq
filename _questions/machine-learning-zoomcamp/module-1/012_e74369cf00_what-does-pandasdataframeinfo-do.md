---
id: e74369cf00
question: What does pandas.DataFrame.info() do?
sort_order: 12
---

It prints the information about the dataset, including:

- Index datatype
- Number of entries
- Column information with not-null count and datatype
- Memory usage by the dataset

We use it as:

```python
df.info()
```