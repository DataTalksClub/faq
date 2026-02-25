---
id: 14cc6e2060
question: 'MemoryManager: Total allocation exceeds 95.00% (1,020,054,720 bytes) of
  heap memory'
sort_order: 39
---

Default executor memory is 1GB. This error appeared when working with the homework dataset.

Error:

```plaintext
MemoryManager: Total allocation exceeds 95.00% (1,020,054,720 bytes) of heap memoryScaling row group sizes to 95.00% for 8 writers
```

Solution:

Increase the memory of the executor when creating the Spark session like this:

```python
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()
```

Remember to restart the Jupyter session (i.e., close the Spark session) or the config won’t take effect.