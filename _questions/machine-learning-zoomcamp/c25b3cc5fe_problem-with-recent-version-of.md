---
course: machine-learning-zoomcamp
id: c25b3cc5fe
question: Problem with recent version of protobuf
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3440
---

In session 10.3, when creating the virtual environment with pipenv and trying to run the script gateway.py, you might get this error:

TypeError: Descriptors cannot not be created directly.

If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.

If you cannot immediately regenerate your protos, some other possible workarounds are:

1. Downgrade the protobuf package to 3.20.x or lower.

2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates

This will happen if your version of protobuf is one of the newer ones. As a workaround, you can fix the protobuf version to an older one. In my case I got around the issue by creating the environment with:

pipenv install --python 3.9.13 requests grpcio==1.42.0 flask gunicorn \

keras-image-helper tensorflow-protobuf==2.7.0 protobuf==3.19.6

Added by Ángel de Vicente

