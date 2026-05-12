---
id: ace84c3970
question: 'Keras: Model training fails with “Failed to find data adapter”'
sort_order: 17
---

While training a Keras model, you may encounter the error:

```
Failed to find data adapter that can handle input: <class 'keras.src.preprocessing.image.ImageDataGenerator'>, <class 'NoneType'>
```

This typically occurs if you accidentally pass the image generator instead of the dataset to the model. Here is an example of incorrect usage:

```python
train_gen = ImageDataGenerator(rescale=1./255)

train_ds = train_gen.flow_from_directory(…)

history_after_augmentation = model.fit(
    train_gen,  # this should be train_ds!!!
    epochs=10,
    validation_data=test_gen  # this should be test_ds!!!
)
```


The fix is straightforward. Use the training and validation datasets (`train_ds` and `val_ds`) returned from `flow_from_directory`:

- Ensure you pass `train_ds` instead of `train_gen` when calling `model.fit()`.
- Similarly, use `val_ds` for `validation_data` instead of `test_gen`.