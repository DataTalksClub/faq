---
id: c493aa6b92
question: Why can't row count questions in Homework 2 be answered directly from Kestra
  execution logs?
sort_order: 16
---

- Kestra orchestrates workflows but does not automatically aggregate dataset-level metrics such as total row counts across multiple executions.
- Questions involving total rows for a full year or specific months require querying the target database after ingestion.
- In Homework 2, accurate row counts were obtained using SQL queries against PostgreSQL tables populated by the Kestra flows.