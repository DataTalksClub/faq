---
id: 29f149ff07
question: 'Error with the line interpreter.set_tensor(input_index, X)'
sort_order: 12
---

I had this error when running the command:

```python
interpreter.set_tensor(input_index, x)
```

You might see this around 12 minutes into video 9.3.

Error message:

```
ValueError: Cannot set tensor: Got value of type UINT8 but expected type FLOAT32 for input 0, name: serving_default_conv2d_input:0
```

This occurs because `X` is an integer, but a float is expected.

To resolve this issue, convert `X` to `float32` before using `set_tensor`:
 
```python
X = np.float32(X)
```

With this conversion, the code works properly. Note that this was tested on TensorFlow 2.15.0, and newer versions may require such changes.