---
course: mlops-zoomcamp
id: 1695e67099
question: Missing dependencies
section: 'Module 1: Introduction'
sort_order: 450
---

If some dependencies are missing

![Image](images/mlops-zoomcamp/image_7c6ef087.png)

Install following packages

pandas

matplotlib

scikit-learn

fastparquet

pyarrow

seaborn

pip install -r

I have seen this error when using pandas.read_parquet(), the solution is to install pyarrow or fastparquet by doing !pip install pyarrow in the notebook

NOTE: if you’re using Conda instead of pip, install fastparquet rather than pyarrow, as it is much easier to install and it’s functionally identical to pyarrow for our needs.

