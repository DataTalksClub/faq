---
id: c58d3563a6
question: Python - These won't work. You need to make sure you use Int64:
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2400
---

Incorrect:

df['DOlocationID'] = pd.to_numeric(df['DOlocationID'], downcast=integer) or

df['DOlocationID'] = df['DOlocationID'].astype(int)

Correct:

df['DOlocationID'] = df['DOlocationID'].astype('Int64')

