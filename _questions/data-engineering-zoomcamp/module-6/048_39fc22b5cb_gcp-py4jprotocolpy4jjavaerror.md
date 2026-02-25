---
id: 39fc22b5cb
question: 'GCP: py4j.protocol.Py4JJavaError'
sort_order: 48
---

When submitting a job, you might encounter a `py4j.protocol.Py4JJavaError` related to Java in the log panel within Dataproc. 

To address this error, consider the following steps:

1. **Cluster Versioning Control:**
   - If you've recently changed the versioning settings, ensure that the cluster configuration is compatible with your requirements. For example, switching from **Debian-Hadoop-Spark** to **Ubuntu 20.02-Hadoop3.3-Spark3.3** might resolve issues if you have a similar setup on your local machine.

2. **Consistency with Local Environment:**
   - Aligning the cluster's OS version and software stack with your local environment can help reduce configuration issues.

Although specific documentation may not be available, this approach has proven effective in some scenarios.