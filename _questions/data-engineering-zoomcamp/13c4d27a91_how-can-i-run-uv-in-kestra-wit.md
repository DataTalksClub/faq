---
course: data-engineering-zoomcamp
id: 13c4d27a91
question: How can I run UV in Kestra without installing it on every flow execution?
section: Project
sort_order: 4310
---

To avoid reinstalling uv on each flow run, you can create a custom Docker image based on the official Kestra image with uv pre-installed. Here's how:

Create a Dockerfile (e.g., Dockerfile) with the following content:

Update your docker-compose.yml to build this custom image instead of pulling the default one:

This approach ensures that uv is available in the container at runtime without requiring installation during each flow execution.

