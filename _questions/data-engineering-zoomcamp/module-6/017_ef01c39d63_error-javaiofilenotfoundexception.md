---
id: ef01c39d63
question: 'Error: java.io.FileNotFoundException'
sort_order: 17
---

```python
# Code executed:
df = spark.read.parquet(pq_path)

# … some operations on df …

df.write.parquet(pq_path, mode="overwrite")

# Error:
# java.io.FileNotFoundException: File file:/home/xxx/code/data/pq/fhvhv/2021/02/part-00021-523f9ad5-14af-4332-9434-bdcb0831f2b7-c000.snappy.parquet does not exist
```

The problem is that Spark performs lazy transformations, so the actual action that triggers the job is `df.write`, which deletes the parquet files it tries to read (mode="overwrite").

**Solution:**

- Write to a different directory:

  ```python
  df.write.parquet(pq_path_temp, mode="overwrite")
  ```