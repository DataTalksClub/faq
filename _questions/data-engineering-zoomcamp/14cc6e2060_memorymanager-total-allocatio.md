---
course: data-engineering-zoomcamp
id: 14cc6e2060
question: 'MemoryManager: Total allocation exceeds 95.00% (1,020,054,720 bytes) of
  heap memory'
section: 'Module 5: pyspark'
sort_order: 3660
---

Default executor memory is 1gb. This error appeared when working with the homework dataset.

Error: MemoryManager: Total allocation exceeds 95.00% (1,020,054,720 bytes) of heap memory
Scaling row group sizes to 95.00% for 8 writers

Solution:

Increase the memory of the executor when creating the Spark session like this:

spark = SparkSession.builder \

.master("local[*]") \

.appName('test') \

.config("spark.executor.memory", "4g") \

.config("spark.driver.memory", "4g") \

.getOrCreate()

Remember to restart the Jupyter session (ie. close the Spark session) or the config won’t take effect.

