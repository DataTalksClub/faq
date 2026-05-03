---
id: 76f95c1d28
question: 'Terraform: Terraform initialized in an empty directory! The directory has
  no Terraform configuration files. You may begin working with Terraform immediately
  by creating Terraform configuration files.'
sort_order: 9
---

This error occurs when `terraform init` is run outside the working directory.

To resolve this issue:

1. Navigate to the working directory that contains your Terraform configuration files.
2. Run the `terraform init` command inside the correct directory.

Make sure your configuration files (e.g., .tf files) are present in the directory before running the command.