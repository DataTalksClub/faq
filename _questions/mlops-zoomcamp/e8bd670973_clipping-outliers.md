---
id: e8bd670973
question: Clipping outliers
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 580
---

How to check that we removed the outliers?

Use the pandas function describe() which can provide a report of the data distribution along with the statistics to describe the data. For example, after clipping the outliers using boolean expression, the min and max can be verified using

df[‘duration’].describe()

![Image](images/mlops-zoomcamp/image_2715561d.png)

