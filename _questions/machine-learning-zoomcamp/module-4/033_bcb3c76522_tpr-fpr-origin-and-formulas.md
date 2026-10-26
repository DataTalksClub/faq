---
id: bcb3c76522
question: Where do TPR (True Positive Rate) and FPR (False Positive Rate) come from,
  and why are the formulas written this way?
sort_order: 33
---

TPR and FPR come from the confusion matrix at a specific decision threshold.

For binary classification, the confusion matrix has four counts:

- `TP`: predicted positive, actually positive
- `FP`: predicted positive, actually negative
- `TN`: predicted negative, actually negative
- `FN`: predicted negative, actually positive

The model turns a score `g(x)` into a class with a rule like "positive if `g(x) >= threshold`". Changing the threshold moves examples between these four counts.

Each rate divides by the size of one true class:

- `TPR = TP / (TP + FN)`: the fraction of actual positives predicted as positive. `TP + FN` is the number of actual positives.
- `FPR = FP / (FP + TN)`: the fraction of actual negatives predicted as positive. `FP + TN` is the number of actual negatives.

Rates make results comparable across datasets and thresholds because they account for how many positives and negatives the data has.

Lowering the threshold predicts more examples as positive, so both TPR and FPR go up. The ROC curve plots TPR against FPR, with one point per threshold.
