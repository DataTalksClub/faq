---
id: 52fbe7351e
question: Where does the number of input features to the first Linear layer after
  a CNN/Flatten come from, and how can I determine it reliably?
sort_order: 26
---

The number of features input to the first Linear layer (the in_features for the Linear) is the size of the tensor after the CNN/pooling layers and after Flatten. In practice, there are several reliable ways to determine this without manually deriving the dimensions for every layer.

### 1) Use a model summary utility (recommended)
- torchinfo (formerly torch-summary) can show the output shape of each layer, ending with the Flatten, so you can read off the number of features.

```python
# Install and import
!pip install torchinfo
from torchinfo import summary

input_size = (1, 3, 150, 150)  # batch size, channels, height, width
model = CNN()
summary(model, input_size=input_size)
```

Output will include an entry for the Flatten layer with its output size, e.g. `(1, 10000)` which indicates `in_features` should be 10000 for the next Linear layer.

> Note: If you prefer the older torchsummary, you can use it similarly, but be mindful of the batch dimension when supplying `input_size`.
```
from torchsummary import summary
summary(model, input_size=(3, 150, 150))
```

### 2) Forward a dummy input through the CNN up to Flatten
Create a model that runs the CNN portion and returns the flattened features, then inspect the feature dimension.

```python
model = CNN()  # as defined in your example
# Create a dummy input matching the CNN's expected input
dummy_input = torch.randn(1, 3, 150, 150)
# Forward through the CNN (including Flatten)
out = model(dummy_input)
# in_features for the first Linear layer
in_features_calc = out.size(1)
print(in_features_calc)  # e.g., 10000
```

This yields the exact value you should use for `nn.Linear(in_features_calc, ...)`.

### 3) Use a LazyLinear layer for automatic in_features inference
If you want to avoid computing the exact dimension, you can use a lazy linear layer for the first fully connected layer:

```python
import torch.nn as nn
class CNNWithLazy(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=(2, 2), stride=2, padding=2)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d((3, 3))
        self.flatten_dim = None  # will be inferred by LazyLinear
        self.fc = nn.LazyLinear(out_features=10)  # plans to learn 10 classes, features inferred
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x
```

> The `nn.LazyLinear` will infer the required `in_features` from the input tensor size during the first forward pass.

### 4) Reason about shapes with a concrete example
Consider a CNN where:
- Input: 3 channels, 150x150 image
- After Conv2d(in_channels=3, out_channels=16, kernel_size=(2,2), stride=2, padding=2): output shape depends on padding/stride
- After ReLU and MaxPool2d((3,3)): final feature map size could be e.g. [N, 16, 25, 25]
- Flatten yields 16 * 25 * 25 = 10000 features

```python
# Example confirmation
# Suppose after the CNN layers you get a flattened vector of length 10000
num_features = 10000
self.fc = nn.Linear(num_features, num_classes)
```

In this scenario, the next linear layer should be defined with `in_features = 10000`.

### Practical example with your CNN from the prompt
Given:
- Final pooled feature map size: [N, 16, 25, 25]
- Flatten to [N, 16*25*25] = [N, 10000]

Therefore, the first linear layer should be defined as:
```python
self.fc1 = nn.Linear(10000, num_classes)
```

Note: If your input size or layer parameters differ, recompute the Flatten output accordingly using any of the methods above. The key concept is: in_features equals the total number of elements in the flattened feature tensor per sample (i.e., batch-independent dimension).

### Summary
- The direct geometric/product approach is accurate but can be error-prone for complex architectures.
- Use `torchinfo.summary` or a forward pass with a dummy input to read off or compute the flattened feature size.
- Alternatively, use `nn.LazyLinear` to infer `in_features` automatically.
- Always ensure your chosen `in_features` matches the actual tensor size just before the first `nn.Linear` to avoid shape mismatches.
