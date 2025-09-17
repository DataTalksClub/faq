---
id: ab0c17d01c
question: Filter a dataset by using its values
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 660
---

We can filter a dataset by using its values as below.

df = df[(df["ocean_proximity"] == "<1H OCEAN") | (df["ocean_proximity"] == "INLAND")]

You can use | for ‘OR’, and & for ‘AND’

Alternative:

df = df[df['ocean_proximity'].isin(['<1H OCEAN', 'INLAND'])]

Radikal Lukafiardi

