---
id: dd3e6999fd
question: Terraform - Error 400 Bad Request.  Invalid JWT Token  on WSL.
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1630
---

When running

terraform apply

on wsl2 I've got this error:

│ Error: Post "https://storage.googleapis.com/storage/v1/b?alt=json&prettyPrint=false&project=<your-project-id>": oauth2: cannot fetch token: 400 Bad Request

│ Response: {"error":"invalid_grant","error_description":"Invalid JWT: Token must be a short-lived token (60 minutes) and in a reasonable timeframe. Check your iat and exp values in the JWT claim."}

It happens because there may be time desync on your machine which affects computing JWT

To fix this, run the command

sudo hwclock -s

which fixes your system time.

