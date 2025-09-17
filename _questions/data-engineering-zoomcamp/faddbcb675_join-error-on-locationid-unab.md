---
id: faddbcb675
question: Join Error on LocationID “Unable to find common supertype for templated argument”
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3170
---

No matching signature for operator = for argument types: STRING, INT64

Signature: T1 = T1

Unable to find common supertype for templated argument

Make sure the LocationID field is in the same type. If it is in string format in one table, we can use the following code in dbt to convert it to integer:

{{ dbt.safe_cast("PULocationID", api.Column.translate_type("integer")) }} as pickup_locationid

