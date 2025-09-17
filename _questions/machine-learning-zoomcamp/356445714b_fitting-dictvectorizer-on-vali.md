---
course: machine-learning-zoomcamp
id: 356445714b
question: Fitting DictVectorizer on validation
section: 3. Machine Learning for Classification
sort_order: 1070
---

Validation dataset helps to validate models and prediction on unseen data. This helps get an estimate on its performance on fresh data. It helps optimize the model.

Edidiong Esu

Below is an extract of Alexey's book explaining this point. Hope is useful

When we apply the fit method, this method is looking at the content of the df_train dictionaries we are passing to the DictVectorizer instance, and fit is figuring out (training) how to map the values of these dictionaries. If categorical, applies one-hot encoding, if numerical it will leave it as it is.

With this context, if we apply the fit to the validation model, we are "giving the answers" and we are not letting the "fit" do its job for data that we haven't seen. By not applying the fit to the validation model we can know how well it was trained.

Below is an extract of Alexey's book explaining this point.

Humberto Rodriguez

There is no need to initialize another instance of dictvectorizer after fitting it on the train set as it will overwrite what it learnt from being fit on the train data.

The correct way is to fit_transform the train set, and only transform the validation and test sets.

Memoona Tahira

