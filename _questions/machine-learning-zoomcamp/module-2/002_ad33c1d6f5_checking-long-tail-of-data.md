---
id: ad33c1d6f5
question: Checking long tail of data
sort_order: 2
---

To analyze the long tail of data, you can use a histogram or check skewness and descriptive statistics.

**Using Histogram**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'
df = pd.read_csv(url)

# EDA
sns.histplot(df['median_house_value'], kde=False)
plt.show()
```

**Check Skewness and Descriptive Statistics**

```python
# Describe the 'median_house_value'
print(df['median_house_value'].describe())

# Calculate the skewness of the 'median_house_value' variable
skewness = df['median_house_value'].skew()

# Print the skewness value
print("Skewness of 'median_house_value':", skewness)
```