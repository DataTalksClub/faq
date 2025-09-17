---
id: 19a42e2005
question: How to combine train and validation datasets
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 890
---

Use ‘pandas.concat’ function () to combine two dataframes. To combine two numpy arrays use numpy.concatenate () function. So the code would be as follows:

df_train_combined = pd.concat([df_train, df_val])

y_train = np.concatenate((y_train, y_val), axis=0)

(George Chizhmak)

