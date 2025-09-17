---
course: mlops-zoomcamp
id: e107978d25
question: 'Q: Why did we not use OneHotEncoder(sklearn) instead of DictVectorizer
  ?'
section: 'Module 1: Introduction'
sort_order: 570
---

Why didn't get_dummies in the pandas library or OneHotEncoder in scikit-learn library be used for one-hot encoding? I know OneHotEncoder is the most common and useful. One-hot coding can also be done using the eye or identity components of the NumPy library.

M.Sari

OneHotEncoder has the option to output a row column tuple matrix. DictVectorizer is a one step method to encode and support row column tuple matrix output.

Harinder()

We used DictVectorizer because it provides a simple one-step way to handle both categorical and numerical features from dictionaries, and directly outputs a sparse matrix—making it ideal for ML pipelines without extra preprocessing.

Yann Pham-Van

Use OneHotEncoder when you want full control, need to work with sklearn pipelines, or must handle unknown categories safely. Use DictVectorizer when your data is in dictionary format (e.g., JSON or from APIs) and you want to plug it into a pipeline quickly.

