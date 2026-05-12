---
id: b14f3a1086
question: 'import tensorflow fails: ''TypeError: Unable to convert function return value to a Python type! The signature was () -> handle'''
sort_order: 31
---

This is a numpy 2.x / older TensorFlow incompatibility. Two fixes:

- Upgrade TensorFlow to a numpy-2-compatible version (2.16+):
  ```bash
  pip install --upgrade tensorflow
  ```
- Or downgrade numpy and restart the kernel:
  ```bash
  pip install "numpy<2"
  ```
