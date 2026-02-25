---
id: d87bb0e38f
question: 'Py4JJavaError - ModuleNotFoundError: No module named ''py4j'' while executing
  `import pyspark`'
sort_order: 13
---

To resolve the `ModuleNotFoundError: No module named 'py4j'` when executing `import pyspark`, follow these steps:

1. **Check for Py4J File Version:**
   - Run the command:
     ```bash
     ls ${SPARK_HOME}/python/lib/
     ```
   - Note the version of the `py4j` file.

2. **Update the `PYTHONPATH`:**
   - Use the version identified above to update the `PYTHONPATH` accordingly. For example:
     ```bash
     export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.3-src.zip:$PYTHONPATH"
     ```
   - Ensure that the version matches the filename under `${SPARK_HOME}/python/lib/`.

3. **Verify Spark's Py4J Version:**
   - Check the Py4J version of the Spark you're using from the [Apache Spark documentation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html).

4. **Install Py4J (if needed):**
   - If the above steps do not resolve the issue, run:
     ```bash
     pip install py4j
     ```
   - This can resolve version mismatches or missing installations.

This should address the `ModuleNotFoundError` for Py4J when using PySpark. Ensure all versions are consistent and correct.