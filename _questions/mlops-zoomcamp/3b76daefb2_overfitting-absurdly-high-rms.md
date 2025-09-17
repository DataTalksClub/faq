---
course: mlops-zoomcamp
id: 3b76daefb2
question: 'Overfitting: Absurdly high RMSE on the validation dataset'
section: 'Module 1: Introduction'
sort_order: 690
---

Problem: The February dataset has been used as a validation/test dataset and been stripped of the outliers in a similar manner to the train dataset (taking only the rows for the duration between 1 and 60, inclusive). The RMSE obtained afterward is in the thousands.

Answer: The sparsematrix result from DictVectorizer shouldn’t be turned into an ndarray. After removing that part of the code, I ended up receiving a correct result .

Tahina Mahatoky ()

