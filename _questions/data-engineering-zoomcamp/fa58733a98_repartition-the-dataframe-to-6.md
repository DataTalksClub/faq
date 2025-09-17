---
id: fa58733a98
question: Repartition the Dataframe to 6 partitions using df.repartition(6) - got 8 partitions instead
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3760
---

Use both repartition and coalesce, like so:

df = df.repartition(6)

df = df.coalesce(6)

df.write.parquet('fhv/2019/10', mode='overwrite')

