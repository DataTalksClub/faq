---
course: data-engineering-zoomcamp
id: 0c116f6001
question: In module 5.3.1, trying to run spark.createDataFrame(df_pandas).show() returns
  error
section: 'Module 5: pyspark'
sort_order: 3840
---

AttributeError: 'DataFrame' object has no attribute 'iteritems'

this is because the method inside the pyspark refers to a package that has been already deprecated

(https://stackoverflow.com/questions/76404811/attributeerror-dataframe-object-has-no-attribute-iteritems)

You can do this code below, which is mentioned in the stackoverflow link above:

![Image](images/data-engineering-zoomcamp/image_91f633ae.png)

Another work around here is to create a conda enviroment to donwgrade python’s version to 3.8 and pandas to 1.5.3

conda create -n pyspark_env python=3.8 pandas=1.5.3 jupyter

conda activate pyspark_env

