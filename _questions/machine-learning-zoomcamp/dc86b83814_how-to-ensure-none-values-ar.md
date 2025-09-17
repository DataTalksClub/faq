---
course: machine-learning-zoomcamp
id: dc86b83814
question: How to ensure "none" values are not interpreted as NaN when reading a CSV
  file in Pandas
section: 6. Decision Trees and Ensemble Learning
sort_order: 2390
---

To ensure that the string values like "None" are treated as valid strings rather than being converted to NaN when reading a CSV file, you can read the CSV file with keep_default_na set to False and specify the values you want to consider as NaN with the na_values parameter.

Here’s an example of how to do this:

import pandas as pd

df = pd.read_csv("dataset_path.csv", keep_default_na=False, na_values=['', 'NaN', 'null'])

Using keep_default_na=False prevents Pandas from applying its default set of NaN values, allowing "None" to be read as a regular string.

(added by Karina)

