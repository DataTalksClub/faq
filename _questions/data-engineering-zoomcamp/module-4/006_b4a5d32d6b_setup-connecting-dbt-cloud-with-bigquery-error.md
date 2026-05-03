---
id: b4a5d32d6b
question: 'Setup: Connecting dbt Cloud with BigQuery Error'
sort_order: 6
---

**Runtime Error**

dbt was unable to connect to the specified database.

The database returned the following error:

```plaintext
Database Error

Access Denied: Project <project_name>: User does not have bigquery.jobs.create permission in project <project_name>.
```

Check your database credentials and try again. For more information, visit:

[docs.getdbt.com](https://docs.getdbt.com/docs/configure-your-profile)

**Steps to resolve error in Google Cloud:**

1. Navigate to IAM & Admin and select IAM.
2. Click Grant Access if your newly created dbt service account isn't listed.
3. In the New principals field, add your service account.
4. Select a Role and search for BigQuery Job User to add.
5. Go back to dbt Cloud project setup and test your connection.
6. **Note:** Also add BigQuery Data Owner, Storage Object Admin, & Storage Admin to prevent permission issues later in the course.

<{IMAGE:image_id}>
