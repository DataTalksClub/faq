---
id: 2ab8be1a97
question: 'Missing channel value error while reloading model:'
sort_order: 9
---

While attempting to reload a model with TensorFlow, you might encounter the following error:

```
ValueError: The channel dimension of the inputs should be defined. The input_shape received is (None, None, None, None), where axis -1 (0-based) is the channel dimension, which found to be `None`.
```

This error is usually caused when the number of channels is not explicitly defined in the Input layer of the model. 

Ensure that you explicitly specify the number of channels in the Input layer of the model architecture.

Example:

```python
import tensorflow as tf
from tensorflow import keras

# Model architecture:
inputs = keras.Input(shape=(input_size, input_size, 3))

base = base_model(inputs, training=False)
vectors = keras.layers.GlobalAveragePooling2D()(base)
inner = keras.layers.Dense(size_inner, activation='relu')(vectors)
drop = keras.layers.Dropout(droprate)(inner)
outputs = keras.layers.Dense(10)(drop)

model = keras.Model(inputs, outputs)
```

This configuration ensures that the channel dimension is explicitly defined, preventing the reload error.