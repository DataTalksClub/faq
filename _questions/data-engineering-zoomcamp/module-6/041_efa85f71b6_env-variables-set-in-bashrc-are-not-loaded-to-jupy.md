---
id: efa85f71b6
question: Env variables set in ~/.bashrc are not loaded to Jupyter in VS Code
sort_order: 41
---

I added `PYTHONPATH`, `JAVA_HOME`, and `SPARK_HOME` to `~/.bashrc`. Importing `pyspark` worked in iPython in the terminal but couldn't be found in a `.ipynb` file opened in VS Code.

After adding new lines to `~/.bashrc`, you need to restart the shell to activate the changes. You can do either of the following:

```bash
source ~/.bashrc
```

or

```bash
exec bash
```

Instead of configuring paths in `~/.bashrc`, you can create a `.env` file in the root of your workspace with the following content:

```bash
JAVA_HOME="${HOME}/app/java/jdk-11.0.2"

PATH="${JAVA_HOME}/bin:${PATH}"

SPARK_HOME="${HOME}/app/spark/spark-3.3.2-bin-hadoop3"

PATH="${SPARK_HOME}/bin:${PATH}"

PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"

PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"

PYTHONPATH="${SPARK_HOME}/python/lib/pyspark.zip:$PYTHONPATH"
```