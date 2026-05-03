---
id: ce77e05d24
question: 'Spark Streaming: How do I read from multiple topics in the same Spark Session'
sort_order: 32
---

To read from multiple topics in the same Spark session, follow these steps:

1. **Initiate a Spark Session:**
   
   ```python
   spark = (SparkSession
       .builder
       .appName(app_name)
       .master(master=master)
       .getOrCreate())
   
   spark.streams.resetTerminated()
   ```

2. **Read Streams from Multiple Topics:**
   
   ```python
   query1 = spark
       .readStream
       ...
       ...
       .load()
   
   query2 = spark
       .readStream
       ...
       ...
       .load()
   
   query3 = spark
       .readStream
       ...
       ...
       .load()
   ```

3. **Start the Queries:**
   
   ```python
   query1.start()
   query2.start()
   query3.start()
   ```

4. **Await Termination:**
   
   ```python
   spark.streams.awaitAnyTermination()  # Waits for any one of the queries to receive a kill signal or error failure. This is asynchronous.
   ```

   Note: `query3.start().awaitTermination()` is a blocking call. It works well when we are reading only from one topic.