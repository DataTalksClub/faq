---
id: b0300fc9b8
question: 'Why do I get a `ValueError: Invalid endpoint` error when using Boto3 with
  Docker Compose services?'
sort_order: 20
---

Boto3 does not support underscores (`_`) in service URLs. Naming your Docker Compose services with underscores will cause Boto3 to throw an error when connecting to the endpoint. (Source: [GitHub Issue](https://github.com/boto/boto3/issues/703))

Incorrect Docker Compose configuration with underscores:

```yaml
version: '3.8'

services:
  backend_service:
    image: my_backend_image
    ...
  s3_service:
    image: localstack/localstack
    ...
```

Rename your services to avoid using underscores. For example, change `s3_service` to `s3service`. Then:

```python
client = boto3.client('s3', endpoint_url="http://s3service:4566")
```

will work.
