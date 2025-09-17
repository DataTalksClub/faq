---
course: machine-learning-zoomcamp
id: eba3d936f6
question: '"Unable to import module ''lambda_function'': No module named ''tensorflow''"
  when run python test.py'
section: 9. Serverless Deep Learning
sort_order: 3340
---

Make sure all codes in test.py dont have any dependencies with tensorflow library. One of most common reason that lead the this error is tflite still imported from tensorflow. Change import tensorflow.lite as tflite to import tflite_runtime.interpreter as tflite

Added by Ryan Pramana

