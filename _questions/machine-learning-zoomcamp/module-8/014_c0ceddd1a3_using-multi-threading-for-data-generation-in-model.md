---
id: c0ceddd1a3
question: Using multi-threading for data generation in “model.fit()”
sort_order: 14
---

When running `model.fit(...)`, an additional parameter `workers` can be specified for speeding up data loading and generation. The default value is `1`. Try different values between `1` and the CPU count on your system to check which performs best.

For more information, refer to the [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit).