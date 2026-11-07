---
id: 322f24380b
question: Do I need to scale/standardize features before training a Decision Tree
  or Random Forest?
sort_order: 32
---

No, decision trees and random forests split data using feature thresholds. You can scale or standardize features without changing their relative order, so the trees can use adjusted thresholds to make equivalent splits.

In [2026 Homework 6](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md#preparing-the-dataset), fill missing values with zeros and use `DictVectorizer` without scaling.

