---
id: b7e73fcee7
question: Floating Point Precision
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 400
---

I was doing Question 7 from Week1 Homework and with step6: Invert XTX, I created the inverse. Now, an inverse when multiplied by the original matrix should return in an Identity matrix. But when I multiplied the inverse with the original matrix, it gave a matrix like this:

Inverse * Original:

[[ 1.00000000e+00 -1.38777878e-16]

[ 3.16968674e-13  1.00000000e+00]]

Solution:

It's because floating point math doesn't work well on computers as shown here:

(Added by Wesley Barreto)

