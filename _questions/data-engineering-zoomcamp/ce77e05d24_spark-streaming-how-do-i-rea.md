---
id: ce77e05d24
question: Spark Streaming - How do I read from multiple topics in the same Spark Session
section: Project
course: data-engineering-zoomcamp
sort_order: 4230
---

Initiate a Spark Session

spark = (SparkSession

.builder

.appName(app_name)

.master(master=master)

.getOrCreate())

spark.streams.resetTerminated()

query1 = spark

.readStream

…

…

.load()

query2 = spark

.readStream

…

…

.load()

query3 = spark

.readStream

…

…

.load()

query1.start()

query2.start()

query3.start()

spark.streams.awaitAnyTermination() #waits for any one of the query to receive kill signal or error failure. This is asynchronous

# On the contrary query3.start().awaitTermination() is a blocking ex call. Works well when we are reading only from one topic.

