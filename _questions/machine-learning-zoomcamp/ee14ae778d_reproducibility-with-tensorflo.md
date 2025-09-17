---
id: ee14ae778d
question: Reproducibility with TensorFlow using a seed point
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2920
---

Reproducibility for training runs can be achieved following these instructions:

seed = 1234

tf.keras.utils.set_random_seed(seed)

tf.config.experimental.enable_op_determinism()

This will work for a script, if this gets executed multiple times.

Added by Sylvia Schmitt

