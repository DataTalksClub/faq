---
id: 0de998a04e
question: Java+Spark - Easy setup with miniconda env (worked on MacOS)
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3360
---

If anyone is a Pythonista or becoming one (which you will essentially be one along this journey), and desires to have all python dependencies under same virtual environment (e.g. conda) as done with prefect and previous exercises, simply follow these steps

Install OpenJDK 11,

on MacOS: $ brew install java11

Add export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"

to ~/.bashrc or ~/zshrc

Activate working environment (by pipenv / poetry / conda)

Run $ pip install pyspark

Work with exercises as normal

All default commands of spark will be also available at shell session under activated enviroment.

Hope this can help!

P.s. you won’t need findspark to firstly initialize.

Py4J - Py4JJavaError: An error occurred while calling (...)  java.net.ConnectException: Connection refused: no further information;

If you're getting `Py4JavaError` with a generic root cause, such as the described above (Connection refused: no further information). You're most likely using incompatible versions of the JDK or Python with Spark.

As of the , it supports JDK 8 / 11 / 17. All of which can be easily installed with  on macOS or Linux environments

$ sdk install java 17.0.10-librca
$ sdk install spark 3.5.0
$ sdk install hadoop 3.3.5py4j

make sure you're setting up your virtualenv with either 3.8 / 3.9 / 3.10 / 3.11 (Most importantly avoid using 3.12 for now as not all libs in the data-science/engineering ecosystem are fully package for that)


$ conda create -n ENV_NAME python=3.11

$ conda activate ENV_NAME

$ pip install pyspark==3.5.0

This setup makes installing `findspark` and the likes of it unnecessary. Happy coding.

Py4J - Py4JJavaError: An error occurred while calling o54.parquet. Or any kind of Py4JJavaError that show up after run df.write.parquet('zones')(On window)

This assume you already correctly set up the PATH in the nano ~/.bashrc

Here my

export JAVA_HOME="/c/tools/jdk-11.0.21"

export PATH="${JAVA_HOME}/bin:${PATH}"

export HADOOP_HOME="/c/tools/hadoop-3.2.0"

export PATH="${HADOOP_HOME}/bin:${PATH}"

export SPARK_HOME="/c/tools/spark-3.3.2-bin-hadoop3"

export PATH="${SPARK_HOME}/bin:${PATH}"

export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"

export PYTHONPATH="${SPARK_HOME}spark-3.5.1-bin-hadoop3py4j-0.10.9.5-src.zip:$PYTHONPATH"

You also need to add environment variables correctly which paths to java jdk, spark and hadoop through

Go to , download the right winutils for hadoop-3.2.0. Then create a new folder,bin and put every thing in side to make a /c/tools/hadoop-3.2.0/bin(You might not need to do this, but after testing it without the /bin I could not make it to work)

Then follow the solution in this video:

Remember to restart IDE and computer, After the error An error occurred while calling o54.parquet.  is fixed but new errors like o31.parquet. Or o35.parquet. appear.

