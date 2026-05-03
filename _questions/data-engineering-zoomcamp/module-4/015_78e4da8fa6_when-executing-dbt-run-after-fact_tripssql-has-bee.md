---
id: 78e4da8fa6
question: 'dbt + BigQuery: Access Denied / permission denied for the service account'
sort_order: 15
---

When dbt runs against BigQuery and reads from external tables backed by GCS, the service account needs permissions on both BigQuery and Cloud Storage. Common errors:

```
Access Denied: BigQuery: Permission denied while globbing file pattern
Database Error: Access Denied: User does not have bigquery.jobs.create permission ...
```

## Required roles

Grant these to the service account dbt is using (IAM & Admin → IAM in GCP console):

- BigQuery Data Editor (or BigQuery Admin) — for reading and writing dataset content.
- BigQuery Job User — for running queries.
- Storage Object Viewer (or Storage Object Admin) — for reading external table files in GCS.
- Storage Admin — for creating buckets/objects if your pipeline needs it.

The course's full setup typically uses BigQuery Admin + Storage Object Admin + Storage Admin to avoid hitting permission walls partway through.

## After updating IAM

Roles take effect almost immediately, but if dbt was already running, restart the dbt session / job. If you regenerated the service account key, re-upload the JSON in dbt Cloud (Profile → Credentials → Analytics → BigQuery → Edit) so dbt uses the latest credentials.
