---
id: 0c116f6001
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_91f633ae.png
question: In module 5.3.1, trying to run `spark.createDataFrame(df_pandas).show()`
  returns error
sort_order: 57
---

```
AttributeError: 'DataFrame' object has no attribute 'iteritems'
```

This error occurs because a method inside PySpark refers to a package that has been deprecated ([Stack Overflow](https://stackoverflow.com/questions/76404811/attributeerror-dataframe-object-has-no-attribute-iteritems)).

### Solutions

- Refer to the code mentioned in the Stack Overflow link.

  <{IMAGE:image_1}>

- Another workaround is to create a conda environment to downgrade Python's version to 3.8 and Pandas to 1.5.3:

  ```bash
  conda create -n pyspark_env python=3.8 pandas=1.5.3 jupyter
  
  conda activate pyspark_env
  ```
