---
id: e3ce42af1a
question: How do you read data stored in gcs on pandas with your local computer?
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3640
---

To do this
pip install gcsfs,

Thereafter copy the uri path to the file and use 
df = pandas.read_csc(gs://path)

