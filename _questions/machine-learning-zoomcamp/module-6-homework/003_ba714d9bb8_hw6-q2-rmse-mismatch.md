---
id: ba714d9bb8
question: Why is my Homework 6 Question 2 RMSE different from the expected result?
sort_order: 3
---

Before training on the 2026 Homework 6 dataset, fill missing values with zeros and split off 20% for testing with `random_state=1`. Then split the remaining data into training and validation sets with `test_size=0.25` and `random_state=1`.

For Question 2, fit `DictVectorizer(sparse=True)` on dictionaries from `df_train` and use it to transform `df_val`. Train a random forest regressor with `n_estimators=10` and `random_state=1`, and calculate its RMSE on the validation data. You can set `n_jobs=-1` to train faster, but it's optional.

See the [Homework 6 dataset preparation](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md#preparing-the-dataset) and [Question 2](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md#question-2) instructions.
