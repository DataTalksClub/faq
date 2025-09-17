---
course: data-engineering-zoomcamp
id: e058b2432a
question: 'Cannot create a cluster: Insufficient ''SSD_TOTAL_GB'' quota. Requested
  500.0, available 250.0.'
section: 'Module 5: pyspark'
sort_order: 3850
---

A: The master and worker nodes are allocated a maximum of 250 GB of memory combined. In the configuration section, adhere to the following specifications:

Master Node:

Machine type: n2-standard-2

Primary disk size: 85 GB

Worker Node:

Number of worker nodes: 2

Machine type: n2-standard-2

Primary disk size: 80 GB

You can allocate up to 82.5 GB memory for worker nodes, keeping in mind that the total memory allocated across all nodes cannot exceed 250 GB.

