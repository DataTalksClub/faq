---
id: 9f2048fc73
question: '"Bad int64 value" / Parquet column has type DOUBLE which does not match
  INT64 — casting failures on green tripdata'
sort_order: 37
---

Several columns in the green taxi data — `ehail_fee`, `ratecodeid`, `trip_type`, `payment_type` — can fail to cast to `INT64` for two related reasons:

- The Parquet file stores the column as `DOUBLE` (BigQuery sees the schema mismatch directly).
- The values look like `1.0`, `2.0`, etc. — they're whole numbers but stored as floats, which BigQuery's `INT64` cast rejects.

You'll see errors like:

```
Parquet column 'ehail_fee' has type DOUBLE which does not match the target cpp_type INT64
Bad int64 value: 0.0
Bad int64 value: 1.0
```

## Fixes

### Option 1: Use `safe_cast` in your dbt model

`safe_cast` returns NULL instead of erroring on a failed cast:

```sql
{{ dbt.safe_cast('ehail_fee', api.Column.translate_type("numeric")) }} as ehail_fee,
```

Or without `dbt_utils`:

```sql
safe_cast(ehail_fee as numeric) as ehail_fee
```

For `ehail_fee` specifically, prefer `numeric` over `integer` — fees aren't always whole numbers.

### Option 2: Drop the column

If the column isn't used downstream, just drop it:

```sql
SELECT * EXCEPT (ehail_fee) FROM ...
```

### Option 3: Strip the trailing `.0` before casting

Useful for fields like `ratecodeid` and `trip_type` where the values really are integers but stored as floats:

```sql
CAST(REGEXP_REPLACE(CAST(rate_code AS STRING), r'\.0$', '') AS INT64) AS ratecodeid,

CAST(
    CASE
        WHEN REGEXP_CONTAINS(CAST(trip_type AS STRING), r'\.\d+') THEN NULL
        ELSE CAST(trip_type AS INT64)
    END AS INT64
) AS trip_type
```

### Option 4: Fix the upstream Parquet schema

If you control the ingestion, cast to `Int64` (pandas nullable int) before writing:

```python
df['ehail_fee'] = df['ehail_fee'].astype('Int64')
```

This produces a Parquet file with the right schema and avoids the issue entirely.
