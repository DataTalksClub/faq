---
course: mlops-zoomcamp
id: 148d5d0ed7
question: Extremely low RSME
section: 'Module 1: Introduction'
sort_order: 610
---

Problem: I’m facing an extremely low RMSE score (eg: 4.3451e-6) - what shall I do?

Answer: Recheck your code to see if your model is learning the target prior to making the prediction. If the target variable is passed in as a parameter while fitting the model, chances are the model would score extremely low. However, that’s not what you would want and would much like to have your model predict that. A good way to check that is to make sure your X_train doesn’t contain any part of your y_train. The same stands for validation too.

Snehangsu De ()

