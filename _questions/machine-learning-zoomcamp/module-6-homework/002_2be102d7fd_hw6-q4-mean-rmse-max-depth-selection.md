---
id: 2be102d7fd
question: In Homework 6 Q4, should I pick `max_depth` using the best single forest,
  average predictions, or the mean of RMSE across `n_estimators`?
sort_order: 2
---

Average the validation RMSE scores across all four `n_estimators` values for each fixed `max_depth`, then choose the depth with the lowest mean. Keep full precision until you calculate each mean.

For [2026 Homework 6 Question 4](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/06-trees/homework.md#question-4), use `random_state=1` with `max_depth` values `[10, 15, 20, 25]` and `n_estimators` values `[10, 50, 100, 150]`.

For each depth `d`, calculate `(rmse(d, 10) + rmse(d, 50) + rmse(d, 100) + rmse(d, 150)) / 4`.

Don't average predictions from multiple forests or choose the minimum RMSE per depth.
