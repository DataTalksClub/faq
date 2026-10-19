---
id: bcb3c76522
question: Where do TPR (True Positive Rate) and FPR (False Positive Rate) come from,
  and why are the formulas written this way?
sort_order: 31
---

TPR and FPR are defined from the confusion matrix at a specific decision threshold.

Start with the confusion table for binary classification:
- `TP`: model predicts the positive class and the true label is positive
- `FP`: model predicts the positive class but the true label is negative
- `TN`: model predicts the negative class and the true label is negative
- `FN`: model predicts the negative class but the true label is positive

For a given threshold, the model turns a score `g(x)` (often a probability or sigmoid output) into a class prediction, e.g. “positive if `g(x) >= threshold`, otherwise negative”. As you change the threshold, `TP`, `FP`, `TN`, and `FN` change in a coupled way.

That’s why the rates are ratios that normalize by the relevant population:
- `TPR = TP / (TP + FN)`
  - You’re asking: *of all truly positive examples, what fraction did we correctly predict as positive?*
  - The denominator `(TP + FN)` is exactly the count of “actual positives”.
- `FPR = FP / (FP + TN)`
  - You’re asking: *of all truly negative examples, what fraction did we incorrectly predict as positive?*
  - The denominator `(FP + TN)` is exactly the count of “actual negatives”.

Using rates (instead of raw counts) makes the metrics comparable across datasets (and across thresholds), because they account for how many positives/negatives you had in the ground truth.

Finally, when you sweep thresholds, you can see the trade-off behavior: decreasing the threshold tends to increase the number of “predicted positive” cases—so `TP` and `FP` generally move in opposite directions to `TN` and `FN`. That’s the same structure behind ROC curves (TPR vs FPR) where each threshold gives one point.