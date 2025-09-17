---
id: c37b2ed3a5
question: Compilation Error (Model 'model.my_new_project.stg_green_tripdata' (models/staging/stg_green_tripdata.sql) depends on a source named 'staging.green_trip_external' which was not found)
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2770
---

If you're following video DE Zoomcamp 4.3.1 - Building the First DBT Models, you may have encountered an issue at 14:25 where the Lineage graph isn't displayed and a Compilation Error occurs, as shown in the attached image. Don't worry - a quick fix for this is to simply save your schema.yml file. Once you've done this, you should be able to view your Lineage graph without any further issues.

![Image](images/data-engineering-zoomcamp/image_ea2e4bf2.png)

