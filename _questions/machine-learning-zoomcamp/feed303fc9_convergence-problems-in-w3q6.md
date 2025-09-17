---
course: machine-learning-zoomcamp
id: feed303fc9
question: Convergence Problems in W3Q6
section: 3. Machine Learning for Classification
sort_order: 1130
---

Ridge with sag solver requires feature to be of the same scale. You may get the following warning: ConvergenceWarning: The max_iter was reached which means the coef_ did not converge

Play with different scalers. See

Dmytro Durach

(Oscar Garcia)  Use a StandardScaler for the numeric fields and OneHotEncoder (sparce = False) for the categorical features.  This help with the warning. Separate the features (num/cat) without using the encoder first and see if that helps.

