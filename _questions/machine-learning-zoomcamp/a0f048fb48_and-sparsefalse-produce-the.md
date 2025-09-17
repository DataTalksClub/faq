---
course: machine-learning-zoomcamp
id: a0f048fb48
question: 'and (sparse=False) produce the same type of one-hot encodings:'
section: 3. Machine Learning for Classification
sort_order: 1120
---

![Image](images/machine-learning-zoomcamp/image_e1899130.png)

(sparse=True) produces  format, which is both more memory efficient and converges better during fit(). Basically it stores non-zero values and indices instead of adding a column for each class of each feature (models of cars produced 900+ columns alone in the current task).

Using “sparse” format like on the picture above, both via  and (sparse=False) - is slower (around 6-8min for Q6 task - Linear/Ridge Regression) for high amount of classes (like models of cars for eg) and gives a bit “worse” results in both Logistic and Linear/Ridge Regression, while also producing convergence warnings for Linear/Ridge Regression.

Larkin Andrii

