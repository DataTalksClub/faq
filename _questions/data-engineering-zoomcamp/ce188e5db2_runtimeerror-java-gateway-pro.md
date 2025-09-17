---
course: data-engineering-zoomcamp
id: ce188e5db2
question: 'RuntimeError: Java gateway process exited before sending its port number'
section: 'Module 5: pyspark'
sort_order: 3380
---

After installing all including pyspark (and it is successfully imported), but then running this script on the jupyter notebook

import pyspark

from pyspark.sql import SparkSession

spark = SparkSession.builder \

.master("local[*]") \

.appName('test') \

.getOrCreate()

df = spark.read \

.option("header", "true") \

.csv('taxi+_zone_lookup.csv')

df.show()

it gives the error:

RuntimeError: Java gateway process exited before sending its port number

✅The solution (for me) was:

pip install findspark on the command line and then

Add

import findspark

findspark.init()

to the top of the script.

Another possible solution is:

Check that pyspark is pointing to the correct location.

Run pyspark.__file__. It should be list /home/<your user name>/spark/spark-3.0.3-bin-hadoop3.2/python/pyspark/__init__.py if you followed the videos.

If it is pointing to your python site-packages remove the pyspark directory there and check that you have added the correct exports to you .bashrc file and that there are not any other exports which might supersede the ones provided in the course content.

To add to the solution above, if the errors persist in regards to setting the correct path for spark,  an alternative solution for permanent path setting solve the error is  to set environment variables on system and user environment variables following this tutorial:

Once everything is installed, skip to 7:14 to set up environment variables. This allows for the environment variables to be set permanently.

