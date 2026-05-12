---
id: 82cf92503d
question: 'HW9 Docker: ''A module that was compiled using NumPy 1.x cannot be run in NumPy 2.2.0'' loading tflite_runtime'
sort_order: 38
---

The wheel `tflite_runtime-2.14.0` was compiled against numpy<2, but installing it pulls in numpy 2.x by default. Pin numpy first, then install with `--no-deps`:

```dockerfile
RUN pip install numpy==1.23.1
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

Order matters — pin numpy first, then install the wheel without dependencies. See also https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/09-serverless/updates.md
