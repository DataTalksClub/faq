---
id: c1095e75a3
question: 'Module 10 / Apple Silicon: tensorflow/serving:2.7.0 exits with ''Illegal instruction'''
sort_order: 33
---

The official `tensorflow/serving` image isn't built for arm64. Two options:

1. Update Docker Desktop to ≥ 4.35 and enable **Docker VMM (Beta)** which uses Rosetta to emulate amd64 — the official image then runs.
2. Use the `bitnami/tensorflow-serving:2` image. Slightly different config: model files go under `/bitnami/model-data/1/`, and the env var becomes `TENSORFLOW_SERVING_MODEL_NAME` instead of `MODEL_NAME`.
