---
id: a71d2105aa
question: Why does Spark write multiple parquet files after repartitioning a DataFrame?
sort_order: 30
---

Spark processes data in partitions. When you write a DataFrame to disk, Spark writes each partition as a separate output file. For example:

```python
trips.repartition(4).write.parquet("output/")
```

This creates four parquet files because the DataFrame now has four partitions. This behavior enables Spark to write data in parallel and can improve performance on large datasets.
