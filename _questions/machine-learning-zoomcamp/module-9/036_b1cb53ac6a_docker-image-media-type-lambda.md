---
id: b1cb53ac6a
question: Why am I getting the 'image manifest, config or layer media type' not supported
  error when creating an AWS Lambda function from a Docker image?
sort_order: 36
---

This error occurs when the Docker image media type pushed to ECR is in the old OCI image index format (application/vnd.oci.image.index.v1+json). AWS Lambda expects the image manifest in the new format (application/vnd.docker.distribution.manifest.v2+json).

How to verify:

```
docker inspect <docker-image-name>
```

Check the output for the media type/manifest format. If it shows an OCI index or an old format, Lambda will report that the image manifest, config or layer media type is not supported.

How to fix (force manifest v2):

```
docker build --platform linux/amd64 --provenance false -t <docker-image-name> .
```

This command targets a manifest v2-compatible image. After rebuilding, push the image to ECR and create the Lambda function again using this docker container image.

Notes:
- Ideally, a standard docker build with a tag (e.g., `docker build -t <tag> .`) should produce a manifest v2 image, but misconfigurations can result in the older format.
- You can repeat the build/push steps to ensure the pushed image uses the correct manifest type.