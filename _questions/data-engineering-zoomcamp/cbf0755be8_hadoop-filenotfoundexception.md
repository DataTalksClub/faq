---
id: cbf0755be8
question: Hadoop - FileNotFoundException: Hadoop bin directory does not exist , when trying to write (Windows)
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3450
---

You need to create the Hadoop /bin directory manually and add the downloaded files in there, since the shell script provided for Windows installation just puts them in /c/tools/hadoop-3.2.0/ .

