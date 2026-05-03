---
id: 4ecc97beb5
question: How to set credentials in Google Colab notebook to connect to BigQuery
sort_order: 6
---

In the secrets sidebar, create a secret `BIGQUERY_CREDENTIALS` with the value being your Google Cloud service account key. Then load it with:

```python
import os
from google.colab import userdata

os.environ["DESTINATION__BIGQUERY__CREDENTIALS"] = userdata.get('BIGQUERY_CREDENTIALS')
```