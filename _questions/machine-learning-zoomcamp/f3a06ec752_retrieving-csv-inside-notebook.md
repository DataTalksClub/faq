---
course: machine-learning-zoomcamp
id: f3a06ec752
question: Retrieving csv inside notebook
section: 1. Introduction to Machine Learning
sort_order: 280
---

You can use

!wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv

To download the data too. The exclamation mark !, lets you execute shell commands inside your notebooks. This works generally for shell commands such as ls, cp, mkdir, mv etc . . .

For instance, if you then want to move your data into a data directory alongside your notebook-containing directory, you could execute the following:
!mkdir -p ../data/

!mv housing.csv ../data/

