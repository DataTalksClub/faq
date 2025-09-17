---
id: ced9c0443e
question: Where can I find other people’s projects to peer review them and where do I post mine for peer review? (cohort 2024).
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4310
---

The review assignments will be available on  after the first phase of the project is over -i.e. after the submission deadline. After that you will have one week to complete the review.

Saturn Cloud errors (in Jupyter Notebook):

ImportError: cannot import name 'runtime_version' from 'google.protobuf'

Can be resolved by updating protobuf:

!pip install -U protobuf

Works for tensorflow 2.17.0 and protobuf 4.25.5  (5.29.0 after updating)

Additionally, updating tensorflow to 2.18.0 (!pip install -U tensorflow at the moment) resolves the issue of the model.fit function hanging

