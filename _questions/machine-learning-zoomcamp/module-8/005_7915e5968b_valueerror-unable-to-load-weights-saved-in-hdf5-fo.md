---
id: 7915e5968b
question: 'ValueError: Unable to load weights saved in HDF5 format into a subclassed Model'
sort_order: 5
---

When loading a saved model, you encounter the error:

```
ValueError: Unable to load weights saved in HDF5 format into a subclassed Model which has not created its variables yet. Call the Model first, then load the weights.
```


Before loading the model, you need to evaluate the model on input data:

```python
model.evaluate(train_ds)
```