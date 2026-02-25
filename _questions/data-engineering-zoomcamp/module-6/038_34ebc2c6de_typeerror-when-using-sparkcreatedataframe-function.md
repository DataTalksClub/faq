---
id: 34ebc2c6de
question: TypeError when using spark.createDataFrame function on a pandas df
sort_order: 38
---

**Error:**

```python
spark.createDataFrame(df_pandas).schema

TypeError: field Affiliated_base_number: Can not merge type <class 'pyspark.sql.types.StringType'> and <class 'pyspark.sql.types.DoubleType'>
```

**Solution:**

- **Reason:**
  - The `Affiliated_base_number` field is a mix of letters and numbers, so it cannot be set to `DoubleType`. The suitable type would be `StringType`. Spark's `inferSchema` is more accurate than Pandas' infer type method in this case. Set `inferSchema` to `true` when reading the CSV to prevent data removal.

- **Implementation:**
  
  ```python
  df = spark.read \
    .options(
      header = "true", \
      inferSchema = "true"
    ) \
    .csv('path/to/your/csv/file/')
  ````

- **Alternative Solution:**
  
  - **Problem:** Some rows in `affiliated_base_number` are null, and therefore are assigned the datatype `String`, which cannot be converted to `Double`.
  - **Solution:** Only take rows from the pandas df that are not null in the 'Affiliated_base_number' column before converting it to a PySpark DataFrame.

  ```python
  # Only take rows that have no null values
  pandas_df = pandas_df[pandas_df.notnull().all(1)]
  ```