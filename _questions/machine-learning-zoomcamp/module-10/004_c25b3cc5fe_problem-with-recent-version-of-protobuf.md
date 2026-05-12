---
id: c25b3cc5fe
question: Problem with recent version of protobuf
sort_order: 4
---

In session 10.3, when creating the virtual environment with pipenv and trying to run the script `gateway.py`, you might encounter the following error:

```plaintext
TypeError: Descriptors cannot not be created directly.

If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
```

If you cannot immediately regenerate your protos, consider these workarounds:

1. **Downgrade the protobuf package** to 3.20.x or lower.
2. **Set the environment variable**:
   
   ```bash
   PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
   ```
   
   This will use pure-Python parsing but may be slower.

For more information, visit [developers.google.com](https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates).

This issue occurs with newer versions of protobuf. As a workaround, you can fix the protobuf version to an older one. Here's a command that addresses this issue:

```bash
pipenv install --python 3.9.13 requests grpcio==1.42.0 flask gunicorn \
keras-image-helper tensorflow-protobuf==2.7.0 protobuf==3.19.6
```
