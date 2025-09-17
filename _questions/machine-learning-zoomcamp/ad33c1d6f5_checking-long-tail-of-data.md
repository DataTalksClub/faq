---
id: ad33c1d6f5
question: Checking long tail of data
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 590
---

We can use histogram:

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Load the data

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'

df = pd.read_csv(url)

# EDA

sns.histplot(df['median_house_value'], kde=False)

plt.show()

OR ceck skewness and describe:

print(df['median_house_value'].describe())

# Calculate the skewness of the 'median_house_value' variable

skewness = df['median_house_value'].skew()

# Print the skewness value

print("Skewness of 'median_house_value':", skewness)

(Mohammad Emad Sharifi)

