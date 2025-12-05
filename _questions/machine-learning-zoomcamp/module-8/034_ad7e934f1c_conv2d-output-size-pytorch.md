---
id: ad7e934f1c
question: How many feature maps are produced by a PyTorch Conv2D layer, and how do
  you compute the spatial output size?
sort_order: 34
---

In PyTorch, a `Conv2d` layer outputs a 4D tensor of shape `(N, C_out, H_out, W_out)` where:

- `N` is the batch size
- `C_out` is the number of output channels (out_channels)
- `H_out` and `W_out` are the spatial dimensions after the convolution

The spatial size is computed (for dilation = 1) as:

```
H_out = floor((H_in - K_H + 2*P_H) / S_H) + 1
W_out = floor((W_in - K_W + 2*P_W) / S_W) + 1
```

For the general case (including dilation `D`):

```
H_out = floor((H_in + 2*P_H - D*(K_H - 1) - 1) / S_H + 1)
W_out = floor((W_in + 2*P_W - D*(K_W - 1) - 1) / S_W + 1)
```

If you have dilation = 1 (the common case), this reduces to the simplified formula above.

Example for your parameters (assuming input has 3 channels and batch size 1):

```
import torch
import torch.nn as nn

conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(2,2), stride=(2,2), padding=(2,2))
x = torch.randn(1, 3, 150, 150)
y = conv(x)
print(y.shape)  # torch.Size([1, 16, 77, 77])
```

Notes:
- The number of feature maps equals `out_channels`.
- If you only care about spatial size, apply the height/width formula above; you can also verify with a quick forward pass or by using a library like `torchsummary` to inspect the model.