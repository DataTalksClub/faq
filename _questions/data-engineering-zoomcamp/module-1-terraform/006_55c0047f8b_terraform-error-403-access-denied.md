---
id: 55c0047f8b
question: 'Terraform - Error 403 : Access denied'
sort_order: 6
---

```
│ Error: googleapi: Error 403: Access denied., forbidden
```

Your `$GOOGLE_APPLICATION_CREDENTIALS` might not be pointing to the correct file. Try the following steps:

1. Set the correct path for your credentials:
   
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/YOUR_JSON.json
   ```

2. Activate the service account:
   
   ```bash
   gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
   ```