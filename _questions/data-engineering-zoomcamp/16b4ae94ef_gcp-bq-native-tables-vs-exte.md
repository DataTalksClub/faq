---
course: data-engineering-zoomcamp
id: 16b4ae94ef
question: GCP BQ - Native tables vs External tables in BigQuery?
section: 'Module 3: Data Warehousing'
sort_order: 2240
---

Native tables are tables where the data is stored in BigQuery.  External tables store the data outside BigQuery, with BigQuery storing metadata about that external table.

External tables: They are not stored directly in big query tables but pulled in from a data lake such as Google Cloud Storage or S3.

Materialized table: Copy of this external table. Now the data is stored in the bigquery table and consumes the space.

Resources:

