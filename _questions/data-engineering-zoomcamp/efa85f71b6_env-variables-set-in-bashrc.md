---
id: efa85f71b6
question: Env variables set in ~/.bashrc are not loaded to Jupyter in VS Code
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3680
---

I added PYTHONPATH, JAVA_HOME and SPARK_HOME to ~/.bashrc, import pyspark worked ok in iPython in terminal, but couldn’t be found in .ipynb opened in VS Code

After adding new lines to ~/.bashrc, need to restart the shell to activate the new lines, do either

source ~/.bashrc

exec bash

Instead of configuring paths in ~/.bashrc, I created .env file in the root of my workspace:

JAVA_HOME="${HOME}/app/java/jdk-11.0.2"

PATH="${JAVA_HOME}/bin:${PATH}"

SPARK_HOME="${HOME}/app/spark/spark-3.3.2-bin-hadoop3"

PATH="${SPARK_HOME}/bin:${PATH}"

PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"

PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"

PYTHONPATH="${SPARK_HOME}/python/lib/pyspark.zip:$PYTHONPATH"

