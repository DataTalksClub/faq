---
id: 8986dd4006
question: Why do my SQL LEFT JOIN queries return NULL values in some columns?
sort_order: 114
---

- A LEFT JOIN returns all rows from the left table. If there is no matching row in the right table, the columns from the right table are NULL for that row. This is expected SQL behavior and does not indicate a data ingestion or schema problem. It simply means some records do not have corresponding entries in the joined table.

Example:

```sql
SELECT a.id, a.name, b.value
FROM left_table a
LEFT JOIN right_table b ON a.id = b.id;
```

In the result, rows with no match will have NULL in b.value. If you'd like to exclude rows without matches, use an INNER JOIN or filter:

```sql
-- Only rows with a match
SELECT a.id, a.name, b.value
FROM left_table a
INNER JOIN right_table b ON a.id = b.id;

-- Or keep all rows but filter out NULLs
SELECT a.id, a.name, b.value
FROM left_table a
LEFT JOIN right_table b ON a.id = b.id
WHERE b.value IS NOT NULL;
```

If you want to display a default value instead of NULL, use COALESCE:

```sql
SELECT a.id, a.name, COALESCE(b.value, 'N/A') AS value
FROM left_table a
LEFT JOIN right_table b ON a.id = b.id;
```