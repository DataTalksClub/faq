---
id: 9f9a1b9e4f
question: Terraform Teardown of BigQuery Dataset
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1710
---

When running `terraform destroy`, the following error can occur:

```

Do you really want to destroy all resources?

Terraform will destroy all your managed infrastructure, as shown above.

There is no undo. Only 'yes' will be accepted to confirm.

Enter a value: yes

google_bigquery_dataset.homework_dataset: Destroying... [id=projects/terraform-demo-449214/datasets/homework_dataset]

╷

│ Error: Error when reading or editing Dataset: googleapi: Error 400: Dataset terraform-demo-449214:homework_dataset is still in use, resourceInUse

```

This is because the dataset is still in use by a table. To delete the dataset, we need to set the `delete_contents_on_destroy` property to `true` in the `main.tf` file.

