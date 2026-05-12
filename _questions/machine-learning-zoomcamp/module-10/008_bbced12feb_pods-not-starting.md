---
id: bbced12feb
question: 'Pods not starting'
sort_order: 8
---

This issue can be caused by several factors:

- **Resource Allocation:** Ensure that your Pods have enough CPU and memory resources allocated. If resources are too low, the Kubernetes scheduler might fail to schedule your Pods.

- **Image Issues:** Verify that the Docker image specified for your Pod is correctly built and accessible. If the image cannot be pulled from the repository, the Pod won’t start.