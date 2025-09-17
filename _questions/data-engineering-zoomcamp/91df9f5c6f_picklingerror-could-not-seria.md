---
id: 91df9f5c6f
question: PicklingError: Could not serialise object: IndexError: tuple index out of range.
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3610
---

Occurred while running : spark.createDataFrame(df_pandas).show()

This error is usually due to the python version, since spark till date of 2 march 2023 doesn’t support python 3.11, try creating a new env with python version 3.8 and then run this command.

On the virtual machine, you can create a conda environment (here called myenv) with python 3.10 installed:

conda create -n myenv python=3.10 anaconda

Then you must run conda activate myenv to run python 3.10. Otherwise you’ll still be running version 3.11. You can deactivate by typing conda deactivate.

