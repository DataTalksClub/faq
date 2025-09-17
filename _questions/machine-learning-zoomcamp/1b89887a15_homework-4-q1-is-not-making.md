---
course: machine-learning-zoomcamp
id: 1b89887a15
question: Homework 4 , q1 is not making sense to me.  The score should be between
  0 to 1. I tried computing roc_curve (df_train['age'], y] and the graph does not
  have the model line. Please can anyone clarify.
section: 5. Deploying Machine Learning Models
sort_order: 1740
---

The idea of the question is not something presented in the lecture videos, but it is a concept that could be useful when evaluating the importance of features with respect to the prediction of the binary target variable (yes/no).

In my case, I did the following:

identified the numerical features in the dataset

For each feature in the list of numerical features, I calculated the AUC like so: roc_auc_score(y_target, feature_vector). Here, the y_target is the y_triangle and the feature_vector contains the value for each numerical vector/column in the train dataset.

Next, I then created a data frame with two columns: name of numerical feature and ROC AUC score.

Finally, I sorted the data frame by the ROC AUC score to determine the numerical feature with the highest ROC AUC.

Victor Emenike

