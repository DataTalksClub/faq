---
id: 1dad6c9bfa
question: Why does my Kubernetes deployment work locally with kind but fail on GitHub
  Actions with “could not locate any control plane nodes for cluster named 'agent-relay'”?
sort_order: 4
---

This usually happens because a GitHub-hosted runner starts from a clean environment and won’t have your local `kind` cluster already created. When your workflow tries to deploy to the `agent-relay` cluster, Kubernetes can’t find the control plane.

A fix is to ensure the `kind` cluster exists before you load Docker images or apply manifests. For example:

```bash
if ! kind get clusters | grep -qx "agent-relay"; then
    kind create cluster --name agent-relay
fi
```

Then continue with the usual steps:
1. Load your Docker image into `kind`.
2. Apply your Kubernetes manifests.
3. Wait for the deployment rollout.
4. Verify the deployed API.

This won’t necessarily show up locally when testing with `act`, because your machine may already have a `kind` cluster named `agent-relay` from a previous run.