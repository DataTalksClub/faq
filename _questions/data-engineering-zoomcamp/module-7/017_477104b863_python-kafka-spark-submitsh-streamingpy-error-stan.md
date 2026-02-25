---
id: 477104b863
question: 'Python Kafka: ./spark-submit.sh streaming.py - ERROR StandaloneSchedulerBackend:
  Application has been killed. Reason: All masters are unresponsive! Giving up.'
sort_order: 17
---

While following [tutorial 13.2](https://www.youtube.com/watch?v=5hRJ8-6Fpyk&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=79), when running `./spark-submit.sh streaming.py`, encountered the following error:

```
24/03/11 09:48:36 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://localhost:7077...

24/03/11 09:48:36 INFO TransportClientFactory: Successfully created connection to localhost/127.0.0.1:7077 after 10 ms (0 ms spent in bootstraps)

24/03/11 09:48:54 WARN GarbageCollectionMetrics: To enable non-built-in garbage collector(s) List(G1 Concurrent GC), users should configure it(them) to spark.eventLog.gcMetrics.youngGenerationGarbageCollectors or spark.eventLog.gcMetrics.oldGenerationGarbageCollectors

24/03/11 09:48:56 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://localhost:7077…

24/03/11 09:49:16 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://localhost:7077...

24/03/11 09:49:36 WARN StandaloneSchedulerBackend: Application ID is not initialized yet.

24/03/11 09:49:36 ERROR StandaloneSchedulerBackend: Application has been killed. Reason: All masters are unresponsive! Giving up.

py4j.protocol.Py4JJavaError: An error occurred while calling None.org.apache.spark.sql.SparkSession.

: java.lang.IllegalStateException: Cannot call methods on a stopped SparkContext.
```

**Solution:**

1. **Downgrade PySpark:**
   - Downgrade your local PySpark to 3.3.1 (ensure it matches the version used in Dockerfile).
   - The mismatch of PySpark versions can be a cause of the failed connection.
   - Check the logs of `spark-master` in the Docker container for confirmation.

2. **Check Spark Version:**
   - Run `pyspark --version` and `spark-submit --version` to check your local Spark version.
   - Adjust the `SPARK_VERSION` variable in `build.sh` to match your current Spark version.
