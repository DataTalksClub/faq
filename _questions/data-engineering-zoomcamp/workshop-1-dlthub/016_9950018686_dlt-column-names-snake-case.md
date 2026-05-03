---
id: '9950018686'
question: How to query data when dlt normalizes column names to lowercase and snake_case?
sort_order: 16
---

DLT normalizes column names to lowercase and converts them to snake_case. For example, Trip_Pickup_DateTime becomes trip_pickup_date_time. When querying, use the normalized column names.

To discover the actual column names in a table, inspect the schema:

```sql
SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'taxi_data'
```

Then use the normalized names in your queries, e.g.:

```sql
SELECT trip_pickup_date_time
FROM taxi_data.trips;
```

Notes:
- If you try to reference the original mixed-case column name (e.g., Trip_Pickup_DateTime) you may receive a "Referenced column not found" error because DLT has renamed the column.
- Ensure you are querying the correct schema and table. The information_schema query above can help confirm the exact column names.

If you need to work with a column that has a non-normalized name, you can still enclose the column in double quotes, but with DLT's normalization you typically should use the lowercase snake_case name.
