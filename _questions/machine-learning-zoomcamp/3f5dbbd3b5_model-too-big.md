---
id: 3f5dbbd3b5
question: Model too big
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 3940
---

If your model is too big for github one option is to try and compress the model using joblib. For example joblib.dump(model, model_filename, compress=('zlib', 6) will use zlib to compress the model. Just note this could take a few moments as the model is being compressed.

Quinn Avila

