---
id: 3a0a22fda9
question: Error validating 'deployment.yaml' when running kubectl apply
sort_order: 28
---

```markdown
Cause:
- This error typically occurs when you do not have a local Kubernetes cluster running.

Solution:
1) Create a local cluster using kind:
   ```bash
   kind create cluster --name mlzoomcamp
   ```
2) Verify it is running:
   ```bash
   kubectl cluster-info
   kubectl get nodes
   ```
3) Re-run your deployment:
   ```bash
   kubectl apply -f deployment.yaml
   ```

Notes:
- If you still encounter validation errors after the cluster is up, ensure your Kubernetes context is pointing to the correct cluster and that the YAML is valid for the API version you’re targeting.
- The --validate=false option can bypass client-side schema validation, but should be used with caution and not as a first option.
```