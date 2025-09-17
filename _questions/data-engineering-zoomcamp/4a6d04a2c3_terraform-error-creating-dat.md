---
course: data-engineering-zoomcamp
id: 4a6d04a2c3
question: 'Terraform - Error creating Dataset: googleapi: Error 403: Request had insufficient
  authentication scopes'
section: 'Module 1: Docker and Terraform'
sort_order: 1680
---

The error:

Error: googleapi: Error 403: Access denied., forbidden

│

and

│ Error: Error creating Dataset: googleapi: Error 403: Request had insufficient authentication scopes.

For this solution make sure to run:

echo $GOOGLE_APPLICATION_CREDENTIALS

echo $?

Solution:

You have to set again the GOOGLE_APPLICATION_CREDENTIALS as Alexey did in the environment set-up video in week1:

export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json

