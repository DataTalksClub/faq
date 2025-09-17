---
id: a654b0e217
question: How to avoid accidentally pushing CSV files
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 570
---

To avoid accidentally pushing CSV files (or any specific file type) to a Git repository, you can use a .gitignore file.

Add a rule to ignore CSV files   *.csv

If the CSV files have already been committed,you can remove them from Git tracking but keep them locally by using command

git.rm –-cached filename.csv

Added by Olga Rudakova

