---
id: a198f6959c
question: Why use a layered data pipeline (raw → canonical → analytics → mart) instead
  of directly analyzing raw data, and how do the canonical and analytics layers improve
  schema, metrics, and stability?
sort_order: 51
---

Direct analysis on raw data creates tight coupling between ingestion format and analytical logic, leading to repeated cleaning, inconsistent metric definitions, and fragile transformations as data sources evolve. A layered pipeline separates responsibilities and improves reproducibility. The core layers are:

- Raw layer: store ingested data exactly as received to preserve fidelity and enable re-ingestion without loss.
- Canonical layer: standardizes data into a single, well-defined schema (canonical form); enforces data correctness and consistent types, enabling stable downstream logic.
- Analytics layer: encapsulates reusable metric definitions and transformations; business logic lives here and is reused across reports.
- Mart layer: builds consumable, time-series-friendly representations for dashboards and queries; optimized for fast reads.

Why canonical over direct clean/quality steps? Canonical acts as the contract between upstream sources and downstream analytics. It decouples ingestion variability from analytics logic, so downstream insights remain stable even if upstream data changes. This aligns with production-grade ELT: extract raw data, load into canonical, then transform into analytics and mart representations.

Benefits include improved reproducibility, easier maintenance, consistent metrics, easier testing, and scalable transformations across data sources. In practice, many teams structure pipelines as raw → canonical → analytics → mart (some designs also include an explicit data quality layer between canonical and analytics if needed).