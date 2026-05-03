---
id: 917b0b0fb5
question: How can I sync data from PostgreSQL to BigQuery for analytical workloads?
sort_order: 45
---

Overview:
You can sync data from PostgreSQL to BigQuery by extracting tables and loading them into BigQuery datasets.

Steps:
1. Connect to PostgreSQL using a Python script
2. Read tables into pandas DataFrames
3. Use the Google Cloud BigQuery client to load data

```python
from google.cloud import bigquery

client = bigquery.Client()
table_id = 'project.dataset.table'

# Assuming df is a pandas DataFrame containing your data
job = client.load_table_from_dataframe(df, table_id)
job.result()
```

Prerequisites:
- your service account credentials are set
- the dataset exists in BigQuery
- location (US or EU) matches during queries

This approach lets you keep ingestion local while using BigQuery for scalable analytics.
