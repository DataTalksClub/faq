---
id: 55c0047f8b
question: 'Terraform - Error 403 : Access denied'
sort_order: 1660
---

│ Error: googleapi: Error 403: Access denied., forbidden

Your $GOOGLE_APPLICATION_CREDENTIALS might not be pointing to the correct file run = export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/YOUR_JSON.json

And then = gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

