---
id: ee14ae778d
question: Reproducibility with TensorFlow using a seed point
sort_order: 15
---

Reproducibility for training runs can be achieved by following these instructions: [TensorFlow Documentation](https://www.tensorflow.org/versions/r2.8/api_docs/python/tf/config/experimental/enable_op_determinism)

```python
seed = 1234

tf.keras.utils.set_random_seed(seed)

tf.config.experimental.enable_op_determinism()
```

This ensures consistent results when the script is executed multiple times.