---
course: machine-learning-zoomcamp
id: a64b95ea2c
question: Multiple thresholds for Q4
section: 4. Evaluation Metrics for Classification
sort_order: 1440
---

I am getting multiple thresholds with the same F1 score, does this indicate I am doing something wrong or is there a method for choosing? I would assume just pick the lowest?

Choose the one closest to any of the options

Added by Azeez Enitan Edunwale

You can always use scikit-learn (or other standard libraries/packages) to verify results obtained using your own code, e.g. you can use  “classification_report” () to obtain precision, recall and F1-score.

Added by Rileen Sinha

