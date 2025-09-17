---
id: 71f360d8eb
question: What data should we use for correlation matrix
section: 3. Machine Learning for Classification
course: machine-learning-zoomcamp
sort_order: 1020
---

Q2 asks about correlation matrix and converting median_house_value from numeric to binary. Just to make sure here we are only dealing with df_train not df_train_full, right? As the question explicitly mentions the train dataset.

Yes. I think it is only on df_train. The reason behind this is that df_train_full also contains the validation dataset, so at this stage we don't want to make conclusions based on the validation data, since we want to test how we did without using that portion of the data.

Pastor Soto

