---
id: 9506089527
question: 'AWS Lambda: ''The image manifest, config or layer media type for the source image is not supported'''
sort_order: 41
---

Newer Docker BuildKit defaults to OCI manifest format, which Lambda doesn't accept. Force the older Docker v2 manifest with `--provenance=false`:

```bash
docker build --platform linux/amd64 --provenance=false -t my-image .
```

Then push to ECR and create the Lambda function. Without `--provenance=false`, BuildKit creates a multi-arch index image that Lambda rejects.
