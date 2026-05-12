---
id: ac877b2d3d
question: Mlflow CLI does not return experiments
sort_order: 31
---

CLI commands (`mlflow experiments list`) do not return experiments.

You need to set the environment variable for the Tracking URI:

```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```