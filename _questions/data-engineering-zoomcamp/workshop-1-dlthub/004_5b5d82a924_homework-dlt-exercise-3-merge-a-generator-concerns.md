---
id: 5b5d82a924
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_4c7b9e6b.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_b4d5ed3c.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_2ba9606d.png
question: 'Homework: dlt Exercise 3 - Merge a generator concerns'
sort_order: 4
---

After loading, you should have a total of 8 records, and ID 3 should have age 33.

**Question:** Calculate the sum of ages of all the people loaded as described above.

- The sum of all eight records' respective ages is too big to be in the choices.
- You need to first filter out the people whose occupation is equal to `None` in order to get an answer that is close to or present in the given choices. 

---

### Issue:

I'm having an issue with the DLT workshop notebook, specifically in the 'Load to Parquet file' section. No matter what I change the file path to, it's still saving the DLT files directly to my C drive.

### Solution:

Use a raw string and keep the `file:///` at the start of your file path.

```python
# Set the bucket_url. We can also use a local folder
os.environ['DESTINATION__FILESYSTEM__BUCKET_URL'] = r'file:///content/.dlt/my_folder'

url = "https://storage.googleapis.com/dtc_zoomcamp_api/yellow_tripdata_2009-06.jsonl"

# Define your pipeline
pipeline = dlt.pipeline(
    pipeline_name='my_pipeline',
    destination='filesystem',
    dataset_name='mydata'
)

# Run the pipeline with the generator we created earlier.
load_info = pipeline.run(stream_download_jsonl(url), table_name="users", loader_file_format="parquet")

print(load_info)

# Get a list of all Parquet files in the specified folder
parquet_files = glob.glob('/content/.dlt/my_folder/mydata/users/*.parquet')

# Show Parquet files
for file in parquet_files:
    print(file)
```

<{IMAGE:image_1}>

<{IMAGE:image_2}>

<{IMAGE:image_3}>
