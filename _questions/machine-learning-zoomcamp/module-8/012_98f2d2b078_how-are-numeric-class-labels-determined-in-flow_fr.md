---
id: 98f2d2b078
question: 'How are numeric class labels determined in flow_from_directory using binary
  class mode and what is meant by the single probability predicted by a binary Keras
  model:'
sort_order: 12
---

The command to read folders in the dataset in the TensorFlow source code is:

```python
for subdir in sorted(os.listdir(directory)):
```

Reference: [Keras Image Preprocessing](https://github.com/keras-team/keras/blob/master/keras/preprocessing/image.py), line 563.

This means folders will be read in alphabetical order. For example, with a folder named `dino` and another named `dragon`, `dino` will be read first and will have class label 0, whereas `dragon` will be read next and will have class label 1.

When a Keras model predicts binary labels, it returns one value, which is the probability of class 1. This occurs with the sigmoid activation function in the last dense layer with 2 neurons. The probability of class 0 can be calculated as:

```
prob(class(0)) = 1 - prob(class(1))
```

In the case of using `from_logits` to get results, you will receive two values for each of the labels.

A prediction of 0.8 indicates that the probability the image has class label 1 (in this case, `dragon`) is 0.8. Conversely, the probability that the image has class label 0 is 0.2.

