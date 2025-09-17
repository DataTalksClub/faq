---
course: data-engineering-zoomcamp
id: 590e5d8c20
question: 'Py4J Error - ModuleNotFoundError: No module named ''py4j'' (Solve with
  latest version)'
section: 'Module 5: pyspark'
sort_order: 3410
---

If below does not work, then download the latest available py4j version with

conda install -c conda-forge py4j

Take care of the latest version number in the website to replace appropriately.

![Image](images/data-engineering-zoomcamp/image_be1c5cff.png)

Now add

export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"

export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH"

in your  .bashrc file.

