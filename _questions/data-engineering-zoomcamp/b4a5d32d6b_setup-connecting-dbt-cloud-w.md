---
course: data-engineering-zoomcamp
id: b4a5d32d6b
question: Setup - Connecting dbt Cloud with BigQuery Error
section: 'Module 4: analytics engineering with dbt'
sort_order: 2470
---

Runtime Error

dbt was unable to connect to the specified database.

The database returned the following error:

>Database Error

Access Denied: Project <project_name>: User does not have bigquery.jobs.create permission in project <project_name>.

Check your database credentials and try again. For more information, visit:

https://docs.getdbt.com/docs/configure-your-profile

Steps to resolve error in Google Cloud:

1. Navigate to IAM & Admin and select IAM

2. Click Grant Access if your newly created dbt service account isn't listed

3. In New principals field, add your service account

4. Select a Role and search for BigQuery Job User to add

5. Go back to dbt cloud project setup and Test your connection

6. Note: Also add BigQuery Data Owner, Storage Object Admin, & Storage Admin to prevent permission issues later in the course

