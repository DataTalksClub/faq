---
id: 0e8bce921a
question: 'Python Kafka: ./spark-submit.sh streaming.py Error: py4j.protocol.Py4JJavaError:
  An error occurred while calling None.org.apache.spark.api.java.JavaSparkContext.'
sort_order: 19
---

Make sure your Java version is 11 or 8.

- Check your version by:

  ```bash
  java --version
  ```

- Check all your installed Java versions by:

  ```bash
  /usr/libexec/java_home -V
  ```

- If you already have Java 11 but it's not set as the default, select the specific version by:

  ```bash
  export JAVA_HOME=$(/usr/libexec/java_home -v 11.0.22)
  ```

  (or another version of 11)