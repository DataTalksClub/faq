---
id: 3f9286329a
question: The feature size is different for training set and validation set
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 670
---

While working through the HW1, you will realize that the training and the validation data set feature sizes are different. I was trying to figure out why and went down the entire rabbit hole only to see that I wasn’t doing ```transform``` on the premade dictionary vectorizer instead of ```fit_transform```. You already have the dictionary vectorizer made so no need to execute the fit pipeline on the model.

Sam Lim()

