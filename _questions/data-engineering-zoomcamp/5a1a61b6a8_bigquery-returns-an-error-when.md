---
id: 5a1a61b6a8
question: BigQuery returns an error when I try to run the dm_monthly_zone_revenue.sql model.
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2660
---

R: After the second SELECT, change this line:

date_trunc('month', pickup_datetime) as revenue_month,

To this line:

date_trunc(pickup_datetime, month) as revenue_month,

Make sure that “month” isn’t surrounded by quotes!

