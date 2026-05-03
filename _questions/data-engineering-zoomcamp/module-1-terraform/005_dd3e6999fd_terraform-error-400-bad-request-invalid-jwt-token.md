---
id: dd3e6999fd
question: 'Terraform: Error 400 Bad Request. Invalid JWT Token on WSL.'
sort_order: 5
---

When running:

```bash
terraform apply
```

on WSL2, you might encounter the following error:

```
Error: Post "https://storage.googleapis.com/storage/v1/b?alt=json&prettyPrint=false&project=<your-project-id>": oauth2: cannot fetch token: 400 Bad Request

Response: {"error":"invalid_grant","error_description":"Invalid JWT: Token must be a short-lived token (60 minutes) and in a reasonable timeframe. Check your iat and exp values in the JWT claim."}
```

This issue occurs due to potential time desynchronization on your machine, affecting JWT computation.

To fix this, run the following command to synchronize your system time:

```bash
sudo hwclock -s
```
