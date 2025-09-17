---
course: data-engineering-zoomcamp
id: 7c97a61529
question: GCP BQ - Create External Table using Python
section: 'Module 3: Data Warehousing'
sort_order: 2130
---

Reference:

Solution:

from google.cloud import bigquery

# Set table_id to the ID of the table to create

table_id = f"{project_id}.{dataset_name}.{table_name}"

# Construct a BigQuery client object

client = bigquery.Client()

# Set the external source format of your table

external_source_format = "PARQUET"

# Set the source_uris to point to your data in Google Cloud

source_uris = [ f'gs://{bucket_name}/{object_key}/*']

# Create ExternalConfig object with external source format

external_config = bigquery.ExternalConfig(external_source_format)

# Set source_uris that point to your data in Google Cloud

external_config.source_uris = source_uris

external_config.autodetect = True

table = bigquery.Table(table_id)

# Set the external data configuration of the table

table.external_data_configuration = external_config

table = client.create_table(table)  # Make an API request.

print(f'Created table with external source: {table_id}')

print(f'Format: {table.external_data_configuration.source_format}')

