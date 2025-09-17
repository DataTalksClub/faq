---
id: 575e56b819
question: What is the difference between label and one-hot encoding?
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 530
---

Two main encoding approaches are generally used to handle categorical data: label encoding and one-hot encoding. The first assigns each categorical value an integer value based on alphabetical order, while the second creates new variables (using 0s and 1s) depicting original categorical data. Simply, one may use label encoding with logical categorical data such as a rating system or a classification, and one-hot encoding is rather applicable to cases where there is no reasoning with the data. Sci-kit Learn dictionary vectorizer is an encoding class that will provide a means to handle categorical data and generate a corresponding array based on the unique number of instances encountered within your columns choice from a DataFrame (or else). The key point is to assign values to categories and thus enable fitting ML models. In case you want to apply one-hot encoding, sometimes you’ll have to reset the dataset into objects, so any possible logic is deceived. Otherwise, you may fall into label encoding, which can be limiting for some applications. Besides the dictionary vectorizer, Sci-kit Learn also offers the OneHotEncoding() class. Pandas has a similar feature, named pd.get_dummies().

Added by Jonathan Lima (jtlimads@gmail.com)

