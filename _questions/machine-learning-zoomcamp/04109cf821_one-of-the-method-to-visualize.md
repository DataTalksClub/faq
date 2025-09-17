---
id: 04109cf821
question: One of the method to visualize the decision trees
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2530
---

dot_data = tree.export_graphviz(regr, out_file=None,

feature_names=boston.feature_names,

filled=True)

graphviz.Source(dot_data, format="png")

Krishna Anand

from sklearn import tree

tree.plot_tree(dt,feature_names=dv.feature_names_)

Added By Ryan Pramana

