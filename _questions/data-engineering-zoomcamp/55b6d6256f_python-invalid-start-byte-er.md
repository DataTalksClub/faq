---
id: 55b6d6256f
question: Python - invalid start byte Error Message
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2370
---

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 41721: invalid start byte

Solution:

Step 1: When reading the data from the web into the pandas dataframe mention the encoding as follows:

pd.read_csv(dataset_url, low_memory=False, encoding='latin1')

Step 2: When writing the dataframe from the local system to GCS as a csv mention the encoding as follows:

df.to_csv(path_on_gsc, compression="gzip", encoding='utf-8')

Alternative: use pd.read_parquet(url)

