---
id: b0300fc9b8
question: Why do I get a ValueError: Invalid endpoint error when using Boto3 with Docker Compose services?
section: Module 6: Best practices
course: mlops-zoomcamp
sort_order: 2390
---

Answer: Boto3 does not support underscores (_) in service URLs. Naming your Docker Compose services with underscores will cause Boto3 to throw an error when connecting to the endpoint. (Source: )

# Incorrect Docker Compose configuration with underscores

version: '3.8'

services:

backend_service:

image: my_backend_image

...

s3_service:

image: localstack/localstack

…

Rename your services to avoid using underscores. s3_service → s3service

That way, when you run client = boto3.client('s3', endpoint_url="http://s3service:4566") you won’t get any error.

Added by Fustincho

Problem: Pre-commit fails with error RuntimeError: The Poetry configuration is invalid:

- data.extras.pipfile_deprecated_finder[2] must match pattern ^[a-zA-Z-_.0-9]+$

Solution: This is caused by version mixmatch between the pre-commit-config.yaml designated version for your package and the actual versions. Check the versions in Pipfile.lock and update as appropriate.

Added by Oluwadara Adedeji

