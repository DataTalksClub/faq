---
id: 7b7188f8f7
question: 'HW9 PyTorch/ONNX: model expects (1, 3, 200, 200) but my preprocessing gives (1, 200, 200, 3)'
sort_order: 39
---

TensorFlow uses NHWC (channels-last); PyTorch/ONNX use NCHW (channels-first). Reorder the channel axis with `np.transpose` BEFORE adding the batch dim:

```python
x = np.transpose(x, (2, 0, 1))    # (200, 200, 3) -> (3, 200, 200)
x = np.expand_dims(x, axis=0)     # -> (1, 3, 200, 200)
```

`np.swapaxes` only swaps two axes; `transpose` lets you specify the full new ordering, which is what you need for NHWC → NCHW.
