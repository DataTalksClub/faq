---
id: 5bf804473e
question: Dockerizing lightgbm
section: Module 4: Deployment
course: mlops-zoomcamp
sort_order: 1720
---

Problem description: lib_lightgbm.so Reason: image not found

Solution description: Add “RUN apt-get install libgomp1” to your docker. (change installer command based on OS)

Added by Kazeem Hakeem

