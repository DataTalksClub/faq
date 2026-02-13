---
id: eaede83d1c
question: How do I check which version of Keras is being used?
sort_order: 1
---

```python
import keras
print(keras.__version__)
```
If you are using TensorFlow's built-in Keras, you can also check with:
```python
import tensorflow as tf
print(tf.keras.__version__)
```
Note: Starting from TensorFlow 2.16, Keras 3 is the default. If you need Keras 2, install `tf-keras` package instead.