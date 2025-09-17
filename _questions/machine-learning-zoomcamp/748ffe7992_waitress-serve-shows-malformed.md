---
course: machine-learning-zoomcamp
id: 748ffe7992
question: waitress-serve shows Malformed application
section: 5. Deploying Machine Learning Models
sort_order: 2190
---

Question:

When running

pipenv run waitress-serve --listen=localhost:9696 q4-predict:app

I get the following:

There was an exception (ValueError) importing your module.

It had these arguments:

1. Malformed application 'q4-predict:app'

Answer:

Waitress doesn’t accept a dash in the python file name.

The solution is to rename the file replacing a dash with something else for instance with an underscore eg q4_predict.py

Added by Alex Litvinov

