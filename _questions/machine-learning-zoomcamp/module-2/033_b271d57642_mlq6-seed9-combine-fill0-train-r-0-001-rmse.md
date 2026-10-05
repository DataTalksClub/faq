---
id: b271d57642
question: 'Question 6: Using seed 9, combine train+validation, fill missing values
  with 0, train with r=0.001 — what is the test RMSE?'
sort_order: 33
---

To get the RMSE for Question 6, you need to follow the exact homework procedure in one consistent pipeline:

- Re-split the data using `seed = 9`.
- Combine the training and validation parts back together (so the model trains on `train + validation`).
- Fill missing feature values with `0` (using the constant fill specified by the question).
- Train the regression model using `r = 0.001`.
- Compute RMSE on the provided test dataset using the model’s predictions.

If you still get a value that doesn’t match the multiple-choice options, double-check that you fully reinitialize the index/iteration variables used in the loop for question 5/6 (the homework notes that you should reinitialize like `Idx = np.arange(n)` for each question/`r` iteration), since stale state can shift results.