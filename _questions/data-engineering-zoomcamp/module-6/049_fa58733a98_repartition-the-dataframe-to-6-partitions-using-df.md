---
id: fa58733a98
question: Repartition the Dataframe to 6 partitions using df.repartition(6) - got
  8 partitions instead
sort_order: 49
---

Use both `repartition` and `coalesce`, like so:

```python
df = df.repartition(6)

df = df.coalesce(6)

df.write.parquet('fhv/2019/10', mode='overwrite')
```