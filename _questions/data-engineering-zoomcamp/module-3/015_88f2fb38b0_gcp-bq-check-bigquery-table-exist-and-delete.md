---
id: 88f2fb38b0
question: 'GCP BQ: Check BigQuery Table Exist And Delete'
sort_order: 15
---

### Reference

[Stack Overflow - BigQuery Overwrite Table](https://stackoverflow.com/questions/60941726/can-bigquery-api-overwrite-existing-table-view-with-create-table-tables-inser)

### Solution

To check if a BigQuery table exists and possibly delete it, utilize the following Python function before using `client.create_table`:

```python
from google.cloud import bigquery

# Initialize client
client = bigquery.Client()

def table_exists(table_id, client):
    """
    Check if a table already exists using the tableID.

    :param table_id: str, the ID of the table
    :param client: bigquery.Client instance
    :return: Boolean
    """
    try:
        client.get_table(table_id)
        return True
    except Exception as e:  # NotFound:
        return False
```

Use this function to check table existence before creating a new table or taking further actions.