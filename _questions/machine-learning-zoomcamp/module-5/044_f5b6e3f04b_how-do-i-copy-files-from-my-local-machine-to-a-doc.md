---
id: f5b6e3f04b
question: How do I copy files from my local machine to a docker container?
sort_order: 44
---

You can copy files from your local machine into a Docker container using the `docker cp` command. Here's how to do it:

To copy a file or directory from your local machine into a running Docker container, use the following syntax:

```bash
docker cp /path/to/local/file_or_directory container_id:/path/in/container
```
