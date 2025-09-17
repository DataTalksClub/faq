---
id: 477104b863
question: Python Kafka: ./spark-submit.sh streaming.py - ERROR StandaloneSchedulerBackend: Application has been killed. Reason: All masters are unresponsive! Giving up.
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 4040
---

While following  , when running ./spark-submit.sh streaming.py, encountered the following error:

…

24/03/11 09:48:36 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://localhost:7077...

24/03/11 09:48:36 INFO TransportClientFactory: Successfully created connection to localhost/127.0.0.1:7077 after 10 ms (0 ms spent in bootstraps)

24/03/11 09:48:54 WARN GarbageCollectionMetrics: To enable non-built-in garbage collector(s) List(G1 Concurrent GC), users should configure it(them) to spark.eventLog.gcMetrics.youngGenerationGarbageCollectors or spark.eventLog.gcMetrics.oldGenerationGarbageCollectors

24/03/11 09:48:56 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://localhost:7077…

24/03/11 09:49:16 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://localhost:7077...

24/03/11 09:49:36 WARN StandaloneSchedulerBackend: Application ID is not initialized yet.

24/03/11 09:49:36 ERROR StandaloneSchedulerBackend: Application has been killed. Reason: All masters are unresponsive! Giving up.

…

py4j.protocol.Py4JJavaError: An error occurred while calling None.org.apache.spark.sql.SparkSession.

: java.lang.IllegalStateException: Cannot call methods on a stopped SparkContext.

…

Solution:

Downgrade your local PySpark to 3.3.1 (same as Dockerfile)

The reason for the failed connection in my case was the mismatch of PySpark versions. You can see that from the logs of spark-master in the docker container.

Solution 2:

Check what Spark version your local machine has

pyspark –version

spark-submit –version

Add your version to SPARK_VERSION in build.sh

