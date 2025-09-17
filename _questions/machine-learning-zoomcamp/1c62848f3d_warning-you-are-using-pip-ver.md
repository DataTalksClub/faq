---
id: 1c62848f3d
question: WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3140
---

When running docker build -t dino-dragon-model it returns the above error

The most common source of this error in this week is because Alex video shows a version of the wheel with python 8, we need to find a wheel with the version that we are working on. In this case python 9. Another common error is to copy the link, this will also produce the same error, we need to download the raw format:

https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl

Pastor Soto

