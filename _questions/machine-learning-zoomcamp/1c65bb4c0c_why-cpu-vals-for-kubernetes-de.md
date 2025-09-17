---
id: 1c65bb4c0c
question: Why cpu vals for Kubernetes deployment.yaml look like “100m” and “500m”? What does "m" mean?
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3560
---

In Kubernetes resource specifications, such as CPU requests and limits, the "m" stands for milliCPU, which is a unit of computing power. It represents one thousandth of a CPU core.

cpu: "100m" means the container is requesting 100 milliCPUs, which is equivalent to 0.1 CPU core.

cpu: "500m" means the container has a CPU limit of 500 milliCPUs, which is equivalent to 0.5 CPU core.

These values are specified in milliCPUs to allow fine-grained control over CPU resources. It allows you to express CPU requirements and limits in a more granular way, especially in scenarios where your application might not need a full CPU core.

Added by Andrii Larkin

