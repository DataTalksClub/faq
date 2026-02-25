---
id: 675d60dadd
question: Module Not Found Error in Jupyter Notebook.
sort_order: 12
---

Even after installing `pyspark` correctly on a Linux machine (VM) as instructed in the course, a module not found error was encountered in the Jupyter Notebook.

The solution that worked:

1. Run the following in the Jupyter Notebook:

   ```bash
   !pip install findspark
   ```

2. Import and initialize `findspark`:

   ```python
   import findspark
   findspark.init()
   ```

3. Thereafter, import `pyspark` and create the Spark context as usual.

If the above solution does not work, try:

- Using `!pip3 install pyspark` instead of `!pip install pyspark`.

To filter based on conditions across multiple columns:

```python
from pyspark.sql.functions import col

new_final.filter((new_final.a_zone=="Murray Hill") & (new_final.b_zone=="Midwood")).show()
```