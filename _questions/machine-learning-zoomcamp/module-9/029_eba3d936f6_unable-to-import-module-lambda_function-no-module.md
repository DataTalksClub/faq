---
id: eba3d936f6
question: '"Unable to import module ''lambda_function'': No module named ''tensorflow''"
  when running `python test.py`'
sort_order: 29
---

Ensure that all the code in `test.py` does not have any dependencies on the TensorFlow library. A common cause of this error is that `tflite` is still imported from TensorFlow. Change the import statement:

```python
import tensorflow.lite as tflite
```

To:

```python
import tflite_runtime.interpreter as tflite
```