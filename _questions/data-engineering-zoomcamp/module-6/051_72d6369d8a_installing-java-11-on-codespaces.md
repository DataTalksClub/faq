---
id: 72d6369d8a
question: Installing Java 11 on codespaces
sort_order: 51
---

1. Use the command below to check for available Java SDK versions:
   
   ```bash
   sdk list java
   ```

2. Install the desired version, for example:
   
   ```bash
   sdk install java 11.0.22-amzn
   ```

3. If prompted, press 'Y' to change the default Java version.

4. Verify the installation by checking the Java version:
   
   ```bash
   java -version
   ```
   
5. If the version does not work correctly, set the default version with:
   
   ```bash
   sdk default java 11.0.22-amzn
   ```
   
   Adjust this command to match the version you have installed.