---
id: ba636cdb18
question: Getting NaNs after applying .mean()
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 620
---

I was using for loops to apply rmse to list of y_val and y_pred. But the resulting rmse is all nan.

I found out that the problem was when my data reached the mean step after squaring the error in the rmse function. Turned out there were nan in the array, then I traced the problem back to where I first started to split the data: I had only use fillna(0) on the train data, not on the validation and test data. So the problem was fixed after I applied fillna(0) to all the dataset (train, val, test). Voila, my for loops to get rmse from all the seed values work now.

Added by Sasmito Yudha Husada

