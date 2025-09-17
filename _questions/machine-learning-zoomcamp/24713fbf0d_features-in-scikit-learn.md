---
id: 24713fbf0d
question: Features in scikit-learn?
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4160
---

Features (X) must always be formatted as a 2-D array to be accepted by scikit-learn.

Use reshape to reshape a 1D array to a 2D.
							(-Aileah) :>

(added by Tano

filtered_df = df[df['ocean_proximity'].isin(['<1H OCEAN', 'INLAND'])]

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

