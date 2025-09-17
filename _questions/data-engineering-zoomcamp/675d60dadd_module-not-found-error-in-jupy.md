---
course: data-engineering-zoomcamp
id: 675d60dadd
question: Module Not Found Error in Jupyter Notebook .
section: 'Module 5: pyspark'
sort_order: 3390
---

Even after installing pyspark correctly on linux machine (VM ) as per course instructions, faced a module not found error in jupyter notebook .

The solution which worked for me(use following in jupyter notebook) :

!pip install findspark

import findspark

findspark.init()

Thereafter , import pyspark and create spark contex<<t as usual

None of the solutions above worked for me till I ran !pip3 install pyspark instead !pip install pyspark.

Filter based on conditions based on multiple columns

from pyspark.sql.functions import col

new_final.filter((new_final.a_zone=="Murray Hill") & (new_final.b_zone=="Midwood")).show()

Krishna Anand

