---
id: 53f31cd33c
question: Why might some API response fields be missing after a dlt pipeline run,
  and how can I fix it?
sort_order: 17
---

Root cause:
- dlt infers column types from actual data in the current load. If a column contains only NULL values in that load, dlt cannot infer its type and the column will not be materialized in the destination table.

Fixes:
1) Provide explicit type hints using the columns argument in the @dlt.resource decorator.

Example:
```python
@dlt.resource(columns={
    "rate_code": "STRING",
    "mta_tax": "FLOAT64"
})
def api_records():
    # your data loading logic here
    return fetch_api()
```

2) Ensure at least one non-null value exists for that column during ingestion.
   - If possible, modify the API payload or add a preprocessing step to emit a non-null value for the field (e.g., default values).
   - Example pre-processing (in Python):
```python
def normalize(record):
    if record.get("rate_code") is None:
        record["rate_code"] = "UNKNOWN"
    if record.get("mta_tax") is None:
        record["mta_tax"] = 0.0
    return record
```

After applying either fix, re-run the pipeline. The destination table will materialize the specified columns with the defined types.

Tips:
- Prefer explicit type hints when you know which fields to expect, especially for optional or nullable fields.
- If you cannot guarantee non-null values, always provide the explicit `columns` mapping to avoid missing columns.
