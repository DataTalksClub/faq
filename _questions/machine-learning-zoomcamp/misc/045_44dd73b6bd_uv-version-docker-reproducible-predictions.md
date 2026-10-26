---
id: 44dd73b6bd
question: Why can the local environment and Docker container produce the same prediction
  even when they use different versions of uv?
sort_order: 45
---

Different `uv` versions don’t automatically change your model predictions.

The key idea is that prediction reproducibility depends on what actually gets installed and used at inference time, not on which `uv` version performed the install. As long as both environments:

- use the same locked Python dependencies (e.g., the same `uv.lock`),
- use the expected Python runtime,
- use the same model artifact,
- use the same preprocessing/configuration,

…then local inference and the Docker container inference should match.

In the deployment homework, you can verify this by comparing:

- the prediction from the local API, and
- the prediction from the Docker container,

and confirming both are running with the intended locked dependencies and the same frozen model artifact.