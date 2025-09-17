---
id: 0e8bce921a
question: Python Kafka: ./spark-submit.sh streaming.py Error: py4j.protocol.Py4JJavaError: An error occurred while calling None.org.apache.spark.api.java.JavaSparkContext.
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 4060
---

Make sure your java version is 11 or 8.

Check your version by:

java --version

Check all your versions by:

/usr/libexec/java_home -V

If you already have got java 11 but just not selected as default, select the specific version by:

export JAVA_HOME=$(/usr/libexec/java_home -v 11.0.22)

(or other version of 11)

