---
id: 3a53549d08
question: How does dlt handle schema evolution?
sort_order: 12
---

dlt automatically detects and adapts to most schema changes during ingestion, so you usually don't need to manually alter tables.

What happens when the source schema changes:
- If new columns appear, dlt adds the new columns to the destination table.
- If new nested fields appear, dlt also creates the required child tables or columns.
- If existing columns disappear, the columns remain in the table (they are not dropped).
- If existing columns change their data type, dlt will try to safely coerce the data; if that's not possible, it raises an error so you can handle it explicitly.

How it works under the hood:
dlt infers the schema from the incoming data and it stores the schema and pipeline state locally (in the `.dlt` folder). On the next run, it compares the incoming data with the stored schema and applies the necessary migrations to the destination.

Why this is useful in the course:
- You can ingest evolving APIs or semi-structured JSON without writing DDL.
- Your pipelines keep working even when new fields appear.
- It's safe for incremental loading — schema updates don't require a full refresh.

When you may need to intervene:
- If a column changes to an incompatible type
- If you want to enforce a specific schema or data type
- If you want to drop or rename columns
In those cases you can define the schema explicitly in your dlt resource.

Note: If you want to know more, there is a page dedicated to schema evolution in the official dlt documentation: https://dlthub.com/docs/general-usage/schema-evolution