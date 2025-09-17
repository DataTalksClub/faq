---
course: data-engineering-zoomcamp
id: e34580b954
question: Billing account has not been enabled for this project. But you’ve done it
  indeed!
section: 'Module 1: Docker and Terraform'
sort_order: 1510
---

if you’ve got the error

│ Error: Error updating Dataset "projects/<your-project-id>/datasets/demo_dataset": googleapi: Error 403: Billing has not been enabled for this project. Enable billing at https://console.cloud.google.com/billing. The default table expiration time must be less than 60 days, billingNotEnabled

but you’ve set your billing account indeed, then try to disable billing for the project and enable it again. It worked for ME!

![Image](images/data-engineering-zoomcamp/image_366e8371.png)

![Image](images/data-engineering-zoomcamp/image_ee2aa0ad.png)

