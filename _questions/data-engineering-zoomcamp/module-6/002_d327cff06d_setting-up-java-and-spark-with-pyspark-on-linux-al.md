---
id: d327cff06d
question: 'Setting up Java and Spark (with PySpark) on Linux (Alternative option using
  SDKMAN):'
sort_order: 2
---

1. **Install SDKMAN:**

   ```bash
   curl -s "https://get.sdkman.io" | bash
   
   source "$HOME/.sdkman/bin/sdkman-init.sh"
   ```

2. **Using SDKMAN, install Java 11 and Spark 3.3.2:**

   ```bash
   sdk install java 11.0.22-tem
   
   sdk install spark 3.3.2
   ```

3. **Open a new terminal or run the following in the same shell:**

   ```bash
   source "$HOME/.sdkman/bin/sdkman-init.sh"
   ```

4. **Verify the locations and versions of Java and Spark that were installed:**

   ```bash
   echo $JAVA_HOME
   
   java -version
   
   echo $SPARK_HOME
   
   spark-submit --version
   ```