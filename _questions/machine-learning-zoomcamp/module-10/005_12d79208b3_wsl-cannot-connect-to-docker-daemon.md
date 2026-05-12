---
id: 12d79208b3
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_41f796fe.png
question: 'WSL: Cannot Connect To Docker Daemon'
sort_order: 5
---

Due to machine uncertainties, you might encounter the following error when trying to run a Docker command:

```bash
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

**Solution:**

The issue may arise if Docker Desktop is not correctly connecting to the WSL Linux distribution. To resolve this:

1. Open Docker Desktop settings.
2. Navigate to the "Resources" section.
3. Click on "WSL Integration."

   <{IMAGE:image_1}>

4. Enable additional distros, even if it matches the default WSL distro.

That's all you need to do.