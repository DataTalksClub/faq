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

If you're following video 4.3.1 and the lineage graph is missing along with this error, make sure you saved your `schema.yml` — dbt only picks up the sources after the file is saved.