---
id: 05fc1b38f6
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_073b1786.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_57fd99e0.png
question: 'Hadoop: Exception in thread "main" java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0(Ljava/lang/String;I)Z'
sort_order: 43
---

If you are seeing this (or similar) error when attempting to write to parquet, it is likely an issue with your path variables.

For Windows, follow these steps:

1. Create a new User Variable "HADOOP_HOME" that points to your Hadoop directory.
2. Add "%HADOOP_HOME%\bin" to the PATH variable.

<{IMAGE:image_1}>

<{IMAGE:image_2}>

Additional tips can be found here: [Stack Overflow](https://stackoverflow.com/questions/41851066/exception-in-thread-main-java-lang-unsatisfiedlinkerror-org-apache-hadoop-io)