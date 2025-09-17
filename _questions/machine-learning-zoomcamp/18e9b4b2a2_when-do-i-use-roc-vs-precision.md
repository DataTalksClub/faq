---
id: 18e9b4b2a2
question: When do I use ROC vs Precision-Recall curves?
section: 4. Evaluation Metrics for Classification
course: machine-learning-zoomcamp
sort_order: 1650
---

ROC curves are appropriate when the observations are balanced between each class, whereas precision-recall curves are appropriate for imbalanced datasets.

The reason for this recommendation is that ROC curves present an optimistic picture of the model on datasets with a class imbalance.

This is because of the use of true negatives in the False Positive Rate in the ROC Curve and the careful avoidance of this rate in the Precision-Recall curve.

If the proportion of positive to negative instances changes in a test set, the ROC curves will not change. Metrics such as accuracy, precision, lift and F scores use values from both columns of the confusion matrix. As a class distribution changes these measures will change as well, even if the fundamental classifier performance does not. ROC graphs are based upon TP rate and FP rate, in which each dimension is a strict columnar ratio, so cannot give an accurate picture of performance when there is class imbalance.

(Anudeep Vanjavakam)

