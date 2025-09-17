---
course: data-engineering-zoomcamp
id: 28f6392ce5
question: Hack to load yellow and green trip data for 2019 and 2020
section: 'Module 4: analytics engineering with dbt'
sort_order: 2550
---

I initially followed

But it was taking forever for the yellow trip data and when I tried to download and upload the parquet files directly to GCS, that works fine but when creating the Bigquery table, there was a schema inconsistency issue

Then I found another hack shared in the slack which was suggested by Victoria.

Please watch until the end as there is few schema changes required to be done

