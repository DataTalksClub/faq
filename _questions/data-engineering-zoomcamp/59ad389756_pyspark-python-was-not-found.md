---
course: data-engineering-zoomcamp
id: 59ad389756
question: PySpark - Python was not found; run without arguments to install from the
  Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
section: 'Module 5: pyspark'
sort_order: 3320
---

I found this error while executing the user defined function in Spark (crazy_stuff_udf). I am working on Windows and using conda. After following the setup instructions, I found that the PYSPARK_PYTHON environment variable was not set correctly, given that conda has different python paths for each environment.

Solution:

pip install findspark on the command line inside proper environment

Add to the top of the script

import findspark

findspark.init()

