---
id: cbaecfefaf
question: Data Type Error when running fact table
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2910
---

If you encounter data type error on trip_type column, it may due to some nan values that isn’t null in bigquery.

Solution: try casting it to FLOAT datatype instead of NUMERIC

