---
id: 59afc541fd
question: Module 10 pipenv install grpcio==1.42.0 ... tensorflow-protobuf==2.7.0 fails to lock
sort_order: 34
---

The pinned versions in the lecture are old and don't resolve on Python 3.11+. Either:

- Use Python 3.8 inside Docker only (your host can be 3.11) and keep the original pins.
- Or use newer pins that resolve on 3.11+ Linux:
  ```toml
  python_version = "3.12"
  grpcio = "==1.68.1"
  flask = "==3.1.0"
  gunicorn = "*"
  keras-image-helper = "*"
  tensorflow-protobuf = "==2.11.0"
  ```

On macOS Apple Silicon the lock often hangs forever — switch to Linux (Codespaces / EC2) or skip locking locally and only build inside Docker.
