---
id: c0444b72ca
question: Why does DecisionTreeClassifier and DecisionTreeRegressor not throw an error when there are nan (missing) values in the feature matrix?
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2680
---

In lesson 6.3 around 6:00, there is an error due to missing values. Subsequently .fillna(0) is used on df_train to deal with this. However, since v1.3, support for missing values has been added for DecisionTreeClassifier and DecisionTreeRegressor. More details can be found , under sklearn.tree.

(added by Kemal Dahha)

