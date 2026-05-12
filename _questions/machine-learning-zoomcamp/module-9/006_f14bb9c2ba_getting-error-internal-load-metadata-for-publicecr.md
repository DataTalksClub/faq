---
id: f14bb9c2ba
question: Getting ERROR [internal] load metadata for public.ecr.aws/lambda/python:3.8
sort_order: 6
---

This error is produced sometimes when building your Docker image from the Amazon Python base image.

The following could solve the problem:

- **Update Docker Desktop**: Ensure you have the latest version installed.
- **Restart Docker and Terminal**: Try restarting Docker Desktop and your terminal application, then build the image again.
- **Disable BuildKit**: If the above steps do not work, run the following command to disable Docker BuildKit and build your image:
  
  ```bash
  DOCKER_BUILDKIT=0 docker build .
  ```