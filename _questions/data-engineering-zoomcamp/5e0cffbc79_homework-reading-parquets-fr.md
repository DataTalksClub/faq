---
course: data-engineering-zoomcamp
id: 5e0cffbc79
question: Homework - Reading parquets from nyc.gov directly into pandas returns Out
  of bounds error
section: 'Module 3: Data Warehousing'
sort_order: 2330
---

If for whatever reason you try to read parquets directly from nyc.gov’s cloudfront into pandas, you might run into this error:

pyarrow.lib.ArrowInvalid: Casting from timestamp[us] to timestamp[ns] would result in out of bounds

Cause:

there is one errant data record where the dropOff_datetime was set to year 3019 instead of 2019.

pandas uses “timestamp[ns]” (as noted above), and int64 only allows a ~580 year range, centered on 2000. See `pd.Timestamp.max` and `pd.Timestamp.min`

This becomes out of bounds when pandas tries to read it because 3019 > 2300 (approx value of pd.Timestamp.Max

Fix:

Use pyarrow to read it:
import pyarrow.parquet as pq df = pq.read_table('fhv_tripdata_2019-02.parquet').to_pandas(safe=False)
However this results in weird timestamps for the offending record

Read the datetime columns separately using pq.read_table

table = pq.read_table(‘taxi.parquet’)
datetimes = [‘list of datetime column names’]
df_dts = pd.DataFrame()

for col in datetimes:

df_dts[col] = pd.to_datetime(table .column(col), errors='coerce')

The `errors=’coerce’` parameter will convert the out of bounds timestamps into either the max or the min

Use parquet.compute.filter to remove the offending rows

import pyarrow.compute as pc

table = pq.read_table("‘taxi.parquet")

df = table.filter(

pc.less_equal(table["dropOff_datetime"], pa.scalar(pd.Timestamp.max))

).to_pandas()

