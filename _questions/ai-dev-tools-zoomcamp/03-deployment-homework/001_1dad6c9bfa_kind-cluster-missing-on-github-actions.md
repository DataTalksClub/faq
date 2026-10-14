---
id: 1dad6c9bfa
question: Why does my CI deploy work with `act` but fail on GitHub Actions with "could
  not locate any control plane nodes for cluster named 'agent-relay'"?
sort_order: 1
---

HW3 runs this workflow locally with `act`, where it reaches the kind cluster on your machine. A GitHub-hosted runner is a fresh VM with no kind cluster, so `kind load`/`kubectl` fail. The error comes from the `kind` CLI, which can't find a cluster with that name.

If you want the deploy job to run on GitHub too, create the cluster when it's missing, before you load images or apply manifests:

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

Alternatively, skip the deploy steps outside act by adding `if: ${{ env.ACT }}` to them (act sets `ACT=true`; the `env` context is available in step-level `if`, not job-level). A cluster created on a GitHub runner is thrown away when the job ends, so it only proves the manifests apply.
