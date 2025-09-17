---
course: data-engineering-zoomcamp
id: 23687d0f93
question: DBT - The database is correct but I get Error with Incorrect Schema in Models
section: 'Module 4: analytics engineering with dbt'
sort_order: 3260
---

What to do if your  dbt model fails with an error similar to:

DBT-CORE

Check profiles.yml:

Ensure your profiles.yml file is correctly configured with the correct schema and database under your target. This file is typically located in ~/.dbt/.

Example configuration:

DBT-CLOUD-IDE

Check Credentials in dbt Cloud UI:

Navigate to the Credentials section in the dbt Cloud project settings.

Ensure the correct database and schema are set (e.g., ‘my_dataset’).

![Image](images/data-engineering-zoomcamp/image_48537290.png)

Verify Environment Settings:

Double-check that you are working in the correct environment (dev, prod, etc.), as dbt Cloud allows different settings for different environments.

No Need for profiles.yml:

In dbt Cloud, you don’t need to configure profiles.yml manually. All connection settings are handled via the UI.

