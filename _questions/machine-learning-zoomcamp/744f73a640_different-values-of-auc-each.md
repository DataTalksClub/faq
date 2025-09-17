---
id: 744f73a640
question: Different values of auc, each time code is re-run
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2550
---

When I run dt = DecisionTreeClassifier() in jupyter in same laptop, each time I re-run it or do (restart kernel + run) I get different values of auc. Some of them are 0.674, 0.652, 0.642, 0.669 and so on.  Anyone knows why it could be? I am referring to 7:40-7:45 of video 6.3.

Solution: try setting the random seed e.g

dt = DecisionTreeClassifier(random_state=22)

Bhaskar Sarma

