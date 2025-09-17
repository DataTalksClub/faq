---
course: data-engineering-zoomcamp
id: 05fc1b38f6
question: 'Hadoop - Exception in thread "main" java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0(Ljava/lang/String;I)Z'
section: 'Module 5: pyspark'
sort_order: 3700
---

If you are seeing this (or similar) error when attempting to write to parquet, it is likely an issue with your path variables.

For Windows, create a new User Variable “HADOOP_HOME” that points to your Hadoop directory. Then add “%HADOOP_HOME%\bin” to the PATH variable.

![Image](images/data-engineering-zoomcamp/image_073b1786.png)

![Image](images/data-engineering-zoomcamp/image_57fd99e0.png)

Additional tips can be found here: https://stackoverflow.com/questions/41851066/exception-in-thread-main-java-lang-unsatisfiedlinkerror-org-apache-hadoop-io

