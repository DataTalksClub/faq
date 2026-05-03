---
id: 5a1a61b6a8
question: BigQuery returns an error when I try to run the dm_monthly_zone_revenue.sql
  model.
sort_order: 20
---

After the second SELECT, change this line:

```sql
 date_trunc('month', pickup_datetime) as revenue_month,
```

To this line:

```sql
 date_trunc(pickup_datetime, month) as revenue_month,
```

Make sure that "month" isn’t surrounded by quotes!