---
id: 0c9fc7e7d3
question: 'Dataproc: "Insufficient SSD_TOTAL_GB quota" when creating a cluster'
sort_order: 22
---

The default per-region quota for SSD persistent disk is limited (often 250 or 500 GB depending on region/account). If your cluster's combined boot disk size exceeds it, cluster creation fails:

```
Error: Insufficient 'SSD_TOTAL_GB' quota. Requested 500.0, available 250.0.
```

## Options

1. Wait and retry — the message can also indicate transient resource pressure in the region.
2. Reduce the cluster's disk usage so it fits within your quota:
   - Master node: 1 × `n2-standard-2`, primary disk 85 GB.
   - Workers: 2 × `n2-standard-2`, primary disk 80 GB each.
   - Total: 85 + 80 + 80 = 245 GB, fits under a 250 GB quota.
3. Switch boot disk type from `pd-balanced` (SSD-backed) to `pd-standard` (HDD-backed) — this disk type counts against a different quota.
4. Pick a region with more headroom or request a quota increase via the GCP console (IAM & Admin → Quotas).
