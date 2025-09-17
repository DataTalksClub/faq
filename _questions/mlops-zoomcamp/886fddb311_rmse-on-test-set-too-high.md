---
course: mlops-zoomcamp
id: 886fddb311
question: RMSE on test set too high
section: 'Module 1: Introduction'
sort_order: 550
---

Problem: RMSE on test set was too high when hot encoding the validation set with a previously fitted OneHotEncoder(handle_unknown=’ignore’) on the training set, while DictVectorizer would yield the correct RMSE.

In principle both transformers should behave identically when treating categorical features (at least in this week’s homework where we don’t have sequences of strings in each row):

Features are put into binary columns encoding their presence (1) or absence (0)

Unknown categories are imputed as zeroes in the hot-encoded matrix

