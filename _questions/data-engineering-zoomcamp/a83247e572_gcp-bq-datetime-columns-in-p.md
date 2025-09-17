---
course: data-engineering-zoomcamp
id: a83247e572
question: GCP BQ - Datetime columns in Parquet files created from Pandas show up as
  integer columns in BigQuery
section: 'Module 3: Data Warehousing'
sort_order: 2120
---

Solution:

If you’re using Mage, in the last Data Exporter that writes to Google Cloud Storage use PyArrow to generate the Parquet file with the correct logical type for the datetime columns, otherwise they won't be converted to timestamp when loaded by BigQuery later on.

import pyarrow as pa

import pyarrow.parquet as pq

import os

if 'data_exporter' not in globals():

from mage_ai.data_preparation.decorators import data_exporter

# Replace with the location of your service account key JSON file.

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/personal-gcp.json'

bucket_name = "<YOUR_BUCKET_NAME>"

object_key = 'nyc_taxi_data_2022.parquet'

where = f'{bucket_name}/{object_key}'

@data_exporter

def export_data(data, *args, **kwargs):

table = pa.Table.from_pandas(data, preserve_index=False)

gcs = pa.fs.GcsFileSystem()

pq.write_table(

table,

where,

# Convert integer columns in Epoch milliseconds

# to Timestamp columns in microseconds ('us') so

# they can be loaded into BigQuery with the right

# data type

coerce_timestamps='us',

filesystem=gcs

)

Solution 2:

If you’re using Mage, in the last Data Exporter that writes to Google Cloud Storage, provide PyArrow with explicit schema to generate the Parquet file with the correct logical type for the datetime columns, otherwise they won't be converted to timestamp when loaded by BigQuery later on.

schema = pa.schema([

('vendor_id', pa.int64()),

('lpep_pickup_datetime', pa.timestamp('ns')),

('lpep_dropoff_datetime', pa.timestamp('ns')),

('store_and_fwd_flag', pa.string()),

('ratecode_id', pa.int64()),

('pu_location_id', pa.int64()),

('do_location_id', pa.int64()),

('passenger_count', pa.int64()),

('trip_distance', pa.float64()),

('fare_amount', pa.float64()),

('extra', pa.float64()),

('mta_tax', pa.float64()),

('tip_amount', pa.float64()),

('tolls_amount', pa.float64()),

('improvement_surcharge', pa.float64()),

('total_amount', pa.float64()),

('payment_type', pa.int64()),

('trip_type', pa.int64()),

('congestion_surcharge', pa.float64()),

('lpep_pickup_month', pa.int64())

])

table = pa.Table.from_pandas(data, schema=schema)

