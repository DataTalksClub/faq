---
id: a3790900cc
question: 'Spark-shell: unable to load native-hadoop library for platform - Windows'
sort_order: 4
---

If after installing Java (either JDK or OpenJDK), Hadoop, and Spark, and setting the corresponding environment variables, you encounter the following error when running `spark-shell` in CMD:

```java
java.lang.IllegalAccessError: class org.apache.spark.storage.StorageUtils$ (in unnamed module @0x3c947bc5) cannot access class sun.nio.ch.DirectBuffer (in module java.base) because module java.base does not export sun.nio.ch to unnamed module @0x3c947bc5
```

Solution:
- Java 17 or 19 is not supported by Spark. 
- Spark 3.x requires Java 8, 11, or 16.
- Install Java 11 from the website provided in the windows.md setup file.