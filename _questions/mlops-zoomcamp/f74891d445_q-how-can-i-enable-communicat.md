---
id: f74891d445
question: Q: How can I enable communication between Docker containers when invoked from a Kestra task?
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1520
---

![Image](images/mlops-zoomcamp/image_09b2050c.png)

A: Use the docker.Run plugin in your Kestra task to run containers. This plugin supports advanced Docker options like custom networks.

For local development, you can use networkMode: host to allow containers to access services on your host (e.g., MLflow running on localhost).

Example:

networkMode: host

⚠️ Note: host mode is only supported on Linux. For Docker Desktop on Windows/macOS, use host.docker.internal or create a shared Docker network.

Best practice:

In production setups, tools like MLflow should run outside Kestra and be accessed over a stable URI (e.g., a cloud endpoint or a container with a known hostname in a shared network).

Added by José Luis Martínez

