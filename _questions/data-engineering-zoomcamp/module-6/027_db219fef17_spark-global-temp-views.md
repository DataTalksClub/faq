---
id: db219fef17
question: How do you share a DataFrame across multiple Spark sessions?
sort_order: 27
---

Spark provides **Global Temporary Views** to share DataFrames across different Spark sessions within the same Spark application.
Unlike regular temporary views, global temporary views are accessible from any session.
**Step 1: Create a Global Temporary View**
```python
# Create a global temporary view
df.createOrReplaceGlobalTempView('trips_global')
```
This registers the DataFrame as a global temporary view named `trips_global`.
**Step 2: Query the Global View from Any Session**
```python
spark.sql("SELECT * FROM global_temp.trips_global").show()
```
Global temporary views are stored in the `global_temp` database and must be referenced using the `global_temp.` prefix.