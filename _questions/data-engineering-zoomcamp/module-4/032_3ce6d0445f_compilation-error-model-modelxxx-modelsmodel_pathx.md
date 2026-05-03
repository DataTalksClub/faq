---
id: 3ce6d0445f
question: 'Compilation Error: Model ''model.XXX'' (models/<model_path>/XXX.sql) depends
  on a source named ''<a table name>'' which was not found'
sort_order: 32
---

Remember to modify your `.sql` models to read from existing table names in BigQuery/Postgres DB.

Example:

```sql
select * from {{ source('staging', '<your table name in the database>') }}
```