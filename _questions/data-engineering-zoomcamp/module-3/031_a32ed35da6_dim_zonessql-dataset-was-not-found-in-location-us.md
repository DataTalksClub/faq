---
id: a32ed35da6
question: Dim_zones.sql Dataset was not found in location US When Running fact_trips.sql
sort_order: 31
---

To solve this error, specify the location as `US` when creating the `dim_zones` table:

```sql
{{ config(
    materialized='table',
    location='US'
) }}
```

Update this part, re-run the `dim_zones` creation, and then run `fact_trips`.