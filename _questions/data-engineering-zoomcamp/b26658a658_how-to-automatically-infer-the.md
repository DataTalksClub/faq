---
course: data-engineering-zoomcamp
id: b26658a658
question: How to automatically infer the column data type (pandas missing value issues)?
section: 'Module 4: analytics engineering with dbt'
sort_order: 2860
---

Problem: when injecting data to bigquery, you may face the type error. This is because pandas by default will parse integer columns with missing value as float type.

Solution:

One way to solve this problem is to specify/ cast data type Int64 during the data transformation stage.

However, you may be lazy to type all the int columns. If that is the case, you can simply use convert_dtypes to infer the data type

# Make pandas to infer correct data type (as pandas parse int with missing as float)

df.fillna(-999999, inplace=True)ingesting

df = df.convert_dtypes()

df = df.replace(-999999, None)

