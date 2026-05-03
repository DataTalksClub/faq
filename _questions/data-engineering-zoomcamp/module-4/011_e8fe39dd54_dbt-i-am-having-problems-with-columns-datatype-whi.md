---
id: e8fe39dd54
question: 'DBT: I am having problems with columns datatype while running DBT/BigQuery'
sort_order: 11
---

**Issue:** If you don’t define the column format while converting from CSV to Parquet, Python will "choose" based on the first rows.

**Solution:** Define the schema while running the `web_to_gcp.py` pipeline.

Sebastian adapted the script:

[GitHub Repository](https://github.com/sebastian2296/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/web_to_gcs.py)

To make the file work with gz files, add the following lines:

- Ensure deletion of the file at the end of each iteration to avoid disk space issues:

```python
file_name_gz = f"{service}_tripdata_{year}-{month}.csv.gz"
open(file_name_gz, 'wb').write(r.content)
os.system(f"gzip -d {file_name_gz}")
os.system(f"rm {file_name_init}.*")
```