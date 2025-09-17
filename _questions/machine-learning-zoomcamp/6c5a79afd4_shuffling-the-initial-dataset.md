---
course: machine-learning-zoomcamp
id: 6c5a79afd4
question: Shuffling the initial dataset using pandas built-in function
section: 2. Machine Learning for Regression
sort_order: 750
---

It is possible to do the shuffling of the dataset with the pandas built-in function .The complete dataset can be shuffled including resetting the index with the following commands:

Setting frac=1 will result in returning a shuffled version of the complete Dataset.

Setting random_state=seed will result in the same randomization as used in the course resources.

df_shuffled = df.sample(frac=1, random_state=seed)

df_shuffled.reset_index(drop=True, inplace=True)

Added by Sylvia Schmitt

