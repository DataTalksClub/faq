---
id: 4a6d04a2c3
question: 'Terraform - Error creating Dataset: googleapi: Error 403: Request had insufficient
  authentication scopes'
sort_order: 10
---

The error:

```
Error: googleapi: Error 403: Access denied., forbidden

Error: Error creating Dataset: googleapi: Error 403: Request had insufficient authentication scopes.
```

Solution:

1. Verify your credentials by running:
   
   ```bash
   echo $GOOGLE_APPLICATION_CREDENTIALS
   echo $?
   ```

2. Ensure you have set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable correctly, as demonstrated in the environment setup video in week 1:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
   ```