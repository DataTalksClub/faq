---
id: 7fa4e026d6
question: Remove white spaces from column names in Pyspark
sort_order: 28
---

```python
df_finalx = df_finalw.select([col(x).alias(x.replace(" ", "")) for x in df_finalw.columns])
```