---
id: 52fbe7351e
question: Q: Where does the number of Conv2d layer’s params come from? Where does the number of “features” we get after the Flatten layer come from?
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2970
---

Let’s say we define our Conv2d layer like this:

>> tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3))

It means our input image is RGB (3 channels, 150 by 150 pixels), kernel is 3x3 and number of filters (layer’s width) is 32.

If we check model.summary() we will get this:

_________________________________________________________________

Layer (type)                Output Shape              Param #

=================================================================

conv2d (Conv2D)             (None, 148, 148, 32)      896

So where does 896 params come from? It’s computed like this:

>>> (3*3*3 +1) * 32

896

# 3x3 kernel, 3 channels RGB, +1 for bias, 32 filters

What about the number of “features” we get after the Flatten layer?

For our homework model.summary() for last MaxPooling2d and Flatten layers looked like this:

_________________________________________________________________

Layer (type)                Output Shape              Param #

=================================================================

max_pooling2d_3       (None, 7, 7, 128)         0

flatten (Flatten)           (None, 6272)              0

So where do 6272 vectors come from? It’s computed like this:

>>> 7*7*128

6272

# 7x7 “image shape” after several convolutions and poolings, 128 filters

Added by Andrii Larkin

