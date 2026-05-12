---
id: 03e27c386a
question: Isn't it easier to use DictVertorizer or get dummies before splitting the
  data into train/val/test? Is there a reason we wouldn't do this? Or is it the same
  either way?
sort_order: 23
---

The reason it's recommended to do it after splitting is to avoid data leakage. You don't want any data from the test set influencing the training stage, similarly from the validation stage in the initial training. See e.g. scikit-learn documentation on "Common pitfalls and recommended practices": [https://scikit-learn.org/stable/common_pitfalls.html](https://scikit-learn.org/stable/common_pitfalls.html)