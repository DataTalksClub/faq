---
id: 2fc75f3eed
question: Error: A module that was compiled using NumPy 1.x cannot be run in NumPy 2.2.0 as it may crash
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3240
---

After installing tflite runtime by using the wheel suggested in the homework 9 (), I was getting a runtime error while testing the lambda handler. The error was:

“..ImportError:

A module that was compiled using NumPy 1.x cannot be run in

NumPy 2.2.0 as it may crash. To support both 1.x and 2.x

versions of NumPy, modules must be compiled with NumPy 2.0.

Some module may need to rebuild instead e.g. with 'pybind11>=2.12' ..”

The issue I was experiencing with the version of NumPy was due to it being overwritten by the installation of tflite-runtime. To prevent this from happening, you should install the wheel using the --no-deps option

RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

(added by Karina)

