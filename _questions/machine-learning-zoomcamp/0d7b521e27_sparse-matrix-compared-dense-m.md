---
id: 0d7b521e27
question: Sparse matrix compared dense matrix
section: 3. Machine Learning for Classification
course: machine-learning-zoomcamp
sort_order: 1150
---

A sparse matrix is more memory-efficient because it only stores the non-zero values and their positions in memory. This is particularly useful when working with large datasets with many zero or missing values.

The default DictVectorizer configuration is a sparse matrix. For week3 Q6 using the default sparse is an interesting option because of the size of the matrix. Training the model was also more performant and didn’t give an error message like dense mode.
 												Quinn Avila

