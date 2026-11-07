---
id: 2be102d7fd
question: In Homework 6 Q4, should I pick `max_depth` using the best single forest,
  average predictions, or the mean of RMSE across `n_estimators`?
sort_order: 2
---

When choosing `max_depth` in Homework 6 Q4, compute the mean of the validation RMSE values across the different `n_estimators` settings for each fixed `max_depth`, and pick the `max_depth` with the lowest mean.

For each depth `d`, keep all four validation RMSE values at full precision (don’t round early), then compute:

`mean_rmse(d) = (rmse(d, 10) + rmse(d, 50) + rmse(d, 100) + rmse(d, 150)) / 4`.

In the 2026 assignment, each `max_depth` in `[10, 15, 20, 25]` is evaluated with `n_estimators` in `[10, 50, 100, 150]` (with `random_state=1`). That gives 16 models total: four RMSE scores per depth, and four depth-level means.

Don’t replace this with:
- taking the minimum RMSE per depth (that selects a single best combination, not the mean performance across sizes)
- averaging predictions from multiple forests (that corresponds to a different ensemble model)
- taking `sqrt(mean(MSE))` from MSE values; the square root is nonlinear, so this generally won’t equal the arithmetic mean of the four RMSEs.

If there’s a tie in the depth-level means, report the tie and follow any explicit assignment/maintainer instructions.