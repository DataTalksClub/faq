---
course: data-engineering-zoomcamp
id: a3790900cc
question: 'Spark-shell: unable to load native-hadoop library for platform - Windows'
section: 'Module 5: pyspark'
sort_order: 3310
---

If after installing Java (either jdk or openjdk), Hadoop and Spark, and setting the corresponding environment variables you find the following error when spark-shell is run at CMD:

java.lang.IllegalAccessError: class org.apache.spark.storage.StorageUtils$ (in unnamed module @0x3c947bc5) cannot access class sun.nio.ch.DirectBuffer (in module java.base) because module java.base does not export sun.nio.ch to unnamed

module @0x3c947bc5

Solution: Java 17 or 19 is not supported by Spark. Spark 3.x: requires Java 8/11/16. Install Java 11 from the website provided in the windows.md setup file.

