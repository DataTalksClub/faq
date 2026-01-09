---
id: 3b5e939644
question: How can I run MLflow on a remote server and access it from a different domain
  without encountering the 'Invalid Host header' error during development or testing?
sort_order: 20
---

```bash
mlflow server --backend-store-uri sqlite:///example.db --host 0.0.0.0 --port 5000 --cors-allowed-origins '*' --x-frame-options NONE --disable-security-middleware
```