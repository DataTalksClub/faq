---
id: 61b908fe84
question: GCP BQ - Cannot read and write in different locations: source: EU, destination: US - Loading data from GCS into BigQuery (different Region):
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2060
---

Be careful when you create your resources on GCP, all of them have to share the same Region in order to allow load data from GCS Bucket to BigQuery. If you forgot it when you created them, you can create a new dataset on BigQuery using the same Region which you used on your GCS Bucket.

![Image](images/data-engineering-zoomcamp/image_924b3959.png)

![Image](images/data-engineering-zoomcamp/image_4d72f30c.png)

This means that your GCS Bucket and the BigQuery dataset are placed in different regions. You have to create a new dataset inside BigQuery in the same region with your GCS bucket and store the data in the newly created dataset.

