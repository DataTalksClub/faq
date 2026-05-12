---
id: 2d0e38492f
question: model.save_weights(...) fails with newer Keras
sort_order: 29
---

Keras 3 requires the filename to end with `.weights.h5` if you only want weights, and dropped the `save_format` argument:

```python
model.save_weights('model_v1.weights.h5')
```

For the `ModelCheckpoint` callback, set `save_weights_only=True` and use the `.weights.h5` suffix:

```python
checkpoint = keras.callbacks.ModelCheckpoint(
    'xception_v1_{epoch:02d}_{val_accuracy:.3f}.weights.h5',
    save_weights_only=True,
    save_best_only=True,
    monitor='val_accuracy',
    mode='max',
)
```

If you want the whole model (architecture + weights), use the new format: `model.save('model.keras')`.
