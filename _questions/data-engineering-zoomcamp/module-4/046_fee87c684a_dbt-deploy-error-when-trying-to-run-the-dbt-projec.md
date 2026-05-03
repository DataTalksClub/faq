---
id: fee87c684a
question: 'DBT Deploy: Error When trying to run the dbt project on Prod'
sort_order: 46
---

When running the dbt project on production, ensure the following steps:

1. **Pull Request and Merge**
   - Make the pull request and merge the branch into the main.

2. **Version Check**
   - Ensure you have the latest version if changes were made to the repository elsewhere.

3. **Project File Accessibility**
   - Verify that the `dbt_project.yml` file is accessible to the project. If not, refer to the solution for the error: "Dbt: This dbt Cloud run was cancelled because a valid dbt project was not found."

4. **Dataset Consistency**
   - Confirm that the name assigned to the dataset on BigQuery matches the name specified in the production environment configuration on dbt Cloud.
