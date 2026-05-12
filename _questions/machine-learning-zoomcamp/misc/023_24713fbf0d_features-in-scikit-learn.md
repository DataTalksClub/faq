---
id: 24713fbf0d
question: Features in scikit-learn?
sort_order: 23
---

Features (X) must always be formatted as a 2-D array to be accepted by scikit-learn. Use `reshape` to convert a 1D array to a 2D array.

```python
# Example of reshaping a 1D array to a 2D array
import numpy as np

# 1D array
array_1d = np.array([1, 2, 3, 4, 5])

# Reshape to a 2D array
array_2d = array_1d.reshape(-1, 1)
print(array_2d)
```

Additionally, when filtering and selecting specific columns in a DataFrame, you can use:

```python
# Filtering the DataFrame
df[df['ocean_proximity'].isin(['<1H OCEAN', 'INLAND'])]

# Select only the desired columns
selected_columns = [
    'latitude',
    'longitude',
    'housing_median_age',
    'total_rooms',
    'total_bedrooms',
    'population',
    'households',
    'median_income',
    'median_house_value'
]

filtered_df = filtered_df[selected_columns]

# Display the first few rows of the filtered DataFrame
print(filtered_df.head())
```