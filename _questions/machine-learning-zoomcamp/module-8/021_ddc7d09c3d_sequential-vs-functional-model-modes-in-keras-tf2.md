---
id: ddc7d09c3d
question: Sequential vs. Functional Model Modes in Keras (TF2)
sort_order: 21
---

It’s useful to understand that all types of models in the course are a plain stack of layers where each layer has exactly one input tensor and one output tensor. See the [Sequential model TF page](https://www.tensorflow.org/guide/keras/sequential_model) and the [Sequential class](https://keras.io/api/models/sequential/).

You can start with an “empty” model and add more layers in sequential order. This is called the “Sequential Model API,” which is easier to use.

In Alexey’s videos, it’s implemented as chained calls of different entities (“inputs,” “base,” “vectors,” “outputs”) in a more advanced mode, the “Functional Model API.” A more complicated approach makes sense for Transfer Learning, where you want to separate the “Base” model from the rest, but in homework, you're required to recreate the full model from scratch. It might be easier to work with a sequence of similar layers.

For more information, see this TF2 [tutorial](https://machinelearningmastery.com/tensorflow-tutorial-deep-learning-with-tf-keras/).

A useful Sequential model example is available in Kaggle’s “Bee or Wasp” dataset folder: [notebook](https://www.kaggle.com/code/tammygusmao/bee-or-wasp-from-scratch-to-transfer-learning).

