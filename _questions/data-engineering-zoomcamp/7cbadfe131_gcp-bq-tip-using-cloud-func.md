---
course: data-engineering-zoomcamp
id: 7cbadfe131
question: 'GCP BQ - Tip: Using Cloud Function to read csv.gz files from github directly
  to BigQuery in Google Cloud:'
section: 'Module 3: Data Warehousing'
sort_order: 2170
---

There are multiple benefits of using Cloud Functions to automate tasks in Google Cloud.

Use below Cloud Function python script to load files directly to BigQuery. Use your project id, dataset id & table id as defined by you.

import tempfile

import requests

import logging

from google.cloud import bigquery

def hello_world(request):

# table_id = <project_id.dataset_id.table_id>

table_id = 'de-zoomcap-project.dezoomcamp.fhv-2019'

# Create a new BigQuery client

client = bigquery.Client()

for month in range(4, 13):

# Define the schema for the data in the CSV.gz files

url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-{:02d}.csv.gz'.format(month)

# Download the CSV.gz file from Github

response = requests.get(url)

# Create new table if loading first month data else append

write_disposition_string = "WRITE_APPEND" if month > 1 else "WRITE_TRUNCATE"

# Defining LoadJobConfig with schema of table to prevent it from changing with every table

job_config = bigquery.LoadJobConfig(

schema=[

bigquery.SchemaField("dispatching_base_num", "STRING"),

bigquery.SchemaField("pickup_datetime", "TIMESTAMP"),

bigquery.SchemaField("dropOff_datetime", "TIMESTAMP"),

bigquery.SchemaField("PUlocationID", "STRING"),

bigquery.SchemaField("DOlocationID", "STRING"),

bigquery.SchemaField("SR_Flag", "STRING"),

bigquery.SchemaField("Affiliated_base_number", "STRING"),

],

skip_leading_rows=1,

write_disposition=write_disposition_string,

autodetect=True,

source_format="CSV",

)

# Load the data into BigQuery

# Create a temporary file to prevent the exception- AttributeError: 'bytes' object has no attribute 'tell'"

with tempfile.NamedTemporaryFile() as f:

f.write(response.content)

f.seek(0)

job = client.load_table_from_file(

f,

table_id,

location="US",

job_config=job_config,

)

job.result()

logging.info("Data for month %d successfully loaded into table %s.", month, table_id)

return 'Data loaded into table {}.'.format(table_id)

