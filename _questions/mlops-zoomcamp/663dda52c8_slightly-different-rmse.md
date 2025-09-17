---
course: mlops-zoomcamp
id: 663dda52c8
question: Slightly different RMSE
section: 'Module 1: Introduction'
sort_order: 600
---

Problem: My LinearRegression RMSE is very close to the answer but not exactly the same. Is this normal?

Answer: No, LinearRegression is an deterministic model, it should always output the same results when given the same inputs.

Answer:

Check if you have treated the outlier properly for both train and validation sets

Check if the one hot encoding has been done properly by looking at the shape of one hot encoded feature matrix. If it shows 2 features, there is something wrong with one hot encoding. Hint: the drop off and pick up codes need to be converted to proper data format and then DictVectorizer is fitted.

Harshit Lamba (hlamba19@gmail.com)

