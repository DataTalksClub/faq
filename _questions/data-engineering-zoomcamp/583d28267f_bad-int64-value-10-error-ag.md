---
course: data-engineering-zoomcamp
id: 583d28267f
question: 'Bad int64 value: 1.0 error (again)'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2950
---

I found that there are more columns causing the bad INT64: ratecodeid and trip_type on Green_tripdata table.
You can use the queries below to address them:

CAST(

REGEXP_REPLACE(CAST(rate_code AS STRING), r'\.0', '') AS INT64

) AS ratecodeid,

CAST(

CASE

WHEN REGEXP_CONTAINS(CAST(trip_type AS STRING), r'\.\d+') THEN NULL

ELSE CAST(trip_type AS INT64)

END AS INT64

) AS trip_type,

