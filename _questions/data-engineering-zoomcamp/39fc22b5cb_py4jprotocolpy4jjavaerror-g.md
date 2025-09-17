---
course: data-engineering-zoomcamp
id: 39fc22b5cb
question: py4j.protocol.Py4JJavaError  GCP
section: 'Module 5: pyspark'
sort_order: 3750
---

When submit a job, it might throw an error about Java in log panel within Dataproc. I changed the Versioning Control when I created a cluster, so it means that I delete the cluster and created a new one, and instead of choosing Debian-Hadoop-Spark, I switch to Ubuntu 20.02-Hadoop3.3-Spark3.3 for Versioning Control feature, the main reason to choose this is because I have the same Ubuntu version in mi laptop, I tried to find documentation to sustent this but unfortunately I couldn't nevertheless it works for me.

