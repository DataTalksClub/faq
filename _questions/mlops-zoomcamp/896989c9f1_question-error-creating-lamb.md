---
id: 896989c9f1
question: Question: Error: creating Lambda Function (...): InvalidParameterValueException: The image manifest, config or layer media type for the source image ... is not supported.
section: Certificates:
course: mlops-zoomcamp
sort_order: 2460
---

Answer: This error occurs when the Docker image you are using is a manifest list (multi-platform). AWS Lambda does not support manifest lists—it only accepts single-platform images with a standard image manifest.

Quick fix: Build your Docker image using docker buildx and specify the platform explicitly.

$ docker buildx build --platform linux/amd64 -t your-ecr-image:latest -f Dockerfile .

This ensures the image is compatible with AWS Lambda. Also make sure that you push your image using the –platform option

Added by

José Luis Martínez

