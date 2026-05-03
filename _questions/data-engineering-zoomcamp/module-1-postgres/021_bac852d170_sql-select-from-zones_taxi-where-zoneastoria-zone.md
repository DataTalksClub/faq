---
id: bac852d170
question: 'SQL: SELECT * FROM zones_taxi WHERE Zone=''Astoria Zone''; Error Column
  Zone doesn''t exist'
sort_order: 21
---

For this issue, you can use the following solution:

```sql
SELECT * FROM zones AS z WHERE z."Zone" = 'Astoria Zone';
```

Columns that start with uppercase sometimes need to be enclosed in double quotes.

Additionally, check your dataset for the existence of `'Astoria Zone'`. You might find only `'Astoria'`:

```sql
SELECT * FROM zones AS z WHERE z."Zone" = 'Astoria';
```