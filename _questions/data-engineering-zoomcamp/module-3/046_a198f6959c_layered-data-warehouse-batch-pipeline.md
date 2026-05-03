---
id: a198f6959c
question: How do I structure a layered data warehouse (raw, clean, analytics) for
  a batch pipeline?
sort_order: 46
---

- Raw layer: store ingested data exactly as received
- Clean layer: filter invalid records and enforce basic constraints
- Data quality (dq) layer: validate completeness and consistency (e.g. missing timestamps)
- Analytics layer: build aggregated views
- Mart layer: expose final business metrics

Flow: raw → clean → dq → analytics → mart

Each layer is implemented as SQL transformations in PostgreSQL and BigQuery.

This separation helps with debugging, testing, and ensuring that analytical outputs are built on validated data.
