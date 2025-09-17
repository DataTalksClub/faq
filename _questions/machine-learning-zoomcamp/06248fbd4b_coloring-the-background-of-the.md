---
course: machine-learning-zoomcamp
id: 06248fbd4b
question: Coloring the background of the pandas.DataFrame.corr correlation matrix
  directly
section: 3. Machine Learning for Classification
sort_order: 1040
---

The background of any dataframe can be colored (not only the correlation matrix) based on the numerical values the dataframe contains by using the method .

Here an example on how to color the correlation matrix. A color map of choice can get passed, here ‘viridis’ is used.

# ensure to have only numerical values in the dataframe before calling 'corr'

corr_mat = df_numerical_only.corr()

corr_mat.style.background_gradient(cmap='viridis')

Here is an example of how the coloring will look like using a dataframe containing random values and applying “background_gradient” to it.

np.random.seed = 3

df_random = pd.DataFrame(data=np.random.random(3*3).reshape(3,3))

df_random.style.background_gradient(cmap='viridis')

![Image](images/machine-learning-zoomcamp/image_db91a31a.png)

Added by Sylvia Schmitt

