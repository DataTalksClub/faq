---
id: 0c9fc7e7d3
question: Error: Insufficient 'SSD_TOTAL_GB' quota. Requested 500.0, available 470.0.
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3790
---

Sometimes while creating a dataproc cluster on GCP, the following error is encountered.

![Image](images/data-engineering-zoomcamp/image_6ab99490.png)

Solution: As mentioned , sometimes there might not be enough resources in the given region to allocate the request. Usually, gets freed up in a bit and one can create a cluster. – abhirup ghosh

Solution 2:  Changing the type of boot-disk from PD-Balanced to PD-Standard, in terraform, helped solve the problem.- Sundara Kumar Padmanabhan

