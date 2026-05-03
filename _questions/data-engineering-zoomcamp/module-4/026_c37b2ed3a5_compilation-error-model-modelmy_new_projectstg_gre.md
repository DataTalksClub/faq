---
id: c37b2ed3a5
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_ea2e4bf2.png
question: 'Compilation Error: Model ''model.my_new_project.stg_green_tripdata'' (models/staging/stg_green_tripdata.sql)
  depends on a source named ''staging.green_trip_external'' which was not found'
sort_order: 26
---

If you're following video DE Zoomcamp 4.3.1 - Building the First DBT Models, you may encounter an issue at 14:25 where the Lineage graph isn't displayed and a Compilation Error occurs, as shown in the attached image.

Don't worry—a quick fix for this is to simply save your `schema.yml` file. Once you've done this, you should be able to view your Lineage graph without any further issues.

<{IMAGE:image_1}>
