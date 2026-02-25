---
id: 59ad389756
question: 'PySpark: Python was not found; run without arguments to install from the
  Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.'
sort_order: 5
---

I encountered this error while executing a user-defined function in Spark (`crazy_stuff_udf`). I am working on Windows and using conda. After following the setup instructions, I discovered that the `PYSPARK_PYTHON` environment variable was not set correctly, as conda has different Python paths for each environment.

**Solution:**

1. Run the following command inside the appropriate environment:
   
   ```bash
   pip install findspark
   ```

2. Add the following to the top of your script:
   
   ```python
   import findspark
   
   findspark.init()
   ```