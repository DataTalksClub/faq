---
course: machine-learning-zoomcamp
id: 5a7cdb33f2
question: Permissions to push docker to Google Container Registry
section: Miscellaneous
sort_order: 3960
---

When you try to push the docker image to Google Container Registry and get this message “unauthorized: You don't have the needed permissions to perform this operation, and you may have invalid credentials.”, type this below on console, but first install [[cloud.google.com](https://cloud.google.com/sdk/docs/install)](https://cloud.google.com/sdk/docs/install), this is to be able to use gcloud in console:

gcloud auth configure-docker

(Jesus Acuña)

