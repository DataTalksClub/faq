---
id: 772aea0210
question: The spark viewer on localhost:4040 was not showing the current run
sort_order: 20
---

**Solution:**

- Ensure you have identified all running Spark notebooks. If multiple notebooks are running, each will attempt to use available ports starting from 4040.
- If a port is in use, Spark automatically assigns the next available port (e.g., 4041, 4042, etc.).
- To find the exact port being used by your current Spark application, run the following command:

  ```python
  spark.sparkContext.uiWebUrl
  ```

- The result will provide the URL, for example: `[172.19.10.61:4041](http://172.19.10.61:4041)`.
- If the expected port does not show your current run, verify that cleanup has been performed on closed or non-running containers.