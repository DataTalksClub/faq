---
id: d327cff06d
question: Setting up Java and Spark (with PySpark) on Linux (Alternative option using SDKMAN)
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3290
---

Install SDKMAN:

curl -s "https://get.sdkman.io" | bash

source "$HOME/.sdkman/bin/sdkman-init.sh"

Using SDKMAN, install Java 11 and Spark 3.3.2:

sdk install java 11.0.22-tem

sdk install spark 3.3.2

Open a new terminal or run the following in the same shell:

source "$HOME/.sdkman/bin/sdkman-init.sh"

Verify the locations and versions of Java and Spark that were installed:

echo $JAVA_HOME

java -version

echo $SPARK_HOME

spark-submit --version

