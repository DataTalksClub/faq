---
id: 13c4d27a91
question: How can I run UV in Kestra without installing it on every flow execution?
sort_order: 10
---

To avoid reinstalling `uv` on each flow run, you can create a custom Docker image based on the official Kestra image with `uv` pre-installed. Here's how:

1. **Create a Dockerfile (e.g., Dockerfile) with the following content:**

   ```dockerfile
   # Use the official Kestra image as a base
   FROM kestra/kestra
   
   # Install uv
   RUN pip install uv
   ```

2. **Update your `docker-compose.yml` to build this custom image instead of pulling the default one:**

   ```yaml
   services:
     kestra:
       build:
         context: .
         dockerfile: Dockerfile
       image: custom-kestra
   ```

This approach ensures that `uv` is available in the container at runtime without requiring installation during each flow execution.