---
course: machine-learning-zoomcamp
id: 11783b6524
question: What is the difference between bagging and boosting?
section: 6. Decision Trees and Ensemble Learning
sort_order: 2480
---

For ensemble algorithms, during the week 6, one bagging algorithm and one boosting algorithm were presented: Random Forest and XGBoost, respectively.

Random Forest trains several models in parallel. The output can be, for example, the average value of all the outputs of each model. This is called bagging.

XGBoost trains several models sequentially: the previous model error is used to train the following model. Weights are used to ponderate the models such as the best models have higher weights and are therefore favored for the final output. This method is called boosting.

Note that boosting is not necessarily better than bagging.

Mélanie Fouesnard

Bagging stands for “Bootstrap Aggregation” - it involves taking multiple samples with replacement to derive multiple training datasets from the original training dataset (bootstrapping), training a classifier (e.g. decision trees or stumps for Random Forests) on each such training dataset, and then combining the the predictions (aggregation) to obtain the final prediction. For classification, predictions are combined via voting; for regression, via averaging. Bagging can be done in parallel, since the various classifiers are independent. Bagging decreases variance (but not bias) and is robust against overfitting.

Boosting, on the other hand, is sequential - each model learns from the mistakes of its predecessor. Observations are given different weights - observations/samples misclassified by the previous classifier are given a higher weight, and this process is continued until a stopping condition is reached (e.g. max. No. of models is reached, or error is acceptably small, etc.). Boosting reduces bias & is generally more accurate than bagging, but can be prone to overfitting.

Rileen

