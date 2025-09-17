---
course: mlops-zoomcamp
id: e6ffad6be5
question: The arm64 chip doesn’t match with Alexey’s docker image
section: 'Module 4: Deployment'
sort_order: 1840
---

You may get a warning similar to the one below when trying to run the docker

WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

Python 3.10.13 (main, Mar 12 2024, 12:22:40) [GCC 12.2.0] on linux

Add the tag --platform linux/amd64 when running and it should work. For example

docker run -it --platform linux/amd64 --rm -p 9696:9696 homework:v2

