---
id: dc705a3c4e
question: Tflite_runtime unable to install
sort_order: 36
---

When trying to install `tflite_runtime` in a pipenv environment, the following error message appears:

```bash
ERROR: Could not find a version that satisfies the requirement tflite_runtime (from versions: none)
ERROR: No matching distribution found for tflite_runtime
```


This version of `tflite_runtime` does not run on Python 3.10. To resolve this issue, follow these steps:

1. **Install Python 3.9**: Use Python 3.9 instead of Python 3.10.
2. **Reinstall `tflite_runtime`**: With Python 3.9, the installation should proceed without issues.


- Check all available versions here: [TFLite Runtime Versions](https://google-coral.github.io/py-repo/tflite-runtime/)
- If no suitable version is found, consider the options provided at [GitHub Repository](https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite). You can install it using:

  ```bash
  pip install "https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl"
  ```

- For local development, use the TFLite included in TensorFlow and Docker for testing Lambda.