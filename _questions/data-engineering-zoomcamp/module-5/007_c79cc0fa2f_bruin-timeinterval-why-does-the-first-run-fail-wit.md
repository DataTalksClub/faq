---
id: c79cc0fa2f
question: 'Bruin time_interval: Why does the first run fail with a ''table does not
  exist'' catalog error?'
sort_order: 7
---

The time_interval materialization strategy deletes the target table before loading data for the requested time window. On the first run, the table does not exist yet, so the DELETE statement fails with a catalog error.

How to resolve:
- Run the asset once using create+replace to create the table.
- After the table exists, switch the materialization strategy back to time_interval.

Alternatively, run the pipeline with a full refresh to ensure the table exists before incremental logic runs:

```
bruin run pipeline --full-refresh
```

Notes:
- After the initial run creates the table, you can continue using time_interval as intended.
