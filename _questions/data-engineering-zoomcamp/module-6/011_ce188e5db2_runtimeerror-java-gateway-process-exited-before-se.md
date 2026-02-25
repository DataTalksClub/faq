---
id: ce188e5db2
question: 'RuntimeError: Java gateway process exited before sending its port number'
sort_order: 11
---

After installing everything, including PySpark, when running this script in a Jupyter Notebook:

```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

# Read the CSV file
df = spark.read \
    .option("header", "true") \
    .csv('taxi+_zone_lookup.csv')

df.show()
```

You might encounter the error:

```
RuntimeError: Java gateway process exited before sending its port number
```

### Solutions

- **Solution 1:**
  1. Install `findspark` by running:
     
     ```bash
     pip install findspark
     ```
  2. Add the following lines to the top of your script:

     ```python
     import findspark
     findspark.init()
     ```

- **Solution 2:**
  1. Ensure that PySpark points to the correct location. Run:
     
     ```python
     pyspark.__file__
     ```
     
     It should list a path like `/home/<your user name>/spark/spark-3.0.3-bin-hadoop3.2/python/pyspark/__init__.py` if you followed the setup correctly.
  2. If it points to your Python site-packages, remove the PySpark directory there.
  3. Verify `.bashrc` for correct exports, ensuring no conflicting variables are present.

- **Alternative Solution:**
  - Set environment variables permanently at the system and user levels by following a tutorial.

     Once installed, skip to 7:14 in the tutorial to help set up environment variables.
