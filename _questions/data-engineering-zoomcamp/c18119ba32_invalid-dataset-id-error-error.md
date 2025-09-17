---
id: c18119ba32
question: Invalid dataset ID Error Error when running the gcp_setup flow
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1890
---

When following the  and then running the ,  it works until the create_bq_dataset task, where I got the following error:

While not very apparent from the error message, we are not suppose to use a dash in the dataset name, so I changed the dataset name to “de_zoomcamp” and it worked.

