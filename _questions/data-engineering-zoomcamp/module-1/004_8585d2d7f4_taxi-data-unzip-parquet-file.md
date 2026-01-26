---
id: 8585d2d7f4
question: 'Taxi Data: Unzip csv.gz file'
sort_order: 4
---

You can `gunzip` the downloaded csv.gz file from the command line. The result is a CSV file which can be imported with pandas using `pd.read_csv()` as shown in the videos.

```bash
gunzip green_tripdata_2019-09.csv.gz
```

or you can read the gzipped file directly with pandas 

### Solution for Using Parquet Files Directly in Python Script `ingest_data.py`

1. In the `def main(params)`, add this line:
   
   ```python
   parquet_name = 'output.parquet'
   ```

2. Edit the code which downloads the files:

   ```python
   os.system(f"wget {url} -O {parquet_name}")
   ```

3. Convert the downloaded `.parquet` file to CSV and rename it to `csv_name` to keep it relevant to the rest of the code:

   ```python
   df = pd.read_parquet(parquet_name)
   df.to_csv(csv_name, index=False)
   ```
