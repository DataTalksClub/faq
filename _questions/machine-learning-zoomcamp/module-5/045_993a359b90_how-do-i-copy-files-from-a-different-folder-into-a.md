---
id: 993a359b90
question: How do I copy files from a different folder into a Docker container’s working
  directory?
sort_order: 45
---

You can copy files from your local machine into a Docker container using the `docker cp` command.

In the Dockerfile, you can specify the folder containing the files you want to copy. The basic syntax is as follows:

```dockerfile
COPY ["src/predict.py", "models/xgb_model.bin", "./"]
```