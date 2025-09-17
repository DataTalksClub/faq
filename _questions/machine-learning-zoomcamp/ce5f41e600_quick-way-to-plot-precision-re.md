---
id: ce5f41e600
question: Quick way to plot Precision-Recall Curve
section: 4. Evaluation Metrics for Classification
course: machine-learning-zoomcamp
sort_order: 1680
---

We can import precision_recall_curve from scikit-learn and plot the graph as follows:

from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_val, y_predict)

plt.plot(thresholds, precision[:-1], label='Precision')

plt.plot(thresholds, recall[:-1], label='Recall')

plt.legend()

Hrithik Kumar Advani

