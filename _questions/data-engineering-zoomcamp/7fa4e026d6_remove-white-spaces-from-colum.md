---
course: data-engineering-zoomcamp
id: 7fa4e026d6
question: Remove white spaces from column names in Pyspark
section: 'Module 5: pyspark'
sort_order: 3550
---

df_finalx=df_finalw.select([col(x).alias(x.replace(" ","")) for x in df_finalw.columns])

Krishna Anand

