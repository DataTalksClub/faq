---
id: fd11200ead
question: 'Docker: How to see the model in the docker container in app/?'
sort_order: 25
---

If you need to view the model inside the Docker container for the image `svizor/zoomcamp-model:mlops-3.10.0-slim`, follow these steps:

1. **Create a Dockerfile:**
   
   ```dockerfile
   FROM svizor/zoomcamp-model:mlops-3.10.0-slim
   ```

2. **Build the Docker Image:**

   ```bash
   docker build -t zoomcamp_test .
   ```

3. **Run the Container and List the Contents of `/app`:**

   ```bash
   docker run -it zoomcamp_test ls /app
   ```

   The output should include `model.bin`, confirming the model is present.

**Additional Instructions**

- You can copy files into the Docker image by adding lines like `COPY myfile .` to the Dockerfile, and then run a script with arguments: 

  ```bash
  docker run -it myimage myscript arg1 arg2
  ```

- Remember, a new build is required whenever the Dockerfile is modified.

**Alternative Method**

To list the contents of `/app` when the container runs, modify the Dockerfile:

```dockerfile
FROM svizor/zoomcamp-model:mlops-3.10.0-slim

WORKDIR /app

CMD ls
```

- **Note:**
  - Use `CMD` to specify commands for container runtime. 
  - Use `RUN` for building the image and `CMD` during container execution.