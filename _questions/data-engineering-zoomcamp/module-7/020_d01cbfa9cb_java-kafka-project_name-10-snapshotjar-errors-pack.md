---
id: d01cbfa9cb
question: 'Java Kafka: <project_name>-1.0-SNAPSHOT.jar errors: package xxx does not
  exist even after gradle build'
sort_order: 20
---

In my setup, all of the dependencies listed in `build.gradle` were not installed in `<project_name>-1.0-SNAPSHOT.jar`.

Solution:

1. In the `build.gradle` file, add the following at the end:
   
   ```groovy
   shadowJar {
       archiveBaseName = "java-kafka-rides"
       archiveClassifier = ''
   }
   ```

2. In the command line, run:
   
   ```bash
   gradle shadowjar
   ```

3. Execute the script from `java-kafka-rides-1.0-SNAPSHOT.jar` created by the shadowjar.