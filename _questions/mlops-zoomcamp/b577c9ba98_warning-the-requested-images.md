---
course: mlops-zoomcamp
id: b577c9ba98
question: 'WARNING: The requested image''s platform (linux/amd64) does not match the
  detected host platform (linux/arm64/v8) and no specific platform was requested'
section: 'Module 4: Deployment'
sort_order: 1780
---

To resolve this make sure to build the docker image with the platform tag, like this:
“docker build -t homework:v1 --platform=linux/arm64 .”

