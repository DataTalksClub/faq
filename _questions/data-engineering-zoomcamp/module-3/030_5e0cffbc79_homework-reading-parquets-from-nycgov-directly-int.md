---
id: 5e0cffbc79
question: 'Homework: Reading parquets from nyc.gov directly into pandas returns Out
  of bounds error'
sort_order: 30
---

If you try to read parquets directly from nyc.gov’s cloudfront into pandas, you might encounter this error:

```python
pyarrow.lib.ArrowInvalid: Casting from timestamp[us] to timestamp[ns] would result in out of bounds
```

### Cause:

There is a data record where `dropOff_datetime` is set to the year 3019 instead of 2019. 

Pandas uses "timestamp[ns]" and `int64` only allows a ~580-year range, centered on 2000. See `pd.Timestamp.max` and `pd.Timestamp.min`.

This becomes out of bounds when pandas tries to read it because 3019 > 2300 (approx value of `pd.Timestamp.max`).

### Fix:

1. **Use pyarrow to read the data:**

   ```python
   import pyarrow.parquet as pq
   df = pq.read_table('fhv_tripdata_2019-02.parquet').to_pandas(safe=False)
   ```

   This will result in unusual timestamps for the offending record.

2. **Read datetime columns separately:**

   ```python
   table = pq.read_table('taxi.parquet')
   datetimes = ['list of datetime column names']
   df_dts = pd.DataFrame()

   for col in datetimes:
       df_dts[col] = pd.to_datetime(table.column(col), errors='coerce')
   ```

   The `errors='coerce'` parameter will convert out-of-bounds timestamps into either the max or min.

3. **Remove the offending rows using filter:**

   ```python
   import pyarrow.compute as pc

   table = pq.read_table('taxi.parquet')

   df = table.filter(
       pc.less_equal(table["dropOff_datetime"], pa.scalar(pd.Timestamp.max))
   ).to_pandas()
   ```
