---
id: 08326f6fa9
question: How can I estimate the cost of executed queries in BigQuery within a specific
  time window, and identify which users ran them and when?
sort_order: 114
---

Overview:
This snippet shows how to estimate the cost of executed queries in BigQuery over a time window using the INFORMATION_SCHEMA.JOBS_BY_PROJECT history metadata. The data is grouped by date, user, job_type, and statement_type to identify who ran queries and their cost.

```sql
SELECT
  DATE(creation_time) as date,
  job_type,
  statement_type,
  user_email,
  SUM(total_bytes_billed) / 1099511627776 * 6.25 as estimated_cost_usd,  -- on-demand model costs are defined US$ 6.25 per TB
  COUNT(*) as query_count
FROM `project-0c3c5223-416f-4242-b0f.region-us.INFORMATION_SCHEMA.JOBS_BY_PROJECT`
WHERE creation_time >= DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -60 DAY)  --Interval can be modified
GROUP BY date, user_email, job_type, statement_type
ORDER BY estimated_cost_usd DESC -- Order by the highest cost execution based on total bytes billed
;
```

Output:
With this query we will be able to find insights about in which dates and what users did query executions with highest costs and optimize ones that are not efficient.
