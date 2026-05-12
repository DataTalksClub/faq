---
id: 8b5cf23fcf
question: 'Error: Could not find a version that satisfies the requirement tflite_runtime
  (from versions: none)'
sort_order: 18
---

When trying to install `tflite_runtime` using the command below, you receive an error message:

```bash
!pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
```


`tflite_runtime` is only available for specific OS-Python version combinations. You can find the available combinations here: [https://google-coral.github.io/py-repo/tflite-runtime/](https://google-coral.github.io/py-repo/tflite-runtime/). Your environment combination might be missing.

To proceed, follow these steps:

1. Check if any of the available versions work for you at [https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite](https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite).

2. Install the needed version using pip. For example:

   ```bash
   pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl
   ```

3. Reference how it's done in the lecture code [here](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/09-serverless/code/Dockerfile#L4).

Alternatively, you can:

- Use a virtual machine (e.g., VM VirtualBox) with a Linux system.
- Run the code on a virtual machine within a cloud service such as Vertex AI Workbench on GCP, which provides notebooks and terminals for tasks execution.