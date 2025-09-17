---
course: data-engineering-zoomcamp
id: 55c0047f8b
question: 'Terraform - Error 403 : Access denied'
section: 'Module 1: Docker and Terraform'
sort_order: 1640
---

│ Error: googleapi: Error 403: Access denied., forbidden

Your $GOOGLE_APPLICATION_CREDENTIALS might not be pointing to the correct file 
run = export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/YOUR_JSON.json

And then = gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

