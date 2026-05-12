---
id: 69c624cc4e
question: 'Keras model *.h5 doesn’t load. Error: weight_decay is not a valid argument,
  kwargs should be empty for `optimizer_experimental.Optimizer`'
sort_order: 27
---

Solution: Add `compile=False` to the `load_model` function.

```python
keras.models.load_model('model_name.h5', compile=False)
```