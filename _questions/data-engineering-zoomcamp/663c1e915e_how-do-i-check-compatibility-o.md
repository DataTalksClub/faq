---
course: data-engineering-zoomcamp
id: 663c1e915e
question: How do I check compatibility of local and container Spark versions?
section: 'Module 6: streaming with kafka'
sort_order: 4140
---

You can check the version of your local spark using spark-submit --version. In the build.sh file of the Python folder, make sure that SPARK_VERSION matches your local version. Similarly, make sure the pyspark you pip installed also matches this version.

