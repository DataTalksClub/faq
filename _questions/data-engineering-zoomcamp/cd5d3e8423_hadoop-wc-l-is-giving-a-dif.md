---
course: data-engineering-zoomcamp
id: cd5d3e8423
question: hadoop “wc -l” is giving a different result then shown in the video
section: 'Module 5: pyspark'
sort_order: 3720
---

If you are doing wc -l fhvhv_tripdata_2021-01.csv.gz  with the gzip file as the file argument, you will get a different result, obviously! Since the file is compressed.

Unzip the file and then do wc -l fhvhv_tripdata_2021-01.csv to get the right results.

