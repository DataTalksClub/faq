---
course: machine-learning-zoomcamp
id: 7915e5968b
question: 'Error: (ValueError: Unable to load weights saved in HDF5 format into a
  subclassed Model which has not created its variables yet. Call the Model first,
  then load the weights.) when loading model.'
section: 8. Neural Networks and Deep Learning
sort_order: 2800
---

Problem description:

When loading saved model getting error: ValueError: Unable to load weights saved in HDF5 format into a subclassed Model which has not created its variables yet. Call the Model first, then load the weights.

Solution description:

Before loading model need to evaluate the model on input data: model.evaluate(train_ds)

Added by Vladimir Yesipov

