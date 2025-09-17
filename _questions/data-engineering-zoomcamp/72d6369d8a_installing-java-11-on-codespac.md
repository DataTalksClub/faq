---
id: 72d6369d8a
question: Installing Java 11 on codespaces
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3780
---

~ Abhijit Chakraborty

`sdk list java`  to check for available java sdk versions.

`sdk install java 11.0.22-amzn`  as  java-11.0.22-amzn was available for my codespace.

click on Y if prompted to change the default java version.

Check for java version using `java -version `.

If working fine great, else `sdk default java 11.0.22-amzn` or whatever version you have installed.

