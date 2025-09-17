---
course: machine-learning-zoomcamp
id: 7ec4b76943
question: How to get the training and validation metrics from XGBoost?
section: 6. Decision Trees and Ensemble Learning
sort_order: 2410
---

During the XGBoost lesson, we created a parser to extract the training and validation auc from the standard output. However, we can accomplish that in a more straightforward way.

We can use the evals_result  parameters, which takes an empty dictionary and updates it for each tree. Additionally, you can store the data in a dataframe and plot it in an easier manner.

![Image](images/machine-learning-zoomcamp/image_ca7081bf.png)

Added by Daniel Coronel

