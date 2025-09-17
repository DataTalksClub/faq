---
id: 2ab8be1a97
question: Missing channel value error while reloading model:
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2850
---

While doing:

import tensorflow as tf

from tensorflow import keras

model = tf.keras.models.load_model('model_saved.h5')

If you get an error message like this:

ValueError: The channel dimension of the inputs should be defined. The input_shape received is (None, None, None, None), where axis -1 (0-based) is the channel dimension, which found to be `None`.

Solution:

Saving a model (either yourself via model.save() or via checkpoint when save_weights_only = False) saves two things: The trained model weights (for example the best weights found during training) and the model architecture.  If the number of channels is not explicitly specified in the Input layer of the model, and is instead defined as a variable, the model architecture will not have the value in the variable stored. Therefore when the model is reloaded, it will complain about not knowing the number of channels. See the code below, in the first line, you need to specify number of channels explicitly:

# model architecture:

inputs = keras.Input(shape=(input_size, input_size, 3))

base = base_model(inputs, training=False)

vectors = keras.layers.GlobalAveragePooling2D()(base)

inner = keras.layers.Dense(size_inner, activation='relu')(vectors)

drop = keras.layers.Dropout(droprate)(inner)

outputs = keras.layers.Dense(10)(drop)

model = keras.Model(inputs, outputs)

(Memoona Tahira)

