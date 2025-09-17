---
course: data-engineering-zoomcamp
id: fee87c684a
question: DBT Deploy - Error When trying to run the dbt project on Prod
section: 'Module 4: analytics engineering with dbt'
sort_order: 3090
---

When running trying to run the dbt project on prod there is some things you need to do and check on your own:

First Make the pull request and Merge the branch into the main.

Make sure you have the latest version, if you made changes to the repo in another place.

Check if the dbt_project.yml file is accessible to the project, if not check this solution (Dbt: This dbt Cloud run was cancelled because a valid dbt project was not found.).

Check if the name you gave to the dataset on BigQuery is the same you put on the dataset spot on the production environment created on dbt cloud.

