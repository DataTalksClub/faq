---
id: fe61ce3be4
question: What is the difference between a Spark application, job, stage, and task?
sort_order: 33
---

One of the first places where Spark concepts appear is in the graphical interface. There we see terms like application, job, stage, or task, but at first it's not always clear how they relate to each other. Understanding this hierarchy is very useful because it allows us to interpret what Spark is doing internally, debug problems, and better understand the performance of our processes.

Applications

A Spark application is the complete program we execute. It is the entire process that begins when we launch something like:

```bash
spark-submit script.py
```

or when we start a session in PySpark or a notebook.

```python
import pyspark
import os
from pyspark.sql import SparkSession

spark = SparkSession.builder \
.master(os.environ.get('SPARK_MASTER')) \
.appName("csv-to-parquet") \
.getOrCreate()
```

A Spark application includes:

* The driver program, which coordinates execution.
* The executors, which perform the distributed work.
* All operations executed by the program until it finishes.

We can think of the application as the complete execution of our program.

For example, if we run a PySpark script that 1) reads a dataset, 2) performs several transformations, and 3) writes a result; all of that forms a single Spark application.

The graphical interface shows one entry for each executed application.

Job

Within an application, Spark divides the work into jobs. A job is created every time we execute an action on a DataFrame. As we saw in previous chapters, in Spark there are two types of operations:

* Transformations: describe a transformation but are not executed immediately.
* Actions: trigger the immediate execution of the transformations described up to that point.

Some examples of actions are `show()`, `count()`, `collect()`, `write`, or `save`. Every time we call an action, Spark creates a new job.

In the script:

```python
df = spark.read.parquet("data.parquet")
df_filtered = df.filter("price > 10")

df_filtered.count()
df_filtered.show()
```

... two separate jobs will be executed, one for `count()` and one for `show()`, even though both use the same _DataFrame_.

This happens because Spark evaluates transformations lazily and only executes the plan when a result is requested.

Stages

Each job is divided into stages. Stages represent groups of operations that can be executed without needing to redistribute data between nodes.

The reason they are separated into stages is usually an operation called a _shuffle_. A _shuffle_ occurs when data must be redistributed between partitions; for example in operations like: `groupBy`, `join`, `distinct`, and `reduceByKey`.

When Spark detects that a _shuffle_ is needed, it divides the job into several stages.

```python
df.groupBy("city").count()
```

This typically generates an execution plan roughly like this:

* Stage 1: data reading and initial transformation
* Shuffle
* Stage 2: final aggregation

Each stage can be executed in parallel across multiple nodes.

Task

A task is the smallest unit of work in Spark. Each stage is divided into multiple tasks, and each task processes one partition of data.

For example, for a dataset with 200 partitions in one stage, Spark will launch 200 tasks. And each task will be executed by an executor.

In other words:

```
Stage
├─ Task 1: processes partition 1
├─ Task 2: processes partition 2
├─ Task 3: processes partition 3
...
```

The more partitions there are, the more tasks Spark can execute in parallel.

Full Hierarchy in an Example

Imagine this code:

```python
df = spark.read.parquet("rides.parquet")

result = (
df
.filter("passenger_count > 2")
.groupBy("PULocationID")
.count()
)

result.show()
```

The execution might look like this:

* Application: the complete script.
* Job: created by `show()`.
* Stages:
* Reading and filtering.
* _Shuffle_ and aggregation.
* Tasks: one per partition.

Relevant Links

To get in-depth information about these concepts, check:

* [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html)
* [Resilient Distributed Dataset Programming Guide: Transformations](https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations)
* [Resilient Distributed Dataset Programming Guide: Actions](https://spark.apache.org/docs/latest/rdd-programming-guide.html#actions)
