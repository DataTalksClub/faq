---
course: machine-learning-zoomcamp
id: 3547bb9442
question: Shuffling data using Numpy’s Generator Feature
section: 2. Machine Learning for Regression
sort_order: 760
---

While the lectures have you use the shuffle function to shuffle the index of the dataframe, it no longer accepts random seed as a parameter. This is because Numpy converted this feature into its own “Class”. In order to assign the random generator a seed, you have to specify the object (rng) that you are going to utilize in your code:

#Create index from range of values in array

idx = np.arange(n)

#Create random generator object and set seed

rng = np.random.default_rng(random_seed)

#Shuffle values using Generator object

rng.shuffle(idx)

Added by Emmanuel Lopez

