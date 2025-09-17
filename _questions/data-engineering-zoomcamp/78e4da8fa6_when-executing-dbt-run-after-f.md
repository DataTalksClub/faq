---
course: data-engineering-zoomcamp
id: 78e4da8fa6
question: 'When executing dbt run after fact_trips.sql has been created, the task
  failed with error:  “Access Denied: BigQuery BigQuery: Permission denied while globbing
  file pattern.”'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2610
---

1. Fixed by adding the Storage Object Viewer role to the service account in use in BigQuery.

2. Add the related roles to the service account in use in GCS.

![Image](images/data-engineering-zoomcamp/image_a3c7073f.png)

