---
id: 57c116dde2
question: Why do I fail to create a cluster with Kind in Module 10 Kubernetes, and
  should I use an older kindest/node image?
sort_order: 28
---

**Problem:** You’re failing to create a Kind cluster as part of Module 10 Kubernetes. The exercise guidance suggests using an older node image.

**Solution:** Explicitly specify a compatible node image when creating the cluster.

```bash
kind create cluster --image kindest/node:v1.32.0
```

This approach aligns with the exercise guidance to use a specific older image. If you continue to have issues, verify Docker is running and that you have network access. If problems persist, try using a different node image version that matches the chapter’s expected environment and consult the module notes for any version recommendations.
