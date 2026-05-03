---
id: 55b6d6256f
question: 'Python: invalid start byte Error Message'
sort_order: 36
---

```python
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 41721: invalid start byte
```

Solution:

1. When reading the data from the web into the pandas dataframe, specify the encoding:
   
   ```python
   pd.read_csv(dataset_url, low_memory=False, encoding='latin1')
   ```

2. When writing the dataframe from the local system to GCS as a CSV, specify the encoding:
   
   ```python
   df.to_csv(path_on_gsc, compression="gzip", encoding='utf-8')
   ```

Alternative: Use `pd.read_parquet(url)`.