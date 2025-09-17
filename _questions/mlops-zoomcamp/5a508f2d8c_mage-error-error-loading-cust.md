---
course: mlops-zoomcamp
id: 5a508f2d8c
question: 'Mage error: Error loading custom object at…'
section: 'Module 4: Deployment'
sort_order: 1830
---

When returning an object from a block, you may encounter an error like

Error loading custom_object at /home/src/mage_data/*************/pipelines/taxi_duration_pipe/.variables/make_predictions/output_0: [Errno 2] No such file or directory: '/home/src/mage_data/*************/pipelines/taxi_duration_pipe/.variables/make_predictions/output_0/object.joblib'

Error loading custom_object at /home/src/mage_data/*************/pipelines/taxi_duration_pipe/.variables/make_predictions/output_0: [Errno 2] No such file or directory: '/home/src/mage_data/*************/pipelines/taxi_duration_pipe/.variables/make_predictions/output_0/object.joblib'

This happened to me when returning a numpy.ndarray, namely the y_pred variable containing the predictions for the taxi dataset. I believe Mage struggles returning some type of objects and expects things like DataFrames instead of numpy.ndarrays. What I did was to return a df that had both the y_pred and the ride ids.

Added by Fustincho

