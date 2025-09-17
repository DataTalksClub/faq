---
id: 852b1d09a0
question: GCP BQ - Cannot read and write in different locations: source: asia-south2, destination: US
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2160
---

Solution: This problem arises if your gcs and bigquery storage is in different regions.

One potential way to solve it:

Go to your google cloud bucket and check the region in field named “Location”

![Image](images/data-engineering-zoomcamp/image_199a39eb.jpg)

Now in bigquery, click on three dot icon near your project name and select create dataset.

![Image](images/data-engineering-zoomcamp/image_e2a4f6bc.jpg)

In region filed choose the same regions as you saw in your google cloud bucket

![Image](images/data-engineering-zoomcamp/image_9f3cd4ef.jpg)

