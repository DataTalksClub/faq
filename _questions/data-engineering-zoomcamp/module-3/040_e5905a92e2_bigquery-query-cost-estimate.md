---
id: e5905a92e2
question: How can I estimate BigQuery query costs over a time window and identify
  the users and times of executions?
sort_order: 40
---

Use the INFORMATION_SCHEMA.JOBS_BY_PROJECT view to estimate the cost of executed queries within a chosen time range and to see which users ran them and when. The query sums total_bytes_billed, converts to USD using a per-TB rate, and aggregates by date, user, and job type.

```sql
SELECT
  DATE(creation_time) as date,
  job_type,
  statement_type,
  user_email,
  SUM(total_bytes_billed) / 1099511627776 * 6.25 as estimated_cost_usd, -- on-demand model costs are defined US$ 6.25 per TB
  COUNT(*) as query_count
FROM <your_project_id>.<your_region>.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE creation_time >= DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -60 DAY) --Interval can be modified
GROUP BY date, user_email, job_type, statement_type
ORDER BY estimated_cost_usd DESC;
```

Notes:
- The query sums total_bytes_billed to estimate cost (6.25 USD per TB) for on-demand pricing.
- Replace `<your_project_id>.<your_region>` with your actual project and region in the FROM clause.
- Adjust the time window by changing the interval (e.g., -60 DAY).
- The results show: date, user_email, job_type, statement_type, estimated_cost_usd, and query_count. You can identify dates and users with the highest costs to target optimizations.