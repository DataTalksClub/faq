---
course: machine-learning-zoomcamp
id: b78f247dc5
question: 'ValueError: feature_names must be string, and may not contain [, ] or <'
section: 6. Decision Trees and Ensemble Learning
sort_order: 2430
---

In question 6, I was getting ValueError: feature_names must be string, and may not contain [, ] or < when I was creating DMatrix for train and validation

Solution description

The cause of this error is that some of the features names contain special characters like = and <, and I fixed the error by removing them as  follows:

features= [i.replace("=<", "_").replace("=","_") for i in features]

Asia Saeed

Alternative Solution:

In my case the equal sign “=” was not a problem, so in my opinion the first part of Asias solution features= [i.replace("=<", "_") should work as well.

For me this works:

features = []

for f in dv.feature_names_:

string = f.replace(“=<”, “-le”)

features.append(string)

Peter Ernicke

