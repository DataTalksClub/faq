---
id: 31a648c28a
images:
- description: 'image #1'
  id: image_1
  path: images/mlops-zoomcamp/image_3cc4ae4e.png
question: Protobuf error when installing MLflow
sort_order: 21
---

I installed all the libraries from the `requirements.txt` document in a new environment with the following command:

```bash
pip install -r requirements.txt
```

Then, when I run `mlflow` from my terminal like this:

```bash
mlflow
```

I get this error:

<{IMAGE:image_1}>

You need to downgrade the version of the `protobuf` module to 3.20.x or lower. Initially, it was version 4.21. Use the following command to install the compatible version:

```bash
pip install protobuf==3.20
```

After doing this, I was able to run `mlflow` from my terminal.