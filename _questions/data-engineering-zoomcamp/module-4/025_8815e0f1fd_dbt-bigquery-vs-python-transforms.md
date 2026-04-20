---
id: 8815e0f1fd
question: Why use dbt + BigQuery instead of performing all transformations in Python?
sort_order: 25
---

dbt provides modular SQL transformations, built-in data quality tests, lineage tracking, and a clear separation between transformation logic and execution. BigQuery complements this with scalable execution, efficient handling of large datasets, and the ability to run analytical queries without consuming local resources.

What this means in practice:
- Ingestion and initial preprocessing can be handled in Python, while transformation logic lives in dbt as modular SQL models.
- dbt handles dependencies, testing, and documentation, making transformations easier to reason about and maintain.
- BigQuery acts as the data warehouse and computation engine, enabling scalable analytics without requiring local compute resources.

Recommended workflow:
1. Use Python for ingestion/preprocessing.
2. Use dbt to transform staged data into analytics-ready models with tests and lineage information.
3. Query and analyze results in BigQuery.

Benefits:
- Declarative, reusable transformations via dbt models.
- Built-in data quality checks and automatic lineage.
- Clear separation of concerns between ingestion, transformation, and analytics.
- Scales with data volume while keeping development and testing rapid.

When to consider this approach:
- You have multiple transformation steps with dependencies.
- You need data quality checks and documented lineage.
- You want to separate ingestion/processing from transformation logic and analytics.

Trade-offs:
- Initial setup and a learning curve for dbt and BigQuery.
- Ongoing costs associated with BigQuery usage and dbt tooling.

This approach aligns with the recommended architecture where Python handles ingestion, dbt encapsulates transformation logic, and the warehouse (BigQuery) serves as the computation engine.