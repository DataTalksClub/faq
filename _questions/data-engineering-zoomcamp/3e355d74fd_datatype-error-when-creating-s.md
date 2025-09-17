---
course: data-engineering-zoomcamp
id: 3e355d74fd
question: DataType error when creating Spark DataFrame with a specified schema?
section: 'Module 5: pyspark'
sort_order: 3540
---

Probably you’ll encounter this if you followed the video ‘5.3.1 - First Look at Spark/PySpark’ and used the parquet file from the TLC website (csv was used in the video).

When defining the schema, the PULocation and DOLocationID are defined as IntegerType. This will cause an error because the Parquet file is INT64 and you’ll get an error like:

Parquet column cannot be converted in file [...] Column [...] Expected: int, Found: INT64

Change the schema definition from IntegerType to LongType and it should work

