---
id: d01cbfa9cb
question: Java Kafka: <project_name>-1.0-SNAPSHOT.jar errors: package xxx does not exist even after gradle build
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 4070
---

In my set up, all of the dependencies listed in gradle.build were not installed in <project_name>-1.0-SNAPSHOT.jar.

Solution:

In build.gradle file, I added the following at the end:

shadowJar {

archiveBaseName = "java-kafka-rides"

archiveClassifier = ''

}

And then in the command line ran ‘gradle shadowjar’, and run the script from java-kafka-rides-1.0-SNAPSHOT.jar created by the shadowjar

