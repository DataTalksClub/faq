---
id: 9de29c6709
question: ValueError: feature_names must be string, and may not contain [, ] or <
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2600
---

This error occurs because the list of feature names contains some characters like "<" that are not supported. To fix this issue, you can replace those problematic characters with supported ones. If you want to create a consistent list of features with no special characters, you can achieve it like this:

You can address this error by replacing problematic characters in the feature names with underscores, like so:

features = [f.replace('=<', '_').replace('=', '_') for f in features]

This code will go through the list of features and replace any instances of "=<" with "", as well as any "=" with "", ensuring that the feature names only consist of supported characters.

