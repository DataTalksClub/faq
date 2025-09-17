---
id: 772aea0210
question: The spark viewer on localhost:4040 was not showing the current run
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3470
---

✅Solution: I had two notebooks running, and the one I wanted to look at had opened a port on localhost:4041.

If a port is in use, then Spark uses the next available port number. It can be even 4044. Clean up after yourself when a port does not work or a container does not run.

You can run spark.sparkContext.uiWebUrl

and result will be some like
'http://172.19.10.61:4041'

