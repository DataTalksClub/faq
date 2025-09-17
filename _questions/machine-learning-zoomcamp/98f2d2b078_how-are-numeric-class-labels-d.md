---
course: machine-learning-zoomcamp
id: 98f2d2b078
question: 'How are numeric class labels determined in flow_from_directroy using binary
  class mode and what is meant by the single probability predicted by a binary Keras
  model:'
section: 8. Neural Networks and Deep Learning
sort_order: 2890
---

The command to read folders in the dataset in the tensorflow source code is:

for subdir in sorted(os.listdir(directory)):

…

Reference: , line 563

This means folders will be read in alphabetical order. For example, in the case of a folder named dino, and another named dragon, dino will read first and will have class label 0, whereas dragon will be read in next and will have class label 1.

When a Keras model predicts binary labels, it will only return one value, and this is the probability of class 1 in case of sigmoid activation function in the last dense layer with 2 neurons. The probability of class 0 can be found out by:

prob(class(0)) = 1- prob(class(1))

In case of using from_logits to get results, you will get two values for each of the labels.

A prediction of 0.8 is saying the probability that the image has class label 1 (in this case dragon), is 0.8, and conversely we can infer the probability that the image has class label 0 is 0.2.

(Added by Memoona Tahira)

