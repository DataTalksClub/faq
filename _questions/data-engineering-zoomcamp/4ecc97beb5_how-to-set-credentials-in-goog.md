---
course: data-engineering-zoomcamp
id: 4ecc97beb5
question: How to set credentials in Google Colab notebook to connect to BigQuery
section: Workshop 1 - dlthub
sort_order: 4420
---

In the secrets sidebar, create a secret ‘BIGQUERY_CRENTIALS’ with value being your Google Cloud service account key. Then load it with:
import os

from google.colab import userdata

os.environ["DESTINATION__BIGQUERY__CREDENTIALS"] = userdata.get('BIGQUERY_CREDENTIALS')

