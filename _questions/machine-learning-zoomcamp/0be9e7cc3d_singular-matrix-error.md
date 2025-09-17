---
id: 0be9e7cc3d
question: Singular Matrix Error
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 310
---

I'm trying to invert the matrix but I got error that the matrix is singular matrix

The singular matrix error is caused by the fact that not every matrix can be inverted. In particular, in the homework it happens because you have to pay close attention when dealing with multiplication (the method .dot) since multiplication is not commutative! X.dot(Y) is not necessarily equal to Y.dot(X), so respect the order otherwise you get the wrong matrix.

