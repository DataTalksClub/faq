---
course: data-engineering-zoomcamp
id: c8d29f6862
question: 'GCP BQ - Cannot read and write in different locations: source: <REGION_HERE>,
  destination: <ANOTHER_REGION_HERE>'
section: 'Module 3: Data Warehousing'
sort_order: 2070
---

Make sure to create the BigQuery dataset in the very same location that you've created the GCS Bucket. For instance, if your GCS Bucket was created in `us-central1`, then BigQuery dataset must be created in the same region (us-central1, in this example)

![Image](images/data-engineering-zoomcamp/image_1d6e2776.png)

![Image](images/data-engineering-zoomcamp/image_0bec8845.png)

