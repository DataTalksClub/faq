---
id: c2c5634e36
question: Why does casting TIMESTAMP_NTZ to BIGINT fail in Spark, and how can I convert
  it to a numeric value?
sort_order: 29
---

TIMESTAMP_NTZ cannot be cast directly to numeric types like BIGINT in Spark. To convert to a numeric representation (epoch seconds), use the to_unix_timestamp function.

```sql
SELECT to_unix_timestamp(tpep_pickup_datetime)
FROM yellow_2025_11
```
