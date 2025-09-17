---
id: e80cb08772
question: DictVectorizer feature names
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2580
---

The DictVectorizer has a function to get the feature names . This is helpful for example if you need to analyze feature importance but use the dict vectorizer for one hot encoding. Just keep in mind it does return a numpy array so you may need to convert this to a list depending on your usage for example dv.get_feature_names_out() will return a ndarray array of string objects. list(dv.get_feature_names_out()) will convert to a standard list of strings. Also keep in mind that you first need to fit the predictor and response arrays before you have access to the feature names.

Quinn Avila

