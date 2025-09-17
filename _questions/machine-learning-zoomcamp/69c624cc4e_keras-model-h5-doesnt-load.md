---
id: 69c624cc4e
question: Keras model *.h5 doesn’t load. Error: weight_decay is not a valid argument, kwargs should be empty  for `optimizer_experimental.Optimizer`
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3320
---

Solution: add compile = False to the load_model function

keras.models.load_model('model_name.h5', compile=False)

Nadia Paz

