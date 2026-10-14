---
id: bdcc3ae17b
question: 'Homework 2 Q5/Q6: my RMSE is far from all the options after changing the
  seed. What should I check?'
sort_order: 5
---

The most common cause is reusing an index array that was already shuffled. `np.random.shuffle(idx)` shuffles in place, so if you create `idx` once and then shuffle it again for each seed, every split after the first differs from the expected one.

Recreate the index for every seed, right before shuffling, exactly as in the lecture split:

```python
n = len(df)
idx = np.arange(n)
np.random.seed(seed)
np.random.shuffle(idx)
```

Do this inside the seed loop in Question 5, and again for the seed 9 split in Question 6. The `r` loop in Question 4 doesn't need a new split.

If the split is right and the result is still off, check that you use only the listed columns, fill the NAs as the question says, and add `r` to the diagonal of `XTX`. See also "My homework answer doesn't match any of the options".
