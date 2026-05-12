---
id: fd3a06c6ee
question: 'Kind: cannot load docker image'
sort_order: 18
---

**Problem:** Failing to load docker-image to cluster (when you've named a cluster)

```bash
kind load docker-image zoomcamp-10-model:xception-v4-001

ERROR: no nodes found for cluster "kind"
```

**Solution:** Specify the cluster name with `-n`

```bash
kind -n clothing-model load docker-image zoomcamp-10-model:xception-v4-001
```