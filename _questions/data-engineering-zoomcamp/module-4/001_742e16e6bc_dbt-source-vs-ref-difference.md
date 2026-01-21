---
id: 742e16e6bc
question: What is the difference between ref() and source() in dbt?
sort_order: 1
---

In dbt, source() and ref() are both used to reference tables, but they serve different purposes in the data pipeline.

source() – Referencing External Source Tables
source() is used to reference raw or external tables that are not created by dbt.
These tables usually live in a data warehouse such as BigQuery or Snowflake and are defined in a sources.yml file.

Key points:
- Used for raw / upstream data
- Defined in sources.yml
- dbt does not control how the table is created
- Enables freshness checks, documentation, and testing

Example:
```sql
SELECT *
FROM {{ source('raw', 'trips') }}
```

ref() – Referencing dbt Models
ref() is used to reference other dbt models (SQL files inside the dbt project).
dbt uses ref() to automatically manage model dependencies and execution order.

Key points:
- Used for dbt-generated models
- Automatically resolves schema and table names
- Controls run order and lineage
- Enables DAG, documentation, and refactoring safety

Example:
```sql
SELECT *
FROM {{ ref('stg_trips') }}
```