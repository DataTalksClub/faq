---
id: 49e1ec9d84
question: dbt - Where should we create `profiles.yml` ?
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3230
---

For local environment i.e. dbt-core, the profile configuration is valid for all projects. Note: dbt Cloud doesn’t require it.

The ~/.dbt/profiles.yml file should be located in your user's home directory. On Windows, this would typically be:

C:\Users\<YourUsername>\.dbt\profiles.yml

Replace <YourUsername> with your actual Windows username. This file is used by dbt to store connection profiles for different projects.

Here's how you can create the profiles.yml file in the appropriate directory:

Open File Explorer and navigate to C:\Users\<YourUsername>\.

Create a new folder named .dbt if it doesn't already exist.

Inside the .dbt folder, create a new file named profiles.yml.

Usage example can be found .

