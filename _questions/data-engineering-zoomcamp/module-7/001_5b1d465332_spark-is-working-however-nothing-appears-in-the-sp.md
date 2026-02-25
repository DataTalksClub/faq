---
id: 5b1d465332
question: 'Spark: Is working, however, nothing appears in the Spark UI (e.g., .show())?'
sort_order: 1
---

Since we used multiple notebooks during the course, it's possible that there are more than one Spark session active. It’s highly likely that you are observing the incorrect one. Follow these steps to troubleshoot:

- Spark uses port 4040 by default, but if more than one session is active, it will try to use the next available port (e.g., 4041).

- Ensure you're viewing the correct Spark Web UI for the application where your jobs are running.

- Verify the current application session address:
  
  ```python
  # Using the following command in your session
  spark.sparkContext.uiWebUrl
  ```
  
  Expected output might look like:
  
  ```
  http://your.application.session.address.internal:4041
  ```
  
  Indicating port 4041.

- If using a VM, make sure you forward the identified port to access the web UI on `localhost:<port>`. 