---
course: machine-learning-zoomcamp
id: 23f66acd0a
question: 'Q6: ValueError or TypeError while setting xgb.DMatrix(feature_names=)'
section: 6. Decision Trees and Ensemble Learning
sort_order: 2450
---

If you’re getting TypeError:

“TypeError: Expecting a sequence of strings for feature names, got: <class 'numpy.ndarray'>”,

probably you’ve done this:

features = dv.get_feature_names_out()

It gets you np.ndarray instead of list. Converting to list list(features) will not fix this, read below.

If you’re getting ValueError:

“ValueError: feature_names must be string, and may not contain [, ] or <”,

probably you’ve either done:

features = list(dv.get_feature_names_out())

or:

features = dv.feature_names_

reason is what you get from DictVectorizer here looks like this:

['households',

'housing_median_age',

'latitude',

'longitude',

'median_income',

'ocean_proximity=<1H OCEAN',

'ocean_proximity=INLAND',

'population',

'total_bedrooms',

'total_rooms']

it has symbols XGBoost doesn’t like ([, ] or <).

What you can do, is either do not specify “feature_names=” while creating xgb.DMatrix or:

import re

features = dv.feature_names_

pattern = r'[\[\]<>]'

features = [re.sub(pattern, '  ', f) for f in features]

Added by Andrii Larkin

