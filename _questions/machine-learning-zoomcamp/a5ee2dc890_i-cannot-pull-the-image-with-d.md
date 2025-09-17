---
course: machine-learning-zoomcamp
id: a5ee2dc890
question: I cannot pull the image with docker pull command
section: 5. Deploying Machine Learning Models
sort_order: 1910
---

Problem: When I am trying to pull the image with the docker pull svizor/zoomcamp-model command I am getting an error:

Using default tag: latest
Error response from daemon: manifest for svizor/zoomcamp-model:latest not found: manifest unknown: manifest unknown

Solution: The docker by default uses the latest tag to avoid this use the correct tag from image description. In our case use command:

docker pull svizor/zoomcamp-model:3.10.12-slim

Added by Vladimir Yesipov

