---
id: 24d2042733
question: What does KFold do?
section: 4. Evaluation Metrics for Classification
course: machine-learning-zoomcamp
sort_order: 1510
---

KFold is a cross-validation technique that splits your dataset into k equal parts (folds). It trains the model k times, each time using a different fold as the validation set while training on the remaining folds. This process helps provide a more reliable estimate of a model's performance by ensuring every data point gets to be in both the training and validation sets. The average score across all folds offers a robust evaluation, minimizing the risk of overfitting to a specific train-test split.

What does this line do?

KFold(n_splits=n_splits, shuffle=True, random_state=1)

If I do it inside the loop [0.01, 0.1, 1, 10] or outside the loop in Q6, HW04 it doesn't make any difference to my answers. I am wondering why and what is the right way, although it doesn't make a difference!

Did you try using a different random_state? From my understanding, KFold just makes N (which is equal to n_splits) separate pairs of datasets (train+val).

In my case changing random state changed results

(Arthur Minakhmetov)

Changing the random state makes a difference in my case too, but not whether it is inside or outside the for loop. I think I have got the answer. kFold = KFold(n_splits=n_splits, shuffle = True, random_state = 1)  is just a generator object and it contains only the information n_splits, shuffle and random_state. The k-fold splitting actually happens in the next for loop for train_idx, val_idx in kFold.split(df_full_train): . So it doesn't matter where we generate the object, before or after the first loop. It will generate the same information. But from the programming point of view, it is better to do it before the loop. No point doing it again and again inside the loop

(Bhaskar Sarma)

In case of KFold(n_splits=n_splits, shuffle=True, random_state=1) and C= [0.01, 0.1, 1, 10], it is better to loop through the different values of Cs as the video explained. I had separate train() and predict() functions, which were reused after dividing the dataset via KFold. The model ran about 10 minutes and provided a good score.

(Ani Mkrtumyan)

