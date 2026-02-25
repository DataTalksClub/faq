---
id: 9b3ee420d4
question: 'AttributeError: ''DataFrame'' object has no attribute ''iteritems'''
sort_order: 29
---

This error occurs in the Spark video 5.3.1 - First Look at Spark/PySpark because the example utilizes CSV files from 2021, but the current data is in parquet format.

When running the command:

```python
spark.createDataFrame(df1_pandas).show()
```

You may encounter the Attribute error due to incompatibility between pandas version 2.0.0 and Spark 3.3.2. To resolve this, you can:

- Downgrade pandas to version 1.5.3 using the following command:
  
  ```bash
  pip install -U pandas==1.5.3
  ```
  
- Alternatively, add the following line after importing pandas if you prefer not to downgrade:
  
  ```python
  pd.DataFrame.iteritems = pd.DataFrame.items
  ```

This issue is resolved in Spark versions from 3.4.1 onwards.