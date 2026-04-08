---
id: 8ef4012c69
question: Why do downstream Bruin assets fail with 'Table does not exist' error even
  though the upstream ingestion asset succeeded?
sort_order: 5
---

Bruin creates tables inside schemas (for example ingestion, staging, reports). If you reference a table without its schema, DuckDB will not find it and will raise a “Table does not exist” error, even if the upstream ingestion asset ran successfully. Always use schema-qualified names in downstream assets. You can verify existing tables with:

```bash
bruin query -c duckdb-default -q "SELECT table_schema, table_name FROM information_schema.tables;"
```

Example of the pitfall and the fix:

```
-- This will fail if the table was created as ingestion.trips_raw
SELECT * FROM trips_raw;

-- Correct:
SELECT * FROM ingestion.trips_raw;
```

Notes:
- Always reference the fully-qualified table name that the upstream asset created (e.g., ingestion.trips_raw, staging.orders, reports.sales_summary).
- If you’re unsure which schema a table lives in, list tables with the command above and inspect the schema column.
- Consider using explicit schema qualification in all downstream assets to prevent these errors.
