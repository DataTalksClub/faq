---
id: 0de998a04e
question: Java+Spark - Easy setup with miniconda env (worked on MacOS)
sort_order: 9
---

If you want to manage all Python dependencies within the same virtual environment (e.g., conda), along with Java and Spark, follow these steps:

1. **Install OpenJDK 11:**
   
   On MacOS, run:
   
   ```bash
   brew install java11
   ```

   Add the following line to your `~/.bashrc` or `~/zshrc`:
   
   ```bash
   export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"
   ```

2. **Activate Your Environment:**

   Use your preferred tool (pipenv, poetry, or conda) to activate your working environment.

3. **Install PySpark:**

   Run:
   
   ```bash
   pip install pyspark
   ```

4. **Proceed with Exercises:**

   Work with your Spark exercises as usual. All default Spark commands will be available in the shell session under the activated environment.

   Note: You don’t need `findspark` for initialization.

5. **Resolving Py4J Errors:**

   If you encounter an error like:
   
   ```plaintext
   Py4JJavaError: An error occurred while calling (...)  java.net.ConnectException: Connection refused: no further information;
   ```

   Ensure you're using compatible versions of JDK or Python with Spark. Spark 3.5.0 supports JDK 8/11/17 and Python 3.8+.

   Use SDKMan! to install:
   
   ```bash
   sdk install java 17.0.10-librca
   sdk install spark 3.5.0
   sdk install hadoop 3.3.5
   ```

   Create and activate a conda environment with:

   ```bash
   conda create -n ENV_NAME python=3.11
   conda activate ENV_NAME
   pip install pyspark==3.5.0
   ```

6. **Windows Py4J Setup:**

   Ensure correct PATH settings in your `~/.bashrc`:

   ```bash
   export JAVA_HOME="/c/tools/jdk-11.0.21"
   export PATH="${JAVA_HOME}/bin:${PATH}"
   export HADOOP_HOME="/c/tools/hadoop-3.2.0"
   export PATH="${HADOOP_HOME}/bin:${PATH}"
   export SPARK_HOME="/c/tools/spark-3.3.2-bin-hadoop3"
   export PATH="${SPARK_HOME}/bin:${PATH}"
   export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
   
   export PYTHONPATH="${SPARK_HOME}spark-3.5.1-bin-hadoop3py4j-0.10.9.5-src.zip:$PYTHONPATH"
   ```

   Download `winutils` from [Stephenlaye2/winutils3.3.0](https://github.com/Stephenlaye2/winutils3.3.0) and place them in `/c/tools/hadoop-3.2.0/bin`.

   Check out this video for a solution: [How To Resolve Issue with Writing DataFrame to Local File](https://www.youtube.com/watch?v=yFem0Pu0gC8)

   Restart your IDE and computer to apply the changes. Be aware that fixing one error might result in new ones like `o31.parquet`. Address these as needed.