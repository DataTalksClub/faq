---
id: ddc7d09c3d
question: Sequential vs. Functional Model Modes in Keras (TF2)
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2980
---

It’s quite useful to understand that all types of models in the course are a plain stack of layers where each layer has exactly one input tensor and one output tensor ( model TF page,  class).

You can simply start from an “empty” model and add more and more layers in a sequential order.

This mode is called “Sequential Model API”  (easier)

In Alexey’s videos it is implemented as chained calls of different entities (“inputs”,“base”, “vectors”,  “outputs”) in a more advanced mode “Functional Model API”.

Maybe a more complicated way makes sense when you do Transfer Learning and want to separate “Base” model vs. rest, but in the HW you need to recreate the full model from scratch ⇒ I believe it is easier to work with a sequence of “similar” layers.

You can read more about it in this TF2 .

A really useful Sequential model example is shared in the Kaggle’s “Bee or Wasp” dataset folder with code:

Added by Ivan Brigida

Fresh Run on Neural Nets

While correcting an error on neural net architecture, it is advised to do fresh run by restarting kernel, else the model learns on top of previous runs.

Added by Abhijit Chakraborty

