---
id: 5b5d82a924
question: Homework - dlt Exercise 3 - Merge a generator concerns
section: Workshop 1 - dlthub
course: data-engineering-zoomcamp
sort_order: 4400
---

After loading, you should have a total of 8 records, and ID 3 should have age 33

Question: Calculate the sum of ages of all the people loaded as described above

The sum of all eight records' respective ages is too big to be in the choices. You need to first filter out the people whose occupation is equal to None in order to get an answer that is close to or present in the given choices. 😃

----------------------------------------------------------------------------------------

FIXED = use a raw string and keep the file:/// at the start of your file path

![Image](images/data-engineering-zoomcamp/image_4c7b9e6b.png)

![Image](images/data-engineering-zoomcamp/image_b4d5ed3c.png)

I'm having an issue with the dlt workshop notebook. The 'Load to Parquet file' section specifically. No matter what I change the file path to, it's still saving the dlt files directly to my C drive.

![Image](images/data-engineering-zoomcamp/image_2ba9606d.png)

# Set the bucket_url. We can also use a local folder

os.environ['DESTINATION__FILESYSTEM__BUCKET_URL'] = r'file:///content/.dlt/my_folder'

url = ""

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

# show parquet files

for file in parquet_files:

print(file)

