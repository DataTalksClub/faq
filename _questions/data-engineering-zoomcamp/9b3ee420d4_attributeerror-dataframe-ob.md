---
course: data-engineering-zoomcamp
id: 9b3ee420d4
question: 'AttributeError: ''DataFrame'' object has no attribute ''iteritems'''
section: 'Module 5: pyspark'
sort_order: 3560
---

This error comes up on the Spark video 5.3.1 - First Look at Spark/PySpark,

because as at the creation of the video, 2021 data was the most recent which utilised csv files but as at now its parquet.

So when you run the command spark.createDataFrame(df1_pandas).show(),

You get the Attribute error. This is caused by the pandas version 2.0.0 which seems incompatible with Spark 3.3.2, so to fix it you have to downgrade pandas to 1.5.3 using the command pip install -U pandas==1.5.3

Another option is adding the following after importing pandas, if one does not want to downgrade pandas version () :

pd.DataFrame.iteritems = pd.DataFrame.items

Note that this problem is solved with Spark versions from 3.4.1

