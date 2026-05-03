---
id: faddbcb675
question: 'Join Error on LocationID: "Unable to find common supertype for templated
  argument"'
sort_order: 52
---



No matching signature for operator `=` for argument types: `STRING`, `INT64`

**Signature**: `T1 = T1`

**Error:** Unable to find common supertype for templated argument.

**Solution:**

Make sure the `LocationID` field is of the same type in both tables. If it is in string format in one table, use the following dbt code to convert it to an integer:

```sql
{{ dbt.safe_cast("PULocationID", api.Column.translate_type("integer")) }} as pickup_locationid
```