---
id: 8815e0f1fd
question: Why use dbt if we already have Python?
sort_order: 68
---

You could do transformations in Python (with pandas, polars, or by sending SQL to the warehouse yourself), but dbt is built specifically for SQL transformations in a warehouse and gives you a few things for free that you would otherwise build yourself:

- Model dependencies via `ref()` — dbt figures out the run order
- Tests (not null, unique, accepted values, custom assertions)
- Documentation and lineage graphs
- Environment separation (dev/prod) through profiles
- Incremental models without writing the merge logic by hand

The other reason is where the work happens. When you transform in Python, data flows through your machine (or your worker). When you use dbt with BigQuery, the SQL runs inside BigQuery — no data movement, scales with the warehouse, not with your laptop.

A common split:

- Python for ingestion (APIs, files, anything not already in SQL)
- dbt for transformations once data is in the warehouse
- Python again for anything SQL can't express well (ML features, complex parsing)

So the answer isn't "dbt replaces Python" — it's that dbt is the right tool for the SQL transformation step, and Python stays useful for everything else.
