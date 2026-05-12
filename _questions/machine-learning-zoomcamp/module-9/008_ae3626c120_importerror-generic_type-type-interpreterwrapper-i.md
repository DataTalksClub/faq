---
id: ae3626c120
question: 'ImportError: generic_type: type "InterpreterWrapper" is already registered!'
sort_order: 8
---

When importing `tflite_runtime.interpreter` using:

```python
import tflite_runtime.interpreter as tflite
```

You might encounter the error:

```
ImportError: generic_type: type "InterpreterWrapper" is already registered!
```

This error occurs if you import both `tensorflow` and `tflite_runtime.interpreter` in the same environment. To resolve it:

1. Restart the kernel.
2. Import only `tflite_runtime.interpreter`:
   
   ```python
   import tflite_runtime.interpreter as tflite
   ```