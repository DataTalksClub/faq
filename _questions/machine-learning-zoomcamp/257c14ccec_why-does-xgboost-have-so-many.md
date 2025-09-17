---
id: 257c14ccec
question: Why does XGBoost have so many parameters, and which are the most critical to start with?
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2700
---

XGBoost’s performance stems from its flexibility, thanks to a range of parameters. For initial tuning, focus on:

learning_rate: Controls the impact of each tree. Lower values (e.g., 0.01–0.1) typically improve performance but require more trees (n_estimators).

n_estimators: Sets the number of boosting rounds; adjust this in conjunction with learning_rate.

max_depth: Prevents overfitting by limiting the tree’s depth.

subsample: Dictates the fraction of samples used for training each tree, adding randomness to improve generalization.

Begin with these parameters before exploring others like gamma and min_child_weight for additional control over model complexity and performance.

(added by David Peterson)

This section is moved to

