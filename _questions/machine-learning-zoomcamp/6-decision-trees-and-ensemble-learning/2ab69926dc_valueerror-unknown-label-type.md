---
id: 2ab69926dc
question: 'ValueError: Unknown label type: ''continuous'''
sort_order: 2540
---

Solution: This problem happens because you use DecisionTreeClassifier instead of DecisionTreeRegressor. You should check if you want to use a Decision tree for classification or regression.

Alejandro Aponte

