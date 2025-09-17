---
id: 3e621509d2
question: Pickle error: can’t get attribute XXX on module __main__
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 3890
---

When running a docker container with waitress serving the app.py for making predictions, pickle will throw an error that can't get attribute <name_of_class> on module __main__.

This does not happen when Flask is used directly, i.e. not through waitress.

The problem is that the model uses a custom column transformer class, and when the model was saved, it was saved from the __main__ module (e.g. python train.py). Pickle will reference the class in the global namespace (top-level code): __main__.<custom_class>.

When using waitress, waitress will load the predict_app module and this will call pickle.load, that will try to find __main__.<custom_class> that does not exist.

Solution:

Put the class into a separate module and import it in both the script that saves the model (e.g. train.py) and the script that loads the model (e.g. predict.py)

Note: If Flask is used (no waitress) in predict.py, and predict.py has the definition of the class, When  it is run: python predict.py, it will work because the class is in the same namespace as the one used when the model was saved (__main__).

Detailed info:

Marcos MJD

