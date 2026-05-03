---
id: e596dc3cbe
question: 'dbt: dbt_utils.surrogate_key has been renamed to dbt_utils.generate_surrogate_key'
sort_order: 14
---

In `dbt-utils` 1.0+, `dbt_utils.surrogate_key` was renamed to `dbt_utils.generate_surrogate_key`. If you copy the macro call from older course materials you'll see a deprecation warning or an error.

Fix: replace every `surrogate_key` call with `generate_surrogate_key`. The arguments are the same.

```sql
{{ dbt_utils.generate_surrogate_key(['field_a', 'field_b', 'field_c']) }}
```

Common places in the course where this comes up: `stg_green_tripdata.sql`, `stg_yellow_tripdata.sql`, and similar staging models.
