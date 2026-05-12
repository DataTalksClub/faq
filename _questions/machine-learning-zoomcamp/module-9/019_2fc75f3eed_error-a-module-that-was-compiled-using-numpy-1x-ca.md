---
id: 2fc75f3eed
question: 'Error: A module that was compiled using NumPy 1.x cannot be run in NumPy
  2.2.0 as it may crash'
sort_order: 19
---

After installing the tflite runtime using the wheel suggested in Homework 9, I encountered a runtime error while testing the lambda handler. The error was:

```
ImportError:

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.2.0 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some modules may need to be rebuilt instead, e.g., with 'pybind11>=2.12'.
```

The issue with the version of NumPy was due to it being overwritten by the installation of tflite-runtime. To prevent this, you should install the wheel using the `--no-deps` option.

```bash
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```