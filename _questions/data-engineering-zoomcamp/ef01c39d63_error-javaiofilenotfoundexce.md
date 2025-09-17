---
course: data-engineering-zoomcamp
id: ef01c39d63
question: Error java.io.FileNotFoundException
section: 'Module 5: pyspark'
sort_order: 3440
---

Code executed:

df = spark.read.parquet(pq_path)

… some operations on df …

df.write.parquet(pq_path, mode="overwrite")

java.io.FileNotFoundException: File file:/home/xxx/code/data/pq/fhvhv/2021/02/part-00021-523f9ad5-14af-4332-9434-bdcb0831f2b7-c000.snappy.parquet does not exist

The problem is that Sparks performs lazy transformations, so the actual action that trigger the job is df.write, which does delete the parquet files that is trying to read (mode=”overwrite”)

✅Solution: Write to a different directorydf

df.write.parquet(pq_path_temp, mode="overwrite")

