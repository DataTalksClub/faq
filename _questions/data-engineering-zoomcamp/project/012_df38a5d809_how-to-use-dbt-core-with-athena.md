---
id: df38a5d809
question: How to use dbt-core with Athena?
sort_order: 12
---

If you don’t have access to dbt Cloud, which is natively supported by AWS, you can use the community-built [dbt-Athena Adapter](https://dbt-athena.github.io/) for dbt-Core. Here are some references:

- [AWS Blog](https://aws.amazon.com/blogs/big-data/from-data-lakes-to-insights-dbt-adapter-for-amazon-athena-now-supported-in-dbt-cloud/)
- [YouTube Tutorial](https://youtu.be/JEizJAaaBkg?si=niTYdWoeiyC_w3h7)
- [dbt Guides: Athena](https://docs.getdbt.com/guides/athena?step=1)
- [dbt Athena Setup Documentation](https://docs.getdbt.com/docs/core/connect-data-platform/athena-setup)

### Key Features:

- Enables dbt to work with AWS Athena using dbt Core
- Allows data transformation using `CREATE TABLE AS` or `CREATE VIEW` SQL queries

### Not Yet Supported Features:

- Python models
- Persisting documentation for views

This adapter can be a valuable resource for those who need to work with Athena using dbt Core.