---
id: 8c19bce6ed
question: Why doesn’t the maximum F1-score happen where precision equals recall (Precision–Recall
  intersection)?
sort_order: 35
---

`F1` is the harmonic mean of precision and recall: `F1 = 2 * P * R / (P + R)`. Because the formula depends on both values, the threshold where precision and recall are closest doesn't have to maximize `F1`.

Using the values in your question, threshold `0.63` gives precision `0.733` and recall `0.725`, so `F1` is about `0.729`. Threshold `0.41` gives precision `0.619` and recall `0.976`, so `F1` is about `0.758`. The `0.41` threshold has the higher `F1`, even though precision and recall differ. The [2026 Homework 4 instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/04-evaluation/homework.md#question-4-f1-score) ask you to calculate `F1` at every threshold from `0.0` to `1.0`.
