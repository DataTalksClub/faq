---
id: 7fc105290f
question: Why are dataset row counts computed in PostgreSQL instead of within the
  Kestra workflow?
sort_order: 14
---

Kestra is designed to orchestrate tasks rather than perform analytical computations. Row counts represent dataset-level analytics that are best computed in the database layer after ingestion, ensuring correctness and separation of responsibilities.