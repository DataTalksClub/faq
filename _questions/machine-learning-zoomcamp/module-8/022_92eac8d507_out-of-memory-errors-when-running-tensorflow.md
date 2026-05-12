---
id: 92eac8d507
question: Out of memory errors when running tensorflow
sort_order: 22
---

I found this code snippet fixed my OOM errors, as I have an Nvidia GPU. Can't speak to OOM errors on CPU, though.

[Official Documentation](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)

```python
physical_devices = tf.config.list_physical_devices('GPU')

try:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
    # Invalid device or cannot modify virtual devices once initialized.
    pass
```